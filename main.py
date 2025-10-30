import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.get_files_info import schema_get_files_info
from functions.write_file import schema_write_file

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def main():
    if len(sys.argv) < 2:
        raise  IndexError("No prompt provided")

    args = []
    verbose = False
    for arg in sys.argv[1:]:
        if not arg.startswith('--'):
            args.append(arg)
        elif arg == "--verbose":
            verbose = True
    
    prompt = " ".join(args)
    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

    available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
        ]
    )   
    
    messages = [types.Content(role="user", parts=[types.Part(text=prompt)]),]
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
    )
    
        

    make_response(prompt, response, verbose)

def make_response(prompt, response, verbose):    
    if verbose:
        print(f"User prompt: {prompt} \n")
    print(response.text)
    if response.function_calls:
        for func in response.function_calls:
            if hasattr(response.candidates[0].content.parts[0], 'function_call') and response.candidates[0].content.parts[0].function_call:
                function_call_part = response.candidates[0].content.parts[0].function_call
                print(f"Calling function: {function_call_part.name}({function_call_part.args})")
            else:
                print(f"Function call detected but function_call part is None")

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
        

if __name__ == "__main__":
    main()
