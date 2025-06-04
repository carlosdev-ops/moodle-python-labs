import pandas as pd
import pymysql

db_config = {
    'host': '10.0.0.230',
    'user': 'moodle_dev',
    'password': 'MotDePasseDev@123',
    'database': 'moodle_dev',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

query = """
SELECT id, username, firstname, lastname, email
FROM mdl_user
WHERE deleted = 0 AND suspended = 0 AND id > 2
ORDER BY id ASC
LIMIT 5;
"""

try:
    print("🔌 Connexion à la base Moodle...")
    conn = pymysql.connect(**db_config)
    with conn.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()

    print("🧾 Résultats bruts :")
    for row in results:
        print(row)

    # Conversion en DataFrame
    df = pd.DataFrame(results)
    print("✅ DataFrame prêt.")
    print(df.head())

    df.to_excel("utilisateurs_moodle.xlsx", index=False)
    print("📁 Fichier Excel exporté.")

except Exception as e:
    print("❌ Erreur :", e)
