#counties = ["Arapahoe","Denver","Jefferson"]
#if counties[1] == 'Denver':
 # print(counties[1])

#if "El Paso" in counties:
    #print("El Paso is in the list of counties.")
#else:
    #print("El Paso is not the list of counties.")

#for county in counties:
   # print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# Print with thousands separator
for county, voters in counties_dict.items():
  print(f'1. {county} county has {voters:,} registered voters')

#Iterate Through a Dictionary
  # Get the Keys of a Dictionary

#for county in counties_dict.keys():
    #print(county)
#for voters in counties_dict.values():
    #print(voters)

#same for values: dict_name[key]
#for county in counties_dict:
   #print(counties_dict[county])

# Get the Values of a Dictionary with .get(key)
#for county in counties_dict:
    #print(counties_dict.get(county))

# Get the Key-Value Pairs of a Dictionary
  # .item() method

#for county, voters in counties_dict.items():
    #print(f'{county} county has {voters} registered voters')

#Iterate Through a List of Dictionaries

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

#for county_dict in voting_data:
    #print(county_dict)

# The same but using range()
#for county in range(len(voting_data)):
    #print(voting_data[county]['county'])

# To get values from a list of Dict. Needs to use Nested loop
#for county_dict in voting_data:
    #for value in county_dict.values():
        #print(value)

# Print with thousands separator

for county in range(len(voting_data)):
  #print(voting_data[county]['registered_voters'])
  
  print(f'2. {voting_data[county]["county"]} county has {voting_data[county]["registered_voters"]:,} registered voters') #string is imp to apply ,thous...separator)

#Print the values of the "roads" key from the nested dictionary.

nested_dict = {"Dakar":{"weather":"sunny", "roads":"dry"}}
ans_1 = nested_dict["Dakar"]["roads"]
print("3. " + ans_1)
