from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
import json, glob
from pathlib import Path
from datetime import datetime
import random
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

Builder.load_file('design.kv')

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current= "sign_up_screen"

    def login(self,uname,pword):
        with open("jsonfiles\\users.json") as file:
            users=json.load(file)
        if uname in users and users [uname] ['password'] == pword:
            self.manager.current='Login_Screen_Success'
        else:
            self.ids.login_wrong.text= "wrong name or password"






class RootWidget(ScreenManager):
    pass


class SignUpScreen(Screen):
    
    def add_user(self,uname,pword):
        print(uname,pword)
        with open("jsonfiles\\users.json") as file:
            users=json.load(file)
      
        users[uname]={'username':uname,'password':pword,
        'created':datetime.now().strftime("%Y %M %D %H %M %S")}
       

        with open("jsonfiles\\users.json",'w') as file:
            json.dump(users,file)
 
        self.manager.current= "sign_up_screen_success"
   
         
class SignUpScreenSuccess(Screen):
    def go_to_login(self):
       self.manager.transition.direction='right'
       self.manager.current='login_screen'

class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction='right'
        self.manager.current='login_screen'

    def get_quote(self,feel):
        feel=feel.lower()
        availabel_feelings =  glob.glob("quotes\\*txt")
        # print(availabel_feelings)

        availabel_feelings=[Path(filename).stem for filename in availabel_feelings]
        if feel in availabel_feelings:
            with open(f"quotes\\{feel}.txt",encoding="utf8" ) as file:
                quotes=file.readlines()
                self.ids.quote.text=random.choice(quotes) 
        else:
            self.ids.quote.text="                           Try another feeling"


        
class ImageButton(ButtonBehavior,HoverBehavior,Image):
    pass
 
class LandingPage(Screen):
    def go_to_login(self):
       self.manager.transition.direction='right'
       self.manager.current='login_screen' 



class MainApp(App):
    def build(self):
        return RootWidget()
       

if __name__ =="__main__":
    MainApp().run()