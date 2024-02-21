has_good_income = True
has_criminal_record = False
if has_good_income and has_criminal_record:
    print("Eligible for loan")
if has_good_income or has_criminal_record:
    print("Eligible for loan")
if has_good_income and not has_criminal_record:
    print("Eligible for loan")