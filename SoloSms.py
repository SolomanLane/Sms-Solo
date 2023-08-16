from colorama import Fore, Style
from time import sleep
from os import system
from requests import get
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
r = get("https://raw.githubusercontent.com/SolomanLane/Sms-Solo/main/sms.py").text
with open("sms.py", "r", encoding="utf-8") as f:
    read = f.read()
if read == r:
    pass
else:
    print(Fore.RED + "Güncelleme yapılıyor...")
    with open("sms.py", "w", encoding="utf-8") as f:
        f.write(r)
from sms import SendSms
r = get("https://raw.githubusercontent.com/SolomanLane/Sms-Solo/main/call.py").text
with open("call.py", "r", encoding="utf-8") as f:
    read = f.read()
if read == r:
    pass
else:
    print(Fore.RED + "Güncelleme yapılıyor...")
    with open("call.py", "w", encoding="utf-8") as f:
        f.write(r)
from call import SendCall
servisler_call = []
for attribute in dir(SendCall):
    attribute_value = getattr(SendCall, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_call.append(attribute)
servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)    
while 1:
    system("cls||clear")
    print("""{}
          
       ▀▄▀▄▀▄ 𝑺𝒐𝒍𝒐𝑺𝒎𝒔 ▄▀▄▀▄▀
        
    Sms: {}                         
    Ara (beta): {}                 
    """.format(Fore.LIGHTRED_EX, len(servisler_sms), len(servisler_call), Style.RESET_ALL, Fore.CYAN))
    print(Fore.LIGHTGREEN_EX+"{/} "+Style.RESET_ALL+"Katkıda bulunanlar: "+Fore.LIGHTGREEN_EX+Style.BRIGHT+"SolomanLane by Alperen Çalışkan\n"+Style.RESET_ALL)
    try:
        menu = int(input(Fore.LIGHTMAGENTA_EX + " 1- SMS Gönder\n 2- Ara\n 3- Çıkış\n\n" + Fore.LIGHTYELLOW_EX + " Seçim: "))
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Hatalı giriş yaptınız. Tekrar deneyiniz.")
        sleep(3)
        continue
    if menu == 1:
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yazınız (birden çoksa 'enter' bas): "+ Fore.LIGHTGREEN_EX, end="")
            tel_no = input()
            if tel_no != "" and len(str(tel_no)) == 10:
                tel_no2 = "bos"
                tel_no3 = "bos"
                tel_no4 = "bos"
                tel_no5 = "bos"
            if tel_no == "":
                system("cls||clear")
                print( Fore.LIGHTGREEN_EX+"[+] "+Fore.CYAN+"TXT dosya formatı:\n"
                      +Fore.LIGHTGREEN_EX+"[+] "+Fore.CYAN+"En fazla 5 numara olacak şekilde başında '+90' olmadan alt alta numaraları yazın.")
                print("")
                print("")
                print(Fore.LIGHTYELLOW_EX + "TXT dosyasının yolunu giriniz: "+ Fore.LIGHTGREEN_EX, end="")
                dosya_yolu = input()
                try:
                    with open(dosya_yolu, 'r') as file:
                        tel_list = file.readlines()
                        for i, number in enumerate(tel_list):
                            if i == 0:
                                tel_no = number.strip()
                            elif i == 1:
                                tel_no2 = number.strip()
                            elif i == 2:
                                tel_no3 = number.strip()
                            elif i == 3:
                                tel_no4 = number.strip()
                            elif i == 4:
                                tel_no5 = number.strip()
                            if len(number.strip()) != 10:
                                raise ValueError
                        if i<4:
                            for j in range(i+1,5):
                                if j==1:
                                    tel_no2 = "bos"
                                elif j==2:
                                    tel_no3 = "bos"
                                elif j==3:
                                    tel_no4 = "bos"
                                elif j==4:
                                    tel_no5 = "bos"
                except FileNotFoundError:
                    system("cls||clear")
                    print(Fore.LIGHTRED_EX + "Dosya bulunamadı. Tekrar deneyiniz.")
                    sleep(3)
                    continue
                except ValueError:
                    system("cls||clear")
                    print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.")
                    sleep(3)
                    continue
            else:
                if len(tel_no) != 10:
                  raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTGREEN_EX+"[+] "+Fore.CYAN+"Birden çok numara varsa her bir numara için.")
            print(Fore.LIGHTYELLOW_EX + "Kaç adet SMS göndermek istiyorsun (sonsuz ise 'enter' bas): "+ Fore.LIGHTGREEN_EX, end="")  
            kere = input()
            if kere:
                kere = int(kere)
            else:
                kere = None
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptınız. Tekrar deneyiniz.") 
            sleep(3)
            continue

        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Kaç saniye aralıkla göndermek istiyorsun: "+ Fore.LIGHTGREEN_EX, end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptınız. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        if kere is not None:
             tel_numbers = [tel_no, tel_no2, tel_no3, tel_no4, tel_no5]
             bos_olmayan = len([x for x in tel_numbers if x != "bos"])
             keree = kere * bos_olmayan
        sms = SendSms(tel_no, tel_no2, tel_no3, tel_no4, tel_no5, mail)
        if isinstance(kere, int):
                  while sms.adet < kere:
                      for attribute in dir(SendSms):
                          attribute_value = getattr(SendSms, attribute)
                          if callable(attribute_value):
                              if attribute.startswith('__') == False:
                                  if sms.adet == keree or sms.adet > keree:
                                      break
                                  exec("sms."+attribute+"()")
                                  sleep(aralik)
                  print(Fore.LIGHTRED_EX + "\nMenüye dönmek için 'enter' tuşuna basınız..")
                  input()
        elif kere is None: 
                  while True:
                      for attribute in dir(SendSms):
                          attribute_value = getattr(SendSms, attribute)
                          if callable(attribute_value):
                              if attribute.startswith('__') == False:
                               exec("sms."+attribute+"()")
                               sleep(aralik)
    elif menu == 2:
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yazınız: "+ Fore.LIGHTGREEN_EX, end="")
            tel_no = int(input())
            if len(str(tel_no)) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + f"Kaç kere aransın (max: {len(servisler_call)}): "+ Fore.LIGHTGREEN_EX, end="")
            kere = int(input())
            if kere > len(servisler_call):
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptınız. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        call = SendCall(tel_no, mail)
        while call.adet < kere:
            for attribute in dir(SendCall):
                attribute_value = getattr(SendCall, attribute)
                if callable(attribute_value):
                    if attribute.startswith('__') == False:
                        if call.adet == kere:
                            break
                        exec("call."+attribute+"()")
        print(Fore.LIGHTRED_EX + "\nMenüye dönmek için 'enter' tuşuna basınız..")
        input()   
    elif menu == 3:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Çıkış yapılıyor...")
        break
