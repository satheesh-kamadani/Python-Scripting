# Run the containers using python script

import os
import subprocess

def docker_deployment():
    subprocess.run("docker run -d nginx", shell=True)

docker_deployment()