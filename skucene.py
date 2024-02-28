import os
import re
import tkinter as tk
from tkinter import filedialog

def extrair_mapname(nome_arquivo):
    padrao = r"^(.*?)_"  # Expressão regular para extrair o texto antes do primeiro '_'
    correspondencia = re.match(padrao, nome_arquivo)
    if correspondencia:
        return correspondencia.group(1)
    else:
        return None

def ler_mapnames_de_ipk(caminho_pasta):
    mapnames = []
    for nome_arquivo in os.listdir(caminho_pasta):
        if nome_arquivo.endswith('.ipk'):
            mapname = extrair_mapname(nome_arquivo)
            if mapname:
                mapnames.append(mapname)
    return mapnames

def gerar_arquivo_skuscene_maps_pc_all(mapnames):
    with open("skuscene_maps_pc_all.isc.ckd", "w") as file:
        file.write('<?xml version="1.0" encoding="ISO-8859-1"?>\n')
        file.write('<root>\n')
        file.write('\t<Scene ENGINE_VERSION="253653" GRIDUNIT="0.500000" DEPTH_SEPARATOR="0" NEAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" FAR_SEPARATOR="1.000000 0.000000 0.000000 0.000000, 0.000000 1.000000 0.000000 0.000000, 0.000000 0.000000 1.000000 0.000000, 0.000000 0.000000 0.000000 1.000000" viewFamily="0">\n')

        for mapname in mapnames:
            file.write('\t\t<ACTORS NAME="Actor">\n')
            file.write('\t\t\t<Actor RELATIVEZ="0.000000" SCALE="1.000000 1.000000" xFLIPPED="0" USERFRIENDLY="{}" MARKER="" POS2D="0.000000 0.000000" ANGLE="0.000000" INSTANCEDATAFILE="" LUA="world/maps/{}/songdesc.tpl">\n'.format(mapname, mapname))
            file.write('\t\t\t\t<COMPONENTS NAME="JD_SongDescComponent">\n')
            file.write('\t\t\t\t\t<JD_SongDescComponent />\n')
            file.write('\t\t\t\t</COMPONENTS>\n')
            file.write('\t\t\t</Actor>\n')
            file.write('\t\t</ACTORS>\n')
        
        file.write('\t\t<sceneConfigs>\n')
        file.write('\t\t\t<SceneConfigs activeSceneConfig="0">\n')
        file.write('\t\t\t\t<sceneConfigs NAME="JD_SongDatabaseSceneConfig">\n')
        file.write('\t\t\t\t\t<JD_SongDatabaseSceneConfig name="" SKU="jd2017-pc-ww" Territory="NCSA" RatingUI="world/ui/screens/bootsequence/rating">\n')
        file.write('\t\t\t\t\t\t<ENUM NAME="Pause_Level" SEL="6" />\n')
        
        for mapname in mapnames:
            file.write('\t\t\t\t\t\t<CoverflowSkuSongs>\n')
            file.write('\t\t\t\t\t\t\t<CoverflowSong name="{}" cover_path="world/maps/{}/menuart/actors/{}_cover_generic.act" />\n'.format(mapname, mapname, mapname))
            file.write('\t\t\t\t\t\t</CoverflowSkuSongs>\n')
            file.write('\t\t\t\t\t\t<CoverflowSkuSongs>\n')
            file.write('\t\t\t\t\t\t\t<CoverflowSong name="{}" cover_path="world/maps/{}/menuart/actors/{}_cover_online.act" />\n'.format(mapname, mapname, mapname))
            file.write('\t\t\t\t\t\t</CoverflowSkuSongs>\n')

            print("Adicionando o mapa:", mapname)
        
        file.write('\t\t\t\t\t</JD_SongDatabaseSceneConfig>\n')
        file.write('\t\t\t\t</sceneConfigs>\n')
        file.write('\t\t\t</SceneConfigs>\n')
        file.write('\t\t</sceneConfigs>\n')
        file.write('\t</Scene>\n')
        file.write('</root>\n')

root = tk.Tk()
root.withdraw()  # Ocultar a janela principal

caminho_pasta_ipk = filedialog.askdirectory(title="Selecione a pasta que contém os arquivos IPK")

if caminho_pasta_ipk:
    mapnames = ler_mapnames_de_ipk(caminho_pasta_ipk)
    if mapnames:
        print("Mapnames encontrados nos arquivos IPK:")
        for mapname in mapnames:
            print("Adicionando o mapa:", mapname)
        gerar_arquivo_skuscene_maps_pc_all(mapnames)
        print("Arquivo skuscene_maps_pc_all.isc.ckd gerado com sucesso!")
    else:
        print("Nenhum arquivo IPK encontrado ou o formato do nome do arquivo não corresponde ao esperado.")
else:
    print("Nenhum diretório selecionado.")

print("Thank You For Use My Skucene Tool, Created By SquareJDBR")
