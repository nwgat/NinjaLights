# NinjaLights
Dim all lights when a movie is playing in Kodi 
work in progress, still need to code the code part

## Features
* Dim all lights

## Usage
The first time the `Bridge` class is used, it will discovery the bridge and then initiate the necessary API username registration. 
```
import hue
h = hue.Bridge()
```
You'll be prompted to press the link button on the Hue Bridge.
```
Bridge located at 192.168.0.7
>>> Press link button on Hue bridge to register <<<
```
