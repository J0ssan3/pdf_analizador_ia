from utils.leitura_pdf import extrair_texto_pdf
from utils.resumo import gerar_resumo

def main():
    caminho_pdf = input("Informe o caminho do arquivo PDF: ")

    try:
        texto = extrair_texto_pdf(caminho_pdf)
        print("\nTexto extraído com sucesso!")
        
        resumo = gerar_resumo(texto)
        print("\nResumo gerado com sucesso:\n")
        print(resumo)

        salvar = input("\nDeseja salvar o resumo em um arquivo? (s/n): ").lower()
        if salvar == 's':
            with open("resumo.txt", "w", encoding="utf-8") as f:
                f.write(resumo)
            print("Resumo salvo como resumo.txt")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
