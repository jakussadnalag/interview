import re


def validate_isbn(isbn):
    length = len(isbn)
    checksum = 0
    for i in range(length):
        if not isbn[i].isdigit():
            if i == length - 1:
                return isbn[i] == "X"
            return False
        checksum += int(isbn[i]) * (i + 1)
    return (length == 10 and checksum % 11 == 0) or (length == 13 and checksum % 10 == 0)


def validate_csv_file():
    with open("tNmieVFn.txt", mode="r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            if not line:
                continue

            columns = line.split(";")
            if len(columns) != 4:
                print(f"Error! {len(columns)} column(s) on line {line_number}!")
                continue

            title, author, isbn, price = columns

            if not title:
                print(f"Missing title on line {line_number}.")

            if not author:
                print(f"Missing author on line {line_number}.")

            if not isbn or not validate_isbn(str(isbn)):
                print(f"Invalid ISBN on line {line_number}.")

            price_pattern = r"[0-9]+[,.][0-9]{1,2}[ ]*[€|Kč]"
            if not price or not re.match(price_pattern, price):
                print(f"Invalid price on line {line_number}.")


# Test the function
validate_csv_file()
