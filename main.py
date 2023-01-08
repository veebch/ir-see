from picamera2 import Picamera2, Preview
import time
picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
capture_config = picam2.create_still_configuration(raw={}, display=None)
picam2.configure(camera_config)
picam2.start_preview(Preview.NULL)
picam2.start()
time.sleep(2)
r = picam2.switch_mode_capture_request_and_stop(capture_config)
# r.save("main", "full.jpg")
r.save_dng("./images/full.dng")
