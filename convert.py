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
				

with open('blocklists.txt','w') as f:
	f.writelines(final)




























































			
			
			
			
			
#keys = list(youtube_accounts['accounts'].keys())[1:]  # Skip the first key
#print(keys)
#for doc in blocklists:
#	print(doc)
#   
#cf_data=blocklists.get('cosmetic-filters',{})
## Iterate over each document and check keys
#for eq_key,details in cf_data.items():
#    if doc is None:
#        continue
#    # Check if all keys from check.yaml are in this document
#    if all(key in details for key in keys):
#        print("Document containing all keys:")
#        print(key)
#    else:
#            print(f"Document with equivalent key '{eq_key}' is missing some keys:")
#            print(details)
	
	#matched_items = []
	#for entry in blocklists.get('cosmetic-filters', []):
	#	if ya_key in entry:
	#		matched_items.append(entry[ya_key])
	#if ya_key in blocklists and not isinstance(blocklists[ya_key], list):
	#	matched_items.append(blocklists[ya_key])
	#
	#print(f"Data for type '{ya_key}':")
	##for item in matched_items:
	##    print(item)
	##    for fruit, qty in item.items():
	##        combined[fruit] = combined.get(fruit, 0) + qty
	#
	#print("\nCombined data across all types:")
	#print(combined)
	#
	#
	## Compare the selectors
	#result = compare_selectors(blocklists_selector, ya_css_path)
    #
	## Print the results
	#print(f"Fork Point: {result['forkpoint']}")
	#print(f"Same Chain: {result['same_chain']}")
	#print(f"Deviated Chain 1: {result['deviated_chain1']}")
	#print(f"Deviated Chain 2: {result['deviated_chain2']}")
	#
	#
	#
	#
	##has_chain= ':has(' + ya_css_path + '[src="'+ya_img + '"])'
	#has_chain= ':has(' + result['deviated_chain2'] + '[src="'+ya_img + '"])'
	##print(has_chain)
	#comment= "!"+blocklists['cosmetic-filters'][accounts]['comment']
	##print(comment)
	#filter="www.youtube.com##"+result['same_chain'] + has_chain +' '+ result['deviated_chain1']
	#print(filter) 
	


