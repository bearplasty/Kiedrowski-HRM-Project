import csv
paintings_dict = {
    "Acrylic and oil":0,
    "Oil on canvas":0,
    "Oil on board":0,
    "Acrylic on canvas":0,
    "Acrylic on paper":0,
    "Oil on paper":0,
    "Casein":0,
    "watercolor on paper":0,
    "graphite on canvas":0,
    "Gouache on board":0,
    "Tempera on board":0,
    "Mixed media on canvas":0,
    "Ink and collage":0,
    "Oil on wood":0,
    "Oil on masonite":0,
    "Other":0}
    
with open('paintings.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         if "Acrylic and oil" in row["Media"]:
            paintings_dict["Acrylic and oil"]=paintings_dict["Acrylic and oil"]+1
         elif "Oil on canvas" in row["Media"] or "Oil on Canvas" in row["Media"]:
            paintings_dict["Oil on canvas"]=paintings_dict["Oil on canvas"]+1
         elif "Oil on board" in row["Media"]:
            paintings_dict["Oil on board"]=paintings_dict["Oil on board"]+1
         elif "Acrylic on canvas" in row["Media"]:
            paintings_dict["Acrylic on canvas"]=paintings_dict["Acrylic on canvas"]+1
         elif "Acrylic on paper" in row["Media"]:
            paintings_dict["Acrylic on paper"]=paintings_dict["Acrylic on paper"]+1
         elif "Oil on paper" in row["Media"]:
            paintings_dict["Oil on paper"]=paintings_dict["Oil on paper"]+1
         elif "Casein" in row["Media"] or "casein" in row["Media"]:
            paintings_dict["Casein"]=paintings_dict["Casein"]+1
         elif "watercolor on paper" in row["Media"]:
            paintings_dict["watercolor on paper"]=paintings_dict["watercolor on paper"]+1
         elif "graphite on canvas" in row["Media"]:
            paintings_dict["graphite on canvas"]=paintings_dict["graphite on canvas"]+1
         elif "Gouache on board" in row["Media"]:
            paintings_dict["Gouache on board"]=paintings_dict["Gouache on board"]+1
         elif "Tempera on board" in row["Media"]:
            paintings_dict["Tempera on board"]=paintings_dict["Tempera on board"]+1
         elif "Mixed media on canvas" in row["Media"]:
            paintings_dict["Mixed media on canvas"]=paintings_dict["Mixed media on canvas"]+1
         elif "Ink and collage" in row["Media"]:
            paintings_dict["Ink and collage"]=paintings_dict["Ink and collage"]+1
         elif "Oil on masonite" in row["Media"]:
            paintings_dict["Oil on masonite"]=paintings_dict["Oil on masonite"]+1
         elif "Oil on wood" in row["Media"]:
            paintings_dict["Oil on wood"]=paintings_dict["Oil on wood"]+1
         elif "Silk" in row["Media"] or "Leather" in row["Media"] or "Oil" in row ["Media"]:
            paintings_dict["Other"]=paintings_dict["Other"]+1
         else:
             print (row["Media"])
         #print(row['Location'], row['Unit/Box #'], row['Accession #'], row['Artist'], row['Title'], row['Date'], row['Media'], row['Dimensions'])

total_percent = 0
for media in paintings_dict:
    paintings_dict[media] = round(paintings_dict[media]/70*100, 2)
    total_percent = total_percent + paintings_dict[media]

print(paintings_dict)
print(total_percent)