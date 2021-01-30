import psycopg2

class Aviso():

    def __init__(self):
        self.con = psycopg2.connect(host='db', database='rdis', user='postgres', password='postgres')


    def close_connection(self):
        self.con.close()

    def consulta_incidentes(self):

        cur = self.con.cursor()
        cur.execute('select * from incidente')
        recset = cur.fetchall()
        for rec in recset:
            print (rec)

    def busca_hostname_aberto(self, hostname):

        cur = self.con.cursor()
        sql = "select count(*) from incidente where hostname = '" + hostname + "' and status = 'Aberto'"
        cur.execute(sql)
        recset = cur.fetchall()
        return recset[0][0]
