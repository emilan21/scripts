import os
import sys
import argparse


# create_repo: creates a github repo when given a name
def create_repo(name, description, path):
    description = f'"{description}"'
    path = f'"{path}"'
    os.system(
        f'gh repo create {name} --public --description {description} --source {path} --push'
    )


# delete_repo: deletes a github repo when given a repo
def delete_repo(repo):
    os.system(f'gh repo delete {repo}')


# list_repo: list github repos for user
def list_repo(user):
    os.system(f'gh repo list {user}')


# view_repo: view github repo
def view_repo(repo):
    os.system(f'gh repo view {repo}')


def main():
    # Top level parser
    parser = argparse.ArgumentParser(prog="github.py")
    subparsers = parser.add_subparsers(help='action subcommand')
    subparsers.required = True
    subparsers.dest = 'action'
    # create the parser for the "create" command
    parser_create = subparsers.add_parser('create',
                                          help='create: create github repo')
    parser_create.add_argument('name', type=str, help='name: github repo name')
    parser_create.add_argument('description',
                               type=str,
                               help='description: github repo description')
    parser_create.add_argument(
        'path',
        type=str,
        help='path: path to directory that you want to create a github repo of'
    )
    # create the parser for the "delete" command
    parser_delete = subparsers.add_parser('delete',
                                          help='delete: delete a github repo')
    parser_delete.add_argument('name', type=str, help='name: github repo name')
    # create the parser for the "list" command
    parser_list = subparsers.add_parser('list',
                                        help='list: list a users github repos')
    parser_list.add_argument('user', type=str, help='user: github username')
    # create the parser for the "view" command
    parser_view = subparsers.add_parser('view', help='view: view github repo')
    parser_view.add_argument('name', type=str, help='name: github repo name')
    args = parser.parse_args()

    if args.action == 'create':
        name = args.name
        description = args.description
        src_path = args.path
        create_repo(name, description, src_path)
    elif args.action == 'delete':
        name = args.name
        delete_repo(name)
    elif args.action == 'list':
        user = args.user
        list_repo(user)
    elif args.action == 'view':
        name = args.name
        view_repo(name)

    sys.exit(0)


if __name__ == '__main__':
    main()
