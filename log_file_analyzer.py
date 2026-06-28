error_count = {}

try:
    file = open("server.log", "r")

    for line in file:

        if "ERROR" in line:

            words = line.split()

            error_code = words[2]

            if error_code in error_count:
                error_count[error_code] += 1
            else:
                error_count[error_code] = 1

    file.close()

    print("\nError Report")
    print("-" * 20)

    for code, count in error_count.items():
        print("Error", code, "occurred", count, "times")

except FileNotFoundError:
    print("Log file not found")
