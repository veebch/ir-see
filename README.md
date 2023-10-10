
![Vitra Museum, Germany. 720nm](/images/vitrasmall.png)

[![YouTube Channel Views](https://img.shields.io/youtube/channel/views/UCz5BOU9J9pB_O0B8-rDjCWQ?label=YouTube&style=social)](https://www.youtube.com/channel/UCz5BOU9J9pB_O0B8-rDjCWQ)

[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/v_e_e_b/)


#  IR-See

Infrared (IR) photography with a Raspberry Pi NoIR Camera Module 3. 

This is intended to be a resource that gives some pointers for easily capturing infrared images using a digital sensor, as well as simple ways to post-process them. 

The software is bare-bones. It would be relatively easy to add a preview window to the body, but for now, this is plenty. The camera is operated headless and is just intended as a simple proof-of-concept. Make sure you use SSH with X forwarding so that you can see the preview window.
 
## Hardware
### For the Photography video
- Raspberry Pi                  (Used a Raspberry Pi 4, but this is overkill, a 3 would most likely be fine)
- Camera Module 3 (NoIR)        (12 Mp Sony IMX708 sensor)
- 720 nm Filter                 (Blocks out almost all visible light, opt for 850nm if you want no colour at all)

### For the 'all seeing eye' video
- 830nm LEDs (20x 3w)
- Constant current power supply for the LEDS
- Raspberry Pi 5

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
python3 main.py
```

Captures will be stored in the `./images` directory.

If you want to manually specify exposure time, focus position or ISO sensitivity, you can get details on those flags using

```
python3 main.py -h
```

## Post processing 

For basic postprocessing: 

1. Import the digital negative into your image editor of choice and open the channel mixer.
2. Swap the green and blue channels. 
3. Following that, look at a HSL adustment to bring out/shift the little colour you have in the image.

In general though, just play with the image until you have something you're happy with.

## Video

A walk-through with a few photos at the end.

[![Explainer video](http://img.youtube.com/vi/uvolslfKxfg/0.jpg)](http://www.youtube.com/watch?v=uvolslfKxfg "Video Title")

## Acknowledgements

The motivation for dipping a toe into IR photography came from a chat with **bj52** and others on **#photogeeks** on **irc.libera.chat**. 
