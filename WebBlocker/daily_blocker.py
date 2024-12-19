import time
from datetime import datetime as dt


host_path=r"C:\Windows\Sistem32\drivers\etc\host"
redirect="127.0.0.1"
website_list="www.facebook.com","www.dub119.mail.com.live.com"
final_list=[redirect+""+i for i in website_list]
final_string_block="\n".join(final_list)

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt(dt.now().year,dt.now().month,dt.now().day,18):
        print("Within time...")
        with open(host_path,"r+") as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+""+website+"\n")
    else:
        with open(host_path,"r+") as file:
            content=file.seek()
            for line in content:
                if not any(website in line for website in website_list):
                    file.write()
            file.truncate()
    time.sleep(2.5)
