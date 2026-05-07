"""
Generates insert_data.sql from the created CSV files.
"""
import csv
import os

DATASET_DIR = r"c:\Users\Admin\Desktop\New folder (2)\dataset"
OUTPUT = r"c:\Users\Admin\Desktop\New folder (2)\schema\insert_data.sql"

def read_csv(filename):
    path = os.path.join(DATASET_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        headers = next(reader)
        rows = list(reader)
    return headers, rows

def sql_val(val, is_string=True):
    if val == "" or val is None:
        return "NULL"
    if is_string:
        return "'" + val.replace("'", "''") + "'"
    return val

# Column type mappings (True = string/date, False = numeric)
TABLE_CONFIGS = [
    ("customers", "customers.csv",
     [False, True, True, True, True, True, True, True]),
    ("products", "products.csv",
     [False, True, True, False, False]),
    ("employees", "employees.csv",
     [False, True, True, True, True]),
    ("orders", "orders.csv",
     [False, False, False, True, True]),
    ("order_items", "order_items.csv",
     [False, False, False, False, False, False]),
    ("payments", "payments.csv",
     [False, False, True, False, True]),
]

with open(OUTPUT, "w", encoding="utf-8") as out:
    out.write("-- ============================================\n")
    out.write("-- RetailPulse — Data Insertion Script\n")
    out.write("-- Auto-generated from CSV dataset files\n")
    out.write("-- Compatible: MySQL | MS SQL Server\n")
    out.write("-- ============================================\n\n")

    for i, (table_name, csv_file, col_types) in enumerate(TABLE_CONFIGS):
        headers, rows = read_csv(csv_file)
        out.write(f"-- ────────────────────────────────────────────\n")
        out.write(f"-- INSERT INTO {table_name} ({len(rows)} rows)\n")
        out.write(f"-- ────────────────────────────────────────────\n")

        for row in rows:
            values = []
            for val, is_str in zip(row, col_types):
                values.append(sql_val(val, is_str))
            cols = ", ".join(headers)
            vals = ", ".join(values)
            out.write(f"INSERT INTO {table_name} ({cols}) VALUES ({vals});\n")

        # Add a newline only if it's not the last table
        if i < len(TABLE_CONFIGS) - 1:
            out.write("\n")
print(f"✅ insert_data.sql generated at: {OUTPUT}")
