from picamera2 import Picamera2, Preview
import time
import os

index = 1
while os.path.exists("./images/capture%s.dng" % index):
    index += 1
picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
capture_config = picam2.create_still_configuration(raw={}, display=None)
picam2.configure(camera_config)
picam2.start_preview(Preview.NULL)
# Exposure time
picam2.set_controls({"ExposureTime": 10000})
# AfMode: Set the AF mode (manual, auto, continuous)
# LensPosition: Manual focus, Set the lens position.
# picam2.set_controls({"AfMode": 0, "LensPosition": 100.0})
picam2.start()

time.sleep(2)
r = picam2.switch_mode_capture_request_and_stop(capture_config)
# r.save("main", "full.jpg")

savestring = "./images/capture" + str(index) + ".dng"
r.save_dng(savestring)
