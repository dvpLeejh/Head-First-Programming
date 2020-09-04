def find_details(id2find):
    surfers_f = open("surfing_data.csv")
    for line in surfers_f:
        s = {}
        (s['id'], s['name'], s['country'], s['average'], s['board'], s['age']) = line.split(';')

        if s['id'] == id2find:
            surfers_f.close()
            return(s)
    surfers_f.close()
    return({})

lookup_id = input(("Enter the id of the surfer: "))

surfer = find_details(lookup_id)

if surfer:
    print("ID:  " + surfer['id'])
    print("Name: " + surfer['name'])
    print("Country: " + surfer['country'])
    print("Average: " + surfer['average'])
    print("Board types: " + surfer['board'])
    print("Age: " + surfer['age'])
    
