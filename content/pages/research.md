Title: Research
Date: 2017-04-02 18:13
Save_as: research.html

## Next-Generation Clocking

The past three decades have seen dramatic shifts and transitions in the design of CMOS 
digital integrated circuits, including the “frequency-race”, increasing variability in 
advanced process technologies, low-voltage operation, and the design of 3D heterogeneous 
complexes. With the exception of resonant clocking, there have been few significant changes 
in the state-of-the-art in system clocking. Clock distributions transitioned from clock 
planes (high performance) to clock trees (lower power) and back to coarse clock meshes (in 
response to process variability).

<img src="/images/res_clk.png" style="margin:0 auto;display:block;" width="397" height="268"/>
<p style="text-align:center;font-style:italic;">Simplified schematic of a quasi-resonant clocking system</p>

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

<img src="/images/elastic_clk.png" style="margin:0 auto;display:block;" width="598" height="246"/>
<p style="text-align:center;font-style:italic;">An elastic clock distribution for efficient, robust clocking</p>


## Power conversion, distribution and regulation

Few areas in IC design are as pervasive and challenging as the analysis and design of power 
supply systems. The progress of clock rates to beyond package resonance frequencies, the 
efficiency-driven push for larger number of on-chip voltage domains, reduced form factors 
in electronic systems, power transfer, conversion and regulation for energy-harvesting 
systems and even challenges in hardware security have all  driven advances in this field.

<img src="/images/buck_converter.png" style="margin:0 auto;display:block;" width="597" height="195"/>
<p style="text-align:center;font-style:italic;">All-digital DC-DC conversion for energy-efficient microprocessors</p>

We are interested in a number of problems in this area:

1. Novel voltage regulation techniques and architectures
2. Analysis, optimization and design of power front-ends for energy-harvesting applications
3. Analysis of supply noise in high performance systems
4. Power delivery and regulation in 3D silicon
5. Analysis and optimization of voltage regulators for bio-implantable systems

<img src="/images/interlocked_osc.jpg" style="margin:0 auto;display:block;" width="300" height="248"/>
<p style="text-align:center;font-style:italic;">A novel system to enable fast, all-digital low-dropout regulators for micro-regulated voltage domains.</p>

Previous selected publications in the area:
[Pat1](https://www.google.com/patents/US20120187991)
[Pat2](https://www.google.com/patents/US8373512)
[ISLPED](http://vlsi.ee.washington.edu/files/2014/10/Deterministic-Dither.pdf)
[ISSCC1](http://vlsi.ee.washington.edu/files/2014/09/a_32nm_fully_integrated_reconfigurable_switched_capacitor_dc_dc_converter_delivering_0.55_at_81_efficiency.pdf)
[ISSCC2](http://vlsi.ee.washington.edu/files/2014/10/clock_stretcher_isscc.pdf)