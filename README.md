
[![YouTube Channel Views](https://img.shields.io/youtube/channel/views/UCz5BOU9J9pB_O0B8-rDjCWQ?label=YouTube&style=social)](https://www.youtube.com/channel/UCz5BOU9J9pB_O0B8-rDjCWQ)

[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/v_e_e_b/)


#  IR-See

Infrared (IR) photography with a Raspberry Pi NoIR Camera Module 3. 

This is intended to be a resource for making something that can give some pointers for easily capturing infrared images using a digital sensor.
 
## Hardware

- Raspberry Pi
- Camera Module 3 (NoIR)        (12 Mp Sony IMX708 sensor)
- 720 nm Filter                 (Blocks out most visible light)

## Running

The code uses autofocus and auto exposure unless told otherwise. To override these defaults, there are a couple of command line flags that you can use,
for more details run

``` ./main.py -h```

## Post processing 

The 720 nm filter means that there will be some visible red light that leaks into the image. 

- Red/Blue channel swap.

## Video

## Acknowledgements

The motivation for dipping a toe into IR photography came from a chat with **bj52** and others on **#photogeeks** on **irc.libera.chat**
