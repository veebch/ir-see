#!/usr/bin/python3
from picamera2 import Picamera2, Preview
from libcamera import controls
import time
import os
import argparse

argParser = argparse.ArgumentParser()
argParser.add_argument("-e", "--exposure", type=int, help="exposure time (us)")
argParser.add_argument("-f", "--focus", type=float, help="lens position (0 for infinity, 10 for 10cm)")
argParser.add_argument("-i", "--iso", type=int, help="iso sensitivity")
argParser.add_argument("-p", "--preview", help="preview window", action='store_true')
args = argParser.parse_args()


print("args=%s" % args)

index = 1
while os.path.exists("./images/capture%s.dng" % index):
    index += 1
picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
capture_config = picam2.create_still_configuration(raw={}, display=None)
picam2.configure(camera_config)
time.sleep(2)
if args.preview is True:
    picam2.start_preview(Preview.QT)
else:
    picam2.start_preview(Preview.NULL)
# Exposure time
if args.exposure is not None:
    print("Exposure time in us:",args.exposure)
    picam2.set_controls({"ExposureTime": int(args.exposure)})

if args.iso is not None:
    picam2.set_controls({"AnalogueGain": int(args.iso)/100})

picam2.set_controls({"AfMode": controls.AfModeEnum.Manual, "LensPosition": 0)  

picam2.start()

time.sleep(2)
# AfMode: Set the AF mode (manual, auto, continuous)
# LensPosition: Manual focus, Set the lens position.
# 0 is infinity, 10.0 is 10cm
if args.focus is not None:
    picam2.set_controls({"AfMode": controls.AfModeEnum.Manual, "LensPosition": int(args.focus)})
else:
    print("Autofocus")
    picam2.set_controls({"AfMode": controls.AfModeEnum.Auto})

time.sleep(10)
r = picam2.switch_mode_capture_request_and_stop(capture_config)
savestring = "./images/capture" + str(index) + ".dng"
r.save_dng(savestring)
time.sleep(2)  # This little sleep seems to prevent QT from getting upset on close
