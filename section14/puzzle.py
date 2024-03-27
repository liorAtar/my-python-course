import shutil
import os
import re


def get_all_files_content():
    """
    Retrieve the content of all text files in the current directory and its subdirectories.

    Returns:
        str: Concatenated content of all text files.
    """
    base_path = os.getcwd()
    content = ""

    for folder, sub_folder, files in os.walk(base_path):
        for file_name in files:
            if file_name.endswith('.txt'):
                file_path = os.path.join(folder, file_name)
                file_content = get_file_content(file_path)
                content += file_content

    return content


def get_file_content(file_path: str):
    """
    Retrieve the content of a text file.

    Args:
        file_path (str): The path of the text file.

    Returns:
        str: The content of the text file.

    Raises:
        FileNotFoundError: If the file is not found.
    """
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
        return file_content
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


if __name__ == '__main__':
    shutil.unpack_archive("unzip_me_for_instructions.zip", "", "zip")

    instructions = get_file_content('extracted_content/instructions.txt')
    print(instructions + '\n')

    all_content = get_all_files_content()

    pattern = r'\d{3}-\d{3}-\d{4}'
    phone_number = re.search(pattern, all_content)
    print("The Phone Number Is:", phone_number.group())
