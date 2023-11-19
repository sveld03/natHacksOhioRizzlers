# natHacks EEG P300 Truth Elicitor

### Setup

1. The subject plays the role of a convicted criminal. We know they had an accomplice, and we have narrowed the search down to **10 suspects**.

2. The subject will be presented with 10 folded pieces of paper. Each piece of paper has a different face on it. The subject will choose one of these 10 images, such that only they know which image they have chosen. This will be the face of their accomplice.

3. To properly assume their role, the subject will be briefed on their relationship with their accomplice, so as to generate an emotional association with the image of their accomplice.
  
4. The 3 safes will be set aside (todo: test in sight setting vs out of sight setting).

5. The subject will then engage with the Truth Elicitor by looking at the **GUI** while pressing the correseponding **buttons**.

##### Blue Safe
- contains a blue, rectangular credit card
- associated with the blue, square button
##### Red Safe
- contains a red, trapezoidal box cutter
- associated with the red, triangular button
##### Yellow Safe
- contains a yellow, cylindrical tube of chapstick
- associated with the yellow, circular button

##### GUI
- once initiated, the GUI will display a black screen for 3 seconds
- the GUI will then randomly display one of the following images for 0.5 seconds:
    - an image of a blue square
    - an image of a red triangle
    - an image of a yellow circle
- the user will then react as rapidly as possible to press the physical button corresponding to the image displayed on screen
- the process then repeats for the desired number of iterations

##### Data Collection
- the user will wear an EEG headset while engaging with the truth elicitor
- when a particular image is shown to the user, the EEG response to that image will be recorded and associated with that image
- the average EEG response to each image will be accumulated and averaged over time for analysis

##### EEG Configuration
- CH1-C3, CH2-Cz, CH3-C4, CH4-P3, CH5-Pz, CH6-P4, CH7-O1, CH8-O2
- 4th order butterworth bandpass filter between 0.1 Hz and 12.5 Hz
