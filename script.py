import os
import fileinput
import sys

def replace_in_file(file_path, old_word, new_word):
    with fileinput.FileInput(file_path, inplace=True) as file:
        for line in file:
            # Replace capitalized plural
            line = line.replace(old_word.capitalize(), new_word.capitalize())
            # Replace lowercase plural
            line = line.replace(old_word.lower(), new_word.lower())
            # Replace uppercase plural
            line = line.replace(old_word.upper(), new_word.upper())
            # Replace capitalized singular
            line = line.replace(old_word[:-1].capitalize(), new_word[:-1].capitalize())
            # Replace lowercase singular
            line = line.replace(old_word[:-1].lower(), new_word[:-1].lower())
            # Replace uppercase singular
            line = line.replace(old_word[:-1].upper(), new_word[:-1].upper())
            print(line, end='')

def rename_file(old_name, new_name):
    os.rename(old_name, new_name)

def main():
    current_dir = os.getcwd()
    files = [file for file in os.listdir(current_dir) if file.endswith('.java') and file != os.path.basename(sys.argv[0])]

    if not files:
        print("Nenhum arquivo Java encontrado na pasta atual.")
        return

    print(f"Encontrados os seguintes arquivos Java para processamento:")
    for file_name in files:
        print(f"- {file_name}")

    proceed = input(f"Deseja prosseguir com a edição desses arquivos? (s/n): ")
    if proceed.lower() != 's':
        return

    old_plural = input("Digite o nome antigo no plural: ")
    new_plural = input("Digite o novo nome no plural: ")
    old_singular = input("Digite o nome antigo no singular: ")
    new_singular = input("Digite o novo nome no singular: ")

    for file_name in files:
        file_path = os.path.join(current_dir, file_name)
        replace_in_file(file_path, old_plural, new_plural)
        replace_in_file(file_path, old_singular, new_singular)
        new_file_name = file_name.replace(old_plural, new_plural).replace(old_singular, new_singular)
        rename_file(file_path, os.path.join(current_dir, new_file_name))

    print("Processo concluído!")

if __name__ == "__main__":
    main()
