import json
def set_user(name):
    user = {
        "name" : name,
        "win" : 0,
        "lose" : 0,
        "life" : 5,
        "skill" : "기회추가"
    }
    with open("static/save.txt", "w", encoding='utf-8') as f:
        json.dump(user, f, ensure_ascii= False, indent=4)
   # print("{0}님 숫자를 맞춰보세요. ({1}승{2}패 입니다.)".format(user["name"], user["win"], user["lose"]))
    return user

def save_game(fname, use):
    f = open(fname, "w", encoding="utf-8")
    for key in use:
        print("%s:%s" % (key, use[key]))
        f.write("%s:%s\n" % (key, use[key]))
    f.close() 
