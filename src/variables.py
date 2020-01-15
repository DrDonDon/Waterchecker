
def variable_codes():
    return {
        100.0: 'waterLevel', 140.0: 'dischargeCMS', 141.0: 'discharge',
        2010.0: 'electricalConductivity', 2080.0: 'temperature',
        10.0: 'rainfall', 130.0: 'reservoirLevel'
    }

def variable_string():
    return  '{"varfrom":100,"varto":100},{"varfrom":"100","varto":"141"}\
    ,{"varfrom":"2010","varto":"2010"},{"varfrom":"10","varto":"10"}\
    ,{"varfrom":"130","varto":"130"},{"varfrom":"2080","varto":"2080"}'


#API request args
'''
Varfrom=100, varto=100, for stored water level in metres
Varfrom=100, varto=140, for discharge in cubic metres/second
Varfrom=100, varto=141, for discharge in megalitres/day
Varfrom=2010, varto=2010, for compensated electrical conductivity in microsiemens/cm
Varfrom=2080, varto=2080, for water temperature in degree Celsius
Varfrom=10, varto=10 for rainfall (mm)
Varfrom=130, varto=130 for Reservoir level (m) - Dam
'''
