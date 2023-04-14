from datetime import datetime

import Adafruit_DHT

#  import MySQLdb

# Configurações do sensor DHT11
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = D17

# Configurações do banco de dados MySQL
DB_HOST = 'localhost'
DB_USER = 'seu_usuario'
DB_PASSWORD = 'sua_senha'
DB_DBNAME = 'nome_do_banco_de_dados'
DB_TABLE = 'nome_da_tabela'


# Função para realizar a leitura do sensor
def ler_sensor():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    return humidity, temperature

'''
# Função para salvar os dados no banco de dados MySQL
def salvar_no_banco(humidity, temperature, medida_realizada):
    conn = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, db=DB_DBNAME)
    cursor = conn.cursor()

    if medida_realizada:
        data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("INSERT INTO {} (humidity, temperature, medida_realizada, data_hora) VALUES ({}, {}, {}, '{}')".format(DB_TABLE, humidity, temperature, 1, data_hora))
    else:
        data_hora = None
        cursor.execute("INSERT INTO {} (humidity, temperature, medida_realizada, data_hora) VALUES ({}, {}, {}, {})".format(DB_TABLE, humidity, temperature, 0, data_hora))

    conn.commit()
    cursor.close()
    conn.close()'''


# Função para realizar a interpolação
def interpolar_dados(dados):
    for i in range(len(dados)):
        if dados[i] is None:
            if i == 0:
                dados[i] = dados[i+1]
            elif i == len(dados)-1:
                dados[i] = dados[i-1]
            else:
                dados[i] = (dados[i-1] + dados[i+1]) / 2
    return dados


# Função principal
def main():
    humidity, temperature = ler_sensor()

    if humidity is not None and temperature is not None:
        print(humidity, temperature,)
        #  salvar_no_banco(humidity, temperature, True)
    else:
        humidity = temperature = None
        salvar_no_banco(humidity, temperature, False)
        print("Falha na leitura do sensor. Realizando interpolação...")

        # Realiza a interpolação
        # Supomos que os dados do sensor são obtidos em intervalos de 5 minutos
        intervalos = 6
        dados_humidity = [humidity] * intervalos
        dados_temperature = [temperature] * intervalos

        dados_humidity = interpolar_dados(dados_humidity)
        dados_temperature = interpolar_dados(dados_temperature)
        '''
        for i in range(intervalos):
            salvar_no_banco(dados_humidity[i], dados_temperature[i], True)
    print("Leitura do sensor concluída e dados salvos no banco de dados.")'''


if __name__ == '__main__':
    main()
