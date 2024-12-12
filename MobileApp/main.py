from kivy.app import App
#from kivy import require
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
#from kivy.uix.gridlayout import GridLayout
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
import json, glob
from datetime import datetime
from pathlib import Path
import random

Builder.load_file('diseno.kv')

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"
        #print("Sign up botton press")

    def login(self,uname,pword):
        with open("users.json") as file:
            users = json.load(file)
        if uname in users and users[uname]['password']==pword:
            self.manager.current = 'login_screen_success'
        else:
            self.ids.login_wrong.text = "Wrong Username or Password"

class RootWidget(ScreenManager): 
    pass

class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
        
        users[uname] = {'username':uname, 'password':pword,
                        'created':datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        
        with open("users.json", 'w') as file:
            json.dump(users,file)
        self.manager.current = "sign_up_screen_success"
        #print(users)
        #pass

class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.transition.direction='right'
        self.manager.current="login_screen"

class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

    def get_quote(self,feel):
        feel = feel.lower()
        avaliable_feelings = glob.glob("quotes/*txt")
        avaliable_feelings = [Path(filename).stem for filename in avaliable_feelings]
        if feel in avaliable_feelings:
            with open(f"quotes/{feel}.txt", encoding="utf-8") as file:
                quotes = file.readlines()
                print(quotes)
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Try another feeling"

class ImageButton(ButtonBehavior,HoverBehavior,Image):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()
    
if __name__ == "__main__":
    MainApp().run()

