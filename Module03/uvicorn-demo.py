async def app(scope, receive, send):
    assert scope["type"] == "http"

    # sending back an object
    await send(
        {
            "type": "http.response.start",
            "status": 200,
            "headers": [[b"content-type", b"application/json"]],
        }
    )

    await send({"type": "http.response.body", "body": b'{message:"Hello, world!"}'})
