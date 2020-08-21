def has_permission(page):
    def inner(user_name):
        if user_name == "Admin":
            return f"{user_name} have page access"
        else:
            return f"Sorry {user_name} no access"
    return inner

check = has_permission("Admin area")
print(check("Adam"))