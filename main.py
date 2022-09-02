import re
from Code import *

def main(spread_sheet_url):
    """Main function that directs all others"""
    id_key = sheet_id(spread_sheet_url)
    work_sheet, wks = return_sheet(id_key)
    cost_dict = power_dict_make(work_sheet)
    return cost_dict

main(URL)
