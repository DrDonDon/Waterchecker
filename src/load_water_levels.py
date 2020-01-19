
from dotenv import load_dotenv
load_dotenv()
import requests
import json
import datetime

request_string = 'https://realtimedata.waternsw.com.au/cgi/webservice.pl?\
{"function":"get_ts_traces","version":"2","params":{"site_list":"401012",\
"datasource":"PROV","varfrom":"100","varto":"141","start_time":"20191210000000",\
"end_time":"20191211000000","interval":"day","multiplier":"1","data_type":"POINT"}}&ver=2'


#we want 'PROV'
def get_sites_by_source(source):
    #to get sites by datasource (we want PROV)
    base_string = 'https://realtimedata.waternsw.com.au/cgi/webservice.pl?'
    sbds_query_object = '{"function": "get_sites_by_datasource","version": 1,\
    "params" : {"datasources": ["'+source+'"]}}'

    response = requests.get(base_string + sbds_query_object)
    return_value = response.json()
    return return_value['_return']['datasources'][0]['sites']


#returns most recent time series values for all available measurements
def query_ts_values(site_id, var_string, var_dict):
    base_string = 'https://realtimedata.waternsw.com.au/cgi/webservice.pl?'


    query_object = '{"function":"get_latest_ts_values","version":2,"params":{"site_list":"' +\
        site_id + '","datasource":"PROV","trace_list":[' + var_string + ']}}'
    signals = []

    response = requests.get(base_string + query_object)
    return_value = response.json()

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


#returns list of sites from the API
def query_site_list():
    base_string = 'https://realtimedata.waternsw.com.au/cgi/webservice.pl?'
    sl_query_object = '{"function": "get_site_list","version": 1,"params": {"site_list": "MATCH(20301*)"}}&ver=1'
    response = requests.get(base_string + sl_query_object)
    return_value = response.json()
    return return_value['_return']['sites']

#print(query_ts_values(Bigarra_id, sample_var_string))
