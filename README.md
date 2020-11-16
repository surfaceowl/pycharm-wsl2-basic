# pycharm-wsl2-basic

Initial repo to demonstrate use of WSL2 and challenges with environments and debugging

**Summary:**
<br>
Developing with PyCharm on Windows 10

*setup options - lots of choices*<br>
Python - which version:  Standard Python (default) or Anaconda <br>
Standard - default, out of the box; impossible to compile C-extensions (scipy!  <br>
Anaconda - separate universe,  slightly different syntax (conda), but compiled C-libraries, not latest version<br>
Which Python - where to install -- windows or WSL<br>
Where to put your code -- possible to read / write between Windows and WSL == good; but filesystem matters<br>
PyCharm - where to install; windows is intuitive/default -- WSL requires complex/nonstandard Xserver magic<br><br>

PyCharm - PyCharm Pro installed on Windows 10<br>
Python3 - installed from<br>
Windows Store --- obscure path<br>
Python.org -- installer (https://www.python.org/downloads/); custom simple path; multiple versions; no<br>
Python.org -- build from source<br><br>

Result - two main choices:<br>
Python on Windows - PyCharm on Windows -- default<br>
virtually impossible to compile packages requiring C and Fortran on Windows (e.g. BLAS/LAPACK); 
a million versions of Microsoft Visual Studio; <br>
Powershell commands different than terminal;<br>
some challenges; started here... kind of the default for Windows Users<br><br>

Python on WSL2 -  - PyCharm on Windows <br>
use linux based python; 
possible! to install C-extensions
easier to leverage code from others
WSL2 <--> Win 10 IO extremely slow!  --> impacts usage of PyCharm based on which file system you are using


Python on WSL2 - challenges<br>
PyCharm connection to WSL2 slow from Windows -> WSL2

mapped file reference - e.g. //wsl<br>
debugger fails -- file path mapping issue between Linux and windows<br>

mapped drive?  e.g. w: -->

SSH - system python (shadow copy) -- <br>
debugger fails -- SSH env does not load SSH user ENV vars from WSL2 -- required by program<br>
-- why?  impossible to upgrade linux system python<br>
-- why? impossible to replace linux system python<br>
-- downside -- does not use venv (like rest of project environments)<br>
-- downside -- only one project at a time (as all packages are installed to local system python)<br>
-- downside -- env vars for use logged in are not automatically loaded<br>
-- downside -- SSH remote copies files to tmp dir; takes very long time for large projects (e.g. anything with node)<br>
```
# sourcing local virtualenv does not seem to work /home/chris/dev/urban-robot/venv/bin/python3.8 "$@"
/usr/local/bin/python3.8
```

SSH - venv
/home/chris/dev/urban-robot/venv/bin/python3.8 <br>
no env vars<br>

SSH - venv / attempt to get SSH user env vars<br>
map to bash script at project root:  wsl_bash_source_python_and_env.sh
contains one line:   /home/chris/dev/urban-robot/venv/bin/python3.8 "$@" <br>

OTHER ISSUES<br>
no nickname multiple WSL environments - they are all UBUNTU2004 (n)<br><br>

System env vars should be there - but are not<br>


**references**<br>
WSL IO speed - https://github.com/microsoft/WSL/issues/4197<br>
recommend use real linux instead:  https://medium.com/for-linux-users/wsl-2-why-you-should-use-real-linux-instead-4ee14364c18<br>
