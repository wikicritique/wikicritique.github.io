import yaml

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
