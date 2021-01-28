

class Criador():

    def cria_incidente(request):
        json = {}
        data = request.data
        for item in data:
            if data[item] != "":
                json[item] = data[item]
        return json
