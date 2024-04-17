# Start to Work
 - clone this repo to local machine

 ```shell
 git clone https://github.com/Green0116/EasyBar.git
 ```
 
 This would pull remote repository to your disk in a folder with the name of the project ("EasyBar" for this project).
 
 - create a personal dev branch

 ```shell
 git checkout -b "your branch name"
 ```
 
 This allows independent personal development without conflicts.
 
 - before pushing changes to remote, check all your changes

 ```shell
 git diff
 ```
 
 This would give you the chance to ensure all updates are as expected.
 
 - add your changes to local git

 ```shell
 git add "your file to be submitted"
 ```
 
 This would put a file into your local git cache.
 
 - create a new local commit

 ```shell
 git commit -m "your commit message"
 ```
 
 This would create a new commit from files stored in your git cache, which is ready to be pushed to remote repository.
 
 - push your changes to remote

 ```shell
 git push origin "your branch name"
 ```
 
 This notifies the remote of the new commit, and keeps it updated.
 
 - keep up-to-date with remote main branch

 ```shell
 git checkout main
 git pull origin main
 git checkout "your branch name"
 git rebase main
 ```
 
 In case of any remote changes happened during your commit, pull them to local repository, then keep your personal dev branch updated with these changes. In case of any potential conflicts, manually choose the changes to be saved.
 
 - push all changes to remote (remote changes and your changes)

 ```shell
 git push -f origin "your branch name"
 ```
 
 You should now be updated with all remote changes (by others) as well as your own commits.
 
 - send a pull request on GitHub

# Departmental Linux Server

 - Establish connection to server

 ```shell
 ssh username@lxfarm06.csc.liv.ac.uk
 ```