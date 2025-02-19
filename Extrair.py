import pandas as pd
import json

def carregar_dados(caminho_arquivo):
    
    try:
        df = pd.read_csv(caminho_arquivo, sep=';', encoding='latin1', low_memory=False)
        return df
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
        return None

def filtrar_dados_paraiba(df):
   
    return df[df['CO_UF'] == 25]

def selecionar_colunas(df):
    
    colunas = ['NO_ENTIDADE','NO_REGIAO', 'CO_UF', 'NO_MUNICIPIO', 'NO_MESORREGIAO', 'NO_MICRORREGIAO', 
    'QT_MAT_BAS','QT_MAT_INF','QT_MAT_FUND','QT_MAT_FUND_AF','QT_MAT_MED','QT_MAT_PROF','QT_MAT_EJA',
    'QT_MAT_ESP']
    return df[colunas]

def salvar_json(dados, censo):
    
    with open(censo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
    print(f"Arquivo JSON salvo como {censo}")

def main():
    caminho_csv = "/escolas.csv"  
    df = carregar_dados(caminho_csv)

    if df is not None:
        df_pb = filtrar_dados_paraiba(df)
        df_pb_selecionado = selecionar_colunas(df_pb)

        lista_instituicoes = df_pb_selecionado.to_dict(orient='records')
        salvar_json(lista_instituicoes, "instituicoes_paraiba.json")

if __name__ == "__main__":
    main()
