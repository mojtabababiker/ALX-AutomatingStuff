#!/usr/bin/python3
"""
DOCOMENTATIONS HERE
"""
import soup
import login
import requests

from pprint import pprint

def get_projectsList() -> dict:
    """
    DOCOMENTAIONS HERE
    """
    dashBoard = login.login()
    pprint(dashBoard.text)
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


def get_project(projectName : str):
    """
    DOCOMENTIONS HERE
    """
    project = get_projectsList().get(projectName, None)
    if project is None:
        raise ValueError("Unrecognized Project Name {}".format(projectName))
    try:
        projectPage = requests.get(r"https://intranet.alxswe.com" + project)

    except ConnectionError as e:
        print(str(e))
        exit(-1)

    #pprint(projectPage.text)
    
if __name__ == "__main__":
    #get_projectsList()
    get_project("0x1A. C - Hash tables")
