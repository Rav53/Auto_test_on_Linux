def check_output(command, text):
    import subprocess
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        
        if text in output:
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False

# Пример использования
command = "ls"  # Пример команды
text = "file.txt"  # Пример текста

result = check_output(command, text)
print(result)