import pytest

from transport.sanic.endpoints.users.get_all import AllUsersEndpoint


@pytest.mark.asyncio
# do not forget to set to proper test name: test_....
async def tst_all_user_endpoint(request_factory, patched_context, mocker):
    patched_query = mocker.patch('db.queries.user.get_users')
    patched_query.return_value = []

    request = request_factory(method='GET')
    endpoint = AllUsersEndpoint(None, patched_context, '', ())

    response = await endpoint(request, token={'id': 1})

    assert response.status == 200
