import streamlit as st
from app.database import insert_product, list_produtos_screen, delete_product
from app.blob_service import upload_image
st.set_page_config(page_title="Cloud E-Commerce Platform")
st.title("Cloud E-Commerce Platform")

name = st.text_input("Nome do Produto")
price = st.number_input("Preço", min_value=0.0, format="%.2f")
description = st.text_area("Descrição")
image = st.file_uploader("Imagem", type=["jpg", "png", "jpeg"])

if st.button("Salvar Produto"):
    if image:
        image_url = upload_image(image)
        insert_product(name, price, description, image_url)
        st.success("Produto cadastrado com sucesso!")
    else:
        st.error("Selecione uma imagem.")

st.header("Produtos Cadastrados")
list_produtos_screen()