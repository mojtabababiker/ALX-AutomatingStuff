#!/usr/bin/python3
"""
This script searches for and replaces GitHub tokens in Git configuration files.
- The script takes a required command line argument, which is the new GitHub
    token to replace the old tokens.
- If directories are provided as optional command line arguments, it searches
    for Git configuration files in those directories.
- If no directories are provided, it searches for Git configuration files
    across the entire system.
- The script reads each Git configuration file, extracts the old token,
    replaces it with the new token, and saves the changes.
- Usage: ./script_name.py <new_token> [optional <directory 1>
    <directory 2> ...]
"""

import os
import re
import sys


current_file_path = os.path.abspath(__file__)
scriptName = os.path.basename(current_file_path)
if len(sys.argv) < 2:
    print(
            "Usage: ./{} <new_token> [optional]<repo 1> <repo 2>...".format(
                scriptName))
    sys.exit(1)
else:
    token = sys.argv[1]


def get_token(file):
    """
    Extracts the old GitHub token from the specified Git configuration file.

    Args:
        file (str): Path to the Git configuration file.

    Returns:
        str or None: The extracted token if found, None otherwise.
    """
    pattern = r"https://(.*?)@github\.com"
    try:
        with open(file, "r") as f:
            contents = f.read()
            content = contents.split('\n')
            for line_number, line in enumerate(content, start=1):
                match = re.search(pattern, line)
                if match:
                    desired_part = match.group(1)
        return desired_part
    except Exception:
        pass


def replace_token(file, old_token):
    """
    Replaces the old GitHub token in the specified Git configuration file
    with the new token provided as a command-line argument.

    Args:
        file (str): Path to the Git configuration file.
        old_token (str): The old GitHub token to be replaced.

    Raises:
        Exception: If an error occurs during the replacement process.
    """
    try:
        with open(file, "r") as f:
            lines = f.readlines()

        with open(file, "w") as f:
            for line in lines:
                modified_line = line.replace(old_token, token)
                f.write(modified_line)
                print("token replaced successfully")
    except Exception as e:
        print(f"An error occured: {str(e)}")


dirs = sys.argv[2:] or "."
for dir in dirs:
    for root, subdirs, files in os.walk(dir):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith(".git/config"):
                try:
                    old_token = get_token(file_path)
                    replace_token(file_path, old_token)
                except Exception as e:
                    print("Error processing {file_path}: {e}")
