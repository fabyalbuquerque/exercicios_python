from pathlib import Path

subpastas = ["subpasta 1/pasta X", "subpasta 2/pasta Y", "subpasta 3/pasta Z"]
pastas_abc = ['pasta a', 'pasta b', 'pasta c']

def cria_estrutura_pastas(diretorio):
    pasta_principal = Path(diretorio)
    pasta_principal.mkdir(parents=True, exist_ok=True)
    
    for subpasta in subpastas:
            caminho_subpasta = pasta_principal /subpasta
            if not caminho_subpasta.exists():
                caminho_subpasta.mkdir(parents=True, exist_ok=True)
                for pasta_abc in pastas_abc:
                    caminho_pasta_abc = caminho_subpasta / pasta_abc
                    caminho_pasta_abc.mkdir(parents=True, exist_ok=True)
                    print(f"Criado {caminho_pasta_abc}")
                
                                      
diretorio = 'pasta_principal' 
     
cria_estrutura_pastas(diretorio) 
          
pastas = Path(diretorio).glob("**/")

for pasta in pastas:
    if pasta.name == "pasta b":
        pasta_h = pasta.parent / "pasta_h"
        pasta.rename(pasta_h)
        print(f"{pasta.name} foi renomeada para pasta_h")     
    
    

        
    
    
