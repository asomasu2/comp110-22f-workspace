"""Finding out the capabilities of a dictionary."""
# declaring type of the dictionary
from re import S


schools: dict[str, int]

# initializing to an empty dictionary
schools = dict()

# set a key-value pairing
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

print(schools)


print(f"UNC has {schools['UNC']} students")


# remove a key value pair from a dictionary
schools.pop("Duke")

# test for existency of key
duke_in_schools: bool = "Duke" in schools
print(duke_in_schools)

# dictionary literals
schools = {}
print(schools)

schools = {
    "UNC": 100, 
    "Duke": 200, 
    "NCSU": 300
    }
print(schools)
# print(schools["UNCC"])
# Example looping over the keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")
