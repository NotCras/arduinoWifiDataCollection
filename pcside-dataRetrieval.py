import csv
import requests # handles html stuff
import time # enables sleep
import keyboard # kills while loop at a press of a key
import sys, os

CSV_URL = 'http://192.168.0.105' #you get this by looking at the serial output from the arduino using something like the WiFiWebServer example in the WiFiNINA library

timeout = 5

while True:
    with requests.Session() as s:
        download = s.get(CSV_URL)
    
        decoded_content = download.content.decode('utf-8')
    
        cr = csv.reader(decoded_content.splitlines(), delimiter=',') #reads in the http data and cleans up most of the non-data
        #see: https://stackoverflow.com/questions/35371043/use-python-requests-to-download-csv
        my_list = list(cr)
        l = len(my_list)

        with open('eggs.csv', 'w') as f:
            fw = csv.writer(f)

            for row in my_list[3:l-1]: #I chose a specific range in the file to ignore the required http header and footer

                v1 = row[0]
                v2 = row[1]
                v2l = len(v2)
                
                clean_row = [v1, v2[:v2l-6]] #this gets rid of <br /> at the end of every line

                fw.writerow(clean_row)
                print(clean_row)

            f.close()
            #print('end of 1 read') #this is just for debugging
            

        #kills for loop if you press n
        if keyboard.is_pressed('n'):
            break

        #pauses the code for 5 seconds
        time.sleep(timeout);
	




