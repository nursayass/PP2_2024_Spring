import json


f=open('sample-data-json.json')
json_data = json.load(f)

a=''' 
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
'''
print(a)

iamdata=json_data["imdata"]

for item in iamdata:
    
    print("{DN:50}{Speed:>30}{MTU:>6}".format(DN=item['l1PhysIf']['attributes']['dn'],Speed=item['l1PhysIf']['attributes']['speed'],MTU=item['l1PhysIf']['attributes']['mtu']))
   