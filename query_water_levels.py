
from dotenv import load_dotenv
load_dotenv()
import requests
import json
import datetime

#MURRAY DARLING POINTS
'''
401012 - Murray @ Bigarra - Level (m), D.O., Discharge (ML/d), EC @ 25C, Temp(C), Rainfall (mm)
401027 - Murray @ Hume Dam - Res. Level (m), % Eff. Full Stor, Volume (ML)
409017 - Murray @ Doctors Point - Level (m), Discharge (ML/d), EC @ 25C, Temp(C)
409023 - Stevens Weir Downstream
425007 - Darling @ Burtundy  - Level (m), D.O., Discharge (ML/d), EC @ 25C, Temp(C), Rainfall (mm)
409001 - Murray @ Albury (Union Bridge) - water temp, level, EC
410130 - Murrumbidgee @ Balranald - Level (m), D.O., Discharge (ML/d), EC @ 25C, Temp(C)
401549 - Murray @ Bringenbong - level, discharge (mld)
401211 - Mitta Mitta @ Colemans - level, discharge (mld)
41310022 - Murray @ Colignan - EC, temp
409002 - Murray @ Corowa - Level (m), Discharge (ML/d), EC @ 25C, Temp(C)
401224A - Mitta Mirra @ Dartmouth Dam - Res. Level (m), % Eff. Full Stor, Volume (ML)
409008 - Edward @ Offtake - Level (m), Discharge (ML/d), EC @ 25C, Temp(C)
409030 - Gulpa Creek @ Offtake - level, discharge (mld)
401013 - Jingellic Creek @ Jingellic - Level (m), Discharge (ML/d), EC @ 25C, Temp(C)
409029 - Mulwala Canal escape @ Edwards River - Level (m), Discharge (ML/d), EC @ 25C, Temp(C)
401014 - Tooma River @ Pinegrove - Level (m), Discharge (ML/d), EC @ 25C, Temp(C), Rainfall (mm)
41310025 - Murray @ Redcliff - temp
409013 - Wakool River @ Stoney Crossing - Level (m), D.O., Discharge (ML/d), EC @ 25C, Temp(C)
409023 - Edward River @ Downstream Steven's Weir - Level (m), Discharge (ML/d), EC @ 25C, Temp(C)
409101 - Edward River @ Upstream Steven's Weir - Res leve (m), level (m)
409204C - Murray @ Swan Hill - no data
401204A - Mitta Mirra @ Tallandoon - no data
409202A - Murray @ Tocumwal - no data
425012 - Darling @ Weir 32 - Level (m), Discharge (ML/d), EC @ 25C, Temp(C)
409025 - Murray @ Yarrawonga Downstream - Level (m), Discharge (ML/d), EC @ 25C, Temp(C)
409216A - Murray @ Yarrawonga Upstream - level (m)
'''

#variable codes
'''
Varfrom=100, varto=100, for stored water level in metres
Varfrom=100, varto=140, for discharge in cubic metres/second
Varfrom=100, varto=141, for discharge in megalitres/day
Varfrom=2010, varto=2010, for compensated electrical conductivity in microsiemens/cm
Varfrom=2080, varto=2080, for water temperature in degree Celsius
Varfrom=10, varto=10 for rainfall (mm)
Varfrom=130, varto=130 for Reservoir level (m) - Dam
'''

Murray_Darling_ids = ['401012','401027','409017','409023','425007','409001',
    '410130','401549','401211','41310022','409002','401224A','409008','409030',
    '401013','409029','401014','41310025','409013','409023','409101','409204C',
    '401204A','409202A','425012','409025','409216A']
Bigarra_id = '401012'

#stores varto values with corresponding measure
variable_dict = {100.0: 'waterLevel', 140.0: 'dischargeCMS', 141.0: 'discharge',
    2010.0: 'electricalConductivity', 2080.0: 'temperature', 10.0: 'rainfall',
    130.0: 'reservoirLevel'}




sample_var_string = '{"varfrom":100,"varto":100},{"varfrom":"100","varto":"141"}\
    ,{"varfrom":"2010","varto":"2010"},{"varfrom":"10","varto":"10"}\
    ,{"varfrom":"130","varto":"130"}'


request_string = 'https://realtimedata.waternsw.com.au/cgi/webservice.pl?' + \
'{"function":"get_ts_traces","version":"2","params":{"site_list":"410001,410004","datasource":"PROV","varfrom":"100","varto":"141","start_time":"20191210000000","end_time":"20191211000000","interval":"day","multiplier":"1","data_type":"POINT"}}&ver=2'

base_string = 'https://realtimedata.waternsw.com.au/cgi/webservice.pl?'
sl_query_object = '{"function": "get_site_list","version": 1,"params": {"site_list": "MATCH(20301*)"}}&ver=1'
#ts_query_object = '{"function":"get_latest_ts_values","version":2,"params":{"site_list":"'+ site_id + '","datasource":"PROV","trace_list":[{"varfrom":100,"varto":141},{"varfrom":"141","varto":"141"}]}}'
sbds_query_object = '{"function": "get_sites_by_datasource","version": 1,"params" : {"datasources": ["PROV"]}}'

# # get number of PROV sites
# response = requests.get(base_string + sbds_query_object)
# return_value = response.json()
# print(len(return_value['_return']['datasources'][0]['sites']))




def query_ts_values(site_id, var_string):
    base_string = 'https://realtimedata.waternsw.com.au/cgi/webservice.pl?'

    query_object = '{"function":"get_latest_ts_values","version":2,"params":{"site_list":"' +\
        site_id + '","datasource":"PROV","trace_list":[' + var_string + ']}}'
    signals = []

    response = requests.get(base_string + query_object)
    return_value = response.json()
    for value in return_value['_return']:
        # print(return_value['_return'][value])
        # print('\n')
        dict_list = return_value['_return'][value]
        for dictionary in dict_list:
            if 'error_num' not in dictionary.keys():

                #each entry in the list in dictionary['values'] has 'v': value,
                #'time': YYYYMMDDHHMMSS ...
                for entry in dictionary['values']:
                    variable_name = variable_dict[float(dictionary['varto'])]
                    time_stamp = datetime.datetime.strptime(entry['time'], '%Y%m%d%H%M%S')
                    signals.append({'t': time_stamp, variable_name: entry['v']})

    return signals

def query_site_list():
    base_string = 'https://realtimedata.waternsw.com.au/cgi/webservice.pl?'
    sl_query_object = '{"function": "get_site_list","version": 1,"params": {"site_list": "MATCH(20301*)"}}&ver=1'
    response = requests.get(base_string + sl_query_object)
    return_value = response.json()
    return return_value['_return']['sites']

print(query_ts_values('401027', sample_var_string))
