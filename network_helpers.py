"""
A network related tasks helper script
"""

# importing subprocess
import subprocess

def getAllWifiRouterNames(print:bool = False) -> list:
    """
    A method that returns all the wifi routers the machine has connected to
    before 

    Parameters
    =--------=
    print: boolean
        A switch to print or not the networks

    Returns
    =-----=
    names: list
        A list of network names
    """
    # getting meta data of the wifi network
    meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])

    # decoding meta data from byte to string
    data = meta_data.decode('utf-8', errors ="backslashreplace")

    # splitting data by line by line
    # string to list
    data = data.split('\n')
    # creating a list of wifi names
    names = []

    # traverse the list
    for i in data:
        
        # find "All User Profile" in each item
        # as this item will have the wifi name
        if "All User Profile" in i :
            
            # if found split the item
            # in order to get only the name
            i = i.split(":")
            
            # item at index 1 will be the wifi name
            i = i[1]
            
            # formatting the name
            # first and last character is use less
            i = i[1:-1]
            
            # appending the wifi name in the list
            names.append(i)

    if print:
        # printing the wifi names
        print("All wifi that system has connected to are ")
        print("-----------------------------------------")
        for name in names:
            print(name)
    
    return names


def ping(address: str = '127.0.0.1', count: int = 10):
    """
    A method used for pinging IP

    Parameters
    =--------=
    address: string
        The address to ping
    count: integer
        The number of ips to ping

    Returns
    =-----=
    None: nothing
        Just print information related to the ping
    """
    for ping in range(1,count):
        address = "127.0.0." + str(ping)
        res = subprocess.call(['ping', '-c', '3', address])
        if res == 0:
            print( "ping to", address, "OK")
        elif res == 2:
            print("no response from", address)
        else:
            print("ping to", address, "failed!")

ping()
