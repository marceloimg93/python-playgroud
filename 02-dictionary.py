# store key value pair

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    1: "Number 1"
}


print(monthConversions["Jan"])
print(monthConversions.get("Apr"))
print(monthConversions.get("Luv", "Not a valid key"))