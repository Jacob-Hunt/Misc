#    File Name: pw_crypt.py
#    Author: Jacob Hunt
#    Author Email: jacobhuntemail@gmail.com
#    Python Version: 3.4.3
#
#    Notes:
#    A short, simple script which generates a hashed Unix password.
#    
#    Known Bugs/Issues:
#        -As of April 2017, only works in a Unix environment (as the
#         crypt library is not supported by Windows Python).

import crypt

def main():
    password = input("Enter password to be encrypted: ")
    salt = input("Enter salt to use: ")
    hashed = crypt.crypt(password, salt=salt)
    print(hashed)

if __name__ == "__main__":
    main()