
import os

from amphora_extensions import file_uploader
import amphora_client
from amphora_client import Configuration, ApiException

from src.sites import site_info
from src.variables import variable_codes, variable_string, vic_variable_codes, vic_variable_string, query_params
from src.load_water_levels import query_ts_values
from src.signals import signals


username=os.getenv('username')
password=os.getenv('password')


# amphora_map == dict from waternsw site id to amphora id
# location_info == dict from wz location to wz location information
def create_or_update_amphorae(amphora_map, location_info):
    # LOAD
    configuration = Configuration()

    # Create an instance of the Authentication class
    auth_api = amphora_client.AuthenticationApi(amphora_client.ApiClient(configuration))
    token_request = amphora_client.TokenRequest(username=username, password=password )

    new_map = dict()
    try:
        print("Logging in")
        token = auth_api.authentication_request_token(token_request = token_request)
        configuration.api_key["Authorization"] = "Bearer " + str(token)
        print("Logged in")
        client=amphora_client.ApiClient(configuration)
        amphora_api = amphora_client.AmphoraeApi(client)
        for key in amphora_map:
            id = amphora_map[key]
            if(id == None):
                # we have to create an Amphora
                waterloc = location_info[key]
                locname = waterloc['name']
                print(f'Creating new Amphora for location {locname}')
                # create the details of the Amphora
                name = 'Water Information: ' + waterloc['name'] + ' (' + waterloc['state'] + ')'
                desc = 'WaterNSW data, from ' + waterloc['name'] + '. WaterNSW site id: ' + key
                dto = amphora_client.CreateAmphoraDto(name=name, description=desc, price=0, lat=waterloc['lat'], lon=waterloc['long'])

                res = amphora_api.amphorae_create(create_amphora_dto=dto)
                # now create the signals
                print("Creating Signals")
                for s in signals():
                    amphora_api.amphorae_create_signal(res.id, signal_dto=s)

                new_map[key] = res.id
            else:
                a = amphora_api.amphorae_read(id)
                print(f'Using existing amphora: {a.name}')
                new_map[key] = id
                existing_signals = amphora_api.amphorae_get_signals(id)
                if(len(existing_signals) > 0):
                    print('Signals exist already')
                else:
                    print('Adding signals')
                    for s in signals():
                        amphora_api.amphorae_create_signal(id, signal_dto= s)

    except ApiException as e:
        print("Error Create or update amphorae: %s\n" % e)
        raise e

    return new_map

# this function runs a single ETL process for 1 WaterNSW location to one Amphora
def upload_signals_to_amphora(site_id, amphora_id, state_service):

    if state_service == 'NSW':
        var_string = variable_string()
        var_dict = variable_codes()
        NSW_params = query_params()[state_service]
        signals = query_ts_values(site_id, var_string, var_dict, NSW_params)

    elif state_service == 'VIC':
        var_string = vic_variable_string()
        var_dict = vic_variable_codes()
        VIC_params = query_params()[state_service]
        signals = query_ts_values(site_id, var_string, var_dict, VIC_params)

    else:
        print("error in upload_signals_to_amphora: state_service must be 'NSW' or 'VIC'")
        return

    if signals == None:
        print("No signals received")
        return

    print(signals)
    # LOAD
    configuration = Configuration()

    # Create an instance of the Authentication class
    auth_api = amphora_client.AuthenticationApi(amphora_client.ApiClient(configuration))
    token_request = amphora_client.TokenRequest(username=username, password=password )

    try:
        print("Logging In")
        token = auth_api.authentication_request_token(token_request = token_request)
        configuration.api_key["Authorization"] = "Bearer " + str(token)
        print("Logged in")
        client=amphora_client.ApiClient(configuration)

        amphora_api = amphora_client.AmphoraeApi(client)
        amphora = amphora_api.amphorae_read(amphora_id)
        print(f'Uploading signals to {amphora.name} {amphora.id}')

        print(signals)

        amphora_api.amphorae_upload_signal_batch(amphora.id, request_body = signals) # this sends the data to Amphora Data

        print(f'Sent {len(signals)} signals')

    except ApiException as e:
        print("Exception: %s\n" % e)
        raise e
