from functions.get_files_info import get_files_info


def tests():
    test_cases = [".", "pkg", "/bin", "../"]

    for case in test_cases:
        if case == ".":
            print(f'Result for current directory:')
        else:
            print(f"Result for '{case}' directory:")
        test_result = get_files_info('calculator', case)
        if test_result.startswith('Error:'):
            print(f'    {test_result}')
        else:
            file_conts = test_result.split("\n")
            for line in file_conts:
                print(f' {line}')
if __name__ == "__main__":
    tests()
        
