import os
import re

FUNCTION_LIST = [
    'confirmTransaction',
    'getSignatureStatus',
    'getSignatureConfirmation',
    'getConfirmedSignaturesForAddress',
    'getConfirmedBlock',
    'getConfirmedBlocks',
    'getConfirmedBlocksWithLimit',
    'getConfirmedTransaction',
    'getConfirmedSignaturesForAddress2',
    'getRecentBlockhash',
    'getFees',
    'getFeeCalculatorForBlockhash',
    'getFeeRateGovernor',
    'getSnapshotSlot',
    'getStakeActivation'
]

def search_functions(root_dir):
    results = {}
    
    file_extensions = ('.js', '.jsx', '.ts', '.tsx')
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if 'node_modules' in dirnames:
            dirnames.remove('node_modules')
            dirnames.remove('.next')
        
        for filename in filenames:
            if filename.endswith(file_extensions):
                filepath = os.path.join(dirpath, filename)
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
                    
                    for func in FUNCTION_LIST:
                        pattern = r'\b' + re.escape(func) + r'\b'
                        matches = re.findall(pattern, content)
                        
                        if matches:
                            if func not in results:
                                results[func] = []
                            results[func].append((filepath, len(matches)))

    return results

def print_results(results):
    for func, occurrences in results.items():
        print(f"\nFunction: {func}")
        for filepath, count in occurrences:
            print(f"  - {filepath}: {count} occurrence(s)")

if __name__ == "__main__":
    repo_path = input("Enter the path to your Next.js repository: ")
    results = search_functions(repo_path)
    print_results(results)