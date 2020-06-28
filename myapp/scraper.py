import csv
import pandas as pd
from bs4 import BeautifulSoup
import os

def write_to_csv(file,rows_list):
  soup = BeautifulSoup(file,'lxml')
  messages = soup.select('div.uiBoxWhite')
  for message in messages:
      d={}
      split=0
      msgs=message.select('div')[4].text
      msg=[]
      for i in range(0,len(msgs)):
        if(msgs[i]==','):
          msg.append(msgs[split:i])
          split=i+1
      try:
        d["Name"]=msg[0]
        d["Phone Number"]=msg[1]
        d["Temperature"]=msg[2]
      except IndexError:
        pass
      d["Timestamp"]=message.select('div')[7].text
      if not d["Info"].startswith('Say hi to your new Facebook friend'):
        rows_list.append(d)
      
