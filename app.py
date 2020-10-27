import subprocess 
import requests
from secret import discToken,discEndpoint

header={
    "authorization":discToken
}
count=0
print("Running")
for ping in range(1,20): 
    address = "192.168.1." + str(ping) 
    res = subprocess.call(['ping', '-c', '3', address]) 
    if res == 0 and ping!=1: 
        count=count+1
        print( "ping to", address, "OK") 
        
    elif res == 2: 
        print("no response from", address) 
    else: 
        print("ping to", address, "failed!")
print("\n\n\n\nScript completed")
data={"content": "{} devices are connected to the network".format(count)}
requests.post(discEndpoint,data=data,headers=header)