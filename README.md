# Message_Scheduler
A python script to send messages.

##  Requirements for twilio
+ Python
+ Python-pip
+ twilio
+ schedule

## Setup
1. Clone the app ``` git clone https://github.com/rohitsh16/Message_Scheduler.git ```
2. ```cd Message_Scheduler```
3. ```cd twilio```
4. ```pip install -r requirements.txt```
5. ```Create a free account on twilio```
6. ```Get a twilio number.```
7. ```Put account ssid and auth token in the python script.```
8. ```Add a verified caller ID by adding and verifying number in twilio in which you want to send message```

## Usage
### Simple Twilio Message
``` python main.py "{{ your_message }}" ```

### Twilio scheduled Message
``` python automate.py "{{ your_message }}" "HH:MM" ```
hi kkc
