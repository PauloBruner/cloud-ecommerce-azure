import pyodbc
import streamlit as st
from app.config import *


# ==============================
# CONEXÃO
# ==============================

def get_connection():
    connection_string = f"""
    DRIVER={{ODBC Driver 17 for SQL Server}};
    SERVER=tcp:{SQL_SERVER},1433;
    DATABASE={SQL_DATABASE};
    UID={SQL_USER};
    PWD={SQL_PASSWORD};
    Encrypt=yes;
    TrustServerCertificate=no;
    Connection Timeout=30;
    """
    return pyodbc.connect(connection_string)


# ==============================
# CREATE
# ==============================

def insert_product(name, price, description, image_url):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO dbo.Products (Name, Price, Description, ImageUrl)
        VALUES (?, ?, ?, ?)
    """, (name, price, description, image_url))

    conn.commit()
    conn.close()


# ==============================
# READ
# ==============================

def list_products():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT Id, Name, Price, Description, ImageUrl
        FROM dbo.Products
        ORDER BY Id DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    products = []

    for row in rows:
        products.append({
            "id": row[0],
            "nome": row[1],
            "preco": float(row[2]),
            "descricao": row[3],
            "imagem_url": row[4]
        })

    return products


# ==============================
# DELETE
# ==============================

def delete_product(product_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM dbo.Products WHERE Id = ?",
        (product_id,)
    )

    conn.commit()
    conn.close()


# ==============================
# TELA LISTAGEM
# ==============================

def list_produtos_screen():
    products = list_products()

    if not products:
        st.info("Nenhum produto encontrado.")
        return

    st.subheader("🛍️ Produtos Disponíveis")

    cards_por_linha = 3

    for i in range(0, len(products), cards_por_linha):
        cols = st.columns(cards_por_linha)

        for col, product in zip(cols, products[i:i+cards_por_linha]):
            with col:

                # Imagem
                if product["imagem_url"]:
                    st.image(product["imagem_url"], width="stretch")

                # Nome
                st.markdown(f"### {product['nome']}")

                # Preço
                st.markdown(
                    f"<h4 style='color:#2e7d32;'>R$ {product['preco']:.2f}</h4>",
                    unsafe_allow_html=True
                )

                # Descrição
                st.write(product["descricao"])

                # Botões
                col1, col2 = st.columns(2)

                with col1:
                    if st.button("Comprar", key=f"buy_{product['id']}"):
                        st.success("Produto adicionado ao carrinho 🛒")

                with col2:
                    if st.button("Excluir", key=f"delete_{product['id']}"):
                        delete_product(product["id"])
                        st.success("Produto excluído com sucesso!")
                        st.rerun()
