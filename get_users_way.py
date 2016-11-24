import vk
from getpass import getpass

APP_ID = 5723136  # app_id - unique code of this app


def get_user_login():
    return input("Input login:\n")


def get_user_password():
    return getpass(prompt="Input password:\n")


def get_all_friends_info(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
    )
    api = vk.API(session)
    return api.friends.get(fields="online", order="name")


def get_online_friends_list(all_friends_info):
    return [friend for friend in all_friends_info if friend["online"] == 1]


def output_online_friends_to_console(online_friends_list):
    print("Number of online friends: {}".format(len(online_friends_list)))
    for number, online_friend in enumerate(online_friends_list, 1):
        if online_friend:
            print("{}) {f[first_name]} {f[last_name]}".format(number, f=online_friend))


if __name__ == '__main__':
    all_friends_info = get_all_friends_info(get_user_login(), get_user_password())
    online_friends_list = get_online_friends_list(all_friends_info)
    output_online_friends_to_console(online_friends_list)
