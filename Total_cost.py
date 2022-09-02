from main import main
from Code import pretty_print
from Code import URL

cost_dict_1 = {"BB": 11.17, "Rachel": 11.17, "Rosie": 11.17, "Shaz": 11.17, "Nic": 11.17, "Oli": 11.17}
cost_dict_2 = {"BB": 16.67, "Rachel": 16.67, "Rosie": 16.67, "Shaz": 16.67, "Nic": 16.67, "Oli": 16.67}

def peoples_total_cost():
    """Calculates the total cost over a period of time"""
    cost_dict = {"BB": 0, "Rachel": 0, "Rosie": 0, "Shaz": 0, "Nic": 0, "Oli": 0}
    current_cost_dict = main(URL)
    for people, cost in cost_dict.items():
        cost_dict[people] = current_cost_dict[people] + cost_dict_1[people] + cost_dict_2[people]
    return cost_dict

peoples_total_cost()


pretty_print(peoples_total_cost())


