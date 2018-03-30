import csv
import datetime
import os
import re
import time

from geopy.geocoders import Nominatim
import twitter


class TwitterDataSheet(object):
    # Zach's Account
    api = twitter.Api(
        consumer_key='ceDtKbZWwrPWKh6iCFUlxCUEq',
        consumer_secret='7btaaEI97fQef8D71hJu5qwgE1x3LUoGG1RMn5CcAU9XEZct1H',
        access_token_key='908045257484283904-JpG0pAber9n0qp1hLRpiYSqIT93VOUm',
        access_token_secret='HsEplzeY7jSvAmn4gLj42ijkSnqFIhm6dWimGZIcB9rvj',
    )
# Rick's Account
# api = twitter.Api(
#         consumer_key='XfyGfnpUqCv90OrBOxDX6g4Ga',
#         consumer_secret='DidKa9XdOOwvHjOqZwWFJdf1Z2ciRgmGuFyux1Tr1mhgDwG2rs',
#         access_token_key='305659119-GMkDSXwlGCnP2j3gT9BMMJcfUCoEJZtVqlyMSmvn',
#         access_token_secret='WHO2Fs9LdrZERaMrx2c4c9J2ieXALsYlrx8vFkl5ZdRdg',
#     )

    def __init__(self, screen_name):
        self.user = self.api.GetUser(screen_name=screen_name)
        self.user.coordinates = self.find_user_coordinates()
        self.user.created_at = self.generate_date_time()
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
    
    def find_user_coordinates(self):
        '''Returns the coordinates of the location field on a user's profile'''
        loc_regex = re.compile(r'[\w\d\s-]+,? [\w\s\d]*')
        location_str = self.user.location
        if re.search(loc_regex, location_str):
            try:
                geolocator = Nominatim()
                location = geolocator.geocode(location_str)
            except AttributeError:
                return None
            except Exception as e:
                print(e)
                time.sleep(2)
                location = geolocator.geocode(location_str)
            try:
                coordinates = (location.latitude, location.longitude)
                print((location.latitude, location.longitude))
            except Exception as e:
                print(e)
            else:
                return coordinates
        return None

    def generate_date_time(self):
        '''Converts Twitter api provided created_at attribute into the
        proper format for Drango ORM DateTimeFields
        '''
        temp = self.user.created_at.split(' ')
        temp2 = temp[0]+" "+temp[1]+" "+temp[2]+" "+temp[3]+" "+temp[5]
        dt = datetime.datetime.strptime(temp2, "%a %b %d %H:%M:%S %Y")
        return dt.strftime('%Y-%m-%d %H:%M:%S')


api = twitter.Api(
        consumer_key='ceDtKbZWwrPWKh6iCFUlxCUEq',
        consumer_secret='7btaaEI97fQef8D71hJu5qwgE1x3LUoGG1RMn5CcAU9XEZct1H',
        access_token_key='908045257484283904-JpG0pAber9n0qp1hLRpiYSqIT93VOUm',
        access_token_secret='HsEplzeY7jSvAmn4gLj42ijkSnqFIhm6dWimGZIcB9rvj',
    )


def build_csv(screen_name):
    fieldnames = ['class', "latitude", "longitude"]
    root = os.getcwd()
    csv_path = "{}/twtr/static/csv/{}.csv".format(root, screen_name)
    with open(csv_path, 'a') as csv_file:
        row_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        friends = api.GetFriends(screen_name=screen_name)
        row_writer.writeheader()
        for friend in friends:
            friend.latitude = None
            friend.longitude = None
            try:
                print(friend.location)
            except Exception as e:
                print(e)
            else:
                friend = find_user_coordinates(friend)
                if type(friend) != 'NoneType':
                    try:
                        row_writer.writerow({
                            'class': "no_time_zone",
                            'latitude': friend.latitude,
                            'longitude': friend.longitude,
                        })
                    except AttributeError:
                        pass
                else:
                    try:
                        row_writer.writerow({
                            'class': friend.time_zone,
                            'latitude': friend.latitude,
                            'longitude': friend.longitude,
                        })
                    except AttributeError as e:
                        pass


def find_user_coordinates(friend):
    '''Returns the coordinates of the location field on a user's profile'''
    loc_regex = re.compile(r'[\w\d\s-]+,? [\w\s\d]*')
    location_str = friend.location
    if re.search(loc_regex, location_str):
        try:
            geolocator = Nominatim()
            location = geolocator.geocode(location_str)
        except AttributeError:
            return None
        except Exception as e:
            print(e)
            time.sleep(5)
            location = geolocator.geocode(location_str)
        try:
            friend.latitude = location.latitude
            friend.longitude = location.longitude
            print(location.latitude, location.longitude)
        except Exception as e:
            print(e)
        else:
            return friend
    return None
