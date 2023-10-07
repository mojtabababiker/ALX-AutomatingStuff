#!/usr/bin/python3
"""
The main running scripts which executes all the other helper modules
"""
import sys
import time

import login
import soup
import requests
import config
import get_project
import buildReadme
import buildFiles


def main():
    """
    Code entry points
    """

    url = config.get_url()
    headers = config.get_headers()

    if len(sys.argv) == 2:
        projectName = sys.argv[1]
    else:
        projectName = input("Enter the required project name: ")


    with requests.Session() as session:
        dashBoard = login.login(session)
        #print(dashBoard.text)
        #exit()
        if not login.check_login(dashBoard.text):
            config.remove_login_credentials()
            #print("Invalid user name or password")
            exit(1)
        projectPage = get_project.get_project(projectName, session, dashBoard)
        #projectText = soup.get_tag(projectPage.text, "body")

        #print(projectText.h1)
        #readme = buildReadme.ReadmeBuilder(projectPage.text, projectName)
        #readme.parse()
        files = buildFiles.FileBuilder(projectPage.text)
        files.parse()

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Time consumed Buillding README.md:",
          " {:4f} seconds".format(end - start))
