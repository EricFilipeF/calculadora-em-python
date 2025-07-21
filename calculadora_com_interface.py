import tkinter as tk


def inputDisplay(event):
    expressao_atual.set(expressao_atual.get() + str(event))

def backspaceDisplay():
    input = expressao_atual.get()
    expressao_atual.set(input[:-1])

def clearDisplay():
    expressao_atual.set("")

def calcularDisplay():
    try:
        expressao_atual.set(eval(expressao_atual.get()))
    except:
        expressao_atual.set("Erro")

    
def main():
    # Janela principal
    janela = tk.Tk()
    janela.iconbitmap("img/calculator_icon-icons.ico")
    janela.title("Calculadora")
    janela.geometry("350x436")
    janela.config(bg="#1C1C1C")

    # ----------------------------Frame do display----------------------------
    frame_display = tk.Frame(janela, background="#202020", width=350, height=80)
    frame_display.pack()
    
    global expressao_atual
    expressao_atual = tk.StringVar()
    expressao_atual.set("")

    # Label do display
    global display
    display = tk.Label(frame_display, textvariable=expressao_atual, background="#1C1C1C", font=("Arial", 24), fg="#ffffff", justify="right", anchor="e", bd="4", relief="sunken")
    display.place(relwidth=1, relheight=1)

    # ----------------------------Frame dos botões----------------------------
    frame_botoes = tk.Frame(janela, background="#202020", width=350, height=356)
    frame_botoes.pack()

    # botões da linha 1
    btn_clear = tk.Button(frame_botoes, text="C", width=16, height=2, font=("Arial", 12, "bold"), command=clearDisplay, bg="#323232", fg="#ffffff", activebackground="#ADADAD", activeforeground="#ffffff")
    btn_clear.place(x=2, y=4)
    
    btn_porcentagem = tk.Button(frame_botoes, text="%", width=7, height=2, font=("Arial", 12, "bold"), command=lambda: inputDisplay("%"), bg="#323232", fg="#ffffff", activebackground="#ADADAD", activeforeground="#ffffff")
    btn_porcentagem.place(x=180, y=4)
    
    btn_backspace = tk.Button(frame_botoes, text="⌫", width=7, height=2, font=("Arial", 12, "bold"), command=backspaceDisplay, bg="#323232", fg="#ffffff", activebackground="#ADADAD", activeforeground="#ffffff")
    btn_backspace.place(x=269, y=4)

    # botões da linha 2
    btn_reciproco = tk.Button(frame_botoes, text="1/x", width=7, height=2, font=("Arial", 12, "bold"), command=lambda: inputDisplay("1/"), bg="#3c3c3c", fg="#ffffff", activebackground="#ADADAD", activeforeground="#ffffff")
    btn_reciproco.place(x=2, y=63)

    btn_sqrt = tk.Button(frame_botoes, text="x²", width=7, height=2, font=("Arial", 12, "bold"), command=lambda: inputDisplay("**2"), bg="#3c3c3c", fg="#ffffff", activebackground="#ADADAD", activeforeground="#ffffff")
    btn_sqrt.place(x=91, y=63)

    btn_raiz_quadrada = tk.Button(frame_botoes, text="√x", width=7, height=2, font=("Arial", 12, "bold"), command=lambda: inputDisplay("**0.5"), bg="#3c3c3c", fg="#ffffff", activebackground="#ADADAD", activeforeground="#ffffff")
    btn_raiz_quadrada.place(x=180, y=63)

    btn_divisao = tk.Button(frame_botoes, text="÷", width=7, height=2, font=("Arial", 12, "bold"), command=lambda: inputDisplay("/"), bg="#323232", fg="#ffffff", activebackground="#ADADAD", activeforeground="#ffffff")
    btn_divisao.place(x=269, y=63)

    # botões da linha 3
    btn_n_7 = tk.Button(frame_botoes, text="7", width=7, height=2, font=("Arial", 12, "bold"), command=lambda: inputDisplay("7"), bg="#3c3c3c", fg="#ffffff", activebackground="#ADADAD", activeforeground="#ffffff")
    btn_n_7.place(x=1, y=122)
    
    btn_n_8 = tk.Button(frame_botoes, text="8", width=7, height=2, font=("Arial", 12, "bold"), command=lambda: inputDisplay("8"), bg="#3c3c3c", fg="#ffffff", activebackground="#ADADAD", activeforeground="#ffffff")
    btn_n_8.place(x=91, y=122)
    
    btn_n_9 = tk.Button(frame_botoes, text="9", width=7, height=2, font=("Arial", 12, "bold"), command=lambda: inputDisplay("9"), bg="#3c3c3c", fg="#ffffff", activebackground="#ADADAD", activeforeground="#ffffff")
    btn_n_9.place(x=180, y=122)
    
    btn_multiplicao = tk.Button(frame_botoes, text="x", width=7, height=2, font=("Arial", 12, "bold"), command=lambda: inputDisplay("*"), bg="#323232", fg="#ffffff", activebackground="#ADADAD", activeforeground="#ffffff")
    btn_multiplicao.place(x=269, y=122)
    
    # botões da linha 4
    btn_n_4 = tk.Button(frame_botoes, text="4", width=7, height=2, font=("Arial", 12, "bold"), command=lambda: inputDisplay("4"), bg="#3c3c3c", fg="#ffffff", activebackground="#ADADAD", activeforeground="#ffffff")
    btn_n_4.place(x=2, y=181)
    
    btn_n_5 = tk.Button(frame_botoes, text="5", width=7, height=2, font=("Arial", 12, "bold"), command=lambda: inputDisplay("5"), bg="#3c3c3c", fg="#ffffff", activebackground="#ADADAD", activeforeground="#ffffff")
    btn_n_5.place(x=91, y=181)
    
    btn_n_6 = tk.Button(frame_botoes, text="6", width=7, height=2, font=("Arial", 12, "bold"), command=lambda: inputDisplay("6"), bg="#3c3c3c", fg="#ffffff", activebackground="#ADADAD", activeforeground="#ffffff")
    btn_n_6.place(x=180, y=181)

    btn_subtracao = tk.Button(frame_botoes, text="-", width=7, height=2, font=("Arial", 12, "bold"), command=lambda: inputDisplay("-"),  bg="#323232", fg="#ffffff", activebackground="#ADADAD", activeforeground="#ffffff")
    btn_subtracao.place(x=269, y=181)
    
    # botões da linha 5
    btn_n_1 = tk.Button(frame_botoes, text="1", width=7, height=2, font=("Arial", 12, "bold"), command=lambda: inputDisplay("1"), bg="#3c3c3c", fg="#ffffff", activebackground="#ADADAD", activeforeground="#ffffff")
    btn_n_1.place(x=2, y=240)
    
    btn_n_2 = tk.Button(frame_botoes, text="2", width=7, height=2, font=("Arial", 12, "bold"), command=lambda: inputDisplay("2"), bg="#3c3c3c", fg="#ffffff", activebackground="#ADADAD", activeforeground="#ffffff")
    btn_n_2.place(x=91, y=240)
    
    btn_n_3 = tk.Button(frame_botoes, text="3", width=7, height=2, font=("Arial", 12, "bold"), command=lambda: inputDisplay("3"), bg="#3c3c3c", fg="#ffffff", activebackground="#ADADAD", activeforeground="#ffffff")
    btn_n_3.place(x=180, y=240)
    
    btn_adicao = tk.Button(frame_botoes, text="+", width=7, height=2, font=("Arial", 12, "bold"), command=lambda: inputDisplay("+"), bg="#323232", fg="#ffffff", activebackground="#ADADAD", activeforeground="#ffffff")
    btn_adicao.place(x=269, y=240)

    # botões da linha 6
    btn_n_0 = tk.Button(frame_botoes, text="0", width=16, height=2, font=("Arial", 12, "bold"), command=lambda: inputDisplay("0"), bg="#3c3c3c", fg="#ffffff", activebackground="#ADADAD", activeforeground="#ffffff")
    btn_n_0.place(x=2, y=299)
    
    btn_ponto = tk.Button(frame_botoes, text=".", width=7, height=2, font=("Arial", 12, "bold"), command=lambda: inputDisplay("."), bg="#3c3c3c", fg="#ffffff", activebackground="#ADADAD", activeforeground="#ffffff")
    btn_ponto.place(x=180, y=299)

    btn_igual = tk.Button(frame_botoes, text="=", width=7, height=2, font=("Arial", 12, "bold"), command=calcularDisplay, bg="#4cc2ff", fg="#3F3F3F", activebackground="#4cc2ff", activeforeground="#3F3F3F")
    btn_igual.place(x=269, y=299)


    # Mantem a janela aberta
    janela.mainloop()

if __name__ == "__main__":
    main()