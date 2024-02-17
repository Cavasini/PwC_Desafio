def extract_address_data(text):
    parts = text.split()
    name = parts[0]
    number = parts[1]
    return [name, number]

examples = ["Miritiba 339", "Babaçu 500", "Cambuí 804B"]

for example in examples:
    result = extract_address_data(example)
    print(result)
