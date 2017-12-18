import csv, re
#open file
p = re.compile('(n\.d\.|[0-9]{4}-[0-9]{2}s|c\.\s*[0-9]{4}-[0-9]{4}|c\.\s*[0-9]{4}\s\(\?\)|c\.\s*[0-9]{4}\s\(neg\.\)|[0-9]{4}s\s*prints|c\.\s*[0-9]{4}|c\.\s*[0-9]{2}|[0-9]{4}-[0-9]{2}|c\.\s*[0-9]{4}\*|late\s*19th\s*C\.|late\s*19th\s*century|late\s*19\s*C\.|c\.\s*[0-9]{4}|late\s*19th\-early\s*20th\s*c\.|[0-9]{2}th\-[0-9]{2}st\s*centuries|early\s*20th\s*century|late\s*19th\.\s*c\?|early\s*20th\s*C\.\?|mid\s*[0-9]{2}th\s*C|early\s*20th\s*C\.|[0-9]{2}th\s*C\.|[0-9]{2}th\s*C\.|[0-9]{2}\s*C\.|[0-9]{4}\s*and\s*earlier|[0-9]{4}\*|20th\s*c\.|late\s*19 c\.|N\.D\.|[0-9]{4}s|mid\-19th C\.|19th\s*C\.|after\s*[0-9]{4}|c\.\s*[0-9]{4}|[0-9]{2}th\s*c\.|19[0-9]{2}|18[0-9]{2}|20[0-9]{2}|[0-9]{4}|[0-9]{2}th-e\.[0-9]{2}th)')

document = 'items-d.csv'

stuff =[]
row_counter = 0

#loop through each for ...
with open(document,'rU',encoding='utf-8') as f:
    reader=csv.reader(f)
    for row in reader:
        m = p.findall(row[3])

        if row[3]=='':
            continue     
    
        if len(m)==0:
            row.append('')
        else:
            row.append(m[0])
        stuff.append(row)
        
with open('items_mod.csv', 'w', newline='') as csvfile:
    stuffwriter = csv.writer(csvfile)
    stuffwriter.writerows(stuff)