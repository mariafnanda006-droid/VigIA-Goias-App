import streamlit as st

st.set_page_config(
    page_title="VigIA Goiás",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CSS — TEMA FUTURISTA
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
        radial-gradient(circle at 85% 10%, rgba(0,255,140,.12), transparent 28%),
        radial-gradient(circle at 10% 90%, rgba(0,180,110,.10), transparent 30%),
        linear-gradient(135deg, #020807 0%, #06110d 45%, #020706 100%);
    color: #f5fff9;
}

.block-container {
    max-width: 1350px;
    padding-top: 1.2rem;
    padding-bottom: 3rem;
}

/* Esconde elementos padrão desnecessários */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {background: transparent !important;}

/* NAV */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.9rem 0 1.4rem 0;
    border-bottom: 1px solid rgba(71,255,143,.13);
}

.logo {
    font-size: 1.45rem;
    font-weight: 800;
    color: white;
    letter-spacing: -0.03em;
}

.logo span {
    color: #45f58a;
}

.nav-links {
    color: #9fb8aa;
    font-size: 0.9rem;
    word-spacing: 1rem;
}

/* HERO */
.hero {
    min-height: 470px;
    display: flex;
    align-items: center;
    position: relative;
    overflow: hidden;
    padding: 4.5rem 3.4rem;
    margin-top: 1rem;
    border-radius: 28px;
    border: 1px solid rgba(76,255,145,.15);
    background:
        radial-gradient(circle at 78% 45%, rgba(24,255,127,.18), transparent 22%),
        linear-gradient(110deg, rgba(4,16,12,.96), rgba(3,10,8,.70));
    box-shadow: 0 0 70px rgba(0,255,130,.06);
}

.hero:after {
    content: "";
    position: absolute;
    width: 420px;
    height: 420px;
    border-radius: 50%;
    right: 7%;
    top: 5%;
    border: 1px solid rgba(61,255,141,.35);
    box-shadow:
        0 0 40px rgba(55,255,140,.16),
        inset 0 0 60px rgba(35,255,130,.07);
}

.hero-content {
    max-width: 690px;
    z-index: 2;
}

.eyebrow {
    color: #48f58e;
    text-transform: uppercase;
    letter-spacing: .16em;
    font-size: .78rem;
    font-weight: 700;
    margin-bottom: 1rem;
}

.hero h1 {
    font-size: 4rem;
    line-height: 1.02;
    font-weight: 800;
    letter-spacing: -0.055em;
    margin: 0 0 1.4rem 0;
    color: white;
}

.hero h1 span {
    color: #55f58a;
    text-shadow: 0 0 25px rgba(66,255,139,.22);
}

.hero p {
    color: #b7c8bf;
    line-height: 1.8;
    font-size: 1.06rem;
    max-width: 610px;
}

.tech-row {
    display: flex;
    gap: 1rem;
    margin-top: 2.2rem;
    flex-wrap: wrap;
}

.tech-pill {
    padding: .7rem 1rem;
    border-radius: 999px;
    border: 1px solid rgba(65,255,139,.23);
    background: rgba(17,61,39,.22);
    color: #c7ffda;
    font-size: .84rem;
}

/* TÍTULOS */
.section-kicker {
    margin-top: 4rem;
    color: #45f58a;
    font-size: .75rem;
    letter-spacing: .14em;
    font-weight: 800;
}

.section-title {
    color: white;
    font-weight: 800;
    font-size: 2.2rem;
    letter-spacing: -0.04em;
    margin: .35rem 0 1.5rem 0;
}

/* UPLOAD CARD */
.upload-shell {
    padding: 2rem;
    border-radius: 24px;
    background: rgba(7, 25, 18, .72);
    border: 1px solid rgba(79,255,145,.18);
    box-shadow:
        inset 0 1px 0 rgba(255,255,255,.03),
        0 18px 60px rgba(0,0,0,.28);
}

.upload-copy h3 {
    color: white;
    margin: 0 0 .6rem 0;
    font-size: 1.5rem;
}

.upload-copy p {
    color: #97aea2;
}

/* File uploader */
div[data-testid="stFileUploader"] {
    background: rgba(6, 21, 15, .75);
    border: 1px dashed rgba(71,255,137,.45);
    border-radius: 18px;
    padding: 1rem;
}

div[data-testid="stFileUploader"] section {
    background: transparent;
}

div[data-testid="stFileUploader"] button {
    background: linear-gradient(90deg, #0c7a45, #1dd66f) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
}

/* CARDS */
.cards-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.2rem;
}

.future-card {
    background: linear-gradient(145deg, rgba(9,31,22,.82), rgba(3,15,10,.72));
    border: 1px solid rgba(70,255,140,.17);
    border-radius: 22px;
    padding: 1.6rem;
    min-height: 250px;
    transition: .25s ease;
    box-shadow: 0 18px 55px rgba(0,0,0,.22);
}

.future-card:hover {
    transform: translateY(-4px);
    border-color: rgba(70,255,140,.4);
    box-shadow: 0 24px 65px rgba(0,255,120,.08);
}

.card-icon {
    width: 48px;
    height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 14px;
    background: rgba(56,255,132,.11);
    border: 1px solid rgba(69,255,137,.25);
    font-size: 1.4rem;
    margin-bottom: 1rem;
}

.future-card h3 {
    color: white;
    margin-bottom: 1rem;
}

.future-card p {
    color: #9eb3a7;
    margin: .55rem 0;
}

/* STATUS */
.status {
    display: inline-flex;
    align-items: center;
    gap: .45rem;
    margin-top: 1rem;
    padding: .4rem .7rem;
    border-radius: 999px;
    background: rgba(255, 193, 7, .08);
    color: #ffd96b;
    border: 1px solid rgba(255, 193, 7, .17);
    font-size: .8rem;
}

/* BOTÃO */
div.stButton > button {
    width: 100%;
    padding: .8rem;
    border-radius: 12px;
    border: 1px solid rgba(67,255,137,.35);
    background: linear-gradient(90deg, #0a7d43 0%, #22d96c 100%);
    color: white;
    font-weight: 800;
    box-shadow: 0 0 30px rgba(42,255,126,.10);
}

div.stButton > button:hover {
    border-color: #5aff99;
    color: white;
    transform: translateY(-1px);
}

/* INFO */
.mission {
    margin-top: 2rem;
    padding: 1.4rem 1.6rem;
    border-radius: 18px;
    background: rgba(18,64,42,.24);
    border: 1px solid rgba(75,255,141,.17);
    color: #bfe8ce;
    text-align: center;
}

.footer-custom {
    color: #668176;
    text-align: center;
    font-size: .8rem;
    margin-top: 3rem;
    padding-top: 1.5rem;
    border-top: 1px solid rgba(70,255,140,.08);
}

/* Mobile */
@media (max-width: 900px) {
    .cards-grid {
        grid-template-columns: 1fr;
    }

    .hero {
        padding: 2.5rem 1.5rem;
        min-height: auto;
    }

    .hero h1 {
        font-size: 2.7rem;
    }

    .hero:after {
        opacity: .3;
        right: -180px;
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
    <div class="logo">◉ Vig<span>IA</span> Goiás</div>
    <div class="nav-links">Início &nbsp;&nbsp; Tecnologia &nbsp;&nbsp; Projeto</div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# HERO
# =========================================================
st.markdown("""
<div class="hero">
    <div class="hero-content">
        <div class="eyebrow">VISÃO COMPUTACIONAL • VIGILÂNCIA AMBIENTAL</div>

        <h1>
            Tecnologia para um
            <span>ambiente mais seguro.</span>
        </h1>

        <p>
            O VigIA Goiás utiliza Inteligência Artificial para reconhecer
            elementos presentes no ambiente e apoiar a identificação de
            condições relevantes à vigilância em saúde.
        </p>

        <div class="tech-row">
            <div class="tech-pill">✦ Inteligência Artificial</div>
            <div class="tech-pill">◉ Dados ambientais</div>
            <div class="tech-pill">⌁ Visão computacional</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# UPLOAD
# =========================================================
st.markdown('<div class="section-kicker">ANÁLISE INTELIGENTE</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Envie uma imagem do ambiente</div>', unsafe_allow_html=True)

st.markdown("""
<div class="upload-shell">
    <div class="upload-copy">
        <h3>▣ Analisar ambiente</h3>
        <p>
            Envie uma fotografia para que o VigIA identifique
            elementos de interesse ambiental.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

imagem = st.file_uploader(
    "Imagem",
    type=["jpg", "jpeg", "png"],
    label_visibility="collapsed"
)

if imagem is not None:
    st.image(imagem, caption="Imagem enviada", use_container_width=True)

    if st.button("✦ Iniciar análise com o VigIA"):
        st.info(
            "Os modelos treinados serão conectados aqui após a conclusão "
            "da etapa de treinamento."
        )

# =========================================================
# CATEGORIAS
# =========================================================
st.markdown('<div class="section-kicker">MÓDULOS DO SISTEMA</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">O que o VigIA identifica?</div>', unsafe_allow_html=True)

st.markdown("""
<div class="cards-grid">

    <div class="future-card">
        <div class="card-icon">♻</div>
        <h3>Recipientes e resíduos</h3>
        <p>✓ Pneus</p>
        <p>✓ Baldes</p>
        <p>✓ Garrafas plásticas</p>
        <p>✓ Latas</p>
    </div>

    <div class="future-card">
        <div class="card-icon">◈</div>
        <h3>Condições ambientais</h3>
        <p>✓ Vegetação</p>
        <p>✓ Água parada</p>
        <p>✓ Matéria orgânica</p>
    </div>

    <div class="future-card">
        <div class="card-icon">⌂</div>
        <h3>Estrutura urbana</h3>
        <p>
            Futuro módulo de análise de infraestrutura,
            saneamento e condições urbanas.
        </p>
        <div class="status">● Em desenvolvimento</div>
    </div>

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
