# Controle de TV básico
class TV:
    def __init__(self, marca, tamanho):
        self.marca = marca
        self.tamanho = tamanho
        self.ligada = False
        self.volume = 50
        self.canal = 1
        self.mutado = False    
        
    def ligar_desligar(self):
        self.ligada = not self.ligada
        estado = "ligada" if self.ligada else "desligada"
        print(f"A TV está {estado}.")

    def controlar_volume(self, aumentar=True):
        if self.ligada:
            if aumentar:
                self.volume = min(100, self.volume + 1)
                print("Volume aumentado para", self.volume)
            else:
                self.volume = max(0, self.volume - 1)
                print("Volume diminuído para", self.volume)
        else:
            print("A TV está desligada.")
            
    def alterar_canal(self, direcao):
        if self.ligada:
            if direcao == "para_cima":
                self.canal += 1
            elif direcao == "para_baixo":
                self.canal -= 1
            print("Canal alterado para", self.canal)
        else:
            print("A TV está desligada.")
    
    def mutar_tv(self):
        if self.ligada:
            self.mutado = not self.mutado
            if self.mutado:
                print("TV mutada.")
            else:
                print("Volume restaurado.")
        else:
            print("A TV está desligada.")

# Exemplo de uso
minha_TV = TV(marca="Samsung", tamanho=32)

minha_TV.ligar_desligar()
minha_TV.controlar_volume(aumentar=True)
minha_TV.controlar_volume(aumentar=False)
minha_TV.alterar_canal(direcao="para_cima")
minha_TV.alterar_canal(direcao="para_baixo")
minha_TV.mutar_tv()
