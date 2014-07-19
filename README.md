### Create a new repository on the command line
``` sh
touch README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/ouchliu/ytrey.git
git push -u origin master
```

### Push an existing repository from the command line
``` sh
git remote add origin https://github.com/ouchliu/ytrey.git
git push -u origin master
```

### Command for fixing problems

```sh
$ git reset --hard commitSHA
```
$ git push -f origin HEAD^:master

### Branch Commands
``` sh
# Creating a new branch
$ git branch # list all branches in the working folder
$ git branch newBranchName
$ git checkout newBranchName # switch to branch newBranchName
$ git push origin newBranchName # adds new branch to github repo

# Mergeing new branch to old branch
$ git checkout oldBranchName
$ git merge newBranchName #
$ git branch -d branchNameToDelete # delete branch while you are on a different branch
```
