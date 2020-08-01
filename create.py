from github import Github
import sys
import os
from dotenv import load_dotenv

load_dotenv()

access_token = os.getenv("ACCESS_TOKEN")

def create():
    folder_name = str(sys.argv[1])
    g = Github(access_token)
    u = g.get_user()
    r = u.create_repo(folder_name) 
    r.create_file('README.md', 'initial commit', '# {}'.format(folder_name)) 
    print("Succesfully created remote repository {}".format(folder_name))
    os.chdir('/home/quibbleahr/Documents/workspace')
    os.system('git clone https://github.com/quibbleahr/{}'.format(folder_name))
    print("Succesfully created local repository {}".format(folder_name))

if __name__ == '__main__':
    create()