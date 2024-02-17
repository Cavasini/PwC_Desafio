def extract_address_data(text):
    parts = text.split()
    name = ''
    number = ''
    found_number = False
    address_types = ["no", "apt", "suite"] 
    
    parts = [part.replace(',', '') for part in parts]

    for i, part in enumerate(parts):
        if part.lower() not in address_types:
            if parts[0][0].isdigit():
                if part[0].isdigit():
                    number += part
                else:
                    name += part + ' '
            else:
                if not found_number:
                    if part[0].isdigit():
                        found_number = True
                        number += part
                    else:
                        name += part + ' '
                else:
                    number += ' '
                    number += part
        else:
            name = name + number
            number = ' '.join(parts[i:])
            break
    
    return [name.strip(), number]

examples = [
    "Miritiba 339", 
    "Babaçu 500", 
    "Cambuí 804B",
    "Rio Branco 23", 
    "Quirino dos Santos 23 b",
    "4, Rue de la République", 
    "100 Broadway Av", 
    "Calle Sagasta, 26", 
    "Calle 44 No 1991", 
    "221B Baker Street",
    
]

for example in examples:
    result = extract_address_data(example)
    print(result)