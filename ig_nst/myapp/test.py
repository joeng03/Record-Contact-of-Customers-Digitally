import csv
import pandas as pd
from bs4 import BeautifulSoup
import os

def write_to_csv(filename,rows_list):
  fp=open(filename,'r',encoding='utf-8')
  soup = BeautifulSoup(fp,'lxml')
  messages = soup.select('div.uiBoxWhite')
  for message in messages:
      d={}
      d["Info"]=message.select('div')[4].text
      d["Timestamp"]=message.select('div')[7].text
      if not d["Info"].startswith('Say hi to your new Facebook friend'):
        rows_list.append(d)
    

if __name__ == "__main__":
    path=r'C:\Users\user\Downloads\facebook-joeng39589149 (1)\inbox'
    rows_list=[]
    for filename in os.listdir(path):
      filename=os.path.join(path,filename,'message_1.html')
      write_to_csv(filename,rows_list)
    df=pd.DataFrame(rows_list)
    df.to_csv('hahaha.csv')
      