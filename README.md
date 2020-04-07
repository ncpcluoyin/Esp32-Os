# Esp32 Os

## Suitable for Esp series and open source operating system where micropython development board can be installed

This is the first stable version v0.1 and is expected to be released in May 2020 0.2
If you want to get the latest development progress, you can use the system provided in the unstable branch

##### All source code of this system is written in python3

#### Installation tutorial

1. Clone the system to local, the default clone branch is stable version
2. Copy main.py, start.py, lib.py and other files with the suffix .py to the file system of the micropython development board, remember not to delete the boot.py that comes with the file system
3. After power on, you can interact in the serial port. The commands are similar to linux, but you need to use "run [filename]" to execute the python program.

#### Instructions for use

1. The system is based on open source gpl 3.0 protocol, such as to be used for commercial purposes have to contact the author: Luo India-mail: 912271673@qq.com
2. The system is updated to github from time to time
3. The production team of this system is syrathon, the official website I asked is www.syrathon.com, forum bbs.syrathon.com

#### Features of this version
1. Stable, using a layered design. When an error occurs in the program, it will not crash but generate a feedback. The shell will print "return false" on the serial port when receiving this feedback, or print "return false" if there is no error feedback. return true "(or not print)
2. Support folder deletion and creation
