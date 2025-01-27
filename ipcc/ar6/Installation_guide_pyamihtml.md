﻿Here's an installation guide for the "pyamihtml" package through Windows Terminal using either Command Prompt or Windows PowerShell:

Step 1: Downloading Python from [www.python.org](http://www.python.org)

1. Go to [www.python.org](http://www.python.org) and hover over the "Downloads" tab.
1. Click on the option to download the latest version of Python for your Windows system.
1. Once the file is downloaded, double click on it to launch the Python for Windows setup.
1. In the Python setup dialog box, make sure to check the option "Add python.exe to PATH" to enable accessing Python from the command line.
1. Click on "Install now" and wait for a few minutes while Python setup completes the installation.

Step 2: Verify Python installation

1. Open your command line interface (CMD or PowerShell).
1. Type either of the following commands:

python --version

or

py --version

1. This command should display the version of Python installed on your machine and verify the successful installation.

Step 3: Installing pip

1. Pip is a package manager in Python that helps you download packages from the Python Package Index (PyPi).
1. Newer versions of Python (starting from Python 3.4) come with pip preinstalled. If you're running an older version, follow these steps to manually install pip from the command line:

` `python -m ensurepip --upgrade

1. To ensure that pip was installed correctly, run the following command:

pip --version

1. If the installation was successful, this command will display the version number of pip.

Step 4: Installing the 'pyamihtml' package through pip

1. In either Command Prompt or PowerShell, paste the following command:

` `pip install pyamihtml

Make sure your computer is connected to the internet as pip will download the package from PyPi.

` `Wait for the installation to complete. To verify that the 'pyamihtml' package was installed, run the following command:

pyamihtml --version

This will display the version of 'pyamihtml' installed. Alternatively, you can run:

pyamihtml --help

1. This will display a list of commands and arguments you can use with 'pyamihtml' to transform or manipulate PDF documents.

Troubleshooting Guide:

Note: You may encounter errors during the installation process. Here are some common errors and their solutions:

Error 1: Trouble installing Pillow

1. Check the installed version of 'pyamihtml' by running the following command:

pyamihtml --version

The latest version as of today is 0.0.5. The output should display the version number.

` `If you get an error or see an older version of 'pyamihtml' installed, uninstall it using the following command:

pip uninstall pyamihtml

Then install the latest version using:

pip install pyamihtml==0.0.5

1. ` `If the pip install command throws an error, try the following command:

` `py -m pip install pyamihtml==0.0.5

Run the following command to ensure 'pyamihtml' is running smoothly:

pyamihtml --help

This should display a list of subcommands and arguments that you can use with 'pyamihtml'.

If you encounter the error "Failed building wheel for Pillow" or related errors, properly install Pillow by running:

pip install Pillow

or

py -m pip install Pillow

This should install Pillow into your system. Now, you can go back to Step 1 or 2 of our troubleshooting guide and repeat those instructions to properly install 'pyamihtml'.


