from alarmes.classificador import Classificador

class Criador():

    def cria_json(request):
        json = {}
        data = request.data
        for item in data:
            if item == "Description":
                data[item] = '\n'.join(data[item])
            if data[item] != "":
                json[item] = data[item]
        return json

    def cria_incidente(request):
        json = Criador.cria_json(request)
        json['AssignmentGroup'], json['equipe'] = Criador.classifica_equipe(json['Description'])
        return json

    def classifica_equipe(descricao):
        equipe = Classificador.classifica(descricao)

        di =  {(0, 'GSERV-AU'),
                (1, 'DAT-SP'),
                (2, 'DITEC/UOS/GPROM/D3/E31/N1 HIGH-END'),
                (3, 'DITEC/UOS/GPROM/D3/E32/N2 WEB HIGH-END'),
                (4, 'DITEC/UOS/GPROM/D3/E33/N2 SO HIGH-END'),
                (5, 'DITEC/UOS/GPROM/D3/E35/N2 BD HIGH-END'),
                (6, 'GPROM-72')}
        di = dict(di)

        return di[equipe[0]], equipe
