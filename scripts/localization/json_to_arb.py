import json, glob, os, collections
from collections import OrderedDict

folder_path = 'lib/l10n/arb/'
json_folder_path = 'lib/l10n/json/'

for jsonFileName in glob.glob(os.path.join(json_folder_path, 'intl_*.json')):
    with open(jsonFileName, 'r+') as json_file:
        currentJson = json.load(json_file, object_pairs_hook=OrderedDict)
        arbName = jsonFileName.split('/')[-1].replace('json','arb')
        arbFileName = os.path.join(folder_path, arbName)
        with open(arbFileName, 'r+') as arb_file:
            currentArb = json.load(arb_file, object_pairs_hook=OrderedDict)
            for item in currentJson:
                currentArb[item] = currentJson[item]
            arbString = json.dumps(currentArb, indent=2)
            arb_file.seek(0)
            arb_file.write(arbString)
            arb_file.truncate()