import csv



# Read from Chrome Passwords.csv
with open("Chrome Passwords.csv", "r") as file:
    reader = csv.reader(file)
    seen = set()
    duplicates = []

    for row in reader:
        row_tuple = tuple(row)  # Convert row to tuple
        if row_tuple in seen:  # Check if tuple is already seen
            duplicates.append(row_tuple)  # Add to duplicates list
        else:
            seen.add(row_tuple)  # Add to seen set

    print(f"Chrome Duplicates: {duplicates}\n")
    print(f"Total Chrome duplicates: {len(duplicates)}")
    print(f"Total Chrome entries: {len(seen)}")

# Read from Firefox Passwords.csv
with open("firefox_passwords.csv", "r") as file:
    reader = csv.reader(file)
    seen_firefox = set()
    duplicates_firefox = []

    for row in reader:
        row_tuple = tuple(row)  # Convert row to tuple
        if row_tuple in seen_firefox:  # Check if tuple is already seen
            duplicates_firefox.append(row_tuple)  # Add to duplicates list
        else:
            seen_firefox.add(row_tuple)  # Add to seen set

    print(f"Firefox Duplicates: {duplicates_firefox}\n")
    print(f"Total Firefox duplicates: {len(duplicates_firefox)}")
    print(f"Total Firefox entries: {len(seen_firefox)}")

    # Merge Chrome and Firefox password entries and remove duplicates
    merged_set = seen.union(seen_firefox)
    with open("merged_passwords.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for entry in merged_set:
            writer.writerow(entry)
    print(f"Total merged entries: {len(merged_set)}")

with open("merged_passwords.csv", "r") as file:
    reader = csv.reader(file)
    seen_merged = set()
    duplicates_merged = []
    for row in reader:
        row_tuple = tuple(row)
        if row_tuple in seen_merged:
            duplicates_merged.append(row_tuple)
        else:
            seen_merged.add(row_tuple)
    print(f"Merged Duplicates: {duplicates_merged}\n")
    print(f"Total merged duplicates: {len(duplicates_merged)}")
    print(f"Total merged entries: {len(seen_merged)}")
