# Week1 - GIT and Linux commands
## Day 2: 11 Aug 2022        
      
### GIT :

GIT is a open source distributed version control system used by programmers collaboratively developing code during a software development.It keeps track of the changes made in a set of files.

### Repository:
A repository  is a storage space for the project . A git repository keeps track and saves history the changes made to the project.This data is stored in a directory called .git .The repository may contain code,text,images or any kind of files.

To create a new local repository use
```
$ git init
```
To clone a remote repository use
```
$ git clone
```

### Branch:
A branch represents an independent line of development.To add any new feature or fix the existing bugs  we create a new branch make  changes, stage and commit and check for the stability before merging it to the main branch. 

To create a new branch in the local repository 

```
$ git branch <branch>
```
to add new branch to the repo either git branch can be used by adding coniguration to the loacl repo config or by pushing the copy of the local branch to the remote repository 

To list all the branches
```
$ git branch
```
To delete a branch in local
``` 
$ git branch -d <branch>
```
To delete a branch in remote
``` 
$ git push origin --delete <branch>
```
### Remote:
As git works as a distributed collaborative model each developer will have their own copy of the repository.
git remote is responsible for syncing changes.It can be used to create, view, and delete connections to other repositories.

To list the reomte connections
```
$ git remote
```
To create a new connection to a remote repository
```
$ git remote add <name> <url>
```
To remove the connection of the remote repository 
```
git remote rm <name>
```

### Local branch and Remote branch:

A local branch is a branch that exists only on the local machine. 
To list the local branches
```
$ git branch
```
A remote branch is a branch on a remote location 
To list the remote branches
```
$ git branch -r
```
To list both local and global branches
```
$ git branch -a
```
### Synchronization of local and remote
What happens when local and remote are not in sync?

when developers work on different aspects of project certain files will differ in both repositories as other developers are merging the code upstream and local branch will not have that changes unless it gets synced to the repository with the current upstream
Synching will override the local repository with a master remote repository. And if there are files in the local repository that do not exist in the remote repo, local files get removed.

To sync the local repository
```
$ git remote add upstream <url>
```
To make origin/master repository the same as upstream repository
```
$ git fetch upstream
$ git checkout master
$ git merge upstream/master
```
### Deleting local and remote branch
when the change or new feature or bug fixes are incorporated into the original version of the project ,the branch can be deleted.
To delete a local branch
```
git branch -d <branch_name>
```
What happens when you delete a local branch? 

Deleting a local branch deletes the branch in the local machine and it do not affect any remote branches


To delete a remote branch
```
git push --delete <remote_name> <branch_name>
```
What happens when you delete a remote branch?

Deleting a remote branch do not affect the local branch .
To prune the local tracking branch of remot branches that have been deleted
```
$ git fetch -p
```
### Merge Requests and Pull Requests

Pull requests are a mechanism for a developer to notify team members that they have completed a feature. Once their feature branch is ready, the developer files a pull request. This lets everybody know that they need to review the code and merge it into the main branch.
Merge request will work just like a pull request.Github uses git pull Request and Git lab uses Git Merge request.

### Fast-forward merge

Fast forward merge moves the main branch’s tip forward to the end of the feature branch.
A fast-forward merge can occur if two branches have not diverged and there is a direct linear path from the target branch to the source branch. 

To make a fast -forward merge
```
git merge --ff <source-branch>
```
### Squashed merge

Squash merging is a merge option that condense the Git history of feature branches. Instead of each commit on the feature branch being added to the history of the default branch, 
a squash merge adds all the file changes to a single new commit on the default branch.

To make a squashed merge
```
git merge -squash <source-branch>
```
### Head
a head is a pointer that points to the tip or latest commit of a branch. 
Repository’s heads can be found in the path .git/refs/heads/. In this path there will be one file for each branch, and the content in each file will be the commit ID of the tip or most recent commit of that branch.

To show the location of the head.
```
$ git show HEAD  
```
### What happens when you try to merge branch source into branch target, but target is ahead?
A fast forward merge is not possible in this case. Instead a new commit is added to the master branch that contains all of the new changes.
```
$ git checkout master
$ git merge <feature_branch>
```
Rebase

The other way is to rebase the feature branch onto master .The branch commits are removed, and added after the current state of the target.
```
$ git checkout <feature_branch>
$ git rebase master
```

### Git vs Github vs Gitlab
Git: GIT is a open source distributed version control system used by programmers collaboratively developing code during a software development.
It keeps track of the changes made in a set of files.

GitHub: GitHub is a cloud based git repository hosting service.

Git Lab: Git lab is a web-based devops life cycle tool provides a git repository manager provides wiki, issue tracking and CI/CD pipe line.

Git Lab has advanced and different features than GitHub & Git:

Authentication Levels: Git lab having features like adding and modifying people’s permissions according to their roles.

Built-in CI/CD tool: GitLab having the feature like automatically testing with CI/CD and no need of humans. It also integrates with external integration applications like jenkins, etc…


