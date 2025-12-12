import random
import tkinter as tk
from tela import JogoAdivinhacaoGUI
if __name__ == "__main__":
      root = tk.Tk()
      jogo = JogoAdivinhacaoGUI(root)
#             self.label_status.config(text=f"Muito alto! Tentativas: {self.tentativas_restantes}")
      root.mainloop()   
numero_secreto = random.randint(1, 100)

for numero_da_tentativa in range(1, 4):
    print(f"\n--- Tentativa {numero_da_tentativa} de 3")
    numero_adivinha = input("adivinha ia fera: ")

    try: 
        na_int = int(numero_adivinha)
    except ValueError:
        print("Por favor, insira um número válido.")
        continue


    if na_int == numero_secreto:
        print("Parabéns! Você adivinhou o número secreto.")
        break

    elif na_int < numero_secreto:
        print("O número secreto é maior que o seu palpite.")

    elif na_int > numero_secreto:
        print("O número secreto é menor que o seu palpite.")

else:
    print(f"Você não adivinhou o número secreto, o numero era: {numero_secreto}.")

