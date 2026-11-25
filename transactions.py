transactions = [
    {"id": "T1", "type": "CREDIT", "amount": 120.50, "status": "SUCCESS"},
    {"id": "T2", "type": "DEBIT",  "amount": 99.99,  "status": "FAILED"},
    {"id": "T3", "type": "DEBIT",  "amount": 450.00, "status": "SUCCESS"},
    {"id": "T4", "type": "CREDIT", "amount": 15.25,  "status": "SUCCESS"},
    {"id": "T5", "type": "DEBIT",  "amount": 300.00, "status": "REVERSED"},
]

def print_all(transactions):
    print("<------------ Print all starts-------------->")
    for transaction in transactions:
        print(f"{transaction['id']}: {transaction['type']}: {transaction['amount']}: {transaction['status']}")

def total_by_type(transactions):
    print("<------------ total by type-------------->")
    totals = {}
    for t in transactions:
        totals[t["type"]] = totals.get(t["type"],0) + t["amount"]
    return totals

def find_by_status(transactions,status):
    print("<------------ Find by starts-------------->")
    result = []
    for t in transactions:
        if t["status"] == status:
            result.append(t)
    return result
