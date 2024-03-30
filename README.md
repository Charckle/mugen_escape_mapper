# WHAT?
- Mugen, fighting emulator, does not have mapping for the back button, or ESC key, for the controllers
- this is anoying, since with no back button, the game is unplayable with controllers only
- this app maps the back button on any connected controller to the escape button

# WHY?
- because: "Just use a third party mapping app" sounds stupid and an overkill, to get basic functionalities
- this code has 32 lines and it does the job
- all you need is python and pip. the code is transparent, easy to use, and above all, simple

# Install
- `sudo apt-get install python3-tk python3-dev python3 python3-pip
- `pip3 -r requirements.txt`


# Usage
- install the requirements
- `python3 multi.py`
- while the app is running, all the controllers connected before you started the app will have the back button mapped to the escape button
- enjoy playing Mugen with just the controllers
