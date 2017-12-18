import csv
drawings_dict = {
    "Pen and ink":0,
    "Pencil and ink":0,
    "Ink on paper":0,
    "Pencil on paper":0,
    "Charcoal on paper":0,
    "Charcoal and pastel":0,
    "Pencil and chalk":0,
    "Ink wash":0,
    "Charcoal and pencil":0,
    "Charcoal and chalk":0,
    "Pastel and graphite":0,
    "Charcoal and ink":0,
    "Ink and pastel":0,
    "Charcoal and crayon":0,
    "Pastel and chalk":0,
    "Watercolor with pen, pencil, or graphite":0,
    "Ink and brush":0,
    "Graphite":0,
    "Pencil and wash":0,
    "Pastel on paper":0,
    "Chalk on paper":0,
    "Charcoal on paper":0,
    "Crayon on paper":0,
    "Other":0}
    
with open('drawings.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         if "Pen and ink" in row["Media"] or "Pen, ink" in row["Media"]:
            drawings_dict["Pen and ink"]=drawings_dict["Pen and ink"]+1
         elif "Ink on paper" in row["Media"] or "Ink on board" in row ["Media"] or "Ink on Paper" in row ["Media"] or "Paper, ink" in row ["Media"]:
            drawings_dict["Ink on paper"]=drawings_dict["Ink on paper"]+1
         elif "Pencil and ink" in row["Media"] or "Ink and pencil" in row ["Media"] or "Pencil, ink" in row ["Media"]:
            drawings_dict["Pencil and ink"]=drawings_dict["Pencil and ink"]+1
         elif "Charcoal on paper" in row["Media"]:
            drawings_dict["Charcoal on paper"]=drawings_dict["Charcoal on paper"]+1
         elif "Charcoal and pastel" in row["Media"] or "Charcoal, pastel" in row ["Media"] or "Pastel and charcoal" in row ["Media"]:
            drawings_dict["Charcoal and pastel"]=drawings_dict["Charcoal and pastel"]+1
         elif "Pencil and chalk" in row["Media"]:
            drawings_dict["Pencil and chalk"]=drawings_dict["Pencil and chalk"]+1
         elif "Ink wash" in row["Media"] or "Ink and wash" in row ["Media"] or "ink wash" in row ["Media"]:
            drawings_dict["Ink wash"]=drawings_dict["Ink wash"]+1
         elif "Charcoal and pencil" in row["Media"] or "Pencil, charcoal" in row ["Media"]:
            drawings_dict["Charcoal and pencil"]=drawings_dict["Charcoal and pencil"]+1
         elif "Charcoal and chalk" in row["Media"] or "Charcoal, white chalk" in row ["Media"] or "Chalk, charcoal" in row ["Media"]:
            drawings_dict["Charcoal and chalk"]=drawings_dict["Charcoal and chalk"]+1
         elif "Pastel and graphite" in row["Media"]:
            drawings_dict["Pastel and graphite"]=drawings_dict["Pastel and graphite"]+1
         elif "Charcoal and ink" in row["Media"]:
            drawings_dict["Charcoal and ink"]=drawings_dict["Charcoal and ink"]+1
         elif "Ink and pastel" in row["Media"]:
            drawings_dict["Ink and pastel"]=drawings_dict["Ink and pastel"]+1
         elif "Charcoal with white crayon" in row["Media"] or "crayon, charcoal" in row["Media"]:
            drawings_dict["Charcoal and crayon"]=drawings_dict["Charcoal and crayon"]+1
         elif "watercolor" in row["Media"] or "Watercolor" in row["Media"] or "gouache" in row["Media"]:
            drawings_dict["Watercolor with pen, pencil, or graphite"]=drawings_dict["Watercolor with pen, pencil, or graphite"]+1
         elif "Pastel and chalk" in row["Media"]:
            drawings_dict["Pastel and chalk"]=drawings_dict["Pastel and chalk"]+1
         elif "Ink and brush" in row["Media"] or "Brush and ink" in row["Media"]:
            drawings_dict["Ink and brush"]=drawings_dict["Ink and brush"]+1
         elif "Graphite" in row["Media"] or "graphite" in row ["Media"]:
            drawings_dict["Graphite"]=drawings_dict["Graphite"]+1
         elif "Pencil and wash" in row["Media"] or "pencil and wash" in row ["Media"]:
            drawings_dict["Pencil and wash"]=drawings_dict["Pencil and wash"]+1
         elif "Pastel on" in row["Media"]:
            drawings_dict["Pastel on paper"]=drawings_dict["Pastel on paper"]+1
         elif "Chalk on" in row["Media"]:
            drawings_dict["Chalk on paper"]=drawings_dict["Chalk on paper"]+1
         elif "Charcoal on" in row["Media"]:
            drawings_dict["Charcoal on paper"]=drawings_dict["Charcoal on paper"]+1
         elif "crayon on" in row["Media"] or "Conte" in row["Media"]:
            drawings_dict["Crayon on paper"]=drawings_dict["Crayon on paper"]+1
         elif "Pencil on paper" in row["Media"] or "Pencil on Paper" in row ["Media"] or "pencil on paper" in row ["Media"] or "Paper, pencil" in row ["Media"] or "Pencil on" in row ["Media"] or "colored pencil" in row ["Media"] or "pencil" in row["Media"]:
            drawings_dict["Pencil on paper"]=drawings_dict["Pencil on paper"]+1
         elif "Metal" in row["Media"] or "Not noted" in row["Media"] or "Mixed" in row["Media"] or "Engraving" in row["Media"] or "Pastel," in row["Media"]:
            drawings_dict["Other"]=drawings_dict["Other"]+1
         else:
             print (row["Media"])
         #print(row['Location'], row['Unit/Box #'], row['Accession #'], row['Artist'], row['Title'], row['Date'], row['Media'], row['Dimensions'])

total_percent = 0
for media in drawings_dict:
    drawings_dict[media] = round(drawings_dict[media]/271*100, 2)
    total_percent = total_percent + drawings_dict[media]

print(drawings_dict)
print(total_percent)