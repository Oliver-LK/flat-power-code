from main import cost_dict_make
from Code import pretty_print
from Code import URL

#  Cost_dict example
cost_dict_1 = {"BB": 11.17, "Rachel": 11.17, "Rosie": 11.17, "Shaz": 11.17, "Nic": 11.17, "Oli": 11.17}

def peoples_total_cost(FN_index, a_cost_dict):
    """Calculates the total cost over a period of time"""
    cost_dict = {"BB": 0, "Rachel": 0, "Rosie": 0, "Shaz": 0, "Nic": 0, "Oli": 0}
    current_cost_dict = cost_dict_make(URL, FN_index)
    for people, cost in cost_dict.items():
        cost_dict[people] = current_cost_dict[people] + a_cost_dict[people]
    return cost_dict



pretty_print(peoples_total_cost(1, cost_dict_1))