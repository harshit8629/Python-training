import csv


def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "F"


with open("students.csv", "r") as infile:
    reader = csv.DictReader(infile)

    data = []

    for row in reader:
        marks = int(row["Marks"])
        grade = calculate_grade(marks)

        data.append({
            "Name": row["Name"],
            "Marks": marks,
            "Grade": grade
        })

with open("results.csv", "w", newline="") as outfile:
    fieldnames = ["Name", "Marks", "Grade"]

    writer = csv.DictWriter(
        outfile,
        fieldnames=fieldnames
    )

    writer.writeheader()

    for row in data:
        writer.writerow(row)

print("Results saved to results.csv")
