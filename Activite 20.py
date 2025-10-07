adresses_ip = [ "192.168.0.1" , "10.0.0.1" , "172.16.0.1" , "200.100.50.1" , "169.254.0.1"]

classes_ip = {
    "192.168.0.1":"classe C",
    "10.0.0.1":"classe A",
    "172.16.0.1":"classe B",
    "200.100.50.1":"adress ip publique",
    "169.254.0.1":"adresse ip de lien local (apipa)"

}

#1
print("1. la premiere adresse dans la liste est : ",adresses_ip[0])
#2
print("2. la derniere adresse dans la liste est : ",adresses_ip[4])
#3
print("3. la troisieme adresse dans la liste est : ",adresses_ip[2])
#4
adresses_ip.append("172.31.0.1")
#5
adresses_ip.remove("200.100.50.1")
#6
print("6. le nombre d'adresses restants est : ",len(adresses_ip))
#7
presence = "192.168.0.1" in adresses_ip
print("7. l'adresse '192.168.0.1' est presente ? ", presence)
#8
print(f"8. la classe de l'adresse ip 10.0.0.1 est {classes_ip["10.0.0.1"]}")
#9
print(f"9. La liste triee est :  {sorted(adresses_ip)}")
#10
toutes_classe_C = True
for ip, classe in classes_ip.items() :
    if classe != "classe C": 
        toutes_classe_C = False
        break

if toutes_classe_C == False:
    print("10. Non, toutes les ip n'appartiennent pas a la classe C")
else:
    print("10. Oui, toutes ip appartiennent a la classe C")
#11
compteur = 0
for ip, classe in classes_ip.items() :
    if classe == "adresse ip publique": 
        compteur += 1
        break

print(f"11. Le nombre d'adresse ip est : {compteur}")