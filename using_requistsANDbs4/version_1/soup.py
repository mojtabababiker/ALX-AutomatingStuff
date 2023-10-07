"""
Syntax:
    import soup

Description:
    The soup functions for finding tags and tags attributes values

Methods:
    1. get_tag(urlPage_text, tagName, **kwargs)
    2. get_attrValue(urlPage_text, tagName, attr, **kwargs)
"""

from bs4 import BeautifulSoup

def get_tag(urlPage_text : str, tagName : str, **kwargs):
    """
    soup.get_tag(urlPage_text : str, tagName : str, **kwargs)

    Description:
        Use the BeautifulSoup Class to parse urlPage_text html and find
        and return the tag tagName

    Return:
        A bs4.element.Tag instance of the tafName
    """

    _soup = BeautifulSoup(urlPage_text, "html.parser")
    tag = _soup.find(tagName, **kwargs)
    #print(tag)
    return tag

def get_attrValue(urlPage_text : str, tagName : str,
                  attr : str, **kwargs) -> str:
    """
    soup.get_attrValue(urlPage_text : str, tagName : str,
                       attr : str, **kwargs) -> str

    Description:
        Call the soup.get_tag(urlPage_text, taggName, **kwargs) passing
        the urlPage_text and tagName beside the **kwargs, and then
        find the attribute attr on it and return its value

    Return:
        A string which represent the attr value, or None in failure
    """

    _tag = get_tag(urlPage_text, tagName, **kwargs)
    try:
        return _tag.get(attr)
    except Exception as e:
        return None
