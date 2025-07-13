from compare_selectors import compare_selectors


def build_accounts_lists(youtube_accounts, blocklists): 
	blocklists_file=[]
	ya_css_path = youtube_accounts['accounts']['css-path']
	# Convert dict items to a list, skip the first item, then convert back to dict
	accounts = dict(list(youtube_accounts['accounts'].items())[1:])
	for account,account_data in accounts.items():
		i=1
		blocklists_file.append('!filterlists for '+account+'\n')
		for i in range(len(blocklists)):
			if 'cosmetic-filters' in blocklists[i]:
				for a,b in blocklists[i]['cosmetic-filters'].items():
					if a==account:
						print(a)
						print(account)
						print("---")
						blocklists_selector= b['selector']
						# Compare the selectors
						result = compare_selectors(blocklists_selector, ya_css_path)			
						ya_img=account_data['img']
						has_chain= ':has(' + result['deviated_chain2'] + '[src="'+ya_img + '"])'
						comment= "!"+b['comment']
						filterline="www.youtube.com##"+result['same_chain'] + has_chain +' '+ result['deviated_chain1']
						blocklists_file.append(comment + '\n')
						blocklists_file.append(filterline + '\n')
						blocklists_file.append('\n')
		blocklists_file.append('\n')
	return blocklists_file

def build_nologin_lists(youtube_accounts, blocklists):
	blocklists_file=[]
	ya_css_path = youtube_accounts['no-login']['css-path']
	# Convert dict items to a list, skip the first item, then convert back to dict
	accounts = dict(list(youtube_accounts['no-login'].items())[1:])
	for account,account_data in accounts.items():
		i=1
		blocklists_file.append('!filterlists for '+account+'\n')
		for i in range(len(blocklists)):
			if 'no-login' in blocklists[i]:
				for a,b in blocklists[i]['no-login'].items():
					if a==account:
						print(a)
						print(account)
						print("---")
						blocklists_selector= b['selector']
						# Compare the selectors
						result = compare_selectors(blocklists_selector, ya_css_path)			
						#ya_img=account_data['img']
						has_chain= ':has(' + result['deviated_chain2'] +')'
						comment= "!"+b['comment']
						filterline="www.youtube.com##"+result['same_chain'] + has_chain +' '+ result['deviated_chain1']
						blocklists_file.append(comment + '\n')
						blocklists_file.append(filterline + '\n')
						blocklists_file.append('\n')
		blocklists_file.append('\n')
	return blocklists_file
	
	
def build_whole_lists(youtube_accounts, blocklists):
	blocklists_file=[]
	ya_css_path = youtube_accounts['whole']['css-path']
	# Convert dict items to a list, skip the first item, then convert back to dict
	accounts = dict(list(youtube_accounts['whole'].items())[1:])
	for account,account_data in accounts.items():
		i=1
		blocklists_file.append('!filterlists for '+account+'\n')
		for i in range(len(blocklists)):
			if 'whole' in blocklists[i]:
				for a,b in blocklists[i]['whole'].items():
					if a==account:
						print(a)
						print(account)
						print("---")
						blocklists_selector= b['selector']
						# Compare the selectors
						#result = compare_selectors(blocklists_selector, ya_css_path)			
						#ya_img=account_data['img']
						#has_chain= ':has(' + result['deviated_chain2'] +')'
						comment= "!"+b['comment']
						filterline="www.youtube.com##"+b['selector']
						blocklists_file.append(comment + '\n')
						blocklists_file.append(filterline + '\n')
						blocklists_file.append('\n')
		blocklists_file.append('\n')
	return blocklists_file
