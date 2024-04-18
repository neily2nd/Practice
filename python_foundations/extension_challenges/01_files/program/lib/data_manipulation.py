import os

# == INSTRUCTIONS ==
#
# Below, you'll find lots of incomplete functions.
#
# Your job: Implement each function so that it does its job effectively.
#
# Tips:
# * Use the material, Python Docs and Google as much as you want
#
# * A warning: the data you are using may not contain quite what you expect;
#   cleaning data (or changing your program) might be necessary to cope with
#   "imperfect" data

# == EXERCISES ==

# Purpose: return a boolean, False if the file doesn't exist, True if it does
# Example:
#   Call:    does_file_exist("nonsense")
#   Returns: False
#   Call:    does_file_exist("AirQuality.csv")
#   Returns: True
# Notes:
# * Use the already imported "os" module to check whether a given filename exists
def does_file_exist(filename):
    
    
    return os.path.exists(filename)
# Purpose: get the contents of a given file and return them; if the file cannot be
# found, return a nice error message instead
# Example:
#   Call: get_file_contents("AirQuality.csv")
#   Returns:
#     Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);[...]
#     10/03/2004;18.00.00;2,6;1360;150;11,9;1046;166;1056;113;1692;1268;[...]
#     [...]
#   Call: get_file_contents("nonsense")
#   Returns: "This file cannot be found!"
# Notes:
# * Learn how to open file as read-only
# * Learn how to close files you have opened
# * Use readlines() to read the contents
# * Use should use does_file_exist()
def get_file_contents(filename):
    if does_file_exist(filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            return lines
    else:
        return "This file cannot be found!"
    
# Purpose: fetch Christmas Day (25th December) air quality data rows, and if
# boolean argument "include_header_row" is True, return the first header row
# from the filename as well (if it is False, omit that row)
# Example:
#   Call: christmas_day_air_quality("AirQuality.csv", True)
#   Returns:
#     Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);[...]
#     25/12/2004;00.00.00;5,9;1505;-200;15,6;1168;567;525;169;1447;[...]
#     [...]
#   Call: christmas_day_air_quality("AirQuality.csv", False)
#   Returns:
#     25/12/2004;00.00.00;5,9;1505;-200;15,6;1168;567;525;169;1447;[...]
#     [...]
# Notes:
# * should use get_file_contents() - N.B. as should any subsequent
# functions you write, using anything previously built if and where necessary
def christmas_day_air_quality(filename, include_header_row):
    data = get_file_contents(filename)
    if "This file cannot be found!" in data:
        return data
    
    lines = [data[0]]
    christmas_data = [] #[print(line) or line for line in lines if "25/12" in line]
    
    for line in data:
        if "25/12" in line:
            christmas_data.append(line)
    
    if include_header_row:
        return [lines[0]] + christmas_data
    else:
        return christmas_data
# Purpose: fetch Christmas Day average of "PT08.S1(CO)" values to 2 decimal places
# Example:
#   Call: christmas_day_average_air_quality("AirQuality.csv")
#   Returns: 1439.21
# Data sample:
# Date;Time;CO(GT);PT08.S1(CO);NMHC(GT);C6H6(GT);PT08.S2(NMHC);NOx(GT);PT08.S3(NOx);NO2(GT);PT08.S4(NO2);PT08.S5(O3);T;RH;AH;;
# 10/03/2004;18.00.00;2,6;1360;150;11,9;1046;166;1056;113;1692;1268;13,6;48,9;0,7578;;
def christmas_day_average_air_quality(filename):
    """ fetch christmas day average of a specific cell?? converting it into a float, does python even do that?"""
    data = get_file_contents(filename)
    if "This file cannot be found!" in data:
        return data
    
    christmas_data = [line for line in data if "25/12" in line]
    
    PT08 = [float(line.split(';') [3].replace(',', '.')) for line in christmas_data]
    if PT08:
        average = sum(PT08) / len(PT08)
        return round(average, 2)
    
    
# Purpose: scrape all the data and calculate average values for each of the 12 months
#          for the "PT08.S1(CO)" values, returning a dictionary of keys as integer
#          representations of months and values as the averages (to 2 decimal places)
# Example:
#   Call: get_averages_for_month("AirQuality.csv")
#   Returns: {1: 1003.47, [...], 12: 948.71}
# Notes:
# * Data from months across multiple years should all be averaged together
def get_averages_for_month(filename):
    data = get_file_contents(filename)
    if "This file cannot be found!" in data:
        return data
    
    month_sum = {i: [0, 0] for i in range(1, 13)} # storing the sum and count for months in a dict
    lines = data[1:] # making sure not to record header
    
    for line in lines:
        fields = line.strip().split(';') #splitting each line into fields at every semi colon
        if len(fields) >=4: # checking that each line has 4 fields
            date_parts = fields[0].split('/') # splitting the dates into parts of day month year
            
            if len(date_parts) >= 3: # because we're changing the 3rd field we need to check it exists
                
                month = int(date_parts[1]) # get the month field and turn it into an integer
                PT08 = float(fields[3].replace(',', '.')) #get PT08's cell and turn it into a float
        
        
                month_sum[month][0] += PT08 # add pt08 to the key in the dictionary
                month_sum[month][1] += 1 # add 1 to the month count in the dictionary
    #this calculates the average for each month if the month has at least 1 count and stores it in the average dict
    average = {month: round(month_sum[month][0] / month_sum[month][1], 2) for month in month_sum if month_sum[month][1] > 0}
        
    return average # returns the average dict
        
        
# Purpose: write only the rows relating to March (any year) to a new file, in the same
# location as the original, including the header row of labels
# Example
#   Call: create_march_data("AirQuality.csv")
#   Returns: nothing, but writes header + March data to file called
#            "AirQualityMarch.csv" in same directory as "AirQuality.csv"
def create_march_data(filename):
    
    data = get_file_contents(filename)
    if "This file cannot be found!" in data:
        return data
    
    march = [line for line in data if "/03" in line] # stores all lines from data that have /03 in them, surely will be related to the date only
    header = data[0] #stores the first line of data in header, first line usually being the header
    
    march_data_with_header = header + '\n'.join(march)
    
    with open("AirQualityMarch.csv", "w") as file:
        file.write(march_data_with_header)
    
# Purpose: write monthly responses files to a new directory called "monthly_responses",
# in the same location as AirQuality.csv, each using the name format "mm-yyyy.csv",
# including the header row of labels in each one.
# Example
#   Call: create_monthly_responses("AirQuality.csv")
#   Returns: nothing, but files such as monthly_responses/05-2004.csv exist containing
#            data matching responses from that month and year
def create_monthly_responses(filename):
    
    data = get_file_contents(filename)
    if "This file cannot be found!" in data:
        return data
    header = data[0]
    data_by_month = {}
    
    for line in data[1:]:
        fields = line.split(';')
        date_parts = fields[0].split('/')
        
        if len(date_parts) >= 3:
            month, year = date_parts[1], date_parts[2]
    
            os.makedirs("monthly_responses", exist_ok=True)
            
            key = f"{month}-{year}"
            data_by_month.setdefault(key, []).append(line)
            
            
            
    for month_year, month_data in data_by_month.items():    
        with open(f"monthly_responses/{month_year}.csv", "w") as file:
            file.writelines(header)
            for data_line in month_data:
                file.writelines(data_line)