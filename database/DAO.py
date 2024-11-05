from database.DB_connect import DBConnect
from model.country import Country
from model.confine import Confine

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllCountries():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * FROM country c order by c.StateNme """
            #query = """SELECT co.StateAbb, co.CCode, co.StateNme
             #   from contiguity c, country co
              #  where c.`year` <= %s
              #  and c.state1no = co.CCode
             #   group by c.state1no ORDER BY StateAbb"""
            cursor.execute(query)
            for row in cursor:
                result.append(Country(**row))
            cursor.close()
            cnx.close()
            return result


    @staticmethod
    def getConfini(anno):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select c.state1no as cnt1, c.state2no as cnt2 from contiguity c
                        where c.year <= %s and c.conttype = 1"""
            cursor.execute(query, (anno,))
            for row in cursor:
                result.append(Confine(**row))
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def getCountryConf(anno):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select co.StateAbb, co.CCode, co.StateNme from contiguity c, country co
                                where c.year <= %s and c.conttype = 1 and c.state1no = co.CCode
                                group by co.CCode order by co.StateNme"""
            cursor.execute(query, (anno,))
            for row in cursor:
                result.append(Country(**row))
            cursor.close()
            cnx.close()
            return result

