# DeepNugget
A flask SMS bot that uses ImageAI, YOLOv3, and the Twilio API to detect, and deepfry chicken nuggets.

![Insp(pip install deeppyer)  iration](https://i.imgur.com/VhqnbbY.png)  
[![License](https://poser.pugx.org/ali-irawan/xtra/license.svg)](https://github.com/getcake/DeepNugget/blob/master/LICENSE)

Inspired by [Hack Club's](https://hackclub.com/) summer of making random-idea generator! 

# Disclaimer 

Requires an older version of tensorflow in order to run, 
so it's reccomended you create a virtualenv. This is also a potential security risk.

# Requirements

A Twilio account (you can get a trial one for free)  

ngrok

requirements.txt
# Setup

~~~
snap install ngrok

virtualenv coolname  

source coolname/bin/activate  

git clone https://github.com/getcake/DeepNugget.git  

pip3 install -r requirements.txt  

ngrok http 5000

Insert your ngrok url into the webhook page on the Twilio console 

Replace the filler url in deep_nugget.py with your ngrok url

~~~
