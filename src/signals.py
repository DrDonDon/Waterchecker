from amphora_client import SignalDto

def signals():
    return [
        SignalDto(_property='description', value_type='String'),
        SignalDto(_property='temperature', value_type='Numeric'),
        SignalDto(_property='rainfall', value_type='Numeric'),
        SignalDto(_property='waterLevel', value_type='Numeric'),
        SignalDto(_property='discharge', value_type='Numeric'),
        SignalDto(_property='dischargeCMS', value_type='Numeric'),
        SignalDto(_property='electricalConductivity', value_type='Numeric'),
        SignalDto(_property='reservoirLevel', value_type='Numeric'),
    ]
