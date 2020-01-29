
#my file
import requests
import json
import datetime
from src.sites import vic_site_info
from src.variables import vic_variable_codes, vic_variable_string
from src.load_water_levels import query_ts_values

def query_ts_values(site_id, var_string, var_dict):
    #changed base_string
    base_string = 'http://data.water.vic.gov.au/cgi/webservice.pl?'

    #changed prov to publish
    query_object = '{"function":"get_latest_ts_values","version":2,"params":{"site_list":"' +\
        site_id + '","datasource":"PUBLISH","trace_list":[' + var_string + ']}}'
    signals = []


    try:
        response = requests.get(base_string + query_object)
        return_value = response.json()
    except:
        print("API call unsuccessful")
        return


    for value in return_value['_return']:
        dict_list = return_value['_return'][value]
        for dictionary in dict_list:
            if 'error_num' not in dictionary.keys():

                #each entry in the list in dictionary['values'] has 'v': value,
                #'time': YYYYMMDDHHMMSS ...
                for entry in dictionary['values']:
                    variable_name = var_dict[float(dictionary['varto'])]

                    #TODO: figure out what timestamp format is best
                    time_stamp = datetime.datetime.strptime(entry['time'], '%Y%m%d%H%M%S')
                        #.strftime("%Y-%m-%d %H:%M:%S")

                    try:
                        entry_value = float(entry['v'])
                    except ValueError as e:
                        print("value not received as float: %s\n" % e)
                        raise e

                    #put values with same timestamp in same dictionary
                    same_time_index = next((index for (index, d) in enumerate(signals) if d['t'] == time_stamp), None)
                    if same_time_index != None:
                        signals[same_time_index][variable_name] = entry_value
                    else:
                        signals.append({'t': time_stamp, variable_name: entry_value})

    return signals

vic_dict = vic_site_info()
for site_id,info in vic_dict.items():

    var_string = vic_variable_string()
    var_dict = vic_variable_codes()
    signals = query_ts_values(site_id, var_string, var_dict)
    print(info['name'] + ': ' + site_id)
    print(signals)
    print('\n')
