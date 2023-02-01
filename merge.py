import json
import glob

result = []
path = "merge_action_test/folder1/*.json"
for filename in glob.glob(path, recursive=True):
    with open(filename, 'r') as infile:
        print(path);
        
    with open("merged_file.json", "w") as outfile:
        json.dump(result, outfile)       
        
       
