import csv
import pandas as pd
from bs4 import BeautifulSoup
import os

def write_to_csv(file,rows_list):
  soup = BeautifulSoup(file,'lxml')
  messages = soup.select('div.uiBoxWhite')
  for message in messages:
      d={}
      d["Info"]=message.select('div')[4].text
      d["Timestamp"]=message.select('div')[7].text
      if not d["Info"].startswith('Say hi to your new Facebook friend'):
        rows_list.append(d)
      