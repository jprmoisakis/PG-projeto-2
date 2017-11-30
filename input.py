

import numpy


def carrega_atributos_camera(camera_entrada)
    with open(camera_entrada, 'r') as camera_config:
        
        configs = camera_config.readlines()
        
        posicao_camera_format = configs[0].split()
        camera_position = numpy.array([float(posicao_camera_format[0]),float(posicao_camera_format[1]),float(posicao_camera_format[2])])
        
        n_format = configs[1].split()
        camera_n = numpy.array([float(posicao_camera_format[0]),float(posicao_camera_format[1]),float(posicao_camera_format[2])])
        
        v_format = configs[2].split()
        camera_v = numpy.array([float(posicao_camera_format[0]),float(posicao_camera_format[1]),float(posicao_camera_format[2])])
        #carrega d hx hy
        parametros_format = configs[3].split()
        d = float(posicao_camera_format[0])
        hx = float(posicao_camera_format[1])
        hy = float(posicao_camera_format[2])


def carregar_vertices(objeto_entrada):
    with open(objeto_entrada) as objeto_config:
        linhas = objeto_config.readlines()

        pontos_num = int(linhas[0].split(" ")[0])

        for x in range(1, pontos_num + 1):
            pontos_format = linhas[x].splitlines()[0].split()
            pontos.append(numpy.array([float(pontos_format[0]),float(pontos_format[1]),float(pontos_format[2])]))
            pontos_normal.append(numpy.array([0.0, 0.0, 0.0]))

        for x in range(pontos_num + 1, len(linhas)):
            triangulos_format = linhas[x].splitlines()[0].split()
            triangulos.append(numpy.array([int(triangulos_format[0]),int(triangulos_format[1]),int(triangulos_format[2])]))


def carregar_iluminacao(iluminacao_entrada):
    with open(iluminacao_entrada, 'r') as iluminacao_config:
        linhas_iluminacao = iluminacao_config.readlines()
        
        n_factor = float(linhas_iluminacao[-1])

        pl_format = linhas_iluminacao[0].split()
        pl = numpy.array([float(pl_format[0]),float(pl_format[1]),float(pl_format[2])])
        ka = float(linhas_iluminacao[1])

        ia_format = linhas_iluminacao[2].split()
        ia = numpy.array([float(ia_format[0]),float(ia_format[1]),float(ia_format[2])])
        kd = float(linhas_iluminacao[3])

        od_format = linhas_iluminacao[4].split()
        od = numpy.array([float(od_format[0]),float(od_format[1]),float(od_format[2])])
        ks = float(linhas_iluminacao[5])

        il_format = linhas_iluminacao[6].split()
        il = numpy.array([float(il_format[0]),float(il_format[1]),float(il_format[2])])


