#!/usr/bin/python3
"""Get login credentials.

syntax:
       import config
Description:
       Handle the user `email` and `password` and the url and header
       generating.
       Checking the `.login_credentials` file first before asking the user
       to enter them.
       The url is cretical, so we have two options for the url:
             1. The default one is the login page of ALX-intranet
             2. The user can enter the specific-required- project.[TODO]
       This module can provide the following functions:
             1. get_login_credentials()
                    Return the logging credentials of the user
             2. get_url()
                    Check if the user provided a url as command line arg,
                    if so it will return the default `url`
                        which is the login page
             3. get_headers()
                    Generate the headers for the url
                    request that will be preduced
"""

# import regex
import shelve
import getpass
import os
import subprocess

def get_login_credentials() -> tuple:
    """Get login credentials.

    syntax:
         config.get_login_credentials()

    Description:
         Check if the user login credentials are avaliable on the shelf,
         if so it will return the credentials on the shelf, else this
         function will ask the user to enter her/his email and password,
         even so this is one time process because the function will store
         these credentials on the shelf for the next time to be used.

    Return:
         a tuple consist of (user_email, user_password)
    """
    user = subprocess.run("whoami", shell=True, capture_output=True,
                          encoding="utf-8")
    h_folder = f"/home/{user.stdout.strip()}/.shelf/"
    h_credentals = os.path.join(h_folder, ".login_credentials")
    try:
        with shelve.open(h_credentals, "r") as fh:
            user_email = fh['user_email']
            user_password = fh['user_password']
        return (user_email, user_password)
    except Exception as e:
        if not os.path.isdir(h_folder):
            os.mkdir(h_folder)
        user_email = input("Enter Email: ")
        user_password = getpass.getpass(prompt="Enter Password: ", stream=None)

        with shelve.open(h_credentals) as fh:
            fh['user_email'] = user_email
            fh['user_password'] = user_password
        except Exception as ex:
            pass

        return (user_email, user_password)

def remove_login_credentials():
    """
    Syntax:
        config.remove_login_credentials()

    Description:
        Delete the credentials file if it's exists
    """

    user = subprocess.run("whoami", shell=True, capture_output=True,
                          encoding="utf-8")

    h_folder = f"/home/{user.stdout.strip()}/.shelf/"
    h_credentials = os.path.join(h_folder, ".login_credentials")
    if os.path.isfile(h_credentials):
        subprocess.run(f"rm -f {h_credentials}", shell=True)

def get_url() -> str:
    """Get project url.

    Syntax:
         config.get_url()

    Description:
         check if a url had been provided as command line argument, if so
         then this `url` will be returned[TODO], else the default `url`
         will be returned

    Return:
         A string representing the `url`
    """
    return r"https://intranet.alxswe.com/auth/sign_in"


def get_headers() -> dict:
    """Get login headers.

    Syntax:
         config.get_headers()

    Description:
         Generate a request header dictionary containing the necessary headers
         to send the required request


    Return:
         a dictionery wich representing the request headers
    """
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Origin": "https://intranet.alxswe.com",
        "Referer": get_url(),
    }
    return headers


if __name__ == "__main__":
    us, ps = get_login_credentials()
    print('User name: {}'.format(us))
    print('User Password: {}'.format(ps))
    #print(get_url())
    #print(get_headers().items())
