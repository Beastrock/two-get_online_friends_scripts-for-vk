## two ways of writing get_friends_online_list function
There are two ways of getting online friends by VK API:  

- The first way is to call `get.friends.getOnline()` for getting **online friends IDs** and then pass it to `get.users()` method which gives us info from user ID.
    
        def get_friends_online_list(login, password):
        session = vk.AuthSession(
            app_id=APP_ID,
            user_login=login,
            user_password=password,
            scope="friends"
        )
        api = vk.API(session)
        online_friends_ids = api.friends.getOnline(order="hints") # here is the difference
        return api.users.get(user_ids=online_friends_ids)     


- Second way is call only one API method `get.users` with `fields="online"` which gets **all you friends IDs**.    

        def get_all_friends_info(login, password):
        session = vk.AuthSession(
            app_id=APP_ID
            user_login=login,
            user_password=password,
        )
        api = vk.API(session)
        return api.friends.get(fields="online", order="name")  #here is the difference
    
    
        def get_online_friends_list(all_friends_info):
            return [friend for friend in all_friends_info if friend["online"] == 1]
        
Comparing with first way, second allows *to order friends list by name* with `order="name"` parameter, which is more convenient for me than  `"random"` and `"hints"` type of order in first way method.  However, *it has additional online-checking function* and *longer code length*. Also, as it is written in vk.API documentation *it works slower* and comparing by help of "TimeIt" then the other order types. According to analyzing, it was choosen to write it in a first way.
