import streamlit as st
import sqlite3

# Função para criar uma conexão com o banco de dados
def create_connection():
    conn = sqlite3.connect('meu_banco.db', check_same_thread=False)
    return conn

# Função para criar a tabela 'usuarios' se ela não existir
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()

# Função para inserir um usuário no banco de dados
def inserir_usuario(conn, nome, email):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO usuarios (nome, email)
        VALUES (?, ?)
    ''', (nome, email))
    conn.commit()

# Função para listar todos os usuários cadastrados
def listar_usuarios(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    return cursor.fetchall()

# Cria a conexão e a tabela, se necessário
conn = create_connection()
create_table(conn)

# Interface do Streamlit
st.title("App com SQLite3 e Streamlit")

st.subheader("Adicionar Usuário")
with st.form(key='form_usuario'):
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    submit_button = st.form_submit_button("Adicionar")

if submit_button:
    try:
        inserir_usuario(conn, nome, email)
        st.success("Usuário adicionado com sucesso!")
    except sqlite3.IntegrityError:
        st.error("Erro ao adicionar usuário. Verifique se o e-mail já existe.")

st.subheader("Lista de Usuários")
if st.button("Listar usuários"):
    usuarios = listar_usuarios(conn)
    if usuarios:
        st.write(usuarios)
    else:
        st.info("Nenhum usuário cadastrado.")

# Fechar a conexão ao encerrar o app (opcional)
# conn.close()
