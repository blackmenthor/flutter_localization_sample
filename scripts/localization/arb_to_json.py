import json, glob, os, collections
from collections import OrderedDict

folder_path = 'lib/l10n/arb/'
json_folder_path = 'lib/l10n/json/'

for filename in glob.glob(os.path.join(folder_path, 'intl_*.arb')):
    if filename != os.path.join(folder_path,'intl_messages.arb'):
    	with open(filename, 'r+') as json_file:
            newJsonOnly = {}
            currentJson = json.load(json_file, object_pairs_hook=OrderedDict)
            for item in currentJson:
                if not item.startswith('@'):
                    newJsonOnly[item] = currentJson[item]
            jsonString = json.dumps(newJsonOnly, indent=2)
            jsonName = filename.split('/')[-1].replace('arb','json')
            jsonFileName = os.path.join(json_folder_path, jsonName)
            with open(jsonFileName, 'w') as json_file_new:
                json_file_new.seek(0)
                json_file_new.write(jsonString)
                json_file_new.truncate()
