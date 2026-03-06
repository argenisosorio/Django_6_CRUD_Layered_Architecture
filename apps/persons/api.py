from ninja import NinjaAPI

api = NinjaAPI()

@api.get("/hello")
def hello_world(request):
    return {"message": "¡Hola mundo desde Django Ninja!"}
