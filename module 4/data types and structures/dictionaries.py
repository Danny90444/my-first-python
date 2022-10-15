x = []
print(type(x))


file_counts = {"Jpg":10, "txt":14, "csv":2, "py":23}
for ext,amount in file_counts.items(): 
 print("There are {} files with the .{} extension".format(amount, ext))
print(file_counts.keys())
print(file_counts.values())

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for top,elements in  wardrobe.items(): 
	for index,color in enumerate(elements):
		print("{} {}".format(color, top))

["apples" , "bannanas" , "bread"]
     

def email_list(domains):
	emails = []
	for domains,users in domains.items():
		for index,person in enumerate(users):
			emails.append("{}@{}".format(person,domains))
		return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			if user not in user_groups:
				user_groups[user] = []
			user_groups[user].append(group)
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))