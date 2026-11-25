def print_summary():
    amounts = [120.50, 99.99, 450.00, 15.25, 300.00]

    total = sum(amounts)
    largest = max(amounts)
    length = len(amounts)
    average = total/length
    big_amounts = [i for i in amounts if i%2==0]

    print(f"Total: {total}")
    print(f"Largest: {largest}")
    print(f"Average: {average:.2f}")
    print(f"Over 100: {big_amounts}")

import transactions as tx
def main():
    tx.print_all(tx.transactions)
    print(tx.total_by_type(tx.transactions))
    print(tx.find_by_status(tx.transactions,"SUCCESS"))


if __name__ == "__main__":
    # print_summary()
    main()
