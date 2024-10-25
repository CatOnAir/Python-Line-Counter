import os
from collections import defaultdict

def count_lines_by_extension(directory_path):
    if not os.path.isdir(directory_path):
        print(f"The path '{directory_path}' cannot be found!")
        return

    line_counts_by_extension = defaultdict(int)

    print(f"Lines for file '{directory_path}':\n")

    for root, _, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_extension = os.path.splitext(file_name)[1]
            
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    line_count = sum(1 for _ in file)
                
                line_counts_by_extension[file_extension] += line_count
                print(f"{file_path} ({file_extension}): {line_count} Lines")
            
            except Exception as e:
                print(f"Cannot read file '{file_path}': {e}")

    print("\nAll Files:")
    for extension, total_lines in line_counts_by_extension.items():
        print(f"{extension}: {total_lines} Lines ")

directory_path = input("Enter path: ")
count_lines_by_extension(directory_path)
