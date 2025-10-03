# versão 1 

obs:Pretendo fazer atualizações, mas vou deixar os códigos e documetações para análise da evolução

# Conversor de Bases Numéricas

## Resumo

Este é um projeto simples e iniciante, feito para fins de aprendizagem e prática em programação com Python. O objetivo principal é facilitar a conversão de números decimais para outras bases (de 2 a 16), usando uma interface web criada com Streamlit.  
O código foi desenvolvido por um estudante do primeiro semestre de Engenharia da Computação, como parte de um desafio proposto em sala de aula.  
Observação: O projeto utiliza lógica manual para conversão, priorizando o entendimento do funcionamento do algoritmo.

---

## Contexto

Estou no primeiro semestre de Engenharia da Computação e comecei a aprender Python agora. Meu professor lançou um desafio: escrever no caderno o maior número possível de números em binário. Achei que seria trabalhoso fazer isso manualmente, então decidi criar uma tabela para facilitar. Aproveitei para explorar Python e aprender mais sobre programação, indo além do conteúdo visto em sala e usando também ferramentas de inteligência artificial para me ajudar.

## Sobre o Streamlit

Para deixar o projeto mais simples e interativo, utilizei o [Streamlit](https://streamlit.io/), uma biblioteca Python que permite criar aplicações web de forma rápida e fácil, sem precisar se preocupar com detalhes complexos de frontend. Com Streamlit, consigo criar campos para o usuário escolher o limite de números e a base de conversão, e exibir o resultado diretamente no navegador.

## Explicação do funcionamento do código

O objetivo do código é criar uma tabela que converte números decimais para qualquer base entre 2 e 16, facilitando a visualização e o estudo das conversões.

### Passo a passo do código

1. **Interface com Streamlit:**  
   Utilizei o Streamlit para criar uma interface web simples, onde o usuário pode escolher o limite do vetor (quantos números serão convertidos) e a base de conversão. Isso torna o uso mais fácil e interativo, sem precisar mexer no código toda vez.

2. **Criação do vetor decimal:**  
   Usei uma lista chamada `vetor_decimal` para armazenar todos os números de 0 até o limite escolhido pelo usuário.  
   Para adicionar cada número à lista, utilizei o método `append`, que insere o valor no final da lista:
   ```python
   vetor_decimal.append(contador)
   ```
   Isso garante que todos os números estejam disponíveis para conversão.

3. **Conversão manual para outras bases:**  
   Para converter cada número decimal para a base escolhida, implementei a lógica manualmente:
   - Criei uma string com todos os dígitos possíveis: `"0123456789ABCDEF"`.
   - Para cada número, faço divisões sucessivas pelo valor da base.  
     O resto da divisão (`numero_atual % base`) indica qual dígito deve ser usado.
   - Cada dígito é adicionado à esquerda da string `convertido`, formando o número na nova base.
   - Repito esse processo até que o número seja reduzido a zero. Se o número for zero, apenas atribuo `"0"`.

   Exemplo simplificado:
   ```python
   while numero_atual > 0:
       resto = numero_atual % base
       convertido = digitos[resto] + convertido
       numero_atual = numero_atual // base
   ```

4. **Formatação e exibição:**  
   Para deixar o resultado organizado, adiciono espaços para alinhar os números e monto uma string com o resultado final.  
   O Streamlit exibe essa string na tela para o usuário copiar ou visualizar.

- Poderia ter usado funções prontas do Python, como `bin()`, `oct()`, ou `hex()`, mas preferi implementar a lógica manualmente para entender melhor como funciona a conversão entre bases.
- O resultado é exibido em formato de tabela usando as funções do Streamlit, facilitando a visualização e a cópia dos dados.

## Acesse o app online

Você pode usar o conversor diretamente pelo navegador, sem instalar nada:

👉 [Abrir Conversor de Bases Numéricas](https://conversordebasesnumericas.streamlit.app/)

---

Se quiser rodar localmente, siga as instruções abaixo.

1. Instale o Streamlit:
   ```
   pip install streamlit
   ```
2. Execute o app:
   ```
   streamlit run app.py
   ```

---

Projeto feito para estudo, prática e para facilitar o desafio proposto em sala!
