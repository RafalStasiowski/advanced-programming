import jwt
import datetime

def get_time():
    return jwt.encode({'time_encode': datetime.datetime.now().__str__()}, 'secret', algorithm='HS256')