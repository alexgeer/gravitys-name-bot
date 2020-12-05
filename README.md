# Gravity's NameBot
Randomly generated possible names for a Thomas Pynchon character. This twitter bot posts them a few times a day. The docker image is currently running on an EC2 instance.
[@gravitysNameBot](https://twitter.com/gravitysNameBot)


## Set up virtual env
This projecct uses a virtual environment (**virtualenv**) to avoid depending on system-wide packages
To create the virtual environment inside the project directory:

```
python3 venv venv
source ./venv/scripts/activate
pip install -r requirements.txt
```