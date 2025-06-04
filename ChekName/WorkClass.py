import json

fileName = 'clients.json'
clients = {
    0:'Alex', 
    1:'Tilda', 
    2:'Martin', 
    3:'Vera'
    }

def start(file, list):
   print("Введите ваше имя или номер: ")
   given = input()
   count = 0

   if given.isdigit() == True:
      digitKey = int(given)

      for key, value in clients.items():
          if digitKey == key:
              print("Добро пожаловать ", value)
              break

          elif digitKey > 3:
              print("Ключ принят, введите имя: ")
              name = input()
              list = {digitKey:name}
              with open(file, 'r+') as f_obj:
                  json.dump(list, f_obj)
                  break

   elif given.isdigit() == False:

        if given.isalpha() == False:
            print("Неправильный формат имени, используйте только\n латинские буквы без пробелов.")
            start(file, list)

        elif given.isalpha() == True:
            for k, v in clients.items():
                if given == v:
                    print("Добро пожаловать, вы номер ", k)
                elif given != v:
                    count += 1
                    continue
                if count == len(clients):
                    list = {k+1:given}
                    with open(file, 'r+') as f_obj:
                        json.dump(list, f_obj)
                        break
start(fileName, clients)

















           

           
   
                 
          







    


