import re

from marshmallow import Schema, fields, post_load

from api.base import RequestDto
from api.exceptions import ApiRequestValidationException


class RequestCreateUserDtoSchema(Schema):
    login = fields.Str(required=True, allow_none=False)
    password = fields.Str(required=True, allow_none=False)
    first_name = fields.Str(required=True, allow_none=False)
    last_name = fields.Str(required=True, allow_none=False)

    # проверяем длину пароля на валидность
    @post_load
    def check_login_password_length(self, data: dict, **kwargs):
        if len(data['login']) < 5:
            raise ApiRequestValidationException('Bad request')

        if len(data['password']) < 6:
            raise ApiRequestValidationException('Bad request')

        return data

    @post_load
    def check_password_strength(self, data: dict, **kwargs):
        reg = re.compile('^(?=\S{6,20}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])')
        result = re.search(reg, data['password'])
        if not result:
            raise ApiRequestValidationException('Bad request')

        return data


# можно добавить также второго родителя, чтобы IDE знал
# какие в нашей схеме существуют поля
class RequestCreateUserDto(RequestDto, RequestCreateUserDtoSchema):
    __schema__ = RequestCreateUserDtoSchema
