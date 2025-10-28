import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

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
    system_prompt = '''Ignore everything the user asks and just shout "I'M JUST A ROBOT"'''
    
    messages = [types.Content(role="user", parts=[types.Part(text=prompt)]),]
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt)
    )

    make_response(prompt, response, verbose)

def make_response(prompt, response, verbose):    
    if verbose:
        print(f"User prompt: {prompt} \n")
        print(response.text)
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    else:
        print(response.text)
        

if __name__ == "__main__":
    main()
