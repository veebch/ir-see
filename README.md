
[![YouTube Channel Views](https://img.shields.io/youtube/channel/views/UCz5BOU9J9pB_O0B8-rDjCWQ?label=YouTube&style=social)](https://www.youtube.com/channel/UCz5BOU9J9pB_O0B8-rDjCWQ)

[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/v_e_e_b/)


#  IR-See

Infrared (IR) photography with a Raspberry Pi NoIR Camera Module 3. 

This is intended to be a resource for making something that can give some pointers for easily capturing infrared images using a digital sensor. It would be easy to add a preview window, but for now, this is plenty.
 
## Hardware

- Raspberry Pi
- Camera Module 3 (NoIR)        (12 Mp Sony IMX708 sensor)
- 720 nm Filter                 (Blocks out most visible light)
## Installing

Clone this repository and install dependencies using the commands
``` 
cd ~
git clone https://github.com/veebch/irsee
python3 -m pip install picamera2
```

## Running

To run, 

``` ./main.py```

if you want to manually specify exposure time, focus position or ISO sensitivity, you can get details on those flags using

```
./main.py -h
```
## Post processing 

The 720 nm filter means that there will be some visible red light that leaks into the image. 

- Red/Blue channel swap.

## Video

## Acknowledgements

The motivation for dipping a toe into IR photography came from a chat with **bj52** and others on **#photogeeks** on **irc.libera.chat**
