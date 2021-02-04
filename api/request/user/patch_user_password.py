# изменение пароля

import re

from marshmallow import Schema, fields, post_load

from api.base import RequestDto
from api.exceptions import ApiRequestValidationException


class RequestPatchUserPasswordDtoSchema(Schema):
    password = fields.Str(required=True, allow_none=False)

    # проверяем длину пароля на валидность
    @post_load
    def check_password_length(self, data: dict, **kwargs):
        if 'password' in data:
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


class RequestPatchUserPasswordDto(RequestDto, RequestPatchUserPasswordDtoSchema):
    __schema__ = RequestPatchUserPasswordDtoSchema
