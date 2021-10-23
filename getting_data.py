import os
import requests



url_samanpura='https://docs.google.com/spreadsheets/d/1fmkYgHTWwEbdgWxQgyRPG5g1ag-iLb3Emnuo-SRrno8/export?format=xlsx&gid=0'
url_drm_office='https://docs.google.com/spreadsheets/d/1fmkYgHTWwEbdgWxQgyRPG5g1ag-iLb3Emnuo-SRrno8/export?format=xlsx&gid=1825925003'
url_govt_high_school='https://docs.google.com/spreadsheets/d/1fmkYgHTWwEbdgWxQgyRPG5g1ag-iLb3Emnuo-SRrno8/export?format=xlsx&gid=1321311482'
url_muradapur='https://docs.google.com/spreadsheets/d/1fmkYgHTWwEbdgWxQgyRPG5g1ag-iLb3Emnuo-SRrno8/export?format=xlsx&gid=409038259'
url_rajbansi_nagar='https://docs.google.com/spreadsheets/d/1fmkYgHTWwEbdgWxQgyRPG5g1ag-iLb3Emnuo-SRrno8/export?format=xlsx&gid=2107345793'

#creating the Data directory
os.mkdir('Data')


#requesting the samanpural file 
r = requests.get(url_samanpura, allow_redirects=True)

open('Data\\samanpura.xlsx', 'wb').write(r.content)

#requesting the samanpural file 
r = requests.get(url_drm_office, allow_redirects=True)

open('Data\\Drm_office.xlsx', 'wb').write(r.content)

#requesting the samanpural file 
r = requests.get(url_govt_high_school, allow_redirects=True)

open('Data\\govt_high_school.xlsx', 'wb').write(r.content)

#requesting the samanpural file 
r = requests.get(url_muradapur, allow_redirects=True)

open('Data\\murdapur.xlsx', 'wb').write(r.content)

#requesting the samanpural file 
r = requests.get(url_rajbansi_nagar, allow_redirects=True)

open('Data\\rajbansi_nagar.xlsx', 'wb').write(r.content)

