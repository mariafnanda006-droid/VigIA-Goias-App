import streamlit as st

st.set_page_config(
    page_title="VigIA Goiás",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 85% 8%, rgba(0,255,140,.13), transparent 24%),
        radial-gradient(circle at 8% 92%, rgba(0,180,120,.10), transparent 26%),
        linear-gradient(135deg, #020706 0%, #05110d 48%, #020807 100%);
    color: #f5fff9;
}

.block-container {
    max-width: 1380px;
    padding-top: 1rem;
    padding-bottom: 3rem;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {background: transparent !important;}

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.9rem 0 1.1rem 0;
    border-bottom: 1px solid rgba(72,255,140,.12);
}

.brand {
    font-size: 1.45rem;
    font-weight: 800;
    letter-spacing: -0.03em;
    color: white;
}

.brand span {
    color: #45f58a;
}

.nav-links {
    color: #9fb3a8;
    font-size: .92rem;
}

.hero {
    position: relative;
    overflow: hidden;
    margin-top: 1rem;
    padding: 4.8rem 3.6rem;
    min-height: 500px;
    border-radius: 30px;
    border: 1px solid rgba(74,255,142,.17);
    background:
        radial-gradient(circle at 77% 42%, rgba(34,255,126,.18), transparent 19%),
        radial-gradient(circle at 88% 55%, rgba(0,130,255,.08), transparent 18%),
        linear-gradient(115deg, rgba(3,15,10,.98), rgba(2,9,7,.82));
    box-shadow:
        0 24px 80px rgba(0,0,0,.38),
        inset 0 1px 0 rgba(255,255,255,.02);
}

.hero:before {
    content: "";
    position: absolute;
    right: 8%;
    top: 8%;
    width: 420px;
    height: 420px;
    border-radius: 50%;
    border: 1px solid rgba(65,255,139,.34);
    box-shadow:
        0 0 60px rgba(50,255,140,.13),
        inset 0 0 80px rgba(50,255,140,.05);
}

.hero:after {
    content: "";
    position: absolute;
    right: 14%;
    top: 18%;
    width: 280px;
    height: 280px;
    border-radius: 50%;
    border: 1px dashed rgba(70,255,140,.22);
}

.hero-content {
    position: relative;
    z-index: 2;
    max-width: 720px;
}

.eyebrow {
    color: #48f58e;
    font-size: .78rem;
    font-weight: 800;
    letter-spacing: .16em;
    text-transform: uppercase;
    margin-bottom: 1rem;
}

.hero h1 {
    margin: 0;
    color: white;
    font-size: 4.25rem;
    line-height: 1.02;
    letter-spacing: -0.055em;
    font-weight: 800;
}

.hero h1 span {
    color: #55f58a;
    text-shadow: 0 0 26px rgba(60,255,140,.20);
}

.hero p {
    color: #b2c3ba;
    font-size: 1.08rem;
    line-height: 1.8;
    max-width: 650px;
    margin-top: 1.5rem;
}

.pills {
    margin-top: 2rem;
    display: flex;
    gap: .8rem;
    flex-wrap: wrap;
}

.pill {
    padding: .72rem 1rem;
    border-radius: 999px;
    border: 1px solid rgba(69,255,140,.24);
    background: rgba(12,49,31,.28);
    color: #d0ffde;
    font-size: .84rem;
}

.section-kicker {
    margin-top: 4rem;
    color: #45f58a;
    font-weight: 800;
    letter-spacing: .14em;
    font-size: .76rem;
}

.section-title {
    margin-top: .35rem;
    margin-bottom: 1.35rem;
    color: white;
    font-size: 2.25rem;
    font-weight: 800;
    letter-spacing: -0.04em;
}

.upload-wrap {
    display: grid;
    grid-template-columns: .8fr 1.2fr;
    gap: 1.2rem;
    padding: 1.4rem;
    border-radius: 24px;
    background: rgba(6,24,17,.72);
    border: 1px solid rgba(73,255,142,.18);
    box-shadow: 0 22px 70px rgba(0,0,0,.28);
}

.upload-info {
    padding: 1.4rem;
    border-radius: 18px;
    background: linear-gradient(145deg, rgba(12,42,29,.74), rgba(5,22,15,.72));
    border: 1px solid rgba(75,255,143,.14);
}

.upload-info .icon {
    font-size: 2rem;
    margin-bottom: 1rem;
}

.upload-info h3 {
    color: white;
    margin-bottom: .6rem;
    font-size: 1.55rem;
}

.upload-info p {
    color: #9fb2a8;
    line-height: 1.7;
}

div[data-testid="stFileUploader"] {
    background: rgba(4,19,13,.74);
    border: 1px dashed rgba(72,255,140,.38);
    border-radius: 18px;
    padding: 1rem;
}

div[data-testid="stFileUploader"] section {
    background: transparent !important;
}

div[data-testid="stFileUploader"] button {
    background: linear-gradient(90deg, #0b7c43, #1fd66e) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
}

div.stButton > button {
    width: 100%;
    padding: .85rem;
    border-radius: 12px;
    background: linear-gradient(90deg, #0a7c43, #22d96d);
    color: white;
    border: 1px solid rgba(88,255,151,.35);
    font-weight: 800;
    box-shadow: 0 0 28px rgba(40,255,126,.10);
}

div.stButton > button:hover {
    color: white;
    border-color: #62ff9f;
    transform: translateY(-1px);
}

.cards-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.2rem;
}

.future-card {
    position: relative;
    overflow: hidden;
    min-height: 285px;
    padding: 1.6rem;
    border-radius: 22px;
    background:
        linear-gradient(145deg, rgba(8,29,20,.88), rgba(3,15,10,.82));
    border: 1px solid rgba(70,255,140,.18);
    box-shadow: 0 20px 60px rgba(0,0,0,.25);
    transition: .25s ease;
}

.future-card:hover {
    transform: translateY(-5px);
    border-color: rgba(70,255,140,.42);
    box-shadow: 0 28px 70px rgba(0,255,130,.07);
}

.future-card:after {
    content: "";
    position: absolute;
    width: 140px;
    height: 140px;
    border-radius: 50%;
    right: -35px;
    bottom: -35px;
    background: radial-gradient(circle, rgba(45,255,135,.10), transparent 68%);
}

.card-icon {
    width: 52px;
    height: 52px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 15px;
    background: rgba(55,255,132,.09);
    border: 1px solid rgba(70,255,140,.24);
    font-size: 1.45rem;
    margin-bottom: 1rem;
}

.future-card h3 {
    color: white;
    font-size: 1.3rem;
    margin-bottom: 1rem;
}

.future-card p {
    color: #a2b5aa;
    margin: .58rem 0;
}

.status {
    display: inline-flex;
    margin-top: 1rem;
    padding: .45rem .7rem;
    border-radius: 999px;
    background: rgba(255,193,7,.07);
    border: 1px solid rgba(255,193,7,.18);
    color: #ffd96f;
    font-size: .8rem;
}

.mission {
    margin-top: 2rem;
    padding: 1.45rem 1.6rem;
    border-radius: 18px;
    background:
        linear-gradient(90deg, rgba(12,51,32,.35), rgba(5,25,17,.25));
    border: 1px solid rgba(72,255,140,.16);
    color: #bfe9ce;
    text-align: center;
}

.footer-custom {
    margin-top: 3rem;
    padding-top: 1.5rem;
    border-top: 1px solid rgba(70,255,140,.08);
    color: #647c70;
    text-align: center;
    font-size: .82rem;
}

@media (max-width: 900px) {

    .hero {
        padding: 2.6rem 1.5rem;
        min-height: auto;
    }

    .hero h1 {
        font-size: 2.8rem;
    }

    .hero:before,
    .hero:after {
        opacity: .25;
        right: -180px;
    }

    .upload-wrap {
        grid-template-columns: 1fr;
    }

    .cards-grid {
        grid-template-columns: 1fr;
    }

    .nav-links {
        display: none;
    }
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# NAV
# =========================================================

st.markdown("""
<div class="navbar">
    <div class="brand">◉ Vig<span>IA</span> Goiás</div>
    <div class="nav-links">Início&nbsp;&nbsp;&nbsp; Projeto&nbsp;&nbsp;&nbsp; Tecnologia</div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class="hero">
    <div class="hero-content">

        <div class="eyebrow">
            VISÃO COMPUTACIONAL • VIGILÂNCIA AMBIENTAL
        </div>

        <h1>
            Tecnologia para um
            <span>ambiente mais seguro.</span>
        </h1>

        <p>
            O VigIA Goiás utiliza Inteligência Artificial para reconhecer
            elementos presentes no ambiente e apoiar a identificação de
            condições relevantes à vigilância em saúde.
        </p>

        <div class="pills">
            <div class="pill">✦ Inteligência Artificial</div>
            <div class="pill">◉ Dados ambientais</div>
            <div class="pill">⌁ Visão computacional</div>
        </div>

    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# UPLOAD
# =========================================================

st.markdown(
    '<div class="section-kicker">ANÁLISE INTELIGENTE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">Analise uma imagem do ambiente</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns([0.8, 1.2], gap="large")

with col1:
    st.markdown("""
    <div class="upload-info">
        <div class="icon">📷</div>
        <h3>Analisar ambiente</h3>
        <p>
            Envie uma fotografia para que o VigIA identifique
            elementos de interesse ambiental.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    imagem = st.file_uploader(
        "Imagem",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed"
    )

if imagem is not None:
    st.image(
        imagem,
        caption="Imagem enviada para análise",
        use_container_width=True
    )

    if st.button("✦ Iniciar análise com o VigIA"):
        st.info(
            "Os modelos treinados serão conectados aqui após a conclusão "
            "da etapa de treinamento."
        )

# =========================================================
# CARDS
# =========================================================

st.markdown(
    '<div class="section-kicker">MÓDULOS DO SISTEMA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">O que o VigIA identifica?</div>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3, gap="large")

with c1:
    st.markdown("""
    <div class="future-card">
        <div class="card-icon">♻️</div>
        <h3>Recipientes e resíduos</h3>
        <p>✓ Pneus</p>
        <p>✓ Baldes</p>
        <p>✓ Garrafas plásticas</p>
        <p>✓ Latas</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="future-card">
        <div class="card-icon">🌱</div>
        <h3>Condições ambientais</h3>
        <p>✓ Vegetação</p>
        <p>✓ Água parada</p>
        <p>✓ Matéria orgânica</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="future-card">
        <div class="card-icon">🏙️</div>
        <h3>Estrutura urbana</h3>
        <p>
            Futuro módulo de análise de infraestrutura,
            saneamento e condições urbanas.
        </p>
        <div class="status">● Em desenvolvimento</div>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# MISSÃO
# =========================================================

st.markdown("""
<div class="mission">
    <strong>VigIA Goiás</strong> — tecnologia e dados para apoiar
    ambientes mais seguros, saudáveis e monitorados.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footer-custom">
    VigIA Goiás • Inteligência Artificial aplicada à vigilância ambiental
</div>
""", unsafe_allow_html=True)
