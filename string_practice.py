###############################################
#Measurement Parser
###############################################

############################
# Part 1 - Email to Name   #
############################

def email_to_name(email):
    """
    (str) -> str
    
    Given a string with the format "first_name.last_name@domain.com",
    return a string "LAST_NAME,FIRST_NAME" where all the characters are upper
    case
    
    
    >>> email_to_name("anna.conda@mail.utoronto.ca")
    'CONDA,ANNA'
    """
    
    ## TODO: YOUR CODE HERE
    email_split = email.split('@')
    name_split = email_split[0].split('.') 
    LAST_NAME = name_split[1].upper()
    FIRST_NAME = name_split[0].upper()
    name = [LAST_NAME,FIRST_NAME]
    return ','.join(name) 


###############################
# Part 2 - Count Measurements #
###############################

def count_measurements(s):
    """
    (str) -> int
 
    Given s, a string representation of comma separated site-measurement
    pairs, return the total number of measurements
 
    >>> count_measurements("B, 5.6, Control, 5.5, Db, 3.2")
    3
    
    >>> count_measurements("Control, 7.5")
    1
    """
    
    #TODO: YOUR CODE HERE
    str_list = s.split(',') #turning the string into a list
    counter = 0
    for index in range(0, len(str_list), 2): #counting the odd-indexed values
        counter += 1
    return counter    



######################################
# Part 3 - Calculate Site Average    #
######################################

def calc_site_average(measurements, site):
    """
    (str, str) -> float
 
    Given s, a string representation of comma separated site-measurement
    pairs, and the name of a site, 
    return the average of the site measurements to one decimal place
    
    
    >>> calc_site_average("A, 4.2, B, 6.7, Control, 7.1, B, 6.5, Control, 7.8, Control, 6.8, A, 3.9", "Control")
    7.2
    """
    
    ## TODO: YOUR CODE HERE
    str_list = measurements.split(',') #turning the string into a list
    average = 0
    counter = 0
    total = 0
    
    for index in range(len(str_list)): 
        if str_list[index].strip() == site:
            total += float(str_list[index+1]) #sum of numbers
            counter += 1 #total values
    
    return round((total / counter),1) 

###############################
# Part 4 - Generate Summary   #
###############################

def generate_summary(measurement_info, site):
    """
    (str, str) -> str
    
    Extract technician name, number of measurements, and average of control
    site pH level measurements from string of technician measurements. Input
    string is formatted as
    
        firstname.lastname@domain.com, date, sitename, measurement, sitename, measurement, ...
    
    returns a string with the extracted information formatted as
    
        LASTNAME,FIRSTNAME,number of measurements,average pH of specified site
 
    >>> generate_summary("dina.dominguez@company.com, 01/11/20, A, 4.2, B, 6.7, Control, 7.1, B, 6.5, Control, 7.8, Control, 6.8, A, 3.9", "Control")
    'DOMINGUEZ,DINA,7,7.2'
    """
    
    ## TODO: YOUR CODE HERE
    info_1 = email_to_name(measurement_info)
    
    new_string = measurement_info.split(",",2)[2] #spliting the string tp start from the 3rd element
    info_2 = count_measurements(new_string)
    
    info_3 = calc_site_average(new_string, site)
    
    info = [info_1,str(info_2),str(info_3)]
    return ','.join(info)    #converting list to string 

