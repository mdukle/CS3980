def concatenate(**kwargs):
    result = ""
    user = kwargs["username"]
    print("username =", user)
    for a in kwargs.values():
        if type(a) is str:
            result += a

    return result


print(concatenate(username="Mia", username2="Macy"))
