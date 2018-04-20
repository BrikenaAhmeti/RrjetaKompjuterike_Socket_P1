import socket
import math
import sys
from _thread import start_new_thread
import re
import datetime
import random

def IPADDR():        
   ip=socket.gethostbyname(socket.gethostname())
   return (str(ip))  

def PORTNR():          
    return(PORTN)

def HOST():              
     HOSTNAME=socket.gethostname()
     return(str(HOSTNAME))

def TIME():              
   return(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
def PRINTO(var):
    var=var.strip()
    return(var)

def LOJA():
   randomnumber=[]
   r=0
   f=0
   for i in range(100):
      number=random.randint(1,99)
      r=r+1
      if f!=20:
         for j in range(r):
            if number not in randomnumber:
               randomnumber.append(number)
               f=f+1
      else:
        break
   randomnumber.sort()   
    
   str1 = ','.join(str(e) for e in randomnumber)
   return(str1)

def ZANORE(var):
   zanore=0
   for i in var:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='y' or i=='Y' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            zanore=zanore+1
    
   return(str(zanore))

def FIBONACCI(n):
    n=int(n)
    list=[]
    if(n < 1):
        return (str(n))
    elif(n==1):
        list=1
        return(str(list))
    else:
       list = [0, 1, 1]                                                                                           
       for f in range(2, n):                                                                                      
           list.append(list[-1] + list[-2])                                                                         
       return (str(list[n]))
def KONVERTO(tr,num):
   if tr.lower()=='celsiustokelvin' :
      kelvin=int(num)+273
      return(str(round(kelvin,2)))
   elif tr.lower()=='celsiustofahrenheit':
      fahrenheit=int(num)*1.8+32
      return(str(round(fahrenheit,2)))
   elif tr.lower()=='kelvintofahrenheit':
      fahrenheit=int(num)*(9/5)-459.67
      return(str(round(fahrenheit,2)))
   elif tr.lower()=='kelvintocelsius':
      celsius=int(num)-273
      return(str(round(celsius,2)))
   elif tr.lower()=='fahrenheittocelsius':
      celsius=(int(num)-32)/1.8
      return(str(round(celsius,2)))
   elif tr.lower()=='fahrenheittokelvin':
      kelvin=(int(num)+ 459.67) * 5/9
      return(str(round(kelvin,2)))
   elif tr.lower()=='poundtokilogram':
      kg=int(num)*0.45359237
      return(str(round(kg,2)))
   elif tr.lower()=='kilogramtopound':
      pound=int(num)/0.45359237
      return(str(round(pound,2)))
def PRIM(n):
  list=[]
  if n==0:
      return (str(0))
  elif n==1:
      return (str(1))
  else:
    for num in range(2,n):
        for i in range(2,num):
            if (num%i==0):
               break
        else:
            list.append(num)
    str1 = ','.join(str(e) for e in list)
    return(str1)

def CountWords(n):
    return(str(len(n.split())))

def ConvertCurrency(s,n):
   if s.lower()=='eurotodollar' :
      dollar=int(n)/0.814509
      return(str(round(dollar,2)))
   elif s.lower()=='dollartoeuro':
      euro=int(n)*0.814509
      return(str(round(euro,2)))
   elif s.lower()=='eurotopound':
      pound=int(n)/1.15
      return(str(round(pound,2)))
   elif s.lower()=='poundtoeuro':
      euro=int(n)*1.15
      return(str(round(euro,2)))
   elif s.lower()=='eurotorupee':
      rupee=int(n)/0.0125
      return(str(round(rupee,2)))
   elif s.lower()=='rupeetoeuro':
      euro=int(n)*0.0125
      return(str(round(euro,2)))
   elif s.lower()=='eurotobrl':
      brl=int(n)/0.242
      return(str(round(brl,2)))
   elif s.lower()=='brlroeuro':
      euro=int(n)*0.242
      return(str(round(euro,2)))

def kontrollo(var):
    if var.lower()=='ip':
        ip=IPADDR()
        return(ip)
    elif var.lower()=='port':
        port=PORTNR()
        return(port)
    elif re.match('(zanore) ([a-z ])+',var.lower()):
        ndarja=(var.lower()).split(" ",1)
        zanoret=ZANORE(ndarja[1])
        return(zanoret)
    elif re.match('(printo) ([a-z 0-9!@#$%^&.,;])+',var.lower()):
        ndarja=var.split(" ",1)
        teksti=PRINTO(ndarja[1])
        return(teksti)
    elif var.lower()=='time':
        time=TIME()
        return(time)
    elif var.lower()=='loja':
        loja=LOJA()
        return(loja)
    elif var.lower()=='host':
        return(HOST())
    elif re.match('(konverto) ([a-z]+) [0-9]+',var.lower()):
        ndarja = (var.lower()).split()
        if ndarja[1]=='celsiustokelvin' or ndarja[1]=='celsiustofahrenheit' or ndarja[1]=='kelvintofahrenheit' or ndarja[1]=='kelvintocelsius' or ndarja[1]=='fahrenheittocelsius' or ndarja[1]=='fahrenheittokelvin' or ndarja[1]=='poundtokilogram' or ndarja[1]=='KilogramToPound':
            konverto=KONVERTO(ndarja[1],ndarja[2])
            return(konverto)
        else:
            return ('')
    elif re.match('(fibonacci) [0-9]+',var.lower()):
         ndarja=var.split(" ",1)
         teksti=FIBONACCI(ndarja[1])
         return(teksti)
    elif re.match('(prim) [0-9]+',var.lower()):
         ndarja=var.split(" ",1)
         teksti=PRIM(int(ndarja[1]))
         return(teksti)
    elif re.match('(countwords) ([a-z 0-9!@#$%^&.,;])+',var.lower()):
        ndarja=var.split(" ",1)
        teksti=CountWords(ndarja[1])
        return(teksti)
    elif re.match('(convertcurrency) ([a-z]+) [0-9]+',var.lower()):
        ndarja = (var.lower()).split()
        if ndarja[1]=='eurotodollar' or ndarja[1]=='dollartoeuro' or ndarja[1]=='eurotopound' or ndarja[1]=='poundtoeuro' or ndarja[1]=='eurotorupee' or ndarja[1]=='rupeetoeuro' or ndarja[1]=='eurotobrl' or ndarja[1]=='brltoeuro':
            currency=ConvertCurrency(ndarja[1],ndarja[2])
            return(currency)
        else:
            return ('')
    else:
        return('')



hOST = '' 
PORT = 11000 
IPADDRESS=''
PORTN=''
HOSTNAME=''
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Soketa nuk mund te krijohet.")
    sys.exit(0)

print("- Soketa u krijua")

# bind socket
try:
    s.bind((hOST, PORT))
    print("- Soketa u lidh ne portin " + str(PORT))
except socket.error:
    print("Lidhja deshtoi.")
    sys.exit()

s.listen(10)
print("Duke degjuar...")



def client_thread(conn):
    output='Lidhja juaj me serverin u realizua...'
    conn.sendall(output.encode('utf-8'))

    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
        except Exception:
             print("Klienti u shkeput")
             break
        dhenat=data.decode('utf-8')
        dhena1=kontrollo(dhenat)
        if dhena1!='':
           E_dhena_e_kontrolluar="Pergjigjja: "+dhena1
           conn.sendall(E_dhena_e_kontrolluar.encode('utf-8'))
       
    conn.close()

while True:
    #pritja per lidhje me klient
    conn, addr = s.accept()
    print("[-] Lidhur me " + addr[0] + " : " + str(addr[1]))
    PORTN=str(addr[1])
    start_new_thread(client_thread, (conn,))

s.close()
