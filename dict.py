info = {
    "name":"Sreekar",
    "age": 20,
    "city": "Hyderabad",
    "marks" : {
        "Maths": 90,
        "Physics": 85,
        "Chemistry": 88
    }
}
info["age"]=21
print(info)
print(len(info))

print(info["marks"]["Maths"])
print(info["marks"].keys())
print(tuple(info["marks"].keys()))
print((type(info["marks"])))