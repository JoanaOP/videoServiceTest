# videoServiceTest

## Introduction
The video service is a module developed in python that receives video frames and shows them.

## Installations
In order to run it you must install Python 3.7. We recomend to use PyCharm as IDE for developments.

## Operation modes
The video service can be run in simulation mode. To run the service you must edit the run/debug configuration in PyCharm in order to pass the required arguments to the script. At least two parameters are required: connection_mode (global or local) and operation_mode (simulation or production). In case of global communication mode, a third parameter is requiered indicating the external broker to be used. In case the external broker requieres credentials, two additional parameters must be includes (username and password).

## Commands
The video service can receive only messages with the *videoFrame* topic. The payload of the message will be the frame to show encoded as text.

