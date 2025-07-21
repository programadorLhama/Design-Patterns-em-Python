
async def request_adapter(request, user):
    body = None
    try:
        body = request.json
    except Exception:
        body = {}

    headers = dict(request.headers)
    query_params = request.args
    path_params = { 'user': user }

    return {
        "header": headers,
        "body": body,
        "query_params": query_params,
        "path_params": path_params,
    }
