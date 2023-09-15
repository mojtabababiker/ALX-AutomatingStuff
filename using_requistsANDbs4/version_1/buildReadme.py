"""
Syntax:
    import buildReadme

Description:
"""
import soup
import sys


class ReadmeBuilder:
    """
    Syntax:
        ReadmeBuilder(projectText)

    Description:
        A class that responsible of generating the README file from the project descripions
        in the ALX intranet project page
    """

    def __init__(self, projectText):
        """
        ReadmeBuilder constructer, initialize the calss with the projectText as
        the project html page source
        """
        self.projectText = projectText
        self.projectName = soup.get_tag(self.projectText, "h1", class_="gap").text
        self.markers = {
            "p": self.pragraph,
            "pre": self.pre,
            "ul": self.ul,
            "a": self.links
            }
            
    def parse(self):
        """
        Syntax:
            ReadmeBuilder.pars(seld)

        Description:
            Parse the project page allocates all the headers, pragrraphs, list elemnts,
            and all the html elements that represent the project description

        """

        self.projDesc = soup.get_tag(self.projectText, "div", class_="panel-body")
        #print(self.projDesc)
        with open("README.md", "w", encoding="utf-8") as fh:
            fh.write("# " + self.projectName + "\n")
            for element in self.projDesc.children:
                line = self.extract(element)
                #print(element)
                if line is not None:
                    fh.write(line + "\n")

                #else:
                    #raise Exception("Unrocognized line")
        print("========Done Creating README.md=======")

    def extract(self, element):
        """
        Syntax:
            ReadmeBuilder.extract(self, element)

        Description:
            Extract the project description lines and creats the equivelant Mark Down
            lines for them, with the use of the helper functions
        """
        elementName = element.name
        #print(element.name, " : ", element.text)
        if self.markers.get(elementName, None):
            return self.markers[elementName](element)
        if elementName == 'h1':
            #print("# ", element.text)
            return "# {}".format(element.text)

        elif elementName == 'h2':
            #print("## ", element.text)
            return "## {}".format(element.text)
        
        elif elementName == 'h3':
            #print("### ", element.text)
            return "### {}".format(element.text)

    def pragraph(self, element):
        """
        Syntax:
            ReadmeBuilder.pragraph(self, element)

        Description:
            Reconsitruct the text in the pragraph element to its equivalent in MarkDown\
        """
        __markdown = element.text.strip()
        #print("*", element.text, "*")
        return __markdown.strip(".")

    def pre(self, element):
        """
        Syntax:
            ReadmeBuilder.pre(self, element)

        Description:
            Reconsitruct the text in the preformated pragraph element to its
            equivalent in MarkDown
        """
        __markdown = "`" + element.text.strip() + "`"
        #print("--", element.text, "--")
        return __markdown

    def ul(self, element):
        """
        Syntax:
            ReadmeBuilder.ul(self, element)

        Description:
            Reconsitruct the text in the unordered list element to its
            equivalent in MarkDown
        """
        __markdown = ""
        #print("[.", element.text)
        for li in element.find_all("li"):
            __markdown += "- " + li.text.strip() + "\n"
        return __markdown

    def links(self, element):
        """
        Syntax:
            ReadmeBuilder.links(self, element)

        Description:
            Reconsitruct the text in the unordered list element to its
            equivalent in MarkDown
        """
        __markdown = ""
        print("[{}]".format(element.text)+"(", element.get("href"), ")")
