from flask import Flask, Response, jsonify, request
from flask_cors import CORS
import join
import os
from math import sqrt

def calcularMatrizHeuris(coordenadas, m):
    listaCoordenadas = list(coordenadas.values())

    for i in range(0, len(listaCoordenadas)):
        m.append([])
        for j in range(0, len(listaCoordenadas)):
            m[i].append(sqrt((listaCoordenadas[i][0] - listaCoordenadas[j][0])**2 + (listaCoordenadas[i][1] - listaCoordenadas[j][1])**2))
    
    return m

def calcularMatrizDist(cods, coordenadas, mr):
    keys = list(cods.keys())

    for i in range(0, len(keys)):
        mr[keys[i]] = []

        if(keys[i] % 10 != 0):
            coord1 = coordenadas.get(keys[i])
            coord2 = coordenadas.get(keys[i - 1])
            mr[keys[i]].append((keys[i - 1], sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)))
        if(i != len(keys) - 1):
            if (keys[i + 1] % 10 != 0):
                coord1 = coordenadas.get(keys[i])
                coord2 = coordenadas.get(keys[i + 1])
                mr[keys[i]].append((keys[i + 1], sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)))

    coord1 = coordenadas.get(13)
    mr[13].append((33, 1.5*sqrt((coord1[0] - coordenadas.get(33)[0])**2 + (coord1[1] - coordenadas.get(33)[1])**2)))
    mr[13].append((43, 1.5*sqrt((coord1[0] - coordenadas.get(43)[0])**2 + (coord1[1] - coordenadas.get(43)[1])**2)))

    mr[24].append((44, 1.5*sqrt((coordenadas.get(24)[0] - coordenadas.get(44)[0])**2 + (coordenadas.get(24)[1] - coordenadas.get(44)[1])**2)))

    coord1 = coordenadas.get(26)
    mr[26].append((34, 1.5*sqrt((coord1[0] - coordenadas.get(34)[0])**2 + (coord1[1] - coordenadas.get(34)[1])**2)))
    mr[26].append((55, 1.5*sqrt((coord1[0] - coordenadas.get(55)[0])**2 + (coord1[1] - coordenadas.get(55)[1])**2)))

    coord1 = coordenadas.get(33)
    mr[33].append((13, 1.5*sqrt((coord1[0] - coordenadas.get(13)[0])**2 + (coord1[1] - coordenadas.get(13)[1])**2)))
    mr[33].append((43, 1.5*sqrt((coord1[0] - coordenadas.get(43)[0])**2 + (coord1[1] - coordenadas.get(43)[1])**2)))

    coord1 = coordenadas.get(34)
    mr[34].append((26, 1.5*sqrt((coord1[0] - coordenadas.get(26)[0])**2 + (coord1[1] - coordenadas.get(26)[1])**2)))
    mr[34].append((55, 1.5*sqrt((coord1[0] - coordenadas.get(55)[0])**2 + (coord1[1] - coordenadas.get(55)[1])**2)))

    coord1 = coordenadas.get(43)
    mr[43].append((13, 1.5*sqrt((coord1[0] - coordenadas.get(13)[0])**2 + (coord1[1] - coordenadas.get(13)[1])**2)))
    mr[43].append((33, 1.5*sqrt((coord1[0] - coordenadas.get(33)[0])**2 + (coord1[1] - coordenadas.get(33)[1])**2)))

    mr[44].append((24, 1.5*sqrt((coordenadas.get(44)[0] - coordenadas.get(24)[0])**2 + (coordenadas.get(44)[1] - coordenadas.get(24)[1])**2)))

    mr[46].append((53, 1.5*sqrt((coordenadas.get(46)[0] - coordenadas.get(53)[0])**2 + (coordenadas.get(46)[1] - coordenadas.get(53)[1])**2)))

    mr[53].append((46, 1.5*sqrt((coordenadas.get(53)[0] - coordenadas.get(46)[0])**2 + (coordenadas.get(53)[1] - coordenadas.get(46)[1])**2)))

    coord1 = coordenadas.get(55)
    mr[55].append((26, 1.5*sqrt((coord1[0] - coordenadas.get(26)[0])**2 + (coord1[1] - coordenadas.get(26)[1])**2)))
    mr[55].append((34, 1.5*sqrt((coord1[0] - coordenadas.get(34)[0])**2 + (coord1[1] - coordenadas.get(34)[1])**2)))

    return mr

    

def adyacentes(cod, mr):
    return mr[cod]


coordenadas = { 10: (34.6046, 58.3993), 11: (34.6044, 58.3923),
                12: (34.6041, 58.3868), 13: (34.6037, 58.3814),
                14: (34.6033, 58.3745), 15: (34.603, 58.37),
                20: (34.6099, 58.4009), 21: (34.6096, 58.3984),
                22: (34.6092, 58.3927), 23: (34.6094, 58.3867),
                24: (34.6091, 58.3825), 25: (34.6088, 58.3786),
                26: (34.6086, 58.3744), 27: (34.6087, 58.3715),
                30: (34.5997, 58.3978), 31: (34.5996, 58.3922),
                32: (34.6018, 58.3844), 33: (34.6045, 58.38), 34: (34.6076, 58.3743),
                40: (34.5912, 58.3752), 41: (34.5955, 58.3774),
                42: (34.6021, 58.3781), 43: (34.6049, 58.3795),
                44: (34.609, 58.3807), 45: (34.6124, 58.3806),
                46: (34.6181, 58.3802), 47: (34.6222, 58.3799), 48: (34.6275, 58.3815),
                50: (34.6231, 58.3971), 51: (34.6227, 58.3914),
                52: (34.6222, 58.3851), 53: (34.6181, 58.3815),
                54: (34.6129, 58.3779), 55: (34.6096, 58.374)}

cods = {10:0, 11:1, 12:2, 13:3, 14:4, 15:5, 20:6, 21:7, 22:8, 23:9, 24:10, 25:11, 26:12, 27:13, 30:14, 31:15, 32:16, 
        33:17, 34:18, 40:19, 41:20, 42:21, 43:22, 44:23, 45:24, 46:25, 47:26, 48:27, 50:28, 51:29, 52:30, 53:31, 54:32, 55:33}
m = []

m = calcularMatrizHeuris(coordenadas, m)

mr = {}

mr = calcularMatrizDist(cods, coordenadas, mr)


def a_Estrella(mDist, orig, dest):
    abiertos = []
    cerrados = []
    abiertos.append((orig, 0, [])) # (codigo, peso acumulado, camino hasta orig)
    predecesor = orig
    encontrado = False
    while(not encontrado):
        if(len(abiertos) == 0):
            print("error")
            return -1
        nodo = abiertos[0] # terminar
        for nd_aux in abiertos:
            if(nd_aux[1] + mDist[cods[orig]][cods[nd_aux[0]]] < nodo[1] + mDist[cods[orig]][cods[nodo[0]]]): 
                nodo = nd_aux

        cerrados.append(nodo)
        abiertos.remove(nodo)
        
        if(nodo[0] == dest):
            nodo[2].append(dest)
            print(nodo[2])
            return nodo[2]
        ady = adyacentes(nodo[0],mr)
        for s in ady:
            esta = False
            for n in abiertos:
                if(s[0] == n[0]):
                    esta = True
                    break
            if (not esta):
                for n in cerrados:
                    if(s[0] == n[0]):
                        esta = True
                        break
            
            if not esta:
                predecesor = nodo
                abiertos.append((s[0], s[1] + predecesor[1], []))
                for c in predecesor[2]:
                    abiertos[len(abiertos)-1][2].append(c)
                abiertos[len(abiertos)-1][2].append(predecesor[0])

app = Flask(__name__)
cors = CORS(app)
@app.route("/api/lechuga", methods=['GET','POST'])
def lechuga():
    ruta = []
    datos = request.json
    datos2 = datos.split(" ")
    paradaIn = int(datos2[0])
    paradaOut = int(datos2[1])
    ruta = a_Estrella(m,paradaIn,paradaOut) #con las cosas inicializada
    print(datos)
    return jsonify(
        {
            "ruta":ruta
        }
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0",debug=False, port=port)

