def str_to_int_from_env(raw_string):
    int_result=[]
    for part in raw_string.split(","):
        int_result.append(int(part.strip()))
    return int_result

def check_in_admins(user_id, admins):
    if user_id not in admins:
        return False
    else:
        return True