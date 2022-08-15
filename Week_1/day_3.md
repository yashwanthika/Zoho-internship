# Week 1 Git and Linux commands
Day:3 12 Aug 2022
## git commands:
### git rebase
Rebase is used to move the entire feature branch to begin on the tip of the main branch, instead of using a merge commit, rebasing re-writes the project history by creating brand new commits for each commit in the original branch.
```
git rebase [maseter] [branch_name]
```
![git rebase [maseter] [branch_name]](https://github.com/yashwanthika/Zoho-internship/blob/main/Week_1/images/Rebase.png)
### git cherry-pick
Cherry picking is the act of picking a commit from a branch and appending it to the current working head.
```
git cherry-pick [commit_reference]
```
![git cherry-pick [commit_reference]](https://github.com/yashwanthika/Zoho-internship/blob/main/Week_1/images/cherry_pick.png)
### git hooks
git hooks run automatically every time a particular event occurs in a Git repository.
Hooks reside in the .git/hooks directory of every Git repository. 

.git/hooks contain:

applypatch-msg.sample    

commit-msg.sample           

post-update.sample          

pre-applypatch.sample       

pre-commit.sample

pre-push.sample

pre-rebase.sample

prepare-commit-msg.sample

update.sample

the .sample extension prevents them from executing by default. To “install” a hook, .sample extension is removed.
In prepare-commit-msg the following is added to show the message "# Please include a commit message!"  when git commit happens
```
#!/bin/sh

echo "# Please include a commit message!" > $1
```
![git_hooks_example](https://github.com/yashwanthika/Zoho-internship/blob/main/Week_1/images/git_hook.png)

## Linux commands

### bashrc

The .bashrc file is a script file that’s executed when a user logs in.
To view the bashrc file
```
$ cat .bashrc
```
To create a .bashrc file
```
$ touch .bashrc
```
To reflect the changes in bash
```
$ source ~/.bash_rc
```

### Environment variables

To set a Environment variable:
```
export NAME=VALUE
```
To unset an environment variable
```
unset VARIABLE_NAME
```
To list all environment variables
```
$ set
```
To output the value of the environment variable from the shell,
```
$ echo $[Variable_name]
```
![Env_variables](https://github.com/yashwanthika/Zoho-internship/blob/main/Week_1/images/Environment_variable.png)

.env file
A . env file is a simple text configuration file for controlling Applications environment variables.
To create .env file
```
$ touch .env
```
### Linux commands:

SSH and SCP:

The Secure Copy Protocol (SCP), is a file transfer network protocol used to move files onto servers, and it fully supports encryption and authentication. 
![scp](https://github.com/yashwanthika/Zoho-internship/blob/main/Week_1/images/SCP.png)

SCP uses Secure Shell (SSH) mechanisms for data transfer and authentication to ensure the confidentiality of the data in transit.
Secure Shell (ssh) transfers the data in encrypted form between the host and the client
```
$ ssh [username]@[server]
```
rsync:

rsync (Remote sync) is used to copy ans synchronize files and directories remotely as well as locally.
```
# rsync options [source] [destination]
```
Options:

-v : verbose

-r : copies data recursively (but don’t preserve timestamps and permission while transferring data.

-a : archive mode, which allows copying files recursively and it also preserves symbolic links, file permissions, user & group ownerships, and timestamps.

-z : compress file data.

-h : human-readable, output numbers in a human-readable format.
![rsync_example](https://github.com/yashwanthika/Zoho-internship/blob/main/Week_1/images/rsync.png)


Find :
Find is a used to search for files and directories(locating) in the Linux filesystem based on certain criteria .
```
$ find . -name [filename]
```
Grep:
grep is a used to search for patterns in the content of files or in the output of other commands.
```
$ grep [pattern] [filename]
```
wc:
wc is used to display the number of lines, number of characters, and the number of words in a file.
```
$ wc [filename]
```
head:
head prints the top N number of data of the given input.
```
$ head [filename]
```
tail:
tail prints the last N number of data of the given input.
```
$ tail [file-name]
```
more:
The 'more' is a terminal paging program that is used to open a given file for interactive reading. If the content of the file is too large to fit in one screen, it displays the contents page by page.
```
$ more [filename]
```
less:
The less command is also a Linux terminal pager that is used to open a given file for interactive reading, allowing scrolling and search. 
```
$ less [filename]
```
which:
which command is used to locate the executable file or location of a program by searching it in the path environment variable.
```
$ which [program_name]
```
![linux_commands](https://github.com/yashwanthika/Zoho-internship/blob/main/Week_1/images/Linux_cmd.png)
### Mount a disk to your machine:

Mount point:
A mount point can be described as a directory to access the data stored in your hard drives.

fstab file:
fstab, is a configuration table designed to ease the burden of mounting and unmounting file systems to a machine.It is designed to configure a rule where specific file systems are detected, then automatically mounted in the user's desired order every time the system boots.
The fstab file is located at:
```
/etc/fstab
```
To mount disk:
```
$ sudo mount -t [filesystem_type] [disk or Partition_name] [mount_point]
```
To unmount disk:
```
$ sudo unmount [disk or Partition_name]
```
To check the partitions of a disk
```
$ df -h
```
### apt
Linux operating systems uses Advanced Package Tool (APT) as a package management system, the apt command installs, removes, upgrades, and manages software packages.
```
$ sudo apt update
```
```
$ sudo apt install <package>
```
```
$ apt show <package>
```
```
$ sudo apt remove <package>
```

### Tmux
To install tmux
```
$sudo apt install tmux
```

### Terminal vs tmux :
Tmux is a terminal program run from a terminal .Tmux is a terminal multiplexer that lets users tile window panes in a command-line environment. 
This in turn allows running multiple programs within one terminal.


### Commands in tmux:

To start a session :
```
$ tmux
```
To start a named session :
```
$ tmux new -s [session_name]
```
To list sessions:
```
$ tmux ls
```
To detach from session:
```
$ ctrl+b d
```
Attached to named session
```
$ tmux a -t [session_name]
```
split pane horizontally
```
ctrl+b "
```
split pane vertically:
```
ctrl+b %
```
To navigate between panes
```
ctrl+b [arrow key]
```
To resize pane (expand the pane down)
```
ctrl+b :
```
kill current pane
```
$ exit
```
or 
```
ctrl+b x
```
To cycle through panes:
```
ctrl+b o
```
To cycle between previous and current pane:
```
ctrl+b ;
```
To kill named session
```
$ tmux kill-session -t [session_name]
```
To kill tmux server, along with all sessions
```
$ tmux kill-server
```
![tmux_commands](https://github.com/yashwanthika/Zoho-internship/blob/main/Week_1/images/tmux.png)

.tmux.conf file 

To customize the tmux configuration, its default configuration file: tmux.confcan be changed. This file is invoked by Tmux at startup. Tmux first looks for the system configuration file inside the directory ‘/etc/tmux.conf’, if it is absent, it then searches inside the home directory of the user. 
To open tmux.conf file
 ```
 $ sudo nano ~/.tmux.conf
 ```
To remap prefix from 'C-b' to 'C-a'
```
unbind C-b
set-option -g prefix C-a
bind-key C-a send-prefix
```
To switch panes using Alt-arrow without prefix
```
bind -n M-Left select-pane -L
bind -n M-Right select-pane -R
bind -n M-Up select-pane -U
bind -n M-Down select-pane -D
```
To enable mouse mode
```
set -g mouse on
```
