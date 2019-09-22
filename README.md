# Minecraft automation scripts

The scripts in this project are used for the automation of AFK Minecraft actions. The scripts have been tested
in Minecraft 1.14.4 on Windows, but they could work in Linux and macOS X depending on the compatibility of the 
libraries used (mainly [pywinauto](https://pywinauto.readthedocs.io/en/latest/)).

## Prerequisites

### Windows

1. The latest stable release of [Python 3](https://www.python.org/downloads/release/python-374/) (3.7.4 at 
the moment of writing).
2. [cmder](https://cmder.net/) to have a better experience with the command line.

## Prepare environment

### Windows

Execute the following instruction only once, when you start using the scripts.

From the command line:

1. Install the latest version of pip with `pythom -m pip install --upgrade pip`,
2. Install `virtualenv` with `pip install virtualenv`,
3. Navigate to the scripts directory.
4. Define a new virtual environment in the script directory with `virtualenv .env`.
5. Activate the virtual environment with `.\.env\Scripts\activate.bat`.
6. Run `pip install -r requirements.txt`.

For the duration of the session in commander, the virtual environment will contain all the libraries necessary to run
the scripts. To deactivate the environment run `.\env\Scripts\deactivate.bat`.

## Load environment

### Windows

Execute the following instruction every time you want to start any of the automation scripts.

From the command line:

1. Navigate to the scripts directory.
2. Activate the virtual environment with `.\.env\Scripts\activate.bat` (`source .env/bin/activate` in Linux/macOS)

Now you can activate any of the scripts.

## Scripts

### Auto Fisher

**Script name:** `auto_fisher.py`

The `auto_fisher.py` script is designed to work with [xisumavoid's AFK fish farm](https://www.youtube.com/watch?v=hTAHK2XnpQs)
for 1.14. The script does nothing more than sending a right-click event to a Minecraft application instance every 0.1
seconds. Arguably, the script could be used for any AFK automation that requires a steady and constant amount of 
right-clicks.

To start the AFK fishing:

1. Start commander and load the the environment as indicated at [Load environment](#load-environment).
2. Build the fish-farm according to Xisumavoid's design. Please take note from the tutorial that you need a fishing rod
enchanted with at least _Mending_ in order to AFK without any limits.
3. Disable auto-pausing in Minecraft with `F3-P`.
4. Point the UI radical to the note-block.
5. `Alt-Tab` to the command line.
6. Start the script with `python auto_fisher.py`.
7. Profit!

As long as the radical in the player UI points to the note-block and a fishing-rod is selected, the script will keep
sending right-clicks to Minecraft every 0.1 seconds starting AFK farming. Minecraft can be minimised while the script is running
and I recommend to disable shaders (if you are using Optifine or other graphical clients) in order to reduce power consumption and reduce GPU utilisation.

To stop the script, simply interrupt the script with `Ctrl-C`.
