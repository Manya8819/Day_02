student_dict = {
    101: "Alice",
    102: "Bob",
    103: "Charlie"
}

def search_name(roll_number):
    return student_dict.get(roll_number, "Student not found.")

# Example search
roll_number_to_search = 102
print("\nSearch Result:")
print(f"Name for Roll Number {roll_number_to_search}: {search_name(roll_number_to_search)}")
