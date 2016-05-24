# Install software on your computer


### Install [git](http://git-scm.com/).

You have it installed if you can run `git --version` at the command
line and get output like `git version 2.3.5`.


### Install [Anaconda](http://continuum.io/downloads).

There are two things you can verify to check your install.

First, from the command line, all of the following should start up
some kind of Python interpreter:

```bash
python
ipython
ipython notebook
spyder
```

Second, inside any of those Python interpreters, you should be able to
do all of these without error:

```python
import numpy
import scipy
import matplotlib
import pandas
import statsmodels
import sklearn
```

### Install [Homebrew](http://brew.sh/) on Mac

If you use a Mac, install Homebrew if you don't
have it yet. You could use Homebrew to manage your `git` and `python`
installs as well, but the methods given above are very good and more
cross-platform.

---

###Q1. Python Version 2 or 3

Did you install Python 2 or 3? Why?  

>> I'm using Python 2.7, because sources that I've learned with (MIT and Learn Python the Hard Way) suggest that I start with Python 2, because it's completely established and supported. Python 3 still needs further development and use, although that may be coming very soon! I can also easily learn Python 3 after Python 2 in the future when necessary.

###Q2. Which Python Version Installed   

How can you check the version of Python installed if you happen to be on an unfamiliar computer?

>> enter "Python -V" at command line
