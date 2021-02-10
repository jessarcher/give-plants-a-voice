# Give Plants a Voice

Source code for my "Give Plants a Voice" project that I created as part of [Mark Rober's Creative Engineering](https://monthly.com/mark-rober-engineering/) course. Made together with my partner, [Lisa Tassone](https://github.com/lisatassone).

## Watch a demo

[![Demo of Give Plants a Voice](https://img.youtube.com/vi/-QyKdW8opks/0.jpg)](https://youtu.be/-QyKdW8opks)

## How it works

On booting, I have set up the Raspberry Pi to start the `main.py` script using a systemd service (I've included an example in the repo).

The script runs an infinite loop that continuously polls the moisture level and the motion detector to decide whether it needs to ask for water or say thank you.

It will continue getting more disgruntled the longer it goes without water. The time between escalating is configurable.

Because the moisture sensor can fluctuate a little bit, there is an upper and lower threshold. The level needs to drop below the lower threshold before it will start getting disgruntled, however the level will need to go above the upper threshold before it will say thank you. This avoids it flip-flopping between being happy and not happy.

I have also included an RGB LED to visually see roughly where the moisture level is, which is also a nice visual indicator that it's actually running!

## Parts used

* Raspberry Pi 2 Model B+
* [Anker Soundcore Mini](https://www.anker.com/products/variant/soundcore-mini/A3101111) Speaker - This was the smallest and cheapest actively powered speaker with aux input that I could get in time for the course. Ultimately I'd like to get a hat for the Raspberry Pi with a small amplifier so that I could use a small passive speaker instead.
* [MCP3008 Analog to Digital Convertor](https://www.microchip.com/wwwproducts/en/MCP3008) - The Raspberry Pi doesn't have an analog inputs like the Ardunio, which the moisture sensor needs to report the specific level (rather than a binary wet/not wet)
* [Soil Moisture Sensor](https://www.dfrobot.com/product-599.html)
* [PIR Motion Detector Module](https://www.jaycar.com.au/arduino-compatible-pir-motion-detector-module/p/XC4444)
* RGB LED
