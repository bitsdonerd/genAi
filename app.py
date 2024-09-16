import pandas as pd 
import streamlit as st
from datetime import time, datetime
from pydantic import ValidationError
import database
from database import salvar_no_postgres
import contrato
from contrato import Vendas

# Estrutura do Dash 
def main():
    # Title: Sistema do CRM 
    st.title('Sitema de CRM para Vendas')

    # Input do email do vendedor 
    email = st.text_input('Insira o Email do vendedor: ')

    # Input da data da venda realizada 
    data = st.date_input('Insira a data da venda: ')

    # Input da hora da compra realizada 
    hora = st.time_input('Insira a hora da venda: ')

    # Input do valor da venda
    valor = st.number_input('Insira o valor da venda: ')

    # Quantidade de produtos 
    quantidade = st.number_input('Insira a quantidade de produtos: ',format='%.0f')

    # Input do produto vendido 
    produto = st.selectbox('Selecione qual o produto vendido:', ("Produto 1","Produto 2", "Produto 3"))

    # Botão para salvar os dados de CRM 
    if st.button('Salvar'):
        try:
            # Combinar as horas e data para o datetime
            data_hora = datetime.combine(data,hora)

            # Validando os dados do Contrato
            venda = Vendas(
                email=email,
                data=data_hora,
                valor=valor,
                quantidade= quantidade,
                produto=produto
        )
         # Salvando os dados no PostgreSQL
            salvar_no_postgres(venda)
            st.success("Dados validados e salvos com sucesso!")
        except ValidationError as e:
            st.error(f"Erro na validação dos dados: {e}")
        except Exception as e:
            st.error(f"Erro ao salvar os dados: {e}")



if __name__ == "__main__":
    main()