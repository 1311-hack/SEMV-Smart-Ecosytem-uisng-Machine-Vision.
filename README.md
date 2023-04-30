# SEMV-Smart-Ecosytem-uisng-Machine-Vision.

Smart Ecosystem using Machine Vision (SEMV) is an innovative engineering
project that aims to automate electrical appliances in schools, colleges, universities,
and workplaces using the power of computer vision. The project uses CCTV cameras
to capture real-time video and then process it to detect the presence of humans in a
particular space. Based on this data, the system can turn on or off the electrical
appliances in the area. The system is advanced enough to locate the exact position of
humans in a classroom or workspace and control the appliances located at that
specific position. The primary goal of SEMV is to prevent the unnecessary wastage
of electricity caused by human negligence and forgetfulness in turning off
appliances. The project aims to save a significant amount of electricity, reduce
carbon footprint, and promote sustainable development. The SEMV project has
several advantages over existing systems. Firstly, the system is low cost, making it an
ideal solution for educational institutions and workplaces with a limited budget.
Secondly, the system uses existing CCTV cameras, which reduces the need for
additional hardware, installation, and maintenance costs. Lastly, the system's use of
machine vision technology ensures that the environment remains sustainable and
efficient, promoting a greener and cleaner planet.

# How to use:

1. Download the code.
2. Upload the code to raspberry pi board.
3. Connect and configure the raspberry pi to ESP8266 WiFi module.
4. Connect the ESP8266 WiFi module to Arduino Uno R3 over WiFI.
5. Connect the Arduino Uno R3 to Relay switches.
6. Connect the relay switches to electrical appliances or LEDs for testing.
7. Run the program.

# Design specifications:

The design approach for the automated electrical appliance system involves using a
combination of hardware and software components to detect the presence of humans
in a room and control the electrical appliances accordingly.
The first component is a CCTV camera that captures a live video feed of the room.
The video feed is then processed by a Raspberry Pi using the MobileNet SSD deep
learning-based object detection algorithm to identify the presence of humans in the
room. The Raspberry Pi sends signals to an Arduino Uno microcontroller board to
control the electrical appliances based on the detected presence of humans.
To ensure wireless communication between the Raspberry Pi and the Arduino, an
ESP8266 Wi-Fi module is used to facilitate the transmission of signals between the
two devices using a PHP server. A relay module is used as an electrical switch to
control the electrical appliances such as lights and fans.
In addition, the system includes a grid-based location detection feature that can
identify the exact location of a human in the room. This is achieved through a grid
system where each electrical appliance is assigned a specific location in the room and
the system can identify the location of the human using computer vision algorithms.
This allows the system to turn on or off the electrical appliances located in that
specific location.
To ensure continuous operation, a stable power supply is required, and the system is
housed in a custom enclosure to ensure safety and durability. The system is designed
to be cost-effective to ensure affordability for educational institutions and
workplaces.
