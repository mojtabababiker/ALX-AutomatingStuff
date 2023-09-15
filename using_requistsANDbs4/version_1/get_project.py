

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
    projectsList = soup.get_tag(dashBoard.text, "ul", class_="list-group")
    projects = dict()

    if projectsList is None:
        raise Exception("A Captian Lock need to be Done")
    
    try:
        for projectItem in projectsList.find_all("li"):
            for projectName in projectItem.find_all("a"):
                projects[projectName.text] = projectName.get("href")
    except Exception as e:
        print(str(e))
        exit(-1)
    #pprint(projects.items())
    return projects


def get_project(projectName : str, session, dashBoard):
    """
    DOCOMENTIONS HERE
    """
    project = get_projectsList(dashBoard).get(projectName, None)
    if project is None:
        raise ValueError("Unrecognized Project Name {}".format(projectName))
    try:
        #print(project)
        projectPage = session.get(r"https://intranet.alxswe.com" + project)
        print(projectPage.status_code)
        #print("https://intranet.alxswe.com" + project)

    except ConnectionError as e:
        print(str(e))

        exit(-1)

    #sop = BeautifulSoup(projectPage.text, 'html.parser')
    #hd = sop.find('h1')
    #print(sop.title)
    return projectPage


if __name__ == "__main__":
    #get_projectsList()
    get_project("0x1A. C - Hash tables")
