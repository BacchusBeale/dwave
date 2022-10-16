import yaml

def getToken():
    apitoken=""
    with open('./data/settings.yml', 'r') as file:
        data = yaml.safe_load(file)
        apitoken = data["apitoken"]