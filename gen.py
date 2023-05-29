#gen nitro dev by 100scpl




def gen():
      import random
import random
import colorama
colorama.init()



print(colorama.Fore.MAGENTA + """ 
███    ██ ██ ████████ ██████   ██████       ██████  ███████ ███    ██ 
████   ██ ██    ██    ██   ██ ██    ██     ██       ██      ████   ██ 
██ ██  ██ ██    ██    ██████  ██    ██     ██   ███ █████   ██ ██  ██                                    𝐝𝐞𝐯 𝐛𝐲 𝟏𝟎𝟎𝐬𝐜𝐩𝐥𝐌𝐒𝐅𝟐#𝟎𝟑𝟑𝟐
██  ██ ██ ██    ██    ██   ██ ██    ██     ██    ██ ██      ██  ██ ██ 
██   ████ ██    ██    ██   ██  ██████       ██████  ███████ ██   ████ 
                                                                      
                                                                \n \n \n""")

upper_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_letter = 'abcdefghijklmnopqrstuvwxyz'
digits = '°123456789'

numbtogen = input('Combien de nitro veut tu gen ? >  ')
upper, lower, nums, = True, True, True


all = ""
mdp = input("PROXIE: Oui/Non ----->  ") 
('', 1)


if upper:
    all += upper_letter
    if lower:
      all += lower_letter
    if nums:
      all += digits

      length = 23
      amount = numbtogen

      for x in range(int(numbtogen)):
            nitro = ''.join(random.sample(all, length))
            print('discord.gift/'+nitro)
            


gen()
gen()
gen()


            
 

      
   


list = ['']


def NitroGen(word, length):
        if length <= 5:
                for letter in list:
                        if mdp == word + letter:
                            print("vous avez trouver le nitro " + word + letter )
                        else:
                            print(word + letter)
                            NitroGen(word + letter, length + 1)

