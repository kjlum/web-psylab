Title: Research
Slug: research
sortorder: 1

[TOC]

## Next-Generation Clocking

The past three decades have seen dramatic shifts and transitions in the design of CMOS 
digital integrated circuits, including the “frequency-race”, increasing variability in 
advanced process technologies, low-voltage operation, and the design of 3D heterogeneous 
complexes. With the exception of resonant clocking, there have been few significant changes 
in the state-of-the-art in system clocking. Clock distributions transitioned from clock 
planes (high performance) to clock trees (lower power) and back to coarse clock meshes (in 
response to process variability).

<img src="/images/res_clk.png" class="centered" width="397" height="268"/>
<p class="caption">Simplified schematic of a quasi-resonant clocking system</p>

Today, several new challenges have emerged in the area of clocking including:

* Low-voltage operation, to near-threshold and sub-threshold voltages
* DVFS systems with wide tuning ranges
* Mitigating the impact of supply noise, especially di/dt
* Synchronization and domain crossing between across multiple clock domains in 
            heterogeneous systems
* The increasing difficulty of analog design techniques for clock generation
* 3D integration

Previous selected publications in the area:
[ISSCC](http://vlsi.ee.washington.edu/files/2014/09/resonant_clock_design_for_a_power_efficient_high_volume_x86-64_microprocessor_isscc.pdf)
[JSSC](http://vlsi.ee.washington.edu/files/2014/09/resonant_clock_design_for_a_power_efficient_high_volume_x86-64_microprocessor.pdf)
[ISLPED](http://vlsi.ee.washington.edu/files/2014/09/quasi_resonant_clocking_a_runtime_control_aproach_for_true_voltage_frequency_scaling.pdf)
[Pat1](https://www.google.com/patents/US20140062566)
[Pat2](https://www.google.com/patents/US8742817)


## Current problems in clocking

The grounds-up research effort in this area focuses on radically different clocking 
circuits and architectures which effectively address these myriad challenges. The group is 
currently focused on:

1. Low-voltage all-digital PLL design
2. Elastic clocking techniques for highly variable and resistive technologies
3. Clock distributions for ultra-wide-range DVFS systems
4. Greedy synchronization for efficient clock domain crossing for future micro-regulated voltage domains
5. Voltage-Frequency scalable clock distribution networks (global and local)

<img src="/images/elastic_clk.png" class="centered" width="598" height="246"/>
<p class="caption">An elastic clock distribution for efficient, robust clocking</p>


## Power conversion, distribution and regulation

Few areas in IC design are as pervasive and challenging as the analysis and design of power 
supply systems. The progress of clock rates to beyond package resonance frequencies, the 
efficiency-driven push for larger number of on-chip voltage domains, reduced form factors 
in electronic systems, power transfer, conversion and regulation for energy-harvesting 
systems and even challenges in hardware security have all  driven advances in this field.

<img src="/images/buck_converter.png" class="centered" width="597" height="195"/>
<p class="caption">All-digital DC-DC conversion for energy-efficient microprocessors</p>

We are interested in a number of problems in this area:

1. Novel voltage regulation techniques and architectures
2. Analysis, optimization and design of power front-ends for energy-harvesting applications
3. Analysis of supply noise in high performance systems
4. Power delivery and regulation in 3D silicon
5. Analysis and optimization of voltage regulators for bio-implantable systems

<img src="/images/interlocked_osc.jpg" class="centered" width="300" height="248"/>
<p class="caption">A novel system to enable fast, all-digital low-dropout regulators for micro-regulated voltage domains.</p>

Previous selected publications in the area:
[Pat1](https://www.google.com/patents/US20120187991)
[Pat2](https://www.google.com/patents/US8373512)
[ISLPED](http://vlsi.ee.washington.edu/files/2014/10/Deterministic-Dither.pdf)
[ISSCC1](http://vlsi.ee.washington.edu/files/2014/09/a_32nm_fully_integrated_reconfigurable_switched_capacitor_dc_dc_converter_delivering_0.55_at_81_efficiency.pdf)
[ISSCC2](http://vlsi.ee.washington.edu/files/2014/10/clock_stretcher_isscc.pdf)

## Neural-signal acquisition and processing

Minimally-invasive ECoG readings taken from the surface of the brain have been shown to contain sufficient information to enable exciting Brain Computer Interface possib￼￼ilities. ECoG signal detection and processing also has other vital clinical applications. We are interested in applying low-power system design principles, and exploiting the available “structure” in the problem of neural signal recording to drive advances in this area. A current project, funded by the Center for Sensorimotor Neural Engineering (CSNE) aims to develop a highly scalable and energy-efficient architecture for integrated neural-signal recording and post-processing.

<img src="/images/ecog_spectrum.png" class="centered" width="434" height="321"/>
<p class="caption">Frequency-time plot comparing original and reconstructed ECOG signals</p>


## Other Research Projects

**Minimum-Energy System Design:** Despite much recent work in the last decade in the area of minimum energy CMOS computation, we still dissipate energy several orders of magnitude  more than postulated by the Landauer limit. I am fascinated by analysis and design of circuits, or systems that will enable us to approach this limit, beyond existing conventional CMOS techniques:
[ISSCC](http://vlsi.ee.washington.edu/files/2014/09/energy_efficient_ghz_class_charge_recovery_logic.pdf)
[Symposium](http://vlsi.ee.washington.edu/files/2014/10/A_187MHz_Subthreshold-Supply_Robust_FIR_Filter_with_Charge-Recovery_Logic.pdf)
[JSSC1](http://vlsi.ee.washington.edu/files/2014/10/Energy-Efficient_GHz-Class_Charge-Recovery_Logic.pdf)
[JSSC2](http://vlsi.ee.washington.edu/files/2014/09/187_mhz_subthreshold_supply_charge_recovery_fir.pdf).
Importantly, instead of focusing on minimum-energy computation, I am interested in more comprehensive system design, leveraging the expertise of my group in the areas of voltage conversion, regulation, and computing circuits and architectures to develop ultra low-power integrated systems.

<img src="/images/charge_recovery_logic.png" class="centered" width="232" height="183"/>
<p class="caption">Charge recovery logic with sub-threshold supply</p>

**Exploiting Resonance:** Resonance by way of resonant clocking has been demonstrated to deliver energy efficiency in integrated circuits. An area I am actively exploring techniques and methods to exploit resonance beyond clocking applications, to develop low-power systems, and escaping the key limitation of frequency-limited operation. Recent efforts in the area have yielded early success.[ISLPED](http://vlsi.ee.washington.edu/files/2014/09/quasi_resonant_clocking_a_runtime_control_aproach_for_true_voltage_frequency_scaling.pdf)

**Special purpose architectures:** Several emerging applications and technological challenges call for a need to rethink existing computational techniques and their VLSI implementations for reasons of robustness, performance or efficiency. Some of these areas include hardware security, machine learning, efficient processing and movement of information within and outside of integrated circuits.


## Prototypes
<img src="/images/qrc_isscc16_dieshot.png" class="centered" width="497" height="255"/>
<p class="caption">The first demonstration of truly voltage-scalable quasi-resonant clocking

Fahim U. Rahman, Visvesh S. Sathe [ISSCC’16]</p>

<img src="/images/afe_ecog.png" class="centered" width="499" height="239"/>
<p class="caption">Prototype demonstrating an optimized ECoG signal chain with reduced noise and ADC requirements, resolved from specific characteristics of ECoG signals.

William A. Smith [ESSCIRC’14 [TBIOCAS’16]</p>

<img src="/images/rf2_dieshot.png" class="centered" width="495" height="256"/>
<p class="caption">RF2: The first-ever fully integrated resonant clocked datapath. The design, operating at 1GHz in 0.13um CMOS, was implemented in a fully ASIC design flow and featured distributed clock generation to automate the resonant clock generation.

Visvesh Sathe,  Jerry Kao [VLSI Symp, JSSC]</p>

<img src="/images/rf1_dieshot.png" class="centered" width="493" height="262"/>
<p class="caption">RF1: Single phase resonant clocked ASIC with programmable operating frequency of 0.8GHz-1.2GHz

Visvesh Sathe, Jerry Kao [CICC, JSSC]</p>

<img src="/images/boost_logic_dieshot.png" class="centered" width="494" height="294"/>
<p class="caption">
Boost Logic: The first-ever GHz-class charge-recovery logic. Operating at 1.1GHz, the fully integrated logic implemented a novel charge recovery logic, “Boost-Logic”, to achieve dramatic speed improvement over the state-of-the-art – Previous charge-recovery logic operating frequencies were in the 200MHz range

Visvesh Sathe  [ISSCC, JSSC]</p>
