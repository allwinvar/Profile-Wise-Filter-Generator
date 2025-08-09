import yaml
import cssselect
from build_accounts_lists import build_accounts_lists
from build_accounts_lists import build_nologin_lists
from build_accounts_lists import build_whole_lists

# Open and read the YAML file
with open('youtube-accounts.yaml', 'r') as file: 
    youtube_accounts = yaml.safe_load(file)
# Open and read the YAML file
with open('blocklists.yaml', 'r') as file:
   blocklists = list(yaml.safe_load_all(file))

blocklists_file_accounts=build_accounts_lists(youtube_accounts, blocklists)
blocklists_file_nologin=build_nologin_lists(youtube_accounts,blocklists)
blocklists_file_whole= build_whole_lists(youtube_accounts, blocklists)				
final= blocklists_file_accounts	+ blocklists_file_nologin + blocklists_file_whole
				
with open('accounts.txt','w') as f:
	f.writelines(blocklists_file_accounts)
	
with open('nologin.txt','w') as f:
	f.writelines(blocklists_file_nologin)


with open('whole.txt','w') as f:
	f.writelines(blocklists_file_whole)


with open('blocklists.txt','w') as f:
	f.writelines(final)
