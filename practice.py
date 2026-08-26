import csv

with open("people.csv", "w", newline = "")as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "email", "City"])
    writer.writerow(["Sweety", "sweety@gmail.com", "New York"])
    writer.writerow(["pinky", "pinky@gmail.com", "orlando"])

print("CSV created!")