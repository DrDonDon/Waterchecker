from dotenv import load_dotenv
load_dotenv(verbose=True)

import os
import json
import amphora_client

from src.mapping import water_save, water_load
from src.sites import site_info
from src.signals import signals
from src.upload_signals import create_or_update_amphorae, upload_signals_to_amphora
#maybe from src.load_water_levels import query_ts_values


sites = site_info()
water_locations = dict()
location_infos = dict()
# check we have all the amphora we need
for key,value in sites.items():
    store = dict()
    location_info = dict()

    code = key
    store[code] = None
    location_info[code] = sites[key]

    water_locations.update(store)
    location_infos.update(location_info)

amphora_map = water_load()

water_locations.update(amphora_map)
print(water_locations)


new_store = create_or_update_amphorae(water_locations, location_infos)
water_save(new_store)

# for each WZ Location, run the ETL process
for water_lc, amphora_id in new_store.items():
    upload_signals_to_amphora(water_lc, amphora_id)



'''
amphora_map = {'401012': '5959944b-579b-4067-a7d7-94207c2d0ed7',
    '401027': '72bbad07-57bb-4973-8602-a6f791415bdb',
    '409017': '910a761c-8a26-4cf6-83d7-b1b3589caf01',
    '425007': 'b7c509a1-28d4-41db-910a-0cb9d4a422dc',
    '409001': '52f4fec3-18e7-4f5a-948c-3a021d7b9ae8',
    '410130': 'e8157f06-a395-4a6c-8bf9-e990a3db0d24',
    '401549': 'b5e88f4f-b718-4e17-a90f-38a6c78bf765',
    '401211': '426f87f5-4bf3-4107-8576-de3674e6ea39',
    '41310022': '31fcc60a-3daf-4b19-828e-5d7c1c50d3e5',
    '409002': '086a48c2-3543-4c73-b5f0-7fc3b8fe0a03',
    '401224A': 'cabfd8c3-68ca-4d70-94d4-e0e52c1f9bb1',
    '409008': 'b4246042-8631-4674-9564-77669d93e7e9',
    '409030': '16ea0df8-5367-4cd8-aa8f-12002c7d6dd1',
    '401013': 'a3fb8762-96bd-4952-8e8e-fc7b8312c712',
    '409029': 'd4eafd3a-473b-4606-a820-9fd07badcbac',
    '401014': '0e3972cf-b9bc-41d8-8368-263e497ca427',
    '41310025': 'a0ec7474-de6e-47c0-a64c-c07182f2e12a',
    '409013': '5805dd7a-a4ed-4493-94f8-28b8b8d22c65',
    '409023': '5d57ea1f-791b-4a26-9d63-b69397299a18',
    '409101': 'c9c5b9a5-1a84-431d-83be-b2773a76ef8a',
    '409204C': 'b22607ee-f751-4a02-9a4f-f31f3a582f18',
    '401204A': '290c73e7-36b8-4859-927c-fcf76ac81ded',
    '409202A': '773731d8-638b-4aeb-be3f-c6547956fa3c',
    '425012': '865b0c2f-658f-4e90-ad2f-a1abec4b95c5',
    '409025': 'f6582344-bb29-47e0-b62c-52e69a89d202',
    '409216A': '8ca1416b-b156-4f11-80c3-7f9f135af70e',
}
'''
