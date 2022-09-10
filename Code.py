import pygsheets

URL = 'https://docs.google.com/spreadsheets/d/1Is-Jf1gZJRj3bEw6Tlaby8uOuXriQCDL8meFgu1jZ4I/edit#gid=0'

PEOPLE = {'BB': 0, "Rachel": 1, "Rosie": 2, "Shaz": 3, "Nic": 4, "Oli": 5}
HEAT_LIST = [1.86, 0, 2.38 , 1.28, 1.85, 1.85]
kWh_cst = 0.303545125229
        
client_var = pygsheets.authorize(service_account_file='firm-source-357906-0d2c70f00dc1.json') #allows access to drive

def sheet_id(spread_sheet_url):
    """Returns the sheet id"""
    split_url = spread_sheet_url.split('/d/')
    url_key = split_url[1].split('/')
    return url_key[0]

def return_sheet(id_key):
    """Opens and returns the worksheet"""
    sheet = client_var.open_by_key(id_key) #opens the sheet based on id
    wks = sheet.worksheet_by_title('Main_sheet') #reads the file as a sheet
    entire_sheet = wks.range('A1:H50', returnas='matrix') #returns only the relative rows &cols
    #cleaned_values = [[item for item in unique_list if item]for unique_list in entire_sheet] #removes empty strings #Probably dont need
    return entire_sheet, wks

#  Needs to be split into two functions
def power_dict_make(work_sheet, FN_index):
    """Returns a dic containing everyone's ind pwr usage & the FN cost"""
    cost_dict = {"BB": 0, "Rachel": 0, "Rosie": 0, "Shaz": 0, "Nic": 0, "Oli": 0}
    FN_counter = 0

    FN_power_people = work_sheet[FN_index]
    work_sheet[FN_index].pop(0) #removes the an unwanted date element
    
    total_pp_cost = 0 #Total power cost from everyone's heaters
    for person in cost_dict.keys(): #Incrementing through the cost dict
        for peep in PEOPLE.items(): #Incrementing through peoples IDs
            if person == peep[0]: #Checks if the person match's the ID with key
                cost_dict[person] = kWh_cst* (float(FN_power_people[peep[1]]) - (14 * HEAT_LIST[peep[1]])) #Sets persons cost
                total_pp_cost += kWh_cst* (float(FN_power_people[peep[1]]) - (14 * HEAT_LIST[peep[1]]))
    
    FN_total_cost = float(FN_power_people[6])
    remainder_cost = FN_total_cost - total_pp_cost
    
    for person, current_cost in cost_dict.items(): #Loop adds on the base power cost
        cost_dict[person] = current_cost + (remainder_cost/6)
    
    return cost_dict

def pretty_print(cost_dict):
    """Prints everything out nicely"""
    print("\n==================")
    print(f"THIS MONTHS POWER")
    for person, cost in cost_dict.items():
        print(f"{person:6}: ${cost:.2f}")

    print("==================\n")


