#https://replit.com/@Nery-EduardoEdu/Olivanders?s=app
clients_number=0
elder_w=0
hawthorn_w=0
willow_w=0
holly_w=0
clientsY=0
clientsN=0
while clients_number<2:
  client=str(input("Does a client come in? (y/n)"))
  if client=="y":
    buy=str(input("Buy something? (y/n)"))
    print("Elder W. [1]")
    print("Hawthorn W. [2]")
    print("Willow W. [3]")
    print("Holly W. [4]")
    wand=int(input("What wand do you want? "))
    clientsY+=1
    if wand==1:
       elder_w+=1
    elif wand==2:
      hawthorn_w+=1
    elif wand==3:
      willow_w+=1
    elif wand==4:
      holly_w+=1
  else:
    clientsN+=1
  clients_number+=1
print("total clients=",clients_number)
print("Customers who bought=",clientsY)
print("Customers who didn't bought=",clientsN)
print("Today's income:")
print("Elders Wand: ",elder_w)
print("Hawthorns Wand: ",hawthorn_w)
print("Willow Wand: ",willow_w)
print("Holly Wand: ",holly_w)
