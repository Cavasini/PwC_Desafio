def extract_address_data(text):
    parts = text.split()
    name = ''
    number = ''
    found_number = False
    for part in parts:
        if not found_number:
            if part[0].isdigit():
                found_number = True
                number += part
            else:
                name += part + ' '
        else:
            number += ' '
            number += part
    
    return [name.strip(), number]

examples = ["Miritiba 339", "Babaçu 500", "Cambuí 804B","Rio Branco 23", "Quirino dos Santos 23 b",]

for example in examples:
    result = extract_address_data(example)
    print(result)