todos = []

for _ in range(20000000):
    print("Was Willst du Tun?")
    print("(1) To-dos anzeigen")
    print("(2) To-dos hinzufügen")
    
    option = input("Bitte Auswählen: ")
    
    if int(option) == 1:
        print("Meine Liste Hat folgende Items ")
        
        for todo in todos:
            print(f"- {todo}")
    
    if int(option) == 2:
        newitem = input("Was Möchtest du noch Hinzufügen: ")
        todos.append(newitem)
    
    print("")
    print("")
    
print("Progamm Beendet")