#%%
import pandas as pd
import os

path_geral = os.path.normpath('C:/Users/Administrador/OneDrive - echope/Documentos/demanda/Vendas/nova_venda')
pastas = ['Fevereiro', 'Março', 'Abril', 'Maio',
          'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro']


for pasta in os.listdir(path_geral):
    novo_path = f'{path_geral}/{pasta}'
    
    if os.path.isdir(novo_path):
        
        for arquivo in os.listdir(novo_path):
            
            if arquivo.endswith('.xlsx'):
                
                file_path = os.path.join(novo_path, arquivo)
                df = pd.read_excel(file_path)
                nome_salvar = arquivo.split('.')
                df.to_csv(f'{novo_path}/{nome_salvar[0]}.csv', encoding='utf-8')
        
