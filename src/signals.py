from amphora_client import Signal

def signals():
    return [
        Signal(_property='description', value_type='String'),
        Signal(_property='temperature', value_type='Numeric', attributes={'units': 'degrees C'}),
        Signal(_property='rainfall', value_type='Numeric', attributes={'units': 'mm'}),
        Signal(_property='waterLevel', value_type='Numeric', attributes={'units': 'm'}),
        Signal(_property='discharge', value_type='Numeric', attributes={'units': 'ML/day'}),
        Signal(_property='elecConductivity', value_type='Numeric', attributes={'units': 'microsiemens/cm'}),
        Signal(_property='reservoirLevel', value_type='Numeric', attributes={'units': 'm'}),
    ]
