# NinjaLights
Simple 

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
