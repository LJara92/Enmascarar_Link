import re
import subprocess
import time

# Validador de URL
def url_checker(url):
    if not re.match(r'^https?://', url):
        print("URL inválida. Por favor, use http o https")
        return False
    return True


def main():
    # Solicitud de URL a enmascarar
    while True:
        phish = input("Pegue la URL de phishing aquí (con http o https): ")
        if url_checker(phish):
            break
    print("La URL es válida:", phish)
    time.sleep(1)


    print("Procesando y modificando la URL de phishing\n")

    # Acorta la URL utilizando el servicio is.gd y captura la URL corta resultante
    short = subprocess.check_output(["curl", "-s", f"https://is.gd/create.php?format=simple&url={phish}"], text=True)
    shorter = short.strip().split("https://")[1]
    print("### Enmascarando el dominio ###")

    # Solicitud de URL como se va a ver
    while True:
        mask = input("Dominio para enmascarar la URL de phishing (con http o https), ej: https://google.com, http://www.youtube.com) : ")
        if url_checker(mask):
            break
    print("\nLa URL es válida:", phish)

    # Texto de ing social
    print('\nEscriba palabras de ingeniería social: (como bitcoin-gratis, gtav-tricks)')
    print("No use espacios, solo use '-' entre las palabras de ingeniería social")
    words = input("=> ")

    # Generando el link, sin y con palabras
    if not words:
        print("No hay palabras.")
        print("\nGenerando enlace enmascarado...\n")
        final = f"{mask}@{shorter}"
        print(f"Aquí está el enlace enmascarado: \033[32m{final}\033[0m\n")
        exit()
    if " " in words:
        print("[!] Palabras inválidas. Por favor, evite los espacios.")
        print("\nGenerando enlace enmascarado...\n")
        final = f"{mask}@{shorter}"
        print(f"Aquí está el enlace enmascarado: \033[32m{final}\033[0m\n")
        exit()
    print("\nGenerando enlace enmascarado...\n")
    final = f"{mask}-{words}@{shorter}"
    print(f"Aquí está el enlace enmascarado: \033[32m{final}\033[0m\n")


if __name__ == "__main__":
    main()
