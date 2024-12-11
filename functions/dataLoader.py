import json
import argparse

def getAllTexts(show: str):
    # Data files
    json_file1 = 'data/'+ show + '-newest-23-02-24.json' # 250
    json_file2 = 'data/'+ show + '-oldest-23-02-24.json' #250
    json_file3 = 'data/'+ show + '-featured-26-02-24.json' # 250

    # Open JSON files 
    with open(json_file1) as json_data:
        data1 = json.load(json_data)

    with open(json_file2) as json_data:
        data2 = json.load(json_data)

    with open(json_file3) as json_data:
        data3 = json.load(json_data)

    # Concatenate files into single array
    data = data1 + data2 + data3

    print(str(len(data)) + ' reviews on ' + show)

    return data




