import mysql.connector

class Query:

    def __init__:
        # text = input()
        # query = str(text)
        pass

    def search_from_mysql(self, query):

        con = mysql.connector.connect(
            user = 'YOUR_USER_NAME',
            password = 'YOUR_PASSWORD',
            host = 'YOUR_HOST',
            dabase = 'YOUR_DATABASE',
        )

        cursor = con.cursor()

        query = cursor.execute('SELECT * FROM ~~~')
        results = cursor.fetchall()

        if results:
            for results in results:
                print(result[1])
        else:
            print('Not Found')

