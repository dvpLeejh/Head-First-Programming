s = {}

line = "101;Johnny 'wave-boy' Jones;USA;8.32;Fish;21"

(s["ID"], s["Name"], s["Country"], s["Average"], s["Board"], s["Age"]) = line.split(";")

print("ID: " + s["ID"])
print("Name: " + s["Name"])
print("Country: " + s["Country"])
print("Average: " + s["Average"])
print("Board: " + s["Board"])
print("Age: " + s["Age"])
 
 
