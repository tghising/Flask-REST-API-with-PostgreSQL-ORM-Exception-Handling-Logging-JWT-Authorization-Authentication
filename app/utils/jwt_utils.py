from flask_jwt_extended import create_access_token, decode_token


def generate_access_token(identity, expires=None):
    return create_access_token(identity=identity, expires_delta=expires)


def decode_access_token(token):
    try:
        return decode_token(token)
    except Exception as e:
        return None
