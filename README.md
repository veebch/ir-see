
![Vitra Museum, Germany. 720nm](/images/vitrasmall.png)

[![YouTube Channel Views](https://img.shields.io/youtube/channel/views/UCz5BOU9J9pB_O0B8-rDjCWQ?label=YouTube&style=social)](https://www.youtube.com/channel/UCz5BOU9J9pB_O0B8-rDjCWQ)

[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/v_e_e_b/)


#  Night Vision

Infrared (**IR**) photography and video with a 12 Megapixel Raspberry Pi **NoIR Camera Module 3**. 

This is intended to be a resource that gives some pointers for easily capturing infrared images using a digital sensor, as well as simple ways to post-process the still images. Invariably, people will ignore all that stuff in favour of making a nightvision camera.

The script is basic. It would be relatively easy to add a physical preview window to the camera body, but for now, this is plenty. The camera is operated headless and is just intended as a simple proof-of-concept. If you're connecting to the Raspberry Pi via SSH don't forget to use X forwarding if you want to see the preview window.
 
## Hardware
### For the Still Photography
- Raspberry Pi 4                (a 3 would be fine)
- Camera Module 3 (NoIR)        (12 Mp Sony IMX708 sensor)
- 720 nm Filter                 (Blocks out almost all visible light, opt for 850nm if you want no colour at all)

### For the 'all seeing eye' video recorder
Since the first video on still photography, we've got our hands on a Raspberry Pi 5. There is a large bump in terms of CPU speed and IO performance between the 4 and the 5 so we we're using the fastest one we've got. We're also using some simple IR LEDs. These are external to the Pi, but would be easy to integrate by using a relay switch.

- Raspberry Pi 5
- Camera Module 3 (NoIR)
- 830nm LEDs (20x 3w)           (These supply the light that your eyes can't see but the camera can)
- Constant current power supply (700ma To power the LEDS - Note that we don't use a constant voltage supply) 

The LEDS are wired together in **series** and connected to the power supply. 

## Installing

Clone this repository and install dependencies using the commands

``` 
cd ~
git clone https://github.com/veebch/ir-see
```


## Running

To run, 

``` 
cd ir-see
python3 photo.py -p 2>'log.txt'
```

This runs the code with a preview window and sends the stderr to a file called 'log.txt' (for debugging purposes). 
Captures will be stored in the `./images` directory:
- Stills: 12 Megapixel digital negative (**dng**) files for post-processing described below
- Video: mp4 video files in **HD** (1920x1080) resolution


If you want to manually specify exposure time, focus position or ISO sensitivity, you can get details on those flags using

```
python3 photo.py -h
```

## Post processing Still Images

For basic postprocessing: 

1. Import the digital negative into your image editor of choice and open the channel mixer.
2. Swap the green and blue channels. 
3. Following that, look at a **HSL** (Hue-Saturation-Lightness) adustment to bring out/shift the little colour you have in the image.

In general though, just play with the image until you have something you're happy with.

## Videos

A walk-through with a few photos at the end.

[![Explainer video](http://img.youtube.com/vi/uvolslfKxfg/0.jpg)](http://www.youtube.com/watch?v=uvolslfKxfg "Video Title")

## Acknowledgements

The motivation for dipping a toe into IR photography came from a chat with **bj52** and others on **#photogeeks** on **irc.libera.chat**. 
