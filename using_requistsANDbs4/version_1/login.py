
"""
Handle the login process, incluing generating the login form data, headers
and send a post requests to the server getting the dashboard of the user.

Methods:
    1. get_loginForm()
    3. login()

"""
import getpass
import requests
import config
import soup


def get_loginForm() -> dict:
    """
    Syntax:
        login.get_loginForm()

    Description:
        Generate the login form pyload as a dictionery, using the soup and
        config beside the requests module

    Return:
        A dictionery which represent the pyload of the login form
    """

    userEmail, userPassword = config.get_login_credentials()
    login_form = {
        'authenticity_token':"",
        'user[email]':userEmail,
        'user[password]':userPassword,
        'user[remember_me]': '0',
        'commit': 'Log in'
    }
    return login_form

def login(session):
    """
    Syntax:
        login.login(session)

    Description:
        Use the config and soup module to generate the login for payload, and
        use the requests.post() function to login to the dashboard.

    Return:
        An responce object of the user dashboard

    """
    url = config.get_url()
    headers = config.get_headers()
    login_form = get_loginForm()

    login_page = session.get(url)
    _auth_tocken = soup.get_attrValue(login_page.text, "input", "value")
    if _auth_tocken is None:
        print("===========[ERROR]==========")
        exit(-1)
    login_form['authenticity_token'] = _auth_tocken
    dash_board = session.post(url, data=login_form, headers=headers)
    #  check if the username and password are correct by passing the message
    #+ shows in the intranet dashboard when login credintials are wrong
    if "Invalid Email or password" in dash_board.text:
        print("Invalid Email or password please try again")
        file_path = ".shelf/.login_credentials"
        try:
            with open(file_path, 'w') as file:
                file.truncate(0)
        except FileNotFoundError:
            pass

        exit()

    return dash_board



if __name__ == "__main__":
    login()
