
def update_config_file(key, value):
    config_file = "/home/skamadan/Devops_Projects/Python-Scripting/app_config.conf"
    key_found = False
    with open(config_file, "r") as f:
        lines = f.readlines()
    with open(config_file, "w") as f:
        for line in lines:
            if key in line:
                line = f"{key} = {value}\n"
                key_found = True
            f.write(line)
        if key_found:
            print("updated the config file")
        else:
            print("key is not present in the config file")

update_config_file("debug_mode", "True")

