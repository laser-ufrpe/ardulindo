# Welcome to ARDULINDO Python Code

This is the micro-python code for Ardulindo, 
a first-place winner in the line-follower category 
at [BJ Bot Cup III](https://sites.google.com/view/bjbotscup/)

## Car Componets
- **Controller:** 1xESP32
- **H-Bridge** 1xL298N
- **Battery:** 2x18650
- **Motors:** 2xN20 6v/3000rpm
- **Sensor:** 1xQRT 8 channels/
- **Tires:** 2xOring with 4mm of diameter
- **Wheels:** 2xPrinted to Oring use
- **Chassis:** 1xPrinted to zip tie use

## How to Setup Debian/Ubuntu Linux
- `sudo apt update`
- `sudo apt install python3 python3-pip`
- `python3 -m pip install esptool`

## How to Flash Code on ESP32
- **Download:** [MicroPython 1.24.1 for ESP32](https://micropython.org/download/ESP32_GENERIC/)
- **Run:** `python3 -m esptool erase_flash`
- **Run:** `python3 -m esptool --baud 460800 write_flash 0x1000 BIN_NAME.bin`
- **Open:** [viper-ide](https://viper-ide.org) 
- **Finally:** Copy boot.py to ESP32 and mount your bot to test

## Acknowledgements
### Special Thanks
We would like to express our deepest gratitude to the individuals whose exceptional contributions made a significant impact on this project:

- **Camila Almeida (Team Leader and Heads Eletronic):** [Linkedin](https://www.linkedin.com/in/camila-almeida-5a1a9a364), [Github](https://github.com/CamisAlmeida)
- **Emmanuel Nascimento (Heads Programming):** [Linkedin](https://www.linkedin.com/in/yet1dev), [Github](https://github.com/yet1dev)
- **Abner Barros (Lab Leader and Project Mentor):** [Linkedin](https://www.linkedin.com/in/abner-barros-5b86409) 

### Internal Team Acknowledgements
Thank you to the internal members of our team for their collaboration, dedication, and hard work throughout the project construction and support:

- **Stella Nazario:** [Linkedin](https://www.linkedin.com/in/stella-naz%C3%A1rio)
- **Elton Oliveira:** [Linkedin](https://www.linkedin.com/in/elton-da-costa), [Github](https://github.com/EltonC06)
- **Gabriel Lima:** [Linkedin](https://www.linkedin.com/in/gabriel-lima-da-silva-), [Github](https://github.com/gabedev0)

### External Collaborators
We also extend our sincere thanks to external contributors and supporters who provided valuable insights, resources, or assistance:

- **Carlos Victor (3D Printing Support):** [Linkedin](https://www.linkedin.com/in/carlos-victor-656465271)
- **Gustavo Felipe (3D Modeling Support):** [Linkedin](https://www.linkedin.com/in/gustavo-felipe-528400246), [Github](https://github.com/GustavoFelipeM)

- **Otoniel Junior:** [Linkedin](https://www.linkedin.com/in/otonielnn), [Github](https://www.linkedin.com/in/camila-almeida-5a1a9a364)
- **Ewerton Farias:** [Github](https://github.com/Ewerton-Jose)
- **Arthur Seabra:** [Linkedin](https://www.linkedin.com/in/arthur-seabra-220733286)

