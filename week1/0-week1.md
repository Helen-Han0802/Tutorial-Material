## Week 1


### Why coding?
* Humans are slow and lazy
* Humans make mistakes from time to time. When the manual workload is huge, it's costly for people double check/reproduce


### Version Control, File Management and Project Management
* (This is heavily based on my personal experiences as research assistant to professors in economics discipline and doing my own research)

* Version Control, File Management 
  - Dropbox (or anyother app can synchronize docs for all members involved)
  - Seperate folders for different functions
 
* Task Management
  - Email is not a good tool for task management
  - Use github instead

### Software/Packages installation (Anaconda/Jupyter Notebook/Python/Chrome Browser...)


#### Github
  - Install Git 
    + For Windows: go to https://gitforwindows.org/, hit "Download" and install using default setting
    + For Mac: (every Mac already has git installed; below is the solution if you need to *upgrade* git)
      
      * 1) Step 1 - Install Homebrew (https://brew.sh/)
        - I recommand you to install Homebrew first, it would make your coding life more easier: 
        - Copy & paste the following into the terminal window and hit Return
          ```  
          /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
          ```  
        - You will be offered to install the Command Line Developer Tools from Apple. Confirm by clicking Install. After the installation finished, continue installing Homebrew by hitting Return again
      
      * 2) Step 2 – Install Git:
        - Copy & paste the following into the terminal window and hit Return
          ```  
          brew install git
          ``` 
#### GitHub Desktop App          
          
You can use GitHub Desktop for a nice graphical interface (https://desktop.github.com/ ). In Lecture 1 I showed how to use the Mac version of GitHub desktop.
The below link shows another good tutorial
https://programminghistorian.org/en/lessons/retired/getting-started-with-github-desktop


Alternatively, you can use the command line options:

#### Github Command Line Option
  - register (please remember your username and password)
  
  - set up Git:
    ```  
    git config --global user.name "Your Name"
    git config --global user.email "youremail@domain.com"

    ```
  
  - other commands
    ```  
    cd /Users/wwp/Desktop/
    git clone https://github.com/HKUST-SOSC4300-5500/Tutorial-Material
    git status
    git add 
    git add
    git commit -m "test"
    git push
    git pull  
    ```
  - Read more: http://www.codebind.com/linux-tutorials/basic-git-commands-list/ 


#### Anaconda (for Python, Jupyter Notebook, R, Java and more)
  

  * Conda installation

    - what is anaconda: Package, dependency and environment management for any language---Python, R, Ruby, Lua, Scala, Java, JavaScript, C/ C++, FORTRAN.
    
    - Conda is an open-source package management system and environment management system that runs on Windows, macOS, and Linux. Conda quickly installs, runs, and updates packages and their dependencies. Conda easily creates, saves, loads, and switches between environments on your local computer. 

    - It was created for Python programs but it can package and distribute software for any language. Conda as a package manager helps you find and install packages. If you need a package that requires a different version of Python, you do not need to switch to a different environment manager because conda is also an environment manager. 

    - With just a few commands, you can set up a totally separate environment to run that different version of Python, while continuing to run your usual version of Python in your normal environment.
  
    - So why Anaconda? it's easy to control your coding environment, which is key to reproduce people's results in your machine
    - [History Installers](https://repo.anaconda.com/archive/)
    - Which Version to install? Choose Anaconda3 instead of Anaconda2!
    - Highly recommend to install Python 3.6 version or above , I'll use this version this semester Anaconda3-2019.03
      + For Mac: https://repo.anaconda.com/archive/Anaconda3-2019.03-MacOSX-x86_64.pkg
      + Windows: https://repo.anaconda.com/archive/Anaconda3-2019.03-Windows-x86_64.exe

    - Not sure about your operation system is 32-bit or 64 bit? check [this](https://www.akaipro.com/kb/32-bit-vs-64-bit-your-questions-answered/)
    - More detailed guidelines for conda, see [link](https://github.com/conda/conda/tree/master/docs/source/user-guide)
    
    - After installation, open Terminal (mac) or Anaconda Prompt (windows) and run the following codes
  
  * Basic Operations (installing packages/ using python)
  ```
  conda info
  conda version
  python
  import redis 
  import torch
  import tensorflow 
  conda install -c conda-forge selenium
  conda install -c conda-forge redis 
  conda install pytorch torchvision -c pytorch
  pip3 install redis
  ```

 * Python version control: To install a different version of Python without overwriting the current version, create a new environment and install the second Python version into it. For example, the below codes created `snakes`
  ```
  conda info --envs
  conda create -n snakes python=3.5 ## create a new environment called snakes
  conda activate snakes ## activate this new environment
  python --version ## show python version to test what we have successfully shifted to the new environmnet
  conda deactivate
  conda create -n snakes2 python=2.7
  conda activate snakes2
  conda deactivate
  conda info --envs # check your environment
  conda remove --name snakes2 --all # remove environment
  conda search python
  ```
  
  
  * Problems when installing Anaconda/packages:
    + For Mac, check: 
      - a) /Library/Frameworks/ for potential previous python installation; 
      - b) /Users/[your_username]/anaconda3/lib/python3.6/site-packages or /Users/[your_username]/anaconda3/lib/python3.7/site-packages for packages installation errors 
      - c) OR remove conda completely and reinstall.
       
    + For windows, check: C:\Users\\[your_username]\\anaconda3\\
  

#### Jupyter Notebook (https://jupyter.org/install)
  
  ```
  conda install -c conda-forge jupyterlab
  pip install jupyterlab
  conda install -c conda-forge notebook
  jupyter notebook
  ```

#### Chrome Browser 
  - https://www.google.com/intl/en_hk/chrome/
  - For web scraping analysis

#### Sublime Text 3 
  - (Highly recommended): https://www.sublimetext.com/3 and choose the file to download 
  - Light IDE
  - Install Package control
  - Install packages you need: python3, latex, stata and etc.


#### Pycharm (https://www.jetbrains.com/pycharm/download) and download the "Community" version 
  - Not recommended if your computer RAM is small.


### Final checks
* Open and run '1-Hello-World.ipynb'

