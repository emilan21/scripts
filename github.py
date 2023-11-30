import os
import sys


# create_repo: creates a github repo when given a name
def create_repo(repo, description, src_path):
    if repo == "":
        sys.exit(1)
    os.system(
        f'gh repo create {repo} --public --description {description} --source {src_path} --push'
    )


# delete_repo: deletes a github repo when given a repo
def delete_repo(repo):
    if repo == "":
        sys.exit(1)
    os.system(f'gh repo delete {repo}')


# list_repo: list github repos for user
def list_repo(user):
    if user == "":
        sys.exit(1)
    os.system(f'gh repo list {user}')


# view_repo: view github repo
def view_repo(repo):
    if repo == "":
        sys.exit(1)
    os.system(f'gh repo view {repo}')


def main():
    action = input("Enter an action(create, delete, list, view): ")
    if action == "create":
        repo = input("Enter a repo: ")
        description = input("Enter a description for this repo: ")
        src_path = input("Enter source path: ")
        create_repo(repo, description, src_path)
    elif action == "delete":
        repo = input("Enter a repo: ")
        delete_repo(repo)
    elif action == "list":
        user = input("Enter a user: ")
        list_repo(user)
    elif action == "view":
        repo = input("Enter a repo: ")
        view_repo(repo)
    else:
        print("Not a vaild action. Exiting program!")
        sys.exit(1)

    sys.exit(0)


if __name__ == '__main__':
    main()
