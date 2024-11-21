""" 
The script requires two kind of inputs:

hash_val: The hash value for which the password is to be cracked.
file_name: The name of the file containing the list of passwords to be checked.
"""
import crypt

def find_password(file_name, hash_val):
    with open(file_name, 'r') as password_file:
        for passwd in password_file:
            passwd = passwd.strip()  # Strip new line characters
            hashed_passwd = crypt.crypt(passwd, hash_val)
            if hashed_passwd == hash_val:
                print("Password found: ", passwd)
                return passwd
    print("Password not found in the provided file.")
    return None


if __name__ == '__main__':
    hash_val = "$6$8HOLitkI$9HECw2MBzISI1O.RoyJdfugy4VHsTOU4RDTewcFECnZdWLpmtVwNo5a1/hg2kw4Qu74F08eMEwpLdK1eovfEd/"
    file_name = "rockyou.txt"
    find_password(file_name, hash_val)
