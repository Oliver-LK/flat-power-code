# flat-power-code
About:
Code to track the power the usage of everyone in the flat based on thier heater usage using a smart plug.
This is tracked in a Google sheet that everyone has access to. Each FN everyone puts their power usage for that month into the Google sheet. However, the kink is that the smart plugs only give a daily break-down of power usage therefore is unable to track the heater usage in the hour of free power, so this has been accounted for in the HEAT_LIST which is the average power usage of their heater inn kWh which can be subtracted off their total power usage.

Code.py is the main file with all the usefull data analysis functions inside it.

Total_cost.py has a single function (at this stage) that chooses the desired row in the google sheet to analyse

FN = fortnight
