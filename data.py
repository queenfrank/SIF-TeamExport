import json

regS = "&#34;"
regS2 = "&#39;"
regSand = "&amp;"


data = json.loads(raw_data)

def data_dict():
    return data