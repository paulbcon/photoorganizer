import os
import os.path

def extract_place(filename):
    try: 
        return filename.split("_")[1]
    except IndexError:
        print("Index is out of range")
def make_place_directories(places):
    for l in places:
        try:
            if not os.path.isdir(l):
                os.mkdir(l)
        except:
            print("There was an error creating directory")
os.chdir("photos")
originals = os.listdir()
places = []
for filename in originals:
    place = extract_place(filename)
    places.append(place)

make_place_directories(places)

for filename in originals:
    place = extract_place(filename)
    if not os.path.exists(os.path.join(place, filename)):
        os.rename(filename, os.path.join(place, filename))

print(os.listdir())

    
