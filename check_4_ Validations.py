import re


with open("input.txt", "r") as infile, \
     open("valid.txt", "w") as validfile, \
     open("invalid.txt", "w") as invalidfile:

    for line in infile:
        line = line.strip()

        
        if not line:
            continue

        
        parts = line.split(",")
        if len(parts) != 4:
            invalidfile.write(line + "\n")
            continue

        name, student_id, email, dob = [part.strip() for part in parts]

        
        name_valid = re.match(r'^[A-Z][a-z]+\s[A-Z][a-z]+$', name)

        
        id_valid = re.match(r'^(FA|SP)\d{2}-(CS|BCS|PH|SE|SW|CE)-\d{3}$', student_id, re.IGNORECASE)

        
        email_valid = re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)

        
        dob_valid = re.match(r'^\d{2}-\d{2}-\d{4}$', dob)

        
        if name_valid and id_valid and email_valid and dob_valid:
            validfile.write(line + "\n")
        else:
            invalidfile.write(line + "\n")


