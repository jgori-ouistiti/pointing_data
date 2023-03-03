Summary:

Most probably, you need the following columns:
time: Timestamp that was actually used for the analysis.
y: Position of pointer on screen in meters
sgy: Pointer position on screen in meters as filtered with Savitzky-Golay
sgv: Pointer velocity on screen in meters as filtered with Savitzky-Golay
sga: Pointer acceleration on screen in meters as filtered with Savitzky-Golay
target: Target center in meters
widthm: Width of target in meters
distancem: Distance between target centers in meters

Overview of all columns:

These columns were not used and can be ignored:
t, participant,variable,variation,task,

trial: Trial number within the current distance/width combination
globaltrial: Overall trial counter of this participant
ID: Index of difficulty of the task log_2(D/W+1)
distance: Distance between target centers in pixels
width: Width of targets in pixels
targetleft: Left border of current target
targetright: Right border of current target
timestamp: Redundant timestamp that was not used
mousex: Aggregated mouse displacements along x axis
mousey: Aggregated mouse displacements along y axis
cursorx: Position of pointer on the screen (subpixel accuracy, in px)
button: Whether a button was pressed in this frame
trialsuccess: Whether the trial was finished successfully in this frame
pause: Whether participants enabled pause state
experimenterattention: Whether the program is waiting for the experimenter to start the next task

These columns were not used and can be ignored:
fitts2prep,fitts2wait,trialstarts,trialtime,

time: Timestamp that was actually used for the analysis.

These columns were not used and can be ignored:
,glfwtime,dx,

y: Position of pointer on screen in meters
target: Target center in meters
widthm: Width of target in meters
distancem: Distance between target centers in meters
sgy: Pointer position on screen in meters as filtered with Savitzky-Golay
sgv: Pointer velocity on screen in meters as filtered with Savitzky-Golay
sga: Pointer acceleration on screen in meters as filtered with Savitzky-Golay

meansurgeerror,meansurgepcttime,meanreactiontime,mediansurgeerror,mediansurgepcttime: Some overall statistics of the task that can be ignored
