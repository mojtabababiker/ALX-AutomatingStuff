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
        projectPage = get_project.get_project(projectName, session, dashBoard)
        #projectText = soup.get_tag(projectPage.text, "body")

        #print(projectText.h1)
        readme = buildReadme.ReadmeBuilder(projectPage.text)
        readme.parse()

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Time consumed Buillding README.md: {:4f} seconds".format(end - start))
