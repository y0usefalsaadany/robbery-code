import requests

banner = """
█▀▀█ █▀▀█ █▀▀▄ █▀▀▄ █▀▀ █▀▀█ █░░█ 
█▄▄▀ █░░█ █▀▀▄ █▀▀▄ █▀▀ █▄▄▀ █▄▄█ 
▀░▀▀ ▀▀▀▀ ▀▀▀░ ▀▀▀░ ▀▀▀ ▀░▀▀ ▄▄▄█

░█████╗░░█████╗░██████╗░███████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░╚═╝██║░░██║██║░░██║█████╗░░
██║░░██╗██║░░██║██║░░██║██╔══╝░░
╚█████╔╝╚█████╔╝██████╔╝███████╗
░╚════╝░░╚════╝░╚═════╝░╚══════╝
"""
print (banner)
url = input("website url?")
fileName = input("file name?")
request = requests.get(url).text
with open(fileName + ".txt", "a") as file :
	print (".........\wait.......")
	print (request,file = file)
print ("done")

