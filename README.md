# Psychopy-Functional-Zoom

Files for the Functional Animation and Zoom Animation paradigms.

Experiment tasks designed for use with the following technologies:

- Stimulus presentation computer:
  - Dell 5500 Latitude laptop PC
  - Monitor refresh rate: `60 Hz`
- Stimulus presentation software
  - [Psychopy]([url](https://www.psychopy.org)) version `3.2.4`
- EEG data collection:
  - 32-channel [BrainVision Liveamp system (Brain Products GmbH)]([url](https://www.brainproducts.com/solutions/liveamp/))
  - A photodiode was used to align timing between animation/zoom onset and serial-port trigger signals from stimulus display PC to EEG recording PC.

To run the tasks:

1) Download this repository
   1) Unzip experiment files
   2) Make sure you retain the folder structure present in the repository
      1) The `Break_Images` folder is referenced from the tasks in the current folder structure
2) Open PsychoPy
   1) Open the *Builder* interface of PsychoPy
   2) Select `File -> Open file...`
   3) Navigate to the paradigm experiment folder and select the Psychopy experiment file
      1) Animation task: [Grid.Animation.Task.psyexp](Grid.Animation.Motion/Grid.Animation.Task.psyexp)
      2) Zoom task: [Grid.Zoom.Task.psyexp](Grid.Zoom.Motion/Grid.Zoom.Task.psyexp)
3) Run the task
   1) Click the **Run** button in Psychopy
   2) A window will appear with two tick-box options
      1) `debug`: if selected, an abbreviated presentation number and duration will be used
      2) `amp connected`:
         1) If selected, serial port will be connected to for sending triggers
         2) If not selected, serial port will not be connected to and triggers will be printed to console
