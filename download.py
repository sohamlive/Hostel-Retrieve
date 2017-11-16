##############################################
##		FINAL HOSTEL IMAGES DOWNLOADER		##
##############################################
# Date - 29th May, 2017
# Version - 1.1
# Use - Run download.py
# ---------------------------------------------------
# INFO - It doesn't work on Hostel J single seater
# TODO - None
# ---------------------------------------------------

import os
import time
import shutil
import urllib.request as ur
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from struct import *

#-------------------------
#-- Global Variables
#-------------------------

#-- Hostel List
hostels = ["A","J","K","PG","E","G","I","ICB","ICG"] 
#-- Path to the Directories
dirpath = "F:\\Scrape\\Hostels\\"
#-- Main URL
url = "http://www.onlinehostel.in/hostel"
#-- File to store the status
file = "status.bin"
#-- Choice
ch = 0
#-- Convert.py to copy to each directory
battery = "convert.py"
#-- Format string to pack the data in struct
#---- FORMAT - String, Bool
#---- BYTES  - 3, 1 = 4
strformat = "3s?"

#-----------------------------------------
#-- Create Directories if not exists
#-----------------------------------------
for h in hostels:
	dires = dirpath+h
	if not os.path.isdir(dires):
		os.makedirs(dires)

#-----------------------------------------
#-- Create Status.bin if not exists
#-----------------------------------------
if not os.path.exists(file):
	open(file,'wb')

#-------------------------
#-- Header Display
#-------------------------
def header():
	print("="*60)
	print(" "*18+"HOSTEL IMAGES DOWNLOADER")
	print("="*60)
	print("\n\n")

#-------------------------
#-- Table Display
#-------------------------
def display():
	header()
	#-- Read 4 bytes at a time
	chunk = 4
	seeker = 0
	#-- Table Serial Number
	sn = 1 
	tab = PrettyTable(["SNo","Hostel","Status"])
	tab.align["Hostel"] = 'c'
	tab.padding_width = 2
	with open(file,'rb') as f:
		while True:
			f.seek(seeker)
			buf = f.read(chunk)
			if buf==b'':
				break
			data = unpack(strformat,buf)
			name = str(hostels[sn-1])
			name.strip()
			tab.add_row([sn,name,data[1]])
			seeker = seeker + 4
			sn = sn+1
	#-- Print Table
	print(tab)
	print("10 - EXIT\n")
	#-- Call the Global ch
	global ch
	#-- Take the user choice
	ch = input("Enter your choice (1-10) : ")

#-------------------------
#-- Status Check
#-------------------------
def status_check():
	os.system('cls')
	#-- Open file in Write Binary mode
	with open(file,'wb') as f:
		f.seek(0)
		for h in hostels:
			dires = dirpath+h
			#-- Convert Hostel Name to byte form
			htb = bytes(h,'utf-8')
			#-- True if files exist in a directory
			#-- False if the directory is empty
			for root, dirs, files in os.walk(dires):
				if not files:
					packed = pack(strformat,htb,False)
				else:
					packed = pack(strformat,htb,True)
				#-- Write to the file
				f.write(bytes(packed))
	#-- Call Table Display
	display()
	
#-------------------------
#-- Download Files
#-------------------------
def download_files(pos):
	#-- Start the timer
	start = time.time()
	#-- Convert the pos to int
	pos = int(pos)
	#-- Image URL Page
	img_url = url+hostels[pos-1]+"/uploads/"
	#-- Open the page
	html = ur.urlopen(img_url)
	#-- BeautifulSoupify the page
	soup = BeautifulSoup(html, "lxml")
	#-- Start the counter
	count = 0
	#-- Some decorations
	print("\n", end="")
	print("*"*30)
	print(" "*10+"Hostel {0}".format(hostels[pos-1]))
	print("*"*30)
	#-- Find all the a tags in the page
	for li in soup.find_all("a"):
		#-- Actual Image URL
		imgURL = img_url+li['href']
		#-- Local Image URL
		imgLOCAL = dirpath+hostels[pos-1]+"\\"+li['href']
		#-- Increment the count
		count = count + 1
		#-- The first count is a reference to the Parent Directory - Ignore
		if count==1:
			pass
		else:
			try:
				#-- Download the Images
				ur.urlretrieve(imgURL, imgLOCAL)
				print("{0}... done!".format(li.text))
				count = count + 1
			except:
				#-- Create a nice exception message
				print("There was some error in saving the file. Please try again.")
				print("Program will now exit.")
				#-- Delay the program for 8 seconds.
				time.sleep(8)
				exit()
	#-- Hostel Directory
	bat_dir = dirpath+hostels[pos-1]
	#-- Copy the battery
	shutil.copy(battery,bat_dir)
	#-- Some more decorations
	print("="*31)		
	print("    IMAGES DOWNLOADED - {0}".format(count-2))
	print("="*31)
	#-- Check the end time
	end = time.time()
	#-- Total time needed
	total = end - start
	total = int(total)
	#-- Does the user want to continue or exit
	status = input("Check status (y/n)? : ")
	if status=='y':
		status_check()
	else:
		print("Hostel {0} all images downloaded in {1} seconds.".format(hostels[pos-1],total))
		time.sleep(4)
		exit()

#-------------------------------
#-- Main Executions Begins
#-------------------------------
status_check()

#-- Loop until False
while True:
	ch = int(ch)

	if ch==1:
		download_files(ch)
	elif ch==2:
		download_files(ch)
	elif ch==3:
		download_files(ch)
	elif ch==4:
		download_files(ch)
	elif ch==5:
		download_files(ch)
	elif ch==6:
		download_files(ch)
	elif ch==7:
		download_files(ch)
	elif ch==8:
		download_files(ch)
	elif ch==9:
		download_files(ch)
	elif ch==10:
		exit()