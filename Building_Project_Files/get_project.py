

#!/usr/bin/python3
"""
DOCOMENTATIONS HERE
"""
import soup
import login
import requests

from pprint import pprint
from bs4 import BeautifulSoup

def get_projectsList(dashBoard) -> dict:
    """
    DOCOMENTAIONS HERE
    """
    #dashBoard = login.login()
    projects_col = soup.get_tag(dashBoard.text, "div", class_="col-md-6")
    projectsList = projects_col.find_all("div", "panel panel-default")[-1]
    projects = dict()

    if projectsList is None:
        print("A Captian Lock need to be Done")
        exit(1)

    try:
        for projectItem in projectsList.find_all("li"):
            for projectName in projectItem.find_all("a"):
                projects[projectName.text.strip()] = projectName.get("href")
    except Exception as e:
        print(str(e))
        exit(-1)

    return projects


def get_project(projectName : str, session, dashBoard):
    """
    DOCOMENTIONS HERE
    """
    project = get_projectsList(dashBoard).get(projectName, None)

    if project is None:
        print("Unrecognized Project Name {}".format(projectName))
        exit(1)
    try:
        projectPage = session.get(r"https://intranet.alxswe.com" + project)
        print(projectPage.status_code)

    except ConnectionError as e:
        print(str(e))
        exit(1)

    #sop = BeautifulSoup(projectPage.text, 'html.parser')
    #hd = sop.find('h1')
    #print(sop.title)
    return projectPage


if __name__ == "__main__":
    #get_projectsList()
    get_project("0x1A. C - Hash tables")
