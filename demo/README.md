<h3 align="center">Demo Examples</h3>

## Why a demo section?

This section's purpose is to illustrate the features of my software and how the provided demoPic deteriorates after certain variables are tweaked in the configuration. While the current features are very basic, as my software becomes more advanced my goal is to flesh out this section to give a quick rundown to anyone curious what this software can do beyond running it themselves. 

This is designed to be pictographic in nature and as such more in-depth explanations can be found in the wiki.

Note I am using maxVari to denote the spread of data from a point. So a maxVari of 3 has at most points of 3 units away from it. Because of how numpy randInt works, the upper end is actually exclusive so the lower end is 3 units away while the upper is 2 units away. This will be fixed in the next patch, though for the purposes of the demo I assumed exclusivity.

## Original Image

<p align="center">
    <img src="https://raw.githubusercontent.com/mrcogllrdo/PixelShift/master/demo/demoPic.jpg" alt="Original Demo Pic" width="630" height="354">
</p>


## 1 Pass, MaxVari 1

<p align="center">
    <img src="https://raw.githubusercontent.com/mrcogllrdo/PixelShift/master/demo/pass1max1.jpg" alt="After 1 pass with maxVari 1" width="630" height="354">
</p>

I circled in red an artifact that popped up that I think is particularly interesting. There is clearly no red in the original picture, yet there's a blob of red in the altered image. This is something to keep in mind when we later analyze images to see how similar they are to each other.

For a quick explanation as to how this red blob appeared, I opened up the approximate location in Paint and sampled the area to get an idea of the RGB values of the region. Here's what I found:

<p align="center">
    <img src="https://raw.githubusercontent.com/mrcogllrdo/PixelShift/master/demo/noRed.jpg" alt="Area outlined in particular" width="630" height="354">
</p>

Since the red value of the region is 0 and we're changing it by -1 or 0, when we add -1 then it rolls over to 255; this causes the pixel to have RGB values (255, 3, 9), causing it to have a pronounced reddish look. Also note how a good chunk of the black disappeared; this is because black is characterized by (0,0,0) and there's a 50% chance an RGB value will change, leading to a 12.5% chance a pixel will remain black (we're not including "good enough" cases like (1,1,1) that looks black and has 100% chance to stay black).

## 1 Pass, maxVari 20

<p align="center">
    <img src="https://raw.githubusercontent.com/mrcogllrdo/PixelShift/master/demo/pass1max20.jpg" alt="After 1 pass with maxVari 20" width="630" height="354">
</p>

There are a lot of red artifacts now and there's less black compared to a maxVari of 1 since "good enough" doesn't cut it anymore. Green is also popping up in the blue since they're relatively close with this particular strain of blue. Something interesting to observe is when this image is compared with another that has instead been passed 4 times with a maxVari 5:

<p align="center">
    <img src="https://raw.githubusercontent.com/mrcogllrdo/PixelShift/master/demo/pass4max5.jpg" alt="After 4 passes with maxVari 5" width="630" height="354">
</p>

The new image doesn't seem to have as much green in some places while still retaining the characteristic red artifacts and lack of black pixels (excluding the edges around the blue wave). This could lead one to think that noise can be thought of as noise = passes x maxVari. This is a relationship that will be examined further and contradicted later in the demo but for now can be assumed to be true.

## 10 Passes, maxVari 20

<p align="center">
    <img src="https://raw.githubusercontent.com/mrcogllrdo/PixelShift/master/demo/pass10max20.jpg" alt="After 10 passes with maxVari 20" width="630" height="354">
</p>

Even the black edges around the blue wave are starting to disappear and it's becoming tougher to notice the inside of the wave as being blue. Let's compare this to an original that has been passed 20 times with a maxVari of 10:

<p align="center">
    <img src="https://raw.githubusercontent.com/mrcogllrdo/PixelShift/master/demo/pass20max10.jpg" alt="After 20 passes with maxVari 10" width="630" height="354">
</p>

The black edges are still noticeable and the inside is clearly blue. This seems rather reminiscent of 1 pass with maxVari 20 except it has a lot more red thrown in. Still, the relationship doesn't truly fail until you reach higher passes and maxVari.

## 20 passes, maxVari 35

<p align="center">
    <img src="https://raw.githubusercontent.com/mrcogllrdo/PixelShift/master/demo/pass20max35.jpg" alt="After 20 passes with maxVari 35" width="630" height="354">
</p>

At this point even the gridlines are gone. While I'm not 100% sure it can be truly said to be practically indistinguishable from noise, at first glance it seems to be good enough. The same cannot be said for an image with 35 passes and maxVari 20:

<p align="center">
    <img src="https://raw.githubusercontent.com/mrcogllrdo/PixelShift/master/demo/pass35max20.jpg" alt="After 35 passes with maxVari 20" width="630" height="354">
</p>

While it's a bit tough to say what the original image was, the characteristic wave is still noticeable and the gridlines can still be made out. This is most certainly not indistinguishable from noise and therefore is clear proof that noise cannot be defined as passes x maxVari. In fact, the key factor is maxVari and NOT passes.

## 2 passes, maxVari 100

<p align="center">
    <img src="https://raw.githubusercontent.com/mrcogllrdo/PixelShift/master/demo/pass2max100.jpg" alt="After 2 passes with maxVari 100" width="630" height="354">
</p>

This scramble is clearly much better than 10 passes with maxVari 20. So what happened? A more in-depth explanation can be found in the wiki once it's added, but essentially there's a chance every pass you "undo" whatever happened prior. An example is 1 pass with maxVari 3 vs 3 passes with maxVari 1. If the goal is to reach -3 from a starting value of 0 then 1 pass with maxVari 3 has a chance of 1/6 due to (-3, -2, -1, 0, 1, 2), while 3 passes with maxVari 1 has to hit -1 thrice in a row, or 1/8.

Since it's more likely to reach -3 from 1 pass with maxVari 3 than it is from 3 passes with maxVari 1, and 1 pass with maxVari 3 yields a uniform distribution, then the resulting distribution from 3 passes with maxVari 1 will not be uniform.