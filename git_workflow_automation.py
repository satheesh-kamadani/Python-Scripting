import subprocess

def git_workflow_automation():
    subprocess.run("git add .", shell=True)
    subprocess.run('git commit -m "Automated Commit"', shell=True)
    subprocess.run("git push origin main", shell=True)

git_workflow_automation()