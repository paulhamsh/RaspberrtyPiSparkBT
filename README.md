# RaspberrtyPiSparkBT
Raspberry Pi Bluetooth connection to Positive Grid Spark amp

Created to run on the Raspberry Pi 400 as a test to connect to the Spark amp


Install dependencies:

sudo apt-get update
sudo apt-get install bluetooth libbluetooth-dev
python3 -m pip install pybluez


Then use the script to connect to the Spark amp - currently it rotates the tone presets!

Based on code from tinderboxpedal here: https://github.com/jrnelson90/tinderboxpedal

