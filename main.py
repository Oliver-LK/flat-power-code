#  Doest really do anything other than a test. Remove???
from Code import *

def cost_dict_make(spread_sheet_url, FN_index):
    """Main function that directs all others"""
    id_key = sheet_id(spread_sheet_url)
    work_sheet, wks = return_sheet(id_key)
    cost_dict = power_dict_make(work_sheet, FN_index)
    return cost_dict

