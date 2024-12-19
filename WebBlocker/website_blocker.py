import time
from datetime import datetime as dt

host_temp="hosts"
host_path=r"C:\Windows\System32\drivers\etc\hosts"      #the "r" do you not use double slash
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","dub119.mail.live.com","www.dub119.mail.live.com"]

#the number in this if dt... indicate the hours advaliable
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8)< dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18):
        print("Working hours...")
        with open(host_temp, 'r+') as file:
            content=file.read()
            #print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(host_temp,'r+') as file:
            content=file.readlines()
            file.seek()
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    #print(1)           
    time.sleep(5)
    #import pyw for run y second pland and do you want add the task initial