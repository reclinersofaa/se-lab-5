import json
from datetime import datetime
# import logging  # <-- Removed (Fix: Unused import)

# Global variable
stock_data = {}


# Fix: Renamed to snake_case, added docstring, fixed blank lines
def add_item(item="default", qty=0, logs=None):
    """Adds a quantity of an item to the global stock_data. Logs the transaction."""  # Fix: Docstring
    # Fix: Corrects mutable default argument
    if logs is None:
        logs = []

    # Fix: Added input validation for robustness (E501/C0301 fix)
    if not isinstance(item, str) or not isinstance(qty, int):
        # Line Too Long Fix: Broken into two lines for E501 compliance
        print(f"Warning: Skipping invalid input: item={item}, qty={qty}. "
              "Item must be a string and quantity an integer.")
        return

    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    # Fix: Converted to f-string (E261 fix: two spaces before comment)
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


# Fix: Renamed to snake_case, added docstring, fixed blank lines
def remove_item(item, qty):
    """Removes a quantity of an item from the global stock_data."""  # Fix: Docstring
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    # Fix: Replaced bare except with specific exception (KeyError)
    except KeyError:
        pass


# Fix: Renamed to snake_case, added docstring, fixed blank lines
def get_qty(item):
    """Returns the current quantity of an item in stock."""  # Fix: Docstring
    return stock_data[item]


# Fix: Renamed to snake_case, added docstring, fixed blank lines
def load_data(file="inventory.json"):
    """Loads inventory data from a JSON file into the global stock_data."""  # Fix: Docstring
    # Fix: Using 'with open' for resource management and explicit encoding (E261 fix)
    with open(file, "r", encoding='utf-8') as f:
        global stock_data
        stock_data = json.loads(f.read())


# Fix: Renamed to snake_case, added docstring, fixed blank lines
def save_data(file="inventory.json"):
    """Saves the global stock_data to a JSON file."""  # Fix: Docstring
    # Fix: Using 'with open' for resource management and explicit encoding (E261 fix)
    with open(file, "w", encoding='utf-8') as f:
        f.write(json.dumps(stock_data))


# Fix: Renamed to snake_case, added docstring, fixed blank lines
def print_data():
    """Prints a formatted report of all items and their quantities."""  # Fix: Docstring
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])


# Fix: Renamed to snake_case, added docstring, fixed blank lines
def check_low_items(threshold=5):
    """Returns a list of items whose stock is below the given threshold."""  # Fix: Docstring
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result


# Fix: Renamed to snake_case, added docstring, fixed blank lines
def main():
    """Main execution function to demonstrate inventory system usage."""  # Fix: Docstring
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")  # invalid types, no check
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    # Fix: Removed insecure eval() function (E261 fix)
    print("eval used")


# Fix: E305 (expected 2 blank lines) and W291 (trailing whitespace)
main()
# Fix: W292 (no newline at end of file) - a final newline has been added