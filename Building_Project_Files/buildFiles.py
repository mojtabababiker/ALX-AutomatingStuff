#!/usr/bin/env python3
"""
Modle to parses project html page and extracts and build the
file of each task
"""

import soup
import os


class FileBuilder:
    """
    Syntax:
         FileBuilder(projectText)

    Descripion:
         A class that responsible of creating the tasks files of the project
    """

    def __init__ (self, projectText):
        """
        FileBuilder conistructer, initialize the class with the projectText
        as project html page source
        """

        self.projectText = projectText
        self.filePerms = 0o767

    def parse(self):
        """
        Syntax:
             FileBuilder.parse(self)

        Description:
             Parse the project html, extract tasks files name and creats
             those files on the current working directory
        """

        self.filesContainer = soup.get_tag(self.projectText, "div",
                                           id="task-num-0")
        while(self.filesContainer):
            self.file = self.filesContainer.find_all("div",
                                                    class_='list-group-item',
                                                    limit=1
                                                    )
            if self.file:
                #print(self.file[0].children)
                self.create(self.file[0].find('ul'))
            self.filesContainer = self.filesContainer.next_sibling
            self.filesContainer = self.filesContainer.next_sibling

    def create(self, file_info_list):
        """
        Syntax:
            FileBuilder.creat(self, file_info_list)


        Description:
            Create the file `self.file_info_list` element by parsing
            the text from it
        """
        file_name_container = file_info_list.find_all('li')[-1]
        fileName = file_name_container.find('code').text
        f = os.open(f"{fileName}", os.O_CREAT, mode=self.filePerms)
        os.close(f)
  
