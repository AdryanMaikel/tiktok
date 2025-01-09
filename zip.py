import os
import zipfile


def encontrar_e_extrair_zip(origem, destino):
    """
    Encontra arquivos .zip em um diretório e os extrai para um destino
    especificado.

    :param origem: Diretório onde os arquivos .zip serão procurados.
    :param destino: Diretório onde os arquivos serão extraídos.
    """
    if not os.path.exists(origem):
        print(f"O diretório de origem '{origem}' não existe.")
        return
    if not os.path.exists(destino):
        os.makedirs(destino)
        print(f"O diretório de destino '{destino}' foi criado.")

    for raiz, _, arquivos in os.walk(origem):
        for arquivo in arquivos:
            if arquivo.endswith(".zip"):
                caminho_zip = os.path.join(raiz, arquivo)
                print(f"Encontrado: {caminho_zip}")

                try:
                    with zipfile.ZipFile(caminho_zip, "r") as zip_ref:
                        zip_ref.extractall(destino)
                        print(f"Extraído: {arquivo} para {destino}")
                    os.remove(caminho_zip)
                except zipfile.BadZipFile:
                    print(f"Erro ao abrir o arquivo .zip: {caminho_zip}")


if __name__ == "__main__":
    origem = r"C:\Users\Adryan\Downloads"
    destino = r"C:\Users\Adryan\Downloads\imagens"
    encontrar_e_extrair_zip(origem, destino)
