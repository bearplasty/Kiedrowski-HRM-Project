import csv
sculptures_dict = {
    "Cast bronze":0,
    "Cast iron":0,
    "Marble":0,
    "Painted vinyl":0,
    "Porcelain":0,
    "Steel":0,
    "Granite":0,
    "Vinyl":0,
    "Neon":0,
    "Earthenware":0,
    "Plaster":0,
    "Wood":0,
    "Ivory":0,
    "Other":0}
    
with open('sculptures.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         if "Cast bronze" in row["Media"] or "bronze" in row["Media"] or "Bronze" in row["Media"]:
            sculptures_dict["Cast bronze"]=sculptures_dict["Cast bronze"]+1
         elif "Cast iron" in row["Media"]:
            sculptures_dict["Cast iron"]=sculptures_dict["Cast iron"]+1
         elif "Painted vinyl" in row["Media"]:
            sculptures_dict["Painted vinyl"]=sculptures_dict["Painted vinyl"]+1
         elif "Porcelain" in row["Media"] or "porcelain" in row["Media"] or "ceramic" in row["Media"]:
            sculptures_dict["Porcelain"]=sculptures_dict["Porcelain"]+1
         elif "Steel" in row["Media"] or "steel" in row["Media"]:
            sculptures_dict["Steel"]=sculptures_dict["Steel"]+1
         elif "Granite" in row["Media"]:
            sculptures_dict["Granite"]=sculptures_dict["Granite"]+1
         elif "Vinyl" in row["Media"] or "vinyl" in row["Media"]:
            sculptures_dict["Vinyl"]=sculptures_dict["Vinyl"]+1
         elif "Neon" in row["Media"] or "neon" in row["Media"]:
            sculptures_dict["Neon"]=sculptures_dict["Neon"]+1
         elif "Marble" in row["Media"] or "marble" in row["Media"]:
            sculptures_dict["Marble"]=sculptures_dict["Marble"]+1
         elif "Plaster" in row["Media"] or "plaster" in row["Media"]:
            sculptures_dict["Plaster"]=sculptures_dict["Plaster"]+1
         elif "Wood" in row["Media"] or "wood" in row["Media"]:
            sculptures_dict["Wood"]=sculptures_dict["Wood"]+1
         elif "Ivory" in row["Media"] or "ivory" in row["Media"]:
            sculptures_dict["Ivory"]=sculptures_dict["Ivory"]+1
         elif "Earthenware" in row["Media"] or "earthenware" in row["Media"]:
            sculptures_dict["Earthenware"]=sculptures_dict["Earthenware"]+1
         elif "Stone" in row["Media"] or "Cash Register" in row["Media"] or "metal" in row ["Media"] or "Metal" in row ["Media"] or "Mixed" in row ["Media"]:
            sculptures_dict["Other"]=sculptures_dict["Other"]+1
         else:
             print (row["Media"])
         #print(row['Location'], row['Unit/Box #'], row['Accession #'], row['Artist'], row['Title'], row['Date'], row['Media'], row['Dimensions'])

total_percent = 0
for media in sculptures_dict:
    sculptures_dict[media] = round(sculptures_dict[media]/100*100, 2)
    total_percent = total_percent + sculptures_dict[media]

print(sculptures_dict)
print(total_percent)