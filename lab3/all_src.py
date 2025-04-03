import os, glob, subprocess


start_dir = os.getcwd()
project_root = os.path.abspath(os.path.join(os.getcwd(), '..'))
print("Лабораторная работа №3")

for script in glob.glob("*/src/*.py", recursive=True):
    script_path = os.path.abspath(script)
    script_dir = os.path.dirname(script_path)

    print("-" * 25)
    subprocess.run(
        ["python", script_path],
        env={**os.environ, "PYTHONPATH": project_root},
        cwd=script_dir
    )
    print("-" * 25)

os.chdir(start_dir)
