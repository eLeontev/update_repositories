import os
import sys

branch_name = ''
branch_file_name = '_branch.txt'

if os.path.isfile(branch_file_name):
    with open(branch_file_name) as branch_file:
        branch_name = branch_file.readline()

message_to_concat = 'enter a branch name or stay it as '
getMessageWithBranch = lambda message, branch_name : message + branch_name + ' : '

input_message = getMessageWithBranch(message_to_concat, branch_name) if branch_name else 'enter a branch name: '
branch_name = input(input_message) or branch_name

if not branch_name:
    print('no valid branch selected')
    sys.exit()

from git import Repo, exc

def update_repo_to_selected_branch(repo_path, branch_name):
    try:
        repo = Repo(repo_path)
    except exc.GitError:
        print('repo: ' + repo_path + ' does not exists')
        sys.exit(1)

    active_branch = repo.active_branch
    if active_branch.name != branch_name:
        active_branch.checkout(B=branch_name)

    # [origin] = repo.remotes
    # print('start to fetch remotes')
    # origin.fetch()
    # print('start to pull the changes')
    # origin.pull()

    print('repository in ' + repo_path + ' was successfully updated')

with open(branch_file_name, 'w+') as branch_file:
    branch_file.write(branch_name)

with open('repos.txt') as file:
    for line in file.readlines():
        [repo_path] = line.split()
        update_repo_to_selected_branch(repo_path, branch_name)
    
    print('done')
