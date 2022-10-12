import mysql.connector


ident = input('Syötä lentokentän ICAO-koodi: ')
yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='1807',
    autocommit=True
    )

def haeICAO(ident):
    sql = "SELECT ident, name FROM airport "
    sql += "WHERE ident='" + ident + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f'Hakemasi lentokentän nimi on: {rivi[1]}')
    return



haeICAO(ident)