
# in dictionaries the key is unique
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions["Nov"])
print(monthConversions.get("Dec", "Not a valid key"))
print(monthConversions.get("Som", "Not a valid key"))
