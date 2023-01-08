#!/usr/bin/python3
from picamera2 import Picamera2, Preview
import time
import os
import argparse

argParser = argparse.ArgumentParser()
argParser.add_argument("-e", "--exposure", help="exposure time")
argParser.add_argument("-f", "--focus", help="lens position as percentage")
argParser.add_argument("-i", "--iso", help="iso sensitivity")
args = argParser.parse_args()


print("args=%s" % args)

index = 1
while os.path.exists("./images/capture%s.dng" % index):
    index += 1
picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
capture_config = picam2.create_still_configuration(raw={}, display=None)
picam2.configure(camera_config)
picam2.start_preview(Preview.NULL)
# Exposure time
if args.exposure is not None:
    print("Exposure time in us:",args.exposure)
    picam2.set_controls({"ExposureTime": int(args.exposure)})

if args.iso is not None:
    picam2.set_controls({"AnalogueGain": int(args.iso)/100})

# AfMode: Set the AF mode (manual, auto, continuous)
# LensPosition: Manual focus, Set the lens position.
if args.focus is not None:
    picam2.set_controls({"AfMode": 0, "LensPosition": int(args.focus)})
else:
    print("Autofocus")
    picam2.set_controls({"AfMode": 1})
picam2.start()

time.sleep(2)
r = picam2.switch_mode_capture_request_and_stop(capture_config)
# r.save("main", "full.jpg")

savestring = "./images/capture" + str(index) + ".dng"
r.save_dng(savestring)
