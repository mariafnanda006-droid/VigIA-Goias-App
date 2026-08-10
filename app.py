import streamlit as st

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================

st.set_page_config(
    page_title="VigIA Goiás",
    page_icon="🌿",
    layout="wide"
)

# =========================
# CABEÇALHO
# =========================

st.title("🌿 VigIA Goiás")

st.subheader(
    "Inteligência Artificial aplicada à vigilância ambiental"
)

st.write(
    """
    O **VigIA Goiás** utiliza Inteligência Artificial para identificar,
    em imagens do ambiente, elementos que podem estar relacionados
    a condições favoráveis à proliferação de vetores e outros riscos
    ambientais.
    """
)

st.divider()

# =========================
# UPLOAD DA IMAGEM
# =========================

st.header("📷 Analisar ambiente")

st.write(
    "Envie uma fotografia do ambiente que deseja analisar."
)

imagem = st.file_uploader(
    "Selecione uma imagem",
    type=["jpg", "jpeg", "png"]
)

if imagem is not None:

    st.image(
        imagem,
        caption="Imagem enviada para análise",
        use_container_width=True
    )

    st.success("Imagem recebida com sucesso!")

    if st.button("🔎 Analisar com o VigIA"):

        st.info(
            "O módulo de Inteligência Artificial será conectado "
            "após a conclusão do treinamento dos modelos."
        )

st.divider()

# =========================
# O QUE O SISTEMA ANALISA
# =========================

st.header("🧠 O que o VigIA identifica?")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🗑️ Recipientes e resíduos")
    st.write(
        """
        • Pneus  
        • Baldes  
        • Garrafas plásticas  
        • Latas
        """
    )

with col2:
    st.subheader("🌱 Ambiente")
    st.write(
        """
        • Vegetação  
        • Água parada  
        • Matéria orgânica
        """
    )

with col3:
    st.subheader("🏙️ Estrutura urbana")
    st.write(
        """
        Módulo em desenvolvimento para análise
        de condições de saneamento e estruturas
        relacionadas ao ambiente urbano.
        """
    )

st.divider()

# =========================
# AVISO
# =========================

st.caption(
    "VigIA Goiás — protótipo de sistema inteligente para "
    "monitoramento ambiental e apoio à vigilância em saúde."
)
