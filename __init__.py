import socket
import sys
import requests

'''
This module is used to easly get your private and public
ip address use you can simple import this module by using
import getip and you can also get the current details of 
your ip address like your ip region, timezone,country, your
internet provider for more information please read the documentation 
'''
'''
The module is developed by lenin_royal and akhil_jinu
By the tamilspyboy for more details please visit our 
youtube channel https://youtube.com/c/tamilspyboy
'''

#Getting your local ip
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]
    s.close()


# Get your public ip from internet
def request_ip_details():
    try:
        output_response = requests.get("https://ipinfo.io/json")
    except:
        print("Please check your internet connection ....")
        sys.exit()
    return output_response.json()


# Getting the public ip
def get_public_ip():
    public_ip = request_ip_details()['ip']
    return public_ip


# Getting the country detail
def get_country():
    country = request_ip_details()['country']
    return country


# Getting region detail
def get_region():
    region = request_ip_details()['region']
    return region


# Your ip timezone
def get_timezone():
    timezone = request_ip_details()['timezone']
    return timezone


# information about internet provider
def get_internet_provider():
    org = request_ip_details()['org']
    return org


#get your result on dic 
def get_dic_result():
    dic_output = {'local_ip':get_local_ip(),'public_ip':get_public_ip(),'region':get_region(),'internet_provider':get_internet_provider(),'country':get_country(),'timezone':get_timezone()}
    return dic_output
    
