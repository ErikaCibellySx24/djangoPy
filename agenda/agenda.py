class Agenda:
    def __init__(self):
        self.contatos = {}

    def mostrar_nomes(self):
        if self.contatos:
            print("\n===== Nomes Agendados =====")
            for nome in self.contatos.keys():
                print(nome)
        else:
            print("Nenhum nome agendado.")  

    def listar_contatos(self):
        print("\n===== Lista de Contatos =====")
        for nome, numero in self.contatos.items():
            print(f"Nome: {nome}, Número: {numero}")

    def procurar_contato(self, nome):
        if nome in self.contatos:
            print(f"Nome: {nome}, Número: {self.contatos[nome]}")
        else:
            print(f"Contato {nome} não encontrado.")

    def adicionar_contato(self, nome, numero):
        self.contatos[nome] = numero
        print(f"Contato {nome} adicionado!")

    def editar_contato(self, nome, novo_numero):
        if nome in self.contatos:
            self.contatos[nome] = novo_numero
            print(f"Número do contato {nome} atualizado!")
        else:
            print(f"Contato {nome} não encontrado.")

    def excluir_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            print(f"Contato {nome} excluído!")
        else:
            print(f"Contato {nome} não encontrado.")

    ## Menu
    def menu_editar_excluir(self):
        while True:
            print("\n===== Menu Editar/Excluir =====")
            print("1. Editar contato")
            print("2. Excluir contato")
            print("3. Voltar ao menu principal")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                nome = input("Digite o nome do contato que deseja editar: ")
                if not isinstance(nome, str):
                    print("Por favor, insira um nome válido.")
                while True:
                    nome = input("Digite o nome do contato que deseja editar: ")
                    if isinstance(nome, str):
                        # Se o nome for uma string, podemos continuar
                        break
                    else:
                        print("Por favor, insira um nome válido.")

                novo_numero = input("Digite o novo número do contato: ")

                self.editar_contato(nome, novo_numero)
            elif opcao == '2':
                nome = input("Digite o nome do contato que deseja excluir: ")
                self.excluir_contato(nome)
            elif opcao == '3':
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

    def menu_mostrar_nomes(self):
        self.mostrar_nomes()  # Chama a função mostrar_nomes dentro do menu

