import json
import glob
cp = '{ "copyright":"aW", "source" :'
result = []
path = "./merge_action_test/folder2/**/*.json"
for filename in glob.glob(path, recursive=True):
    with open(filename, 'r') as infile:
        print(filename);
       
        result.extend(json.load(infile))
        
        
with open("./merged_file.json", "w") as outfile:
     o1.write('')
     o1.write(cp)
     json.dump(result, outfile)
     o1.write('}')   
   #  print(result)
       
