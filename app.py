import streamlit as st

st.set_page_config(
    page_title="VigIA Goiás",
    page_icon="🌿",
    layout="wide"
)

# =========================
# CSS
# =========================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(180deg, #f7fbf7 0%, #ffffff 45%, #f4f8f5 100%);
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.hero {
    background: linear-gradient(135deg, #0f5132 0%, #198754 55%, #6abf69 100%);
    color: white;
    padding: 3rem;
    border-radius: 28px;
    margin-bottom: 2rem;
    box-shadow: 0 16px 40px rgba(20, 80, 50, 0.16);
}

.hero h1 {
    font-size: 3.2rem;
    margin-bottom: 0.3rem;
}

.hero h3 {
    font-weight: 500;
    opacity: 0.95;
}

.hero p {
    max-width: 800px;
    font-size: 1.05rem;
    line-height: 1.7;
}

.section-title {
    font-size: 2rem;
    font-weight: 800;
    margin-top: 1.5rem;
    margin-bottom: 1.2rem;
    color: #153b2d;
}

.card {
    background: white;
    padding: 1.6rem;
    border-radius: 22px;
    box-shadow: 0 8px 28px rgba(33, 70, 50, 0.08);
    border: 1px solid #e4eee7;
    min-height: 230px;
}

.card-green {
    border-top: 5px solid #198754;
}

.card-blue {
    border-top: 5px solid #168aad;
}

.card-purple {
    border-top: 5px solid #6f42c1;
}

.card h3 {
    margin-bottom: 1rem;
}

.upload-card {
    background: white;
    border-radius: 24px;
    padding: 2rem;
    box-shadow: 0 10px 35px rgba(33, 70, 50, 0.09);
    border: 1px solid #e5efe8;
    margin-bottom: 2rem;
}

.info-banner {
    background: #eaf6ee;
    padding: 1.2rem 1.5rem;
    border-radius: 18px;
    border-left: 6px solid #198754;
    margin-top: 2rem;
    color: #174a30;
}

.footer {
    text-align: center;
    padding: 2rem 0 0.5rem 0;
    color: #587066;
    font-size: 0.9rem;
}

div[data-testid="stFileUploader"] {
    background: #f8fbf9;
    border: 2px dashed #9bc7aa;
    border-radius: 18px;
    padding: 1rem;
}

div.stButton > button {
    width: 100%;
    border-radius: 14px;
    background: #198754;
    color: white;
    border: none;
    font-weight: 700;
    padding: 0.8rem 1rem;
}

div.stButton > button:hover {
    background: #126b43;
    color: white;
    border: none;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HERO
# =========================

st.markdown("""
<div class="hero">
    <h1>🌿 VigIA Goiás</h1>
    <h3>Inteligência Artificial aplicada à vigilância ambiental</h3>
    <p>
        Uma plataforma para identificar condições ambientais de interesse à
        vigilância em saúde por meio de visão computacional e integração
        de dados ambientais e epidemiológicos.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# UPLOAD
# =========================

st.markdown('<div class="section-title">📷 Analisar ambiente</div>', unsafe_allow_html=True)

st.markdown("""
<div class="upload-card">
    <h3>Envie uma fotografia</h3>
    <p>
        Selecione uma imagem do ambiente para que o VigIA possa identificar
        elementos relevantes para a análise ambiental.
    </p>
</div>
""", unsafe_allow_html=True)

imagem = st.file_uploader(
    "Selecione uma imagem",
    type=["jpg", "jpeg", "png"],
    label_visibility="collapsed"
)

if imagem is not None:
    st.image(
        imagem,
        caption="Imagem enviada",
        use_container_width=True
    )

    if st.button("🔎 Analisar com o VigIA"):
        st.info(
            "Os modelos de Inteligência Artificial serão conectados "
            "a esta interface após a conclusão do treinamento."
        )

# =========================
# CATEGORIAS
# =========================

st.markdown(
    '<div class="section-title">🧠 O que o VigIA identifica?</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card card-green">
        <h3>🗑️ Recipientes e resíduos</h3>
        <p>✅ Pneus</p>
        <p>✅ Baldes</p>
        <p>✅ Garrafas plásticas</p>
        <p>✅ Latas</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card card-blue">
        <h3>🌱 Condições ambientais</h3>
        <p>✅ Vegetação</p>
        <p>✅ Água parada</p>
        <p>✅ Matéria orgânica</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card card-purple">
        <h3>🏙️ Estrutura urbana</h3>
        <p>
            Módulo em desenvolvimento para identificação de condições
            de saneamento e estruturas urbanas relacionadas ao risco ambiental.
        </p>
    </div>
    """, unsafe_allow_html=True)

# =========================
# OBJETIVO
# =========================

st.markdown("""
<div class="info-banner">
    <strong>🎯 Objetivo do projeto</strong><br><br>
    Apoiar a identificação de condições ambientais relevantes para a vigilância
    em saúde e transformar imagens e dados locais em informações úteis para
    prevenção e monitoramento.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    VigIA Goiás • Tecnologia, ciência e meio ambiente
</div>
""", unsafe_allow_html=True)
