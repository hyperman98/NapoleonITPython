from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request import RequestPatchUserLoginDto

from db.database import DBSession
from db.exceptions import DBIntegrityException, DBDataException, DBUserDeletedException, DBUserAlreadyExistsException
from db.queries import user as user_queries

from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicDBException, SanicUserDeletedException


class ChangeLoginEndpoint(BaseEndpoint):

    async def method_patch(
            self, request: Request, body: dict, session: DBSession, user_id: int, token: dict, *args, **kwargs
    ) -> BaseHTTPResponse:

        # проверяем, что пользователь посылает запрос от своего имени
        if token.get('id') != user_id:
            return await self.make_response_json(status=403)

        request_model = RequestPatchUserLoginDto(body)

        try:
            user_queries.change_login(session, request_model.login, user_id)
        except DBUserAlreadyExistsException:
            return await self.make_response_json(status=409, message='User already exists')
        except DBUserDeletedException:
            raise SanicUserDeletedException('User deleted')

        try:
            session.commit_session()
        except (DBIntegrityException, DBDataException) as error:
            raise SanicDBException(str(error))

        return await self.make_response_json(status=200)
