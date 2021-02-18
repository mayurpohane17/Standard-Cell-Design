
# Standard-Cell-Design and NLDM using NGSPICE


The flow uses control commands based on ngspice to construct the Non-Linear Delay Model(NLDM) for the custom standard cell. This repo aims to introduce an approach of using open-source resources to do custom cell characterization.

- [Semi-Automated Non Linear Delay Model Generator using NGSPICE](#semi-automated-non-linear-delay-model-generator-using-ngspice)
  - [Prerequisite](#prerequisite)
  - [What is Non Linear Delay Model(NLDM)?](#what-is-non-linear-delay-modelnldm)
    - [Define Cell Rise, Cell Fall, Rise Transition and Fall Transition?](#define-cell-rise-cell-fall-rise-transition-and-fall-transition)
  - [Proposed Flow for Timing Characterization?](#proposed-flow-for-timing-characterization)
  - [Explaining Flow using OR Gate example](#explaining-flow-using-or-gate-example)
    - [NGSPICE File Setup](#ngspice-file-setup)
    - [Process for Text File Creation](#process-for-text-file-creation)
    - [Timing Block .lib Format Generation](#timing-block-lib-format-generation)
    - [Comparison of Timing values from Skywater130nm PDK](#comparison-of-timing-values-from-skywater130nm-pdk)

## Prerequisite 

## What is Non Linear Delay Model(NLDM)?

NLDM is derived from SPICE characterizations and is a highly reliable timing model. The table model is referred to as an NLDM and is used to measure the
delay, performance slew, or other timing checks. Most of the cell libraries used table models to specify the delay and timing checks for different cell timing arcs.
​
For different combinations of input at the cell input pin and multiple output capacitance at the cell output pin, the table provides the delay through the
cell. In a two-dimensional array, where the two independent variables are the input transition and the capacitance of the output load and the entries in the table 
are the delays.
The characterization is performed using the ngspice open source circuit simulator.

### Define Cell Rise, Cell Fall, Rise Transition and Fall Transition? 
The time taken by a signal to increase from 20 percent to 80 percent of its maximum value is known as transition delay or slew. This is referred to as "rise time".
Similarly, it is possible to describe "fall time" as the time taken by a signal to fall from 80 to 20 percent of its maximum value.
​
The time taken for a signal to propagate through a gate or net is the propagation delay.
Therefore, you can call it a "Gate or Cell Delay" if it is a cell.
The time it takes for a signal at the input pin to impact the output signal at the output pin is the propagation delay of a gate or cell.
A delay of 50 percent of the input transition to the corresponding 50 percent of the output transition is calculated for any gate propagation.


## Proposed Flow for Timing Characterization?

## Explaining Flow using OR Gate example
Start with simple schematic design using Xcircuit or any schematic capture tool and generate spice file subckt as shown below               
![Spice File](images/spice_file.png)

Once this file is created, we are ready to perform NGSPICE simulation.

### NGSPICE File Setup
This setup is divided into three sections:
* **Adding Required Libraries and Sub-circuit:** '.include' commands are used for adding the subcircuit and skywater nfet and pfet libraries.
* **Setting up Power Supplies and loads:** Power Supplies VDD and VSS as per the .lib file voltage requirement(1.8V). The Pulse supply type should be provided to the input pin which is considered related to the Output and other input pins need to be biased as they are not affecting the output. Assign a load capacitor(c1) as shown below:
![Test Harness(File Name: or2.cir](images/test_harness.png)

* **Control Commands:** These are the commands provided by ngspice to do sequence simulation with different sets of device parameter values and also helps in post-simulation analysis. Commands shown below for measuring different timing figures:
![Timing Measurement Commands(File Name: or2.cir](images/timing_measure.png)

Also, these commands store these values in a .txt( in 'text_files' folder) for verification and generating .lib based timing format.
### Process for Text File Creation
Follow the Steps:
  1. Make sure text_files folder is empty, otherwise delete the files using `rm` command.
  2. `cd` to the root folder(in which sky130nm.lib exists) and type on the terminal `ngspice ngspice or2_custom/or2_0/or2.cir`
  3. Check all the five files are generated into the text_files folder. This particular folder consisting of different timing .txt file is used by the python file for generating      the .lib type timing block. 
### Timing Block .lib Format Generation
Run this command in the terminal `./scripts/timing.py -loc text_files/ -pin A`
Also, for help, type `./scripts/timing.py -h`

### Comparison of Timing values from Skywater130nm PDK
=======
# Standard-Cell-Design

Custom standard cells are designed for the Skywater130nm node

## Standard Cells
1.And2_1x

2.And3_1x

3.And4_1x

4.And2_2x

5.And3_2x

6.And4_2x

7.a2111oi

8.a311oi

9.a31oi

10.a32oi

## What is Non Linear Delay Model(NLDM)?
NLDM is derived from SPICE characterizations and is a highly reliable timing model. The table model is referred to as an NLDM and is used to measure the delay, performance slew, or other timing checks. Most of the cell libraries used table models to specify the delay and timing checks for different cell timing arcs.

For different combinations of input at the cell input pin and multiple output capacitance at the cell output pin, the table provides the delay through the cell. In a two-dimensional array, where the two independent variables are the input transition and the capacitance of the output load and the entries in the table are the delays. The characterization is performed using the ngspice open source circuit simulator.

## Cell Rise Time, Fall Time, Rise Transition and Fall Transition

The time taken by a signal to increase from 20 percent to 80 percent of its maximum value is known as "rise time". 
The time taken by a signal to increase from 80 percent to 20 percent of its maximum value is known as "fall time".

The time taken for a signal to propagate through a gate or net is the propagation delay. The time taken by a signal at the input pin to impact the output signal at the output pin is the propagation delay of a gate or cell. A delay of 50 percent of the input transition to the corresponding 50 percent of the output transition is calculated for any gate propagation.

Considering the rise/fall of both input and output, we are faced with four propagation delays:

50% of input rise to 50% of output rise.
50% of input rise to 50% of output fall.
50% of input fall to 50% of output rise.
50% of input fall to 50% of output fall.
All the delays will have different values, or in some cases same values.

## Schematic Diagram 
The following schematic are designed using Xschem.

![](Images/AND_schematic.PNG)


## Pre Layout Simulation

The simulation is done using the Ngspice. Ngspice is a open source simulation and analysis tool.

To run spice simulation use `ngspice <filename>.spice`
Include the lib file which contains the model file locations.
pfet and nfet are used here.
Using the spice commands, Calculate the Fall time Rise time and Transition Fall and Rise Delay.

### Fall Time
        Measuring Cell Fall Time @ 50% of VDD(1.8V) 
        meas tran tinfall when v(A)=0.9 FALL=1 
        meas tran tofall when v(X)=0.9 FALL=1
        let cfall = (tofall-tinfall)/1e-9
### Rise Time
        Measuring Cell Rise Time @ 50% of VDD(1.8V) 
        meas tran tinrise when v(in1)=0.9 RISE=1 
        meas tran torise when v(out)=0.9 RISE=1
        let crise = (torise-tinrise)/1e-9
### Fall Transition        
        Measuring Fall Transion Time @ 80-20% of VDD(1.8V) 
        meas tran ft1 when v(out)=1.44 FALL=1 
        meas tran ft2 when v(out)=0.36 FALL=1
        let fall_tran = (ft2-ft1)/1e-9
### Rise Transition        
        Measuring Rise Transion Time @ 20-80% of VDD(1.8V) 
        meas tran rt1 when v(out)=1.44 RISE=1 
        meas tran rt2 when v(out)=0.36 RISE=1
        let rise_tran = (rt1-rt2)/1e-9
