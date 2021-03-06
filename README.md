# <img src="https://github.com/kuj0210/opensourceproject/blob/master/README/pet_Image.jpg" width="64">Pet House System
### Pet House System is a tool that allows you to manage through Messenger.

## Index
* [Features](#features)
* [Requirement](#requirement)
* [Settings & Installation](#settings--installation)
  * [Settings](#settings)
  * [Installation](#installation)
* [Pet House Structure](#pet-house-structure)
* [Motor operation structure](#motor-operation-structure)
  * [Food](#food)
  * [Water](#water)
  * [Door](#door)
* [Client & Server Structure](#client--server-structure)
* [How to use](#how-to-use)
* [Notes](#notes)
* [How to connect motor wires](#how-to-connect-motor-wires)
  * [Food Motor](#food-motor)
  * [Water Motor](#water-motor)
  * [Door Motor](#door-motor)
 
## **Features**
 - Usage through Messenger
 - Raspberry Pi with chat-bot based System
 - Using communication with flask server
 - Using 2 flask servers.(Main Server(in aws), PiServer(in raspberryPi))
 - You can check the status of your pet with PiCamera
 - You can manage meal and to give water to your pet(s).


## **Requirement**
 - Raspnerry Pi 3 module B (used in Pi Server)
 - 3 servo-motors(for meal,water,door) and PiCamera
 - Computer or Notebook(used to chat-bot API Server)
 - Smart Phone for using chat-bot(used in client)

## **Settings & Installation**

### **Settings** 
 - Using 2 static ip address.
 - Main server is in AWS.(This server manage chat-bot API.)
 - PiServer is in RaspberryPi (This server manage RaspberryPi)
 - Using python 3.x version. Because Hangul generate error with uni-code/utf8.
 
### **Installation**
 
 **1) Server side**
  - Install MySQL.
  ```
  sudo apt-get update
  sudo apt-get install mysql-server
  ```
  
  - Install python3 modules; requests, flask, pymysql 
  ```
  sudo pip3 install requests
  sudo pip3 install flask
  sudo pip3 install pymsql
  ```
   
 **2) PiServer side**
  - Install GPIO modules.
  ```
  sudo apt-get install python-dev
  sudo apt-get install python-rpi.gpio
  ```
   
  - Install flask, requests modules.
  ```
  sudo pip3 install flask
  sudo pip3 install requests
  ```

## **Pet House Structure**

![](https://github.com/kuj0210/opensourceproject/blob/master/README/Pet_House_Structure.png)

Manage the doors, feeds and water using three motors

## **Motor operation structure** 

### Food

![](https://github.com/kuj0210/opensourceproject/blob/master/README/motor_food.png)

Rotate and restore the motor for a short time, and feed the prey by opening and closing the entrance

### Water

![](https://github.com/kuj0210/opensourceproject/blob/master/README/motor_water.png)

Water is given by folding or unfolding the tube with the motor

### Door

![](https://github.com/kuj0210/opensourceproject/blob/master/README/motor_open.png)

Open the door by pulling the thread by the rotation of the motor

![](https://github.com/kuj0210/opensourceproject/blob/master/README/motor_close.png)

When the motor stops, the door is closed by the resilience of the weight.

## **Client & Server Structure**

![](https://github.com/kuj0210/opensourceproject/blob/master/README/Client&Server_Structure.png?raw=true)

## **How to use**

1) Add Official account of Messanger(Pet House System)

2) Enter chat in the format “[등록]/e-mail/Product”

     ![](https://github.com/kuj0210/opensourceproject/blob/master/README/Insert_User.png)

3) Enter chats that associated with food, water and door opening

     ![](https://github.com/kuj0210/opensourceproject/blob/master/README/How_to_use.png)
     
     
 ## **Notes**
 
 - In issue#36 :: 참고용 PPT 및 동영상
 
   https://github.com/kuj0210/opensourceproject/issues/36
   
 - 라즈비안 설치 방법
 
   https://www.raspberrypi.org/documentation/installation/installing-images/
   
## **How to connect motor wires**

![](https://github.com/kuj0210/opensourceproject/blob/master/README/raspberry-pi-pinout.png)

### Food Motor

Orange wired: connects to pin 35

Red wired: connects to 3v3 or 5v pin(one of pin 1, 2, 4, 17)

Brown wired: connects to GND pin(one of pin 6, 9, 14, 20, 25, 30, 34, 39)

### Water Motor

Orange wired: connects to pin 32

Red wired: connects to 3v3 or 5v pin(one of pin 1, 2, 4, 17)

Brown wired: connects to GND pin(one of pin 6, 9, 14, 20, 25, 30, 34, 39)

### Door Motor

Orange wired: connects to pin 12

Red wired: connects to 3v3 or 5v pin(one of pin 1, 2, 4, 17)

Brown wired: connects to GND pin(one of pin 6, 9, 14, 20, 25, 30, 34, 39)
