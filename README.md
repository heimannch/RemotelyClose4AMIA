# RemotelyClose4AMIA
Code for the solution submitted to AMIA Student Challenge 2018.

You can access the working version of this code at: http://remotelyclose.hopto.org:42042/forms/

This website runs in Django, and this repository contains all the files required by this platform, although only two of them matter for the purposes of our project.

The code developed for this project is available at the following files: 
- main.py: this module contains all the functions to process the input received from the Remotely Close platform
- views.py: collects the input information and outputs which notification would be triggered by the Remotely Close platform. In this prototype, the input information (such as minutes of exercise per day, perceived progress score) is informed by the user.

The working version of the Remotely Close for TKA would receive all this information from the current Remotely Close platform (https://www.remotelyclose.com/). More information about the whole framework is available in the Supplementary Materials, especially at Appendix B.
