# GitHub Token Replacement Automation

This Python script automates the process of searching for and replacing GitHub tokens in Git configuration files. This can be especially useful when you need to update GitHub tokens across multiple repositories or directories.

## Features

- **Token Replacement:** The script replaces existing GitHub tokens with a new token provided as a command-line argument.
- **Directory Option:** You can specify specific directories to search for Git configuration files. If no directories are provided, the script will search for files across the entire system.
- **Informative Output:** The script provides informative output, indicating the number of tokens found and replaced in each file.

## Prerequisites

- **Python 3:** Make sure you have Python 3 installed on your system.

## Usage

To use this script, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/mojtabababiker/ALX-AutomatingStuff.git
   cd ALX-AutomatingStuff/Github-token_replace/

    Run the Script:

    bash

   ```bash

	./script_name.py <new_token> [optional <directory 1> <directory 2> ...]
	
	bash

Replace <new_token> with the new GitHub token you want to replace the old tokens with. You can also specify optional directories to limit the search scope.

Example:

	```bash

	./token-replace.py ghp_newToken123 /path/to/repo/directory

	bash

View Output:
The script will display message, indicating the token has been replaced successfully.
