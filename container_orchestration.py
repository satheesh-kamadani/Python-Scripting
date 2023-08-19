# Container orchestration using python script

import docker

client = docker.from_env()

def orchestrate_container():
    container = client.run("nginx", detach=True)
    print(f"Container ID {container.id}")

orchestrate_container()