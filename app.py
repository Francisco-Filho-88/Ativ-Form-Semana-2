class Elevador:
    def __init__(self, andar_atual=1, total_andares=6):
        self.andar_atual = andar_atual
        self.total_andares = total_andares

    def subir(self):
        if self.andar_atual < self.total_andares:
            self.andar_atual += 1
        return self.andar_atual

    def descer(self):
        if self.andar_atual > 1:
            self.andar_atual -= 1
        return self.andar_atual

    def ir_para(self, andar):
        if 1 <= andar <= self.total_andares:
            self.andar_atual = andar
        return self.andar_atual


if __name__ == "__main__":
    elevador = Elevador()
    print(f"Andar inicial: {elevador.andar_atual}")
    
    elevador.subir()
    print(f"Andar após subir: {elevador.andar_atual}")
    
    elevador.ir_para(5)
    print(f"Andar atual: {elevador.andar_atual}")
