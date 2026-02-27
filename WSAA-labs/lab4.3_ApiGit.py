#

from github import Github 
#import sys
#sys.path.append("..") 
from config4 import apikeys as cfg 
import requests


apikey = cfg["pfda_assignments"] 
g = Github(apikey) 

# Checking that PyGithub works and that the key is valid by printing the name of the authenticated user
# & repositories of the authenticated user
#print(g.get_user().name)
#for repo in g.get_user().get_repos(): 
	#print(repo.name) 

# Getting a specific repository by name and printing its clone URL
repo = g.get_repo("NibnabCodes/pfda_assignments") 
#print(repo.clone_url) 

# Getting specific file in the repository and printing its download URL
fileInfo = repo.get_contents("test.txt") 
urlOfFile = fileInfo.download_url 
#print (urlOfFile) 

# Downloading the content of the file using the download URL and printing it
response = requests.get(urlOfFile) 
contentOfFile = response.text 
#print (contentOfFile) 

# Appending some text to the content of the file and printing the new content
newContents = contentOfFile + " more stuff \n" 
#print(newContents) 

# Updating the file in the repository with the new content and printing the response from GitHub
gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",
newContents,fileInfo.sha) 
print (gitHubResponse) 