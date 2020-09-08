# HW 2

## Part 1: Dealing with git

**1. Describe what is the output of the following commands**

    -  `git branch` 
    -  `git checkout BRANCH_NAME` (USE THE NAME OF AN EXISTING BRANCH)
    -  `git log --decorate`

```
git branch - shows the branches in the repo
git checkout math - switches to the math branch
git log --decorate - shows the commits, but I don't see a difference when I omit `--decorate`
```

**2. Try `git log --graph --all`. What do you see?**

```
It shows the repo "tree" with all the branches and where they come from.
```

**3. Use `git diff BRANCH_NAME` to view the differences from a branch and the current branch.
   Summarize the difference from master to the other branch.**

```
Math adds some of the math operations. Master is dumb dumb.
```

**4. Write a command sequence to merge the non-master branch into `master`**

```
git checkout master
git merge math
```


**5. Write a command (or sequence) to (i) create a new branch called `math` (from the `master`)
and (ii) change to this branch**

```
git checkout master
git branch -D math
git checkout -b math
```
   
**6. Edit B.py adding the following source code below the content you have there**
```
print 'I know math, look:'
print 2+2
```

**7. Write a command (or sequence) to commit your changes**
```
git status
git commit -av
```

**8. Change back to the `master` branch and change B.py adding the following source code (commit your change to `master`):**
```
print 'hello world!'
```

**9. Write a command sequence to merge the `math` branch into `master` and describe what happened**
```
git merge math

We get a merge conflict and markers are put in the file.
```
   
**10. Write a set of commands to abort the merge**
```
git merge --abort
```
   
**11. Now repeat item 9, but proceed with the manual merge (Editing B.py). All implemented functions are needed. Explain your procedure**
```
I merged, then opened the file in emacs, deleted the markers, removed whitespace, and now I can do math!!!! YEEEAAAA
```

**12. Write a command (or set of commands) to proceed with the merge and make `master` branch up-to-date**
```
git commit -av
```

## Part 2: Using GitHub

**Report your experience of making this submission**
```
1. Fork repo through the web UI.

2. Clone repo in terminal.

3. Make file according to spec in students/

4. Commit and push changes.

5. Pull request. This is where I had issues. I couldn't find any good docs on it. 
I found githubs docs messy and disorganized. It had me follow bunch of links to 
what seemed to be unfinished documents. Conceptually I understand a pull request. 
I'm telling you "hey I made a change, pull it down". But when I went to your repo to 
initiate it, I could not proceed. I hit the Slack and Tosin mentioned I had to be 
in my own repo. It worked. Not that intuitive but I'm still thinking it through. 
I would think I go to your repo to make the request but I guess it's simpler this way.
```
