import yaml

# Fonction pour ajouter les sous-pages à une catégorie
def add_subpages(yaml_path, base_path, parent_title):
    with open(yaml_path, "r", encoding="utf-8") as f:
        contenu = yaml.safe_load(f)
    items = []
    for item in contenu['data']:
        if parent_title == "Contre-arguments":
            title = item['argument']
            link = f"{base_path}/{item['id']}.md"
        elif parent_title == "Évènements historiques majeurs peu connus":
            title = item['titre'].replace(":", "-")
            link = item['lien']
        else:
            title = item.get('nom', 'No title')
            link = item.get('lien', '#')
        items.append({title: link})
    return items

# Générer la structure nav
def generate_nav():
    nav = [
        {"C'est quoi ce wiki ?": "index.md"},
        {
            "Contre-arguments": [
                {"Contre-arguments": "contre_arguments.md"},
            ]
        },
        {
            "Évènements historiques majeurs peu connus": [
                {"Évènements historiques majeurs peu connus": "evenements.md"},
            ]
        },
        {
            "Personnalités majeures peu connues": [
                {"Personnalités majeures peu connues": "personnalites.md"},
            ]
        },
        {
            "Courants de pensée": [
                {"Courants de pensée": "courants.md"},
            ]
        },
        {
            "Notions et vocabulaire": [
                {"Notions et vocabulaire": "notions.md"},
            ]
        },
    ]

    nav[1]["Contre-arguments"].extend(add_subpages("contenu/contre_arguments.yml", "contre_arguments", "Contre-arguments"))
    nav[2]["Évènements historiques majeurs peu connus"].extend(add_subpages("contenu/evenements.yml", "evenements", "Évènements historiques majeurs peu connus"))
    nav[3]["Personnalités majeures peu connues"].extend(add_subpages("contenu/personnalites.yml", "personnalites", "Personnalités majeures peu connues"))
    nav[4]["Courants de pensée"].extend(add_subpages("contenu/courants.yml", "courants", "Courants de pensée"))
    nav[5]["Notions et vocabulaire"].extend(add_subpages("contenu/notions.yml", "notions", "Notions et vocabulaire"))

    with open('nav.yml', "w", encoding="utf-8") as f:
        f.write("nav:\n")
        yaml.dump(nav, f, allow_unicode=True, sort_keys=False, indent=2)

if __name__ == "__main__":
    generate_nav()
