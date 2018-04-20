import socket
import sys
import re
def kontrollo(var):
    if var.lower()=='ip':
        return('IP')
    elif 'ip'in var.lower():
        print('Per metoden ip address ju duhet te shkruani IP')
        return('')
    elif var.lower()=='port':
        return('PORT')
    elif 'port'in var.lower():
        print('Per metoden port nr ju duhet te shkruani PORT')
        return('')
    elif re.match('(zanore) ([a-z ])+',var.lower()):
        return(var)
    elif 'zanore'in var.lower():
        print('Per metoden zanore ju duhet te shkruani ZANORE')
        return('')
    elif re.match('(printo) ([a-z 0-9!@#$%^&.,;])+',var.lower()):
        return(var)
    elif 'printo'in var.lower():
        print('Per metoden printo ju duhet te shkruani PRINTO Teksti')
        return('')
    elif var.lower()=='host':
        return('HOST')
    elif 'host'in var.lower():
        print('Per metoden host ju duhet te shkruani HOST')
        return('')
    elif var.lower()=='time':
        return('TIME')
    elif 'time'in var.lower():
        print('Per metoden time ju duhet te shkruani TIME')
        return('')
    elif var.lower()=='loja':
        return('LOJA')
    elif 'loja'in var.lower():
        print('Per metoden loja ju duhet te shkruani LOJA')
        return('')
    elif var.lower()=='konverto':
        print('Zgjidh njeren nga opsionet: \nCelsiusToKelvin \nCelsiusToFahrenheit \nKelvinToFahrenheit \nKelvinToCelsius \nFahrenheitToCelsius \nFahrenheitToKelvin \nPoundToKilogram \nKilogramToPound')
        var1=input("Opsioni qe zgjedhni: ")
        if var1.lower()=='celsiustokelvin' or var1.lower()=='celsiustofahrenheit' or var1.lower()=='kelvintofahrenheit' or var1.lower()=='kelvintocelsius' or var1.lower()=='fahrenheittocelsius' or var1.lower()=='fahrenheittokelvin' or var1.lower()=='poundtokilogram' or var1.lower()=='kilogramtopound':
           var2=input("Vlera qe do te konvertohet: ")
           if re.match('[0-9]+',var2):
               konverto=var+" "+var1+" "+var2
               return(konverto)
           else:
               print("Vlera e kthyer duhet te jete numer i plote")
               return('')
        else:
            print("Nje opsion i tille nuk egziston")
            return('')
    elif 'konverto' in var.lower():
            print("Per metoden Konverto ju duhet te shkruani KONVERTO")
            return ('')
    elif re.match('(fibonacci) [0-9]+',var.lower()):
        return(var)
    elif 'fibonacci'in var.lower():
        print('Per metoden fibonacci ju duhet te shkruani FIBONACCI Numrin')
        return('')
    elif re.match('(prim) [0-9]+',var.lower()):
        return(var)
    elif 'prim'in var.lower():
        print('PEr metoden prim ju duhet te shkruani PRIM Numrin')
        return('')
    elif re.match('(countwords) ([a-z 0-9!@#$%^&.,;])+',var.lower()):
        return(var)    
    elif 'countwords'in var.lower():
        print('Per metoden countwords ju duhet te shkruani CountWords Teksti')
        return('')
    elif re.match('(convertcurrency) ([a-z]+) [0-9]+',var.lower()):
        ndarja = (var.lower()).split()
        if ndarja[1]=='eurotodollar' or ndarja[1]=='dollartoeuro' or ndarja[1]=='eurotopound' or ndarja[1]=='poundtoeuro' or ndarja[1]=='eurotorupee' or ndarja[1]=='rupeetoeuro' or ndarja[1]=='eurotobrl' or ndarja[1]=='brltoeuro':
           return(var)
        else:
            return ('')
    elif 'currency'in var.lower():
        print('Per metoden convertcurrencu ju duhet te shkruani CONVERTCURRENCY MONEDHANEMONEDHEN Numrin \nOpsionet jane: \nEuroToDollar \nDollarToEuro \nEuroToPound \nPoundToEuro \nEuroToRupee \nRupeeToEuro \nEuroToBrl \nBrlToEuro')
        return('')
    else:
        return('')
host='localhost'
i=True;
while i:
  port=input("Vendosni portin(per tu lidhur me serverin Fiek zgjedh 11000):")
  if port=="11000":
     port=int(port)
     i=False
  else:
      print("Nuk eshte gjetur server ne kete port")
      continue
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
data = s.recv(1024)
print(data.decode("utf-8"))
print('Ju lutem zgjedhni njeren nga metodat duke shkruar emrin  \nIPADDR, PORTNR, ZANORE, PRINTO, HOST, TIME, LOJA, KONVERTO, FIBONACCI, CountWords,PRIM dhe ConvertCurrency \nPer IPADDR shkruaj --> IP \nPer PORTNR --> PORT \nPer ZANORE -->ZANORE Tekstin (Psh. ZANORE BrikenaAhmeti)\nPer PRINTO --> PRINTO tekstin (Psh. PRINTO Ky eshte nje paragraf)\nPer HOST --> HOST \nPer TIME --> TIME \nPer LOJA --> LOJA \nPer KONVERTO --> KONVERTO \nPer FIBONACCI -->FIBONACCI Numri (Psh.FIBONACCI 7) \nPer PRIM -->PRIM Numri (numri tregon kufirin deri ku te gjenden numrat prim) \nPer CountWords --> CountWords Teksti \nPer ConvertCurrency -->ConvertCurrency MonedhenNeMonedhen Numrin (Psh.ConvertCurrency EuroToDollar 10)')
try:
  while 1:
    var = input('\nZgjedhja juaj: ')
    Edhena_e_kontrolluar=kontrollo(var)
    if Edhena_e_kontrolluar!='':
        s.sendall(str.encode(Edhena_e_kontrolluar))
        data = s.recv(1024)
        print(data.decode("utf-8"))
    else:
        continue
except Exception:
    print("Serveri nuk gjendet")
s.close()