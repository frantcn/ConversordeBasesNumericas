import streamlit as st

st.title("Conversor de bases numéricas")
st.markdown(" usando Python (Streamlit)")

limite = st.number_input(
    'Digite o limite do vetor (começando do 0):', 
    min_value=0, 
    max_value=5000,  
    value=10, 
    step=1
)
LIMITE = int(limite)

base = st.number_input(
    'Digite a base para conversão (entre 2 e 36):',
    min_value=2,
    max_value=36,
    value=2,
    step=1
)

saida_tabela = ""

vetor_decimal = []
contador = 0

while contador <= LIMITE:
    vetor_decimal.append(contador)
    contador = contador + 1

for decimal in vetor_decimal:
    if decimal == 0:
        convertido = "0"
    else:
        convertido = ""
        numero_atual = decimal
        digitos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while numero_atual > 0:
            resto = numero_atual % base
            convertido = digitos[resto] + convertido
            numero_atual = numero_atual // base

    espacos = " " * (4 - len(str(decimal)))
    saida_tabela += f"Decimal: {decimal}{espacos} -> Base {base}: {convertido}\n"

st.header("Resultado da Tabela")

st.text(saida_tabela)

