import csv
import mysql.connector



conn = mysql.connector.connect(
    host = '153.92.215.93',
    user = 'frnimoaq_mintic',
    password = 'unal@2021',
    port = '3306',
    database = 'frnimoaq_nomina'
)

cursor = conn.cursor()



grangrupo_inserted = []
gg_id:str
gg_codigo:str
gg_nombre:str

subgrupo_principal_inserted = []
sp_id:str
sp_codigo:str
sp_nombre:str
sp_grangrupo:str

subgrupo_inserted = []
s_id:str
s_codigo:str
s_nombre:str
s_subgrupoprincipal:str

grupoprimario_inserted = []
gp_id:str
gp_codigo:str
gp_nombre:str
gp_subgrupo:str

cargo_inserted = []
c_id:str
c_codigo:str
c_nombre:str
c_grupoprimario:str



reader = csv.reader(open('CIUOv2.csv', encoding = 'utf-8'), delimiter = ';')
for row in reader:
    if row[1] not in grangrupo_inserted:
        gg_id = '1' + row[0]
        gg_codigo = row[0]
        gg_nombre = row[1]
        query1 = '''insert into gran_grupo values(%s, %s, %s)'''
        grangrupo_inserted.append(row[1])
        cursor.execute(query1, (gg_id, gg_codigo, gg_nombre))
        conn.commit()
    if row[3] not in subgrupo_principal_inserted:
        sp_id = '1' + row[2]
        sp_codigo = row[2]
        sp_nombre = row[3]
        sp_grangrupo = gg_id
        query2 = '''insert into subgrupo_principal values(%s, %s, %s, %s)'''
        subgrupo_principal_inserted.append(row[3])
        cursor.execute(query2, (sp_id, sp_codigo, sp_nombre, sp_grangrupo))
        conn.commit()
    if row[5] not in subgrupo_inserted:
        s_id = '1' + row[4]
        s_codigo = row[4]
        s_nombre = row[5]
        s_subgrupoprincipal = sp_id
        query3 = '''insert into subgrupo values(%s, %s, %s, %s)'''
        subgrupo_inserted.append(row[5])
        cursor.execute(query3, (s_id, s_codigo, s_nombre, s_subgrupoprincipal))
        conn.commit()
    if row[7] not in grupoprimario_inserted:
        gp_id = '1' + row[6]
        gp_codigo = row[6]
        gp_nombre = row[7]
        gp_subgrupo = s_id
        query4 = '''insert into grupo_primario values(%s, %s, %s, %s)'''
        grupoprimario_inserted.append(row[7])
        cursor.execute(query4, (gp_id, gp_codigo, gp_nombre, gp_subgrupo))
        conn.commit()
    if row[9] not in cargo_inserted:
        c_id = '1' + row[8]
        c_codigo = row[8]
        c_nombre = row[9]
        c_grupoprimario = gp_id
        query5 = '''insert into cargo values(%s, %s, %s, %s)'''
        cargo_inserted.append(row[9])
        cursor.execute(query5, (c_id, c_codigo, c_nombre, c_grupoprimario))
        conn.commit()

conn.close()