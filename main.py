import os
import yaml
from jinja2 import Environment, FileSystemLoader

files = [
    'contre_arguments',
    'evenements',
    'courants',
    'notions',
    'personnalites'
]

def define_env(env):
    @env.macro
    def get_data():
        data = {}
        for file in files:
            with open(f'contenu/{file}.yml', encoding='utf-8') as f:
                raw = yaml.safe_load(f)
                # Replace all -> in fields where needed
                for item in raw['data']:
                    for key in item:
                        if isinstance(item[key], str):
                            item[key] = item[key].replace('->', ':octicons-arrow-right-24:')
                data[file] = raw
        return data

# Génération des individuelles de contre-arguments

# data = yaml.safe_load(open("contenu/contre_arguments.yml"))
# env = Environment(loader=FileSystemLoader("templates"))
# template = env.get_template("contre_arguments_template.md.j2")

# for item in data["data"]:
#     content = template.render(item=item)
#     path = f"docs/contre_arguments/{item['id']}.md"
#     os.makedirs(os.path.dirname(path), exist_ok=True)
#     with open(path, "w") as f:
#         f.write(content)