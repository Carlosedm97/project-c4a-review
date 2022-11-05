from pymongo import MongoClient
import json
import certifi

ca = certifi.where() 

def loadConfigFile(): #Cargar el archivo de configuración.
    with open('database/config.json') as f:
        data = json.load(f)
    return data

def dbConnection(): #Función de conexión
    dataConfig = loadConfigFile()
    try:
        client = MongoClient(dataConfig['MONGO_URI_SERVER'], tlsCAFile = ca) # Conexión con atlas
        # client = MongoClient(dataConfig['MONGO_URI_LOCAL'], dataConfig['LOCAL_PORT']) # Conexión local
        db = client["project_c4a_review"]
    except ConnectionError:
        print("Error de conexión con la base de datos.")
    return db