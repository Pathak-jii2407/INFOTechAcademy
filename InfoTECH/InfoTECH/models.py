# models.py
from django.db import models
import datetime as dt
from . import mysql_data



class Subscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    
    def __init__(self,email,password):
        self.email=email
        self.password=password
    
    def __str__(self):
        return self.email
    
    def wish_():
        time=dt.datetime.now().hour
        wish=''
        if time>1 and time<12:
            wish='Good Morning!'
        elif time>12 and time<15:
            wish='Good Evening!'
        else:
            wish='Good Afternoon!'
        return wish
    
    def send_to_index(self):
        data = mysql_data.get_data(self.email,self.password)
        return data
    def lanugage(subject):
        lang=mysql_data.subject(subject)
        return lang
    
    def extra_data(self):
        data = mysql_data.get_data(self.email,self.password)
        language=data['language']
        lang_count=Subscription.lanugage(language)
        total_students=mysql_data.total_students()
        data['total_students']=total_students
        data['language_number']=lang_count
        return data

    
    
    