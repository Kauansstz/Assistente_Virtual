from distutils.core import setup
import py2exe

setup(
    name="Nome do seu projeto",
    version="1.0",
    description="""
      Descrição
    """,
    author="Kauan dos Santos de Souza",
    console=["diretório do seu projeto"],
    options={
        "py2exe": {
            "packages": ["os", "sys"],  # Pacotes adicionais a serem incluídos
            "includes": [
                "as importações do seu projeto vem aqui, sem 'From' e 'impor', somente o nome da importação"
            ],
            "excludes": ["Tkinter"],  # Módulos a serem excluídos
        }
    },
    data_files=[("images", ["logo.png"])],  # Arquivos adicionais a serem incluídos
)
