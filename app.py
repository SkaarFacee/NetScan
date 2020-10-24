import subprocess 
import requests
from secret import discToken,discEndpoint
data={
    "content": "Update the message"

}
header={
    "authorization":discToken
}
for ping in range(1,20): 
    address = "192.168.1." + str(ping) 
    res = subprocess.call(['ping', '-c', '3', address]) 
    if res == 0: 
        if(address=="192.168.1.6"):
            requests.post(discEndpoint,data=data,headers=header)
        print( "ping to", address, "OK") 
        
    elif res == 2: 
        print("no response from", address) 
    else: 
        print("ping to", address, "failed!")