from database.csv_manager import CSVManager
from backend.pixela.utils import calculate_bmr, get_activity_multiplier

USER_DB_FILE = "resources/users.csv"


def update_user(username, age, gender, height, weight, activity_level):
    users = CSVManager(USER_DB_FILE).read_data()
    updated = False
    for user in users:
        if user['username'] == username:
            bmr = calculate_bmr(age, weight, height, gender)
            activity_multiplier = get_activity_multiplier(activity_level)
            token = user['token']
            user.update({
                'username': username,
                'token': token,
                'bmr': bmr,
                'activity_multiplier': activity_multiplier,
            })
            updated = True
            break
    if not updated:
        return "User not found."
    CSVManager(USER_DB_FILE).write_data(users)
    return "User details updated successfully."
