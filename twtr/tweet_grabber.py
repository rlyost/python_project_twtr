import twitter

class TwitterDataSheet(object):
    # api = twitter.Api(
    #     consumer_key='ceDtKbZWwrPWKh6iCFUlxCUEq',
    #     consumer_secret='7btaaEI97fQef8D71hJu5qwgE1x3LUoGG1RMn5CcAU9XEZct1H',
    #     access_token_key='908045257484283904-JpG0pAber9n0qp1hLRpiYSqIT93VOUm',
    #     access_token_secret='HsEplzeY7jSvAmn4gLj42ijkSnqFIhm6dWimGZIcB9rvj',
    # )
    api = twitter.Api(
            consumer_key='XfyGfnpUqCv90OrBOxDX6g4Ga',
            consumer_secret='DidKa9XdOOwvHjOqZwWFJdf1Z2ciRgmGuFyux1Tr1mhgDwG2rs',
            access_token_key='305659119-GMkDSXwlGCnP2j3gT9BMMJcfUCoEJZtVqlyMSmvn',
            access_token_secret='WHO2Fs9LdrZERaMrx2c4c9J2ieXALsYlrx8vFkl5ZdRdg',
        )

    def __init__(self, screen_name):
        self.user = self.api.GetUser(screen_name=screen_name)
        # self.user in an object containing the following attributes:
        # 'param_defaults', 'contributors_enabled', 'created_at',
        # 'default_profile', 'default_profile_image', 'description',
        # 'email', 'favourites_count', 'followers_count', 'following',
        # 'friends_count', 'geo_enabled', 'id', 'id_str', 'lang',
        # 'listed_count', 'location', 'name', 'notifications',
        # 'profile_background_color', 'profile_background_image_url',
        # 'profile_background_image_url_https', 'profile_background_tile',
        # 'profile_banner_url', 'profile_image_url', 'profile_image_url_https',
        # 'profile_link_color', 'profile_sidebar_border_color',
        # 'profile_sidebar_fill_color', 'profile_text_color',
        # 'profile_use_background_image', 'protected', 'screen_name',
        # 'status', 'statuses_count', 'time_zone', 'url', 'utc_offset',
        # 'verified', 'withheld_in_countries', 'withheld_scope', '_json']

        self.friends = self.api.GetFriends(screen_name=screen_name)
        # This is a list of Twitter User objects
        # Each Friend in self.friends has the same attributes as above

        self.friend_locations = self.find_friend_locations()

    # Basic User Info Attributes:
    # - name: Rick L Yost
    # - notifications: False
    # - screen_name: ryost_esq
    # - statuses_count 366
    # - time_zone: Eastern Time (US & Canada)
    # - url: https://t.co/PabZ7AGIr3
    # - location: San Francisco Bay Area, CA
    # - listed_count: 22
    # - friends_count: 673 
    # - following: False
    # - followers_count: 418
    # - favourites_count: 435
    # - email: None
    # - description: South Dakotan, JD/MBA PMP #veteran #airborne #ranger #Entrepreneur @vetlistus @adjutantadmn @sheepdogbook @RangerAssoc
    # - created_at: Thu May 26 15:50:21 +0000 2011
    
    def find_friend_locations(self):
        '''Returns a list of a user's friends locations with the duplicates
        removed
        '''
        return set(
            [friend.location for friend in self.friends if friend.location]
        )
