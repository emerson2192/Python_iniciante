nome  = str(input("Digite o nome completo: ")).strip()
print('Analisando seu nome...')
print(f'seu nome em maiúscula é {nome.upper()}')
print(f'Seu nome em minúscula é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome.replace(" ", ""))} letras')
primeiro_nome = nome.split()[0]
numero_letras_primeiro_nome = len(primeiro_nome)
print(f'Seu primeiro nome tem {numero_letras_primeiro_nome} letras')
