#

from github import Github 
from config import config as cfg 


apikey = cfg["githubkey"] 
# use your own key 
g = Github(apikey) 