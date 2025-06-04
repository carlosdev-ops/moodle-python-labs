# 📊 moodle-python-labs

Scripts Python pour extraire, analyser et automatiser des données à partir d’une base Moodle.

## 📦 Objectif

Ce dépôt regroupe des laboratoires progressifs en Python pour :
- Automatiser des rapports Moodle
- Générer des exports Excel
- Construire des dashboards interactifs
- Modifier ou enrichir la base en environnement de développement

---

## 🔬 Laboratoires disponibles

| Labo         | Description                                      |
|--------------|--------------------------------------------------|
| `labo1`      | Connexion et extraction des utilisateurs Moodle |
| `labo2`      | Rapport des inscriptions par cours              |
| `labo3`      | Mise à jour contrôlée d'utilisateurs            |
| `labo4`      | Dashboard interactif avec Streamlit             |
| `labo5`      | Script déclenché par webhook Moodle             |

---

## ▶️ Démarrage rapide

```bash
git clone https://github.com/<ton_user>/moodle-python-labs.git
cd moodle-python-labs/moodle_labo1
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python extract_users.py
