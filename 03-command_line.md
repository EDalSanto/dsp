# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

* ls:
  * ls: lists all 'visible' files and folders in directory
  * ls -a: list all files, including invisible files and folders(prepending of .)
  * ls -l: list in long format
  * ls -lh: list in long format human readable size

* pwd: prints working directory

* cp:
  * cp <filename> <directory>: copies file to directory
  * cp <filename> <copiedfilename>: copies file with new name in current directory
  * cp -r <old directory> <new directory>: copy recursively all files in old directory in new directory
* mv:
  * mv <oldfilename> <newfilename>: rename file
  * mv <filename><directory>: move file to directory
  * mv <foldername><foldername2>: move folder in folder2
* grep:
  * grep <text pattern> <filename>: search for text in file
    * -i: ignore case
  * grep -r <text pattern> <folder>: recursively search for text in all files of folder

* cd:
  * cd: go to root directory
  * cd .. go up one directory
  * cd <foldername>: change into foldername

* wc:
  * wc: count of lines, words, and characters in file
  * wc -l: only lines
  * wc -c: only characters
  * wc -w: only words

* cat:
  * cat <filename>: print file to screen

* echo:
  * echo <text>: print text to screen
  * echo <text> > <newfilename>: append text to new file
  * echo <text> >> <filename>: append text to existing file

* less:
  * less <filename>: page through a file

* head:
  * head <filename>: print out first 10 lines of file by default
  * head -n <filename>: print out first n lines

* tail:
  * tail <filename>: print out last 10 lines of file by default
  * tail -n <filename>: print out last n lines of file

* mkdir:
  * mkdir <dir name>: make directory with name in current directory
  * mkdir <path to new directory>: make new directory with in path

* rm:
  * rm <filename>: remove filename
  * rm -r <foldername>: delete foldername
  * rm -f <filename>: force remove filename
  * rm -rf <folder>: force remove folder
  * rm -i <filename>: ask for permission

* touch:
  * touch <filename>: create file in current directory

* &&
  * &&: combine commands

* |:
  * |: pipe output of commands into new commands

* rmdir:
  * rmdir <directory>: remove directory

* man:
  * man <command>: display man page for command

* sudo:
  * sudo <command>: uses root user authorization; very powerful
  "sudo make me a sandwich"

* find:
  * find . -name <pattern>

* curl: let's us query URL from CL; can be used to download API
  * curl <url>: raw html
    get request


---

###Q2.  List Files in Unix   

What do the following commands do:  
* `ls`: list all visible files and folders in working directory
* `ls -a`: list both invisible and visible files and folders in working directory
* `ls -l`: list in long format all visible files in wd
* `ls -lh`: list in long format all visible files with size in human readable format
* `ls -lah`: list in long format all visible and invisible files in human readable format
* `ls -t`: list sorted by time last modified
* `ls -Glp` : list long-format, p: write a slash after each file name if file is directory, G: colorized format

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

* `ls -R`: list subdirectories as well
* `ls -a`: list both invisible and visible files
* `ls -lh`: list in long format, human-readable
* `ls -t`: list sorted by time last modified
* `ls -x`: list files as rows across screen

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

* `xargs` expects stdin input and echos it
examples of how to use it:
  * xargs, enter input and hit ctrl-d to have input echoed on screen
  * further reference: http://www.thegeekstuff.com/2013/12/xargs-examples/
