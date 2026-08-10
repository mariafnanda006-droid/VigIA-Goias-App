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

st.html("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 88% 8%, rgba(0,255,140,.12), transparent 25%),
        radial-gradient(circle at 8% 90%, rgba(0,170,110,.08), transparent 27%),
        linear-gradient(135deg, #010604 0%, #03100b 48%, #010706 100%);
    color: white;
}

.block-container {
    max-width: 1380px;
    padding-top: 1rem;
    padding-bottom: 3rem;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

/* NAVBAR */

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 0 1.2rem 0;
    border-bottom: 1px solid rgba(72,255,140,.12);
}

.brand {
    color: white;
    font-size: 1.5rem;
    font-weight: 800;
}

.brand span {
    color: #45f58a;
}

.nav-links {
    color: #8ca398;
    font-size: .9rem;
}

/* HERO */

.hero {
    position: relative;
    overflow: hidden;
    margin-top: 1rem;
    padding: 5rem 3.7rem;
    min-height: 470px;
    border-radius: 30px;
    border: 1px solid rgba(74,255,142,.18);

    background:
        radial-gradient(circle at 79% 44%, rgba(36,255,127,.18), transparent 20%),
        radial-gradient(circle at 88% 55%, rgba(0,130,255,.08), transparent 17%),
        linear-gradient(115deg, rgba(3,15,10,.98), rgba(2,9,7,.84));

    box-shadow:
        0 25px 80px rgba(0,0,0,.40),
        inset 0 1px 0 rgba(255,255,255,.02);
}

.hero::before {
    content: "";
    position: absolute;
    right: 7%;
    top: 7%;
    width: 420px;
    height: 420px;
    border-radius: 50%;
    border: 1px solid rgba(65,255,139,.32);
    box-shadow:
        0 0 70px rgba(50,255,140,.13),
        inset 0 0 80px rgba(50,255,140,.05);
}

.hero::after {
    content: "";
    position: absolute;
    right: 13%;
    top: 17%;
    width: 285px;
    height: 285px;
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
    font-size: .77rem;
    font-weight: 800;
    letter-spacing: .17em;
    margin-bottom: 1.1rem;
}

.hero h1 {
    margin: 0;
    color: white;
    font-size: 4.3rem;
    line-height: 1.03;
    letter-spacing: -0.055em;
    font-weight: 800;
}

.hero h1 span {
    color: #55f58a;
    text-shadow: 0 0 30px rgba(60,255,140,.22);
}

.hero p {
    max-width: 650px;
    margin-top: 1.6rem;
    color: #afc2b7;
    font-size: 1.07rem;
    line-height: 1.8;
}

.pills {
    display: flex;
    flex-wrap: wrap;
    gap: .8rem;
    margin-top: 2rem;
}

.pill {
    padding: .72rem 1rem;
    border-radius: 999px;
    border: 1px solid rgba(69,255,140,.24);
    background: rgba(12,49,31,.28);
    color: #d0ffde;
    font-size: .84rem;
}

/* SEÇÕES */

.section-kicker {
    margin-top: 4rem;
    color: #45f58a;
    font-size: .76rem;
    font-weight: 800;
    letter-spacing: .15em;
}

.section-title {
    margin-top: .35rem;
    margin-bottom: 1.4rem;
    color: white;
    font-size: 2.3rem;
    font-weight: 800;
}

/* UPLOAD */

.upload-info {
    min-height: 205px;
    padding: 1.7rem;
    border-radius: 22px;

    background:
        linear-gradient(
            145deg,
            rgba(10,38,26,.82),
            rgba(4,18,12,.82)
        );

    border: 1px solid rgba(75,255,143,.16);
    box-shadow: 0 20px 60px rgba(0,0,0,.25);
}

.upload-icon {
    width: 52px;
    height: 52px;

    display: flex;
    align-items: center;
    justify-content: center;

    margin-bottom: 1rem;
    border-radius: 15px;

    background: rgba(55,255,132,.09);
    border: 1px solid rgba(70,255,140,.24);

    font-size: 1.5rem;
}

.upload-info h3 {
    color: white;
    font-size: 1.5rem;
}

.upload-info p {
    color: #9fb3a8;
    line-height: 1.7;
}

div[data-testid="stFileUploader"] {
    min-height: 205px;
    display: flex;
    align-items: center;

    background:
        linear-gradient(
            145deg,
            rgba(6,25,17,.85),
            rgba(3,15,10,.85)
        );

    border: 1px dashed rgba(72,255,140,.38);
    border-radius: 22px;
    padding: 1.2rem;

    box-shadow: 0 20px 60px rgba(0,0,0,.22);
}

div[data-testid="stFileUploader"] section {
    background: transparent !important;
}

div[data-testid="stFileUploader"] button {
    background: linear-gradient(90deg, #08763e, #20d76e) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
}

/* BOTÃO */

div.stButton > button {
    width: 100%;
    padding: .9rem;
    border-radius: 13px;
    background: linear-gradient(90deg, #087a41, #22d96d);
    color: white;
    border: 1px solid rgba(88,255,151,.35);
    font-weight: 800;
}

/* CARDS */

.future-card {
    position: relative;
    overflow: hidden;
    min-height: 285px;
    padding: 1.7rem;
    border-radius: 22px;

    background:
        linear-gradient(
            145deg,
            rgba(8,29,20,.90),
            rgba(3,15,10,.86)
        );

    border: 1px solid rgba(70,255,140,.18);
    box-shadow: 0 20px 60px rgba(0,0,0,.25);

    transition: .25s ease;
}

.future-card:hover {
    transform: translateY(-5px);
    border-color: rgba(70,255,140,.42);
}

.card-icon {
    width: 52px;
    height: 52px;

    display: flex;
    align-items: center;
    justify-content: center;

    margin-bottom: 1rem;

    border-radius: 15px;

    background: rgba(55,255,132,.09);
    border: 1px solid rgba(70,255,140,.24);

    font-size: 1.45rem;
}

.future-card h3 {
    color: white;
    font-size: 1.3rem;
}

.future-card p {
    color: #a2b5aa;
    margin: .58rem 0;
}

.check {
    color: #4df58d;
    font-weight: 700;
}

.status {
    display: inline-flex;
    margin-top: 1rem;

    padding: .45rem .75rem;

    border-radius: 999px;

    background: rgba(255,193,7,.07);
    border: 1px solid rgba(255,193,7,.18);

    color: #ffd96f;
    font-size: .8rem;
}

/* MISSÃO */

.mission {
    margin-top: 2.3rem;
    padding: 1.6rem;

    border-radius: 20px;

    background:
        linear-gradient(
            90deg,
            rgba(12,51,32,.35),
            rgba(5,25,17,.25)
        );

    border: 1px solid rgba(72,255,140,.16);

    color: #bfe9ce;
    text-align: center;
}

.mission strong {
    color: #54f591;
}

/* FOOTER */

.footer-custom {
    margin-top: 3rem;
    padding-top: 1.5rem;

    border-top: 1px solid rgba(70,255,140,.08);

    color: #647c70;
    text-align: center;
    font-size: .82rem;
}

</style>
""")

# =========================================================
# NAVBAR
# =========================================================

st.html("""
<div class="navbar">

    <div class="brand">
        ◉ Vig<span>IA</span> Goiás
    </div>

    <div class="nav-links">
        Início &nbsp;&nbsp;&nbsp;
        Projeto &nbsp;&nbsp;&nbsp;
        Tecnologia
    </div>

</div>
""")

# =========================================================
# HERO
# =========================================================

st.html("""
<div class="hero">

    <div class="hero-content">

        <div class="eyebrow">
            VISÃO COMPUTACIONAL • VIGILÂNCIA AMBIENTAL
        </div>

        <h1>
            Tecnologia para um<br>
            <span>ambiente mais seguro.</span>
        </h1>

        <p>
            O VigIA Goiás utiliza Inteligência Artificial para reconhecer
            elementos presentes no ambiente e apoiar a identificação de
            condições relevantes à vigilância em saúde.
        </p>

        <div class="pills">

            <div class="pill">
                ✦ Inteligência Artificial
            </div>

            <div class="pill">
                ◉ Dados ambientais
            </div>

            <div class="pill">
                ⌁ Visão computacional
            </div>

        </div>

    </div>

</div>
""")

# =========================================================
# UPLOAD
# =========================================================

st.html("""
<div class="section-kicker">
    ANÁLISE INTELIGENTE
</div>

<div class="section-title">
    Analise uma imagem do ambiente
</div>
""")

col1, col2 = st.columns(
    [0.8, 1.2],
    gap="large"
)

with col1:

    st.html("""
    <div class="upload-info">

        <div class="upload-icon">
            📷
        </div>

        <h3>
            Analisar ambiente
        </h3>

        <p>
            Envie uma fotografia do ambiente para que o VigIA
            possa identificar elementos relevantes para a
            vigilância ambiental.
        </p>

    </div>
    """)

with col2:

    imagem = st.file_uploader(
        "Selecione uma imagem",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed"
    )

# =========================================================
# IMAGEM
# =========================================================

if imagem is not None:

    st.image(
        imagem,
        caption="Imagem enviada para análise",
        use_container_width=True
    )

    if st.button(
        "✦ Iniciar análise com o VigIA",
        use_container_width=True
    ):

        st.info(
            "Os modelos de Inteligência Artificial serão "
            "conectados após a conclusão do treinamento."
        )

# =========================================================
# MÓDULOS
# =========================================================

st.html("""
<div class="section-kicker">
    MÓDULOS DO SISTEMA
</div>

<div class="section-title">
    O que o VigIA identifica?
</div>
""")

c1, c2, c3 = st.columns(
    3,
    gap="large"
)

# CARD 1
with c1:

    st.html("""
    <div class="future-card">

        <div class="card-icon">
            ♻️
        </div>

        <h3>
            Recipientes e resíduos
        </h3>

        <p>
            <span class="check">✓</span>
            Pneus
        </p>

        <p>
            <span class="check">✓</span>
            Baldes
        </p>

        <p>
            <span class="check">✓</span>
            Garrafas plásticas
        </p>

        <p>
            <span class="check">✓</span>
            Latas
        </p>

    </div>
    """)

# CARD 2
with c2:

    st.html("""
    <div class="future-card">

        <div class="card-icon">
            🌱
        </div>

        <h3>
            Condições ambientais
        </h3>

        <p>
            <span class="check">✓</span>
            Vegetação
        </p>

        <p>
            <span class="check">✓</span>
            Água parada
        </p>

        <p>
            <span class="check">✓</span>
            Matéria orgânica
        </p>

    </div>
    """)

# CARD 3
with c3:

    st.html("""
    <div class="future-card">

        <div class="card-icon">
            🏙️
        </div>

        <h3>
            Estrutura urbana
        </h3>

        <p>
            Futuro módulo de análise de infraestrutura,
            saneamento e condições urbanas relacionadas
            ao ambiente.
        </p>

        <div class="status">
            ● Em desenvolvimento
        </div>

    </div>
    """)

# =========================================================
# MISSÃO
# =========================================================

st.html("""
<div class="mission">

    <strong>VigIA Goiás</strong>

    — tecnologia, Inteligência Artificial e dados ambientais
    para apoiar ambientes mais seguros, saudáveis e monitorados.

</div>
""")

# =========================================================
# FOOTER
# =========================================================

st.html("""
<div class="footer-custom">

    VigIA Goiás •
    Inteligência Artificial aplicada à vigilância ambiental

</div>
""")
