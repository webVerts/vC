import json
with open('data.json') as f1:
    f2 = json.load(f1)
    data = json.dumps(f2)

cp = '{ "copyright":"me", "source" :'
with open('everythingdata.json', 'w') as o1:
  o1.write('')
  o1.write(cp)
  json.dump(f2, o1)
  o1.write('}')
    print(cp);
        
       
