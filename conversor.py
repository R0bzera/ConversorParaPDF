import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def selecionar_fotos():
    arquivos = filedialog.askopenfilenames(
        title="Selecione as fotos",
        filetypes=[("Imagens", "*.jpg *.jpeg *.png *.bmp *.tiff")]
    )
    if arquivos:
        lista_fotos.set('\n'.join(arquivos))

def converter_para_pdf():
    fotos = lista_fotos.get().split('\n')
    if not fotos or fotos == ['']:
        messagebox.showerror("Erro", "Nenhuma foto selecionada!")
        return
    
    try:
        imagens = []
        for foto in fotos:
            img = Image.open(foto).convert("RGB")
            imagens.append(img)
        
        arquivo_pdf = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF", "*.pdf")],
            title="Salvar como"
        )
        if arquivo_pdf:
            imagens[0].save(arquivo_pdf, save_all=True, append_images=imagens[1:])
            messagebox.showinfo("Sucesso", f"PDF salvo com sucesso em:\n{arquivo_pdf}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao converter as fotos: {str(e)}")

janela = tk.Tk()
janela.title("Conversor de Foto para PDF")
janela.geometry("400x300")

lista_fotos = tk.StringVar()

frame = tk.Frame(janela, padx=10, pady=10)
frame.pack(fill="both", expand=True)

btn_selecionar = tk.Button(frame, text="Selecionar Fotos", command=selecionar_fotos, width=20)
btn_selecionar.pack(pady=5)

lbl_fotos = tk.Label(frame, text="Fotos Selecionadas:")
lbl_fotos.pack(anchor="w")

txt_fotos = tk.Label(frame, textvariable=lista_fotos, bg="white", relief="sunken", anchor="nw", justify="left")
txt_fotos.pack(fill="both", expand=True, pady=5)

btn_converter = tk.Button(frame, text="Converter para PDF", command=converter_para_pdf, width=20)
btn_converter.pack(pady=5)

janela.mainloop()