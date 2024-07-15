import mysql.connector

# Connexion à base1
conn_base1 = mysql.connector.connect(
    host='localhost',
    user='root',  
    password='',  
    database='base1'
)
cursor_base1 = conn_base1.cursor()

# Connexion à base2
conn_base2 = mysql.connector.connect(
    host='localhost',
    user='root',  
    password='',  
    database='base2'
)
cursor_base2 = conn_base2.cursor()

# Récupérer les données de base1
cursor_base1.execute("SELECT c2t1 FROM t1")
data_c2t1 = cursor_base1.fetchall()

cursor_base1.execute("SELECT c1t2 FROM t2")
data_c1t2 = cursor_base1.fetchall()

# Insérer les données dans la table cc de base2
insert_query = "INSERT INTO cc (c2t1, c1t2) VALUES (%s, %s)"
for row_c2t1, row_c1t2 in zip(data_c2t1, data_c1t2):
    cursor_base2.execute(insert_query, (row_c2t1[0], row_c1t2[0]))

# Valider les changements
conn_base2.commit()

# Vérifier les données insérées
cursor_base2.execute("SELECT * FROM cc")
rows = cursor_base2.fetchall()

print("Données insérées dans la table cc de base2 :")
for row in rows:
    print(row)

# Fermer les curseurs et les connexions
cursor_base1.close()
conn_base1.close()
cursor_base2.close()
conn_base2.close()

print("Les données ont été transférées avec succès.")
