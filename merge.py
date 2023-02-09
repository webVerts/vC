import json
import glob
import time

today = time.strftime("%d-%b-%Y %I:%M:%S %p - %Z" )


result = []
path = "./merge_action_test/folder2/**/*.json"
for filename in glob.glob(path, recursive=True):
    with open(filename, 'r') as infile:
        print(filename);
       
        f2=result.extend(json.load(infile))

length=length=len(f2)        
cp = '{ "copyright":"me","updated_on":"'+today +'","total":"'+length+'", "source" :'        
with open("./merged_file.json", "w") as o1:
     o1.write('')
     o1.write(cp)
     o1.write("\n")
     json.dump(result, o1)
     o1.write("\n")
     o1.write('}')   
   #  print(result)
       
