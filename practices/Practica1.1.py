#vaidar si una contraseña es segura
import re

def valida_contra(contra):
    if 8<= len(contra) <= 16: 
        if re.search('[a-z]', contra) and re.search('[A-Z]', contra):
            if re.search('[0-9]', contra):
                if re.search('[$#@]', contra):
                    return True
                return False
            
clave = input('Escriba la contraseña: ')
print (valida_contra(clave))
