# Scooby Doo Eyes

This is fun art.

OpenCV is used to reflect back the eyes of the watcher - Scooby Doo style.

![Scooby Doo Eyes](file:///Projects/scooby_doo_eyes/eyes.jpg)

Credits:
* This is inspired by, and re-uses code from [Real-time facial landmark detection with OpenCV, Python, and dlib](https://www.pyimagesearch.com/2017/04/17/real-time-facial-landmark-detection-opencv-python-dlib/) by Adrian Rosebrock 
* Uses [Dlib's](http://dlib.net/) face detection model, trained on data from [Imperial College London](https://ibug.doc.ic.ac.uk/resources/facial-point-annotations/) - _C. Sagonas, E. Antonakos, G, Tzimiropoulos, S. Zafeiriou, M. Pantic.  300 faces In-the-wild challenge: Database and results. Image and Vision Computing (IMAVIS), Special Issue on Facial Landmark Localisation "In-The-Wild". 2016._  **Note: this data set not for comercial use**

## Getting it going

If you know Python, then you may have your own way of getting setup. I suggest using Miniconda Python because it will download the prebuilt libraries required.

A lot of stuff gets download, so it might take a while, but it should be simple.

### Windows (64 bit)

Download [Miniconda3 4.5.4](https://repo.continuum.io/miniconda/Miniconda3-4.5.4-Windows-x86_64.exe).  This installs Python 3.6.5 which is known to work (a dependency is broken in Miniconda 4.7.12 - latest at Nov 2019).

Run the installer and accept all the defaults.

Find and run "Anaconda Prompt" from the Windows menu, and skip down to "Install required packages".

### Other operating systems

Download the relevant Miniconda3 4.5.4 (not Miniconda2) from <https://repo.continuum.io/miniconda/>.

Install by muddling through <https://conda.io/projects/conda/en/latest/user-guide/install/index.html>.

### Install required packages

At the "Anaconda Prompt" enter:

    conda config --add channels conda-forge
    conda install py-opencv scipy imutils dlib pyautogui

This bit takes a while.

### Fetch face detector

At the "Anaconda Prompt" enter:

    pip install wget
    python fetch-model.py

### Run

At the "Anaconda Prompt" enter:

    python scooby_doo_eyes.py

Quit by typing q
