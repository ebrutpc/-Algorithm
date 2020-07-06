pangramexp1="Pijamalı hasta yağız şoföre çabucak güvendi"
pangramexp2="Hayvancık tüfekçide bagaj törpüsü olmuş"



def pangram_checker(pangram):
  alphabet="abcçdefgğhıijklmnoöprsştuüvyz" # sabit dizi - alfabe
  pangram=(pangram.replace(" ", "")).lower() # ifadeyi önişlem yapar 
                                            #replace() fonk boşlukları kaldırır
                                            #lower() tüm harfleri küçük yapar
  newexp=[] # tekrar eden harfleri teke indirge ve listeye ata
  count=0
  for i in pangram:
    if i not in newexp:
      newexp.append(i)
  for i in newexp:
    if i in alphabet:
      count+=1
  if count==29: # len(alphabet==29)
    print("yes")
  else:
    print("no")


pangram_checker(pangramexp1)
pangram_checker(pangramexp2)
