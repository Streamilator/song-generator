# SUPER COOL TITLE !1!!!!!11111
print('''                                                                                 
eeeee eeeee eeeee eeeee    eeeee eeee eeeee eeee eeeee  eeeee eeeee eeeee eeeee  
8   " 8  88 8   8 8   8    8   8 8    8   8 8    8   8  8   8   8   8  88 8   8  
8eeee 8   8 8e  8 8e       8e    8eee 8e  8 8eee 8eee8e 8eee8   8e  8   8 8eee8e 
   88 8   8 88  8 88 "8    88 "8 88   88  8 88   88   8 88  8   88  8   8 88   8 
8ee88 8eee8 88  8 88ee8    88ee8 88ee 88  8 88ee 88   8 88  8   88  8eee8 88   8 
                                                                                 ''')

########################
# IMPORTS              #
########################

import json, pathlib

########################
# INPUTS               #
########################

songname = input("Song name: ")
songauthor = input("Song author: ")
songfile = input("Song file: ")
jsonfile = input("Songs.json file path: ")
if jsonfile == "":
    jsonfile = "C:\\Users\\wlodz\\Desktop\\.py\\streamilator\\songs.json"
elif not jsonfile.lower().startswith("c:"):
    
    print('Getting current working directory : ', str(pathlib.Path().absolute()))
    jsonfile = str(pathlib.Path().absolute()) + '\\' + jsonfile

if __name__ == '__main__':
    
    # Opening JSON file
    f = open(jsonfile)
    
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    
    # Editing json
    data["entries"] += 1
    data["names"][str(data["entries"])] = f"{songauthor}: {songname}"
    print()
    print(json.dumps(data, indent=4, separators=(", ", ": ")))
    print("\n")
    # Closing file
    f.close()

    # Open file for writing
    f = open(jsonfile, "w")
    f.write(json.dumps(data, indent=4, separators=(", ", ": ")))
    print("Don e!\n")
    print(f'Please save your song as {data["enteries"]}.mp3')

else:
    print("please run the .py file")