import requests

# NOTE: This url is genereted by ngrok, a local host tunneling service, and thus 
# this url can change with every execution of the ngrok server
API_ENDPOINT = "http://3934774e.ngrok.io"

# data to be sent to api 
data = {'filename': 'demo.mp4'} 

# filename = "demo.mp4"
  
# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, data = data) 
  
# extracting response text  
pastebin_url = r.text 
print("The pastebin URL is:%s"%pastebin_url)