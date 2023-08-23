import pandas as pd
from datetime import date

gsheetid = "1wCOGd7sitAIfKp1G1Shf0NdYM-P7AVt2ZZVRmaE_unE"
sheet_name = "Data"

gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)

df = pd.read_csv(gsheet_url)

current_date = date.today().strftime("%d/%m")

birthdays = df[df["date"] == current_date]
name_of_birthday_people = birthdays["name"]
name_of_birthday_people = name_of_birthday_people.to_string(index=False)

print(name_of_birthday_people)
