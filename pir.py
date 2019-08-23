#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import os
import smtplib
from picamera import PiCamera

camera = PiCamera()
sensor = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)
previous_state = False
current_state = False
username = 'fancyusername'
password = 'fancypassword'
smtp = "fancy.smtp.server"
smtpport = 587
mfrom = 'fancy@email.ofyours'
mto = 'fancy@email.ofyours'
msubj = "Motion detected"
mbody = "Check photo"
path = '/home/pi/pir'
try: 
    os.makedirs(path)
except OSError:
    if not os.path.isdir(path):
        raise
try:
	while 1:
	    time.sleep(0.1)
	    previous_state = current_state
	    current_state = GPIO.input(sensor)
	    if current_state != previous_state:
	        new_state = "HIGH" if current_state else "LOW"
		server = smtplib.SMTP(smtp,smtpport)
		server.starttls()
		server.login(username,password)
		from subprocess import call
		from email.MIMEMultipart import MIMEMultipart
		from email.MIMEText import MIMEText
		from email.MIMEImage import MIMEImage
		msg = MIMEMultipart()
		msg['Subject'] = msubj
		msg['From'] = mfrom
		msg['To'] = mto
		text = MIMEText(mbody)
		msg.attach(text)
		timestr = time.strftime("%Y-%m-%d_%H:%M:%S")
		filename = path + '/image_' + timestr + '.jpg'
		camera.capture(filename)
		img = open(filename,'rb').read()
		imag = MIMEImage(img,name=os.path.basename(filename))
		msg.attach(imag)
		server.sendmail(msg['From'],msg['To'], msg.as_string())
		server.quit()
		command = "rm " + filename
		os.system(command)
except KeyboardInterrupt:
               print "Bye bye!"
               GPIO.cleanup()
