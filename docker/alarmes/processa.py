from alarmes.classificador import Classificador
import json as js

class Processa():

    def cria_incidente(request):
        json = Processa.cria_json(request)
        json['AssignmentGroup'], json['equipe'], json['Hostname'] = Processa.classifica_equipe(json['Description'])
        return json

    def cria_json(request):
        json = {}
        data = request.data
        for item in data:
            if item == "Description":
                for i in item:
                    if i is None:
                        item.remove(i)
                data[item] = '\n'.join(data[item])
            if data[item] is not None:
                json[item] = data[item]
        return json


    def classifica_equipe(descricao):
        equipe , hostname = Classificador.classifica(descricao)

        di =  {(0, 'GSERV-AU'),
                (1, 'DAT-SP'),
                (2, 'DITEC/UOS/GPROM/D3/E31/N1 HIGH-END'),
                (3, 'DITEC/UOS/GPROM/D3/E32/N2 WEB HIGH-END'),
                (4, 'DITEC/UOS/GPROM/D3/E33/N2 SO HIGH-END'),
                (5, 'DITEC/UOS/GPROM/D3/E35/N2 BD HIGH-END'),
                (6, 'GPROM-72')}
        di = dict(di)

        return di[equipe[0]], equipe, hostname
