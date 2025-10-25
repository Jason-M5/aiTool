from functions.get_files_info import get_files_info


def tests():
    test_cases = [".", "pkg", "/bin", "../"]

    for i in test_cases:
        if i == ".":
            print(f'Result for current directory:')
        else:
            print(f"Result for '{i}' directory:")
        test_result = get_files_info('calculator', i)
        if test_result.startswith('Error:'):
            print(f'    {test_result}')
        else:
            file_conts = test_result.split("\n")
            for i in file_conts:
                print(f' {i}')
tests()
        
