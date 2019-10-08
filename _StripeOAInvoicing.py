def solve(queries):
    records = {} # id and value
    for query in queries:
        query = query.lower()
        keyword, params = query.split(": ")
        print(keyword, params, "keyword", "param")
        # all is string
        ident, record, currency = parseParams(params)
        # print(ident, record, currency)
        if (keyword != "pay" and currency != "usd"):
            continue
        if (keyword == "create"):
            if (int(ident) in records):
                continue
            records[int(ident)] = (int(record), 0)
            # print(query, "create")
        elif(keyword == "finalize"):
            if (int(ident) not in records):
                continue
            if (records[int(ident)][1] != 0):
                continue
            records[int(ident)] = (int(record), 1)
            # print(query, "create")
        elif(keyword == "pay"):
            if (int(ident) not in records):
                continue
            if (records[int(ident)][1] != 1):
                continue
            records[int(ident)] = (0, 2)
            # print(query, "pay")
    print(records, "in")
    res = 0
    for (idx, (value, state)) in records.items():
        res += value
    return res

def parseParams(s):
    params = s.split("&")
    record = {}
    for param in params:
        print(param)
        key, value = param.split("=")
        record[key] = value
    # all return value is in string
    return (record.get("id", None), record.get("amount", None), record.get("currency", None))

queries = [
    "CREATE: id=14&amount=800&currency=USD", 
    "FINALIZE: id=14&amount=800&currency=USD", 
    "PAY: id=14"
    ]

hardQueries = ['CREATE: id=1&amount=5000&currency=USD',
    'FINALIZE: id=1&amount=5000&currency=USD',
    'PAY: id=1',
    'CREATE: id=2&amount=2500&currency=USD',
    'FINALIZE: id=2&amount=0&currency=USD',
    'FINALIZE: id=3&amount=3000&currency=USD',
    'CREATE: id=3&amount=3000&currency=USD',
    'FINALIZE: id=4&amount=3500&currency=USD',
    'CREATE: id=5&amount=70000&currency=USD',
    'PAY: id=5',
    'CREATE: id=6&amount=19000&currency=CAD',
    'PAY: id=4',
    'CREATE: id=7&amount=6000&currency=USD',
    'FINALIZE: id=7&amount=6500&currency=USD',
    'CREATE: id=8&amount=3000&currency=USD',
    'FINALIZE: id=8&amount=2500&currency=USD',
    'PAY: id=8',
    'PAY: id=1',]

print(solve(hardQueries))
# print("123")