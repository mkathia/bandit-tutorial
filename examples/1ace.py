# Dangerous dynamic execution of code snippets (arbitrary code execution)
def run_user_script():
    script = input("Enter your Python script: ")
    print("Running script...")
    exec(script)

run_user_script()
