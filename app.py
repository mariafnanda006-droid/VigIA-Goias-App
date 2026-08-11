import streamlit as st
import base64
from pathlib import Path

# =========================================================
# CONFIGURAÇÃO
# =========================================================

st.set_page_config(
    page_title="VigIA Goiás",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# CARREGAR IMAGENS
# =========================================================

def imagem_base64(caminho):
    arquivo = Path(caminho)

    if not arquivo.exists():
        return ""

    return base64.b64encode(
        arquivo.read_bytes()
    ).decode("utf-8")


logo = imagem_base64("Logo Vigia Goias.png")
foto_natureza = imagem_base64("Foto Natureza 1.jpg")
foto_cidade = imagem_base64("Foto Cidade Goiania.jpg")


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

* {
    box-sizing: border-box;
}

html, body, [class*="css"] {
    font-family: Arial, Helvetica, sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 88% 5%, rgba(0, 255, 130, .11), transparent 24%),
        radial-gradient(circle at 5% 90%, rgba(0, 180, 100, .08), transparent 25%),
        #010806;
    color: white;
}

.block-container {
    max-width: 1400px;
    padding-top: 1.2rem;
    padding-bottom: 4rem;
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


/* ========================================================
   NAVBAR
======================================================== */

.navbar {
    display: flex;
    align-items: center;
    justify-content: space-between;

    padding: 5px 5px 18px 5px;

    border-bottom: 1px solid rgba(71, 255, 141, .13);
}

.brand {
    display: flex;
    align-items: center;
    gap: 15px;
}

.logo {
    width: 92px;
    height: 92px;

    object-fit: contain;

    border-radius: 18px;

    filter:
        drop-shadow(0 0 20px rgba(65, 255, 140, .15));
}

.brand-title {
    color: #ffffff;

    font-size: 1.5rem;
    font-weight: 800;

    letter-spacing: -.03em;
}

.brand-title span {
    color: #49f58a;
}

.brand-subtitle {
    color: #789488;

    font-size: .70rem;

    margin-top: 4px;

    letter-spacing: .05em;
}

.nav-links {
    color: #8ba399;

    font-size: .86rem;

    word-spacing: 20px;
}


/* ========================================================
   HERO
======================================================== */

.hero {
    position: relative;

    overflow: hidden;

    min-height: 510px;

    margin-top: 20px;

    padding: 75px 65px;

    border-radius: 32px;

    border: 1px solid rgba(66, 255, 137, .20);

    background:
        radial-gradient(
            circle at 78% 48%,
            rgba(0, 255, 123, .14),
            transparent 19%
        ),
        linear-gradient(
            120deg,
            rgba(2, 20, 13, .98),
            rgba(1, 10, 7, .95)
        );

    box-shadow:
        0 30px 100px rgba(0, 0, 0, .45);
}


/* círculo grande */

.hero::before {
    content: "";

    position: absolute;

    width: 430px;
    height: 430px;

    right: 6%;
    top: 7%;

    border-radius: 50%;

    border: 1px solid rgba(66, 255, 137, .30);

    box-shadow:
        0 0 80px rgba(30, 255, 130, .10);
}


/* círculo interno */

.hero::after {
    content: "";

    position: absolute;

    width: 290px;
    height: 290px;

    right: 11%;
    top: 21%;

    border-radius: 50%;

    border: 1px dashed rgba(66, 255, 137, .18);
}


.hero-content {
    position: relative;

    z-index: 2;

    max-width: 750px;
}

.eyebrow {
    color: #49f58a;

    font-size: .76rem;

    font-weight: 800;

    letter-spacing: .18em;

    margin-bottom: 20px;
}

.hero h1 {
    color: white;

    margin: 0;

    font-size: clamp(3rem, 5vw, 5rem);

    line-height: 1.02;

    letter-spacing: -.055em;

    font-weight: 850;
}

.hero h1 span {
    color: #50f58c;

    text-shadow:
        0 0 35px rgba(57, 255, 135, .20);
}

.hero-description {
    max-width: 660px;

    margin-top: 26px;

    color: #adc2b7;

    font-size: 1.08rem;

    line-height: 1.75;
}


.pills {
    display: flex;

    flex-wrap: wrap;

    gap: 12px;

    margin-top: 30px;
}

.pill {
    padding: 11px 17px;

    border-radius: 999px;

    color: #caffdb;

    font-size: .82rem;

    border: 1px solid rgba(68, 255, 139, .25);

    background: rgba(12, 54, 33, .30);

    backdrop-filter: blur(8px);
}


/* ========================================================
   TÍTULOS
======================================================== */

.section {
    margin-top: 70px;
}

.section-label {
    color: #49f58a;

    font-size: .73rem;

    font-weight: 800;

    letter-spacing: .17em;

    margin-bottom: 8px;
}

.section-title {
    color: white;

    font-size: 2.45rem;

    font-weight: 800;

    letter-spacing: -.04em;

    margin-bottom: 25px;
}


/* ========================================================
   ÁREA DE ANÁLISE
======================================================== */

.analysis-info {
    min-height: 230px;

    padding: 30px;

    border-radius: 24px;

    border: 1px solid rgba(70, 255, 140, .17);

    background:
        linear-gradient(
            145deg,
            rgba(9, 42, 27, .74),
            rgba(3, 18, 12, .90)
        );

    box-shadow:
        0 20px 60px rgba(0, 0, 0, .25);
}

.analysis-icon {
    display: flex;

    align-items: center;
    justify-content: center;

    width: 55px;
    height: 55px;

    margin-bottom: 18px;

    border-radius: 16px;

    font-size: 1.55rem;

    border: 1px solid rgba(72, 255, 142, .25);

    background: rgba(39, 255, 127, .08);
}

.analysis-info h3 {
    color: white;

    margin: 0 0 10px 0;

    font-size: 1.45rem;
}

.analysis-info p {
    color: #9db4a8;

    line-height: 1.65;

    margin: 0;
}


/* uploader do Streamlit */

div[data-testid="stFileUploader"] {
    min-height: 230px;

    display: flex;
    align-items: center;

    padding: 20px;

    border-radius: 24px;

    border: 1px dashed rgba(70, 255, 140, .35);

    background:
        linear-gradient(
            145deg,
            rgba(7, 30, 20, .78),
            rgba(3, 16, 11, .90)
        );
}

div[data-testid="stFileUploader"] section {
    background: transparent !important;
}

div[data-testid="stFileUploader"] button {
    border: none !important;

    border-radius: 12px !important;

    background:
        linear-gradient(
            90deg,
            #087940,
            #21d970
        ) !important;

    color: white !important;
}


/* ========================================================
   CARDS COM IMAGENS
======================================================== */

.future-card {
    position: relative;

    overflow: hidden;

    min-height: 390px;

    padding: 30px;

    border-radius: 25px;

    border: 1px solid rgba(70, 255, 140, .23);

    background-size: cover !important;

    background-position: center !important;

    box-shadow:
        0 25px 65px rgba(0, 0, 0, .35);

    transition:
        transform .25s ease,
        border-color .25s ease,
        box-shadow .25s ease;
}

.future-card:hover {
    transform: translateY(-7px);

    border-color: rgba(70, 255, 140, .55);

    box-shadow:
        0 30px 80px rgba(0, 255, 128, .10);
}


/* brilho no topo dos cards */

.future-card::before {
    content: "";

    position: absolute;

    top: 0;
    left: 0;
    right: 0;

    height: 1px;

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(75, 255, 145, .8),
            transparent
        );
}


.card-content {
    position: relative;

    z-index: 2;
}


.card-icon {
    display: flex;

    align-items: center;
    justify-content: center;

    width: 55px;
    height: 55px;

    margin-bottom: 22px;

    border-radius: 16px;

    font-size: 1.55rem;

    background: rgba(1, 15, 9, .72);

    border: 1px solid rgba(72, 255, 142, .28);

    backdrop-filter: blur(10px);
}

.future-card h3 {
    color: white;

    margin-bottom: 18px;

    font-size: 1.45rem;

    font-weight: 750;

    text-shadow:
        0 3px 15px rgba(0, 0, 0, .95);
}

.future-card p {
    color: #f0fff5;

    margin: 10px 0;

    line-height: 1.55;

    text-shadow:
        0 2px 12px rgba(0, 0, 0, 1);
}

.check {
    color: #4df58c;

    font-weight: 900;

    margin-right: 5px;
}

.status {
    display: inline-block;

    margin-top: 18px;

    padding: 8px 12px;

    border-radius: 999px;

    color: #ffe080;

    font-size: .78rem;

    background: rgba(4, 15, 9, .70);

    border: 1px solid rgba(255, 205, 72, .32);

    backdrop-filter: blur(8px);
}


/* ========================================================
   MISSÃO
======================================================== */

.mission {
    margin-top: 45px;

    padding: 28px;

    border-radius: 22px;

    text-align: center;

    color: #b7d9c5;

    line-height: 1.7;

    border: 1px solid rgba(70, 255, 140, .16);

    background:
        linear-gradient(
            90deg,
            rgba(10, 50, 31, .35),
            rgba(4, 22, 14, .25)
        );
}

.mission strong {
    color: #51f58d;
}


/* ========================================================
   FOOTER
======================================================== */

.custom-footer {
    margin-top: 55px;

    padding-top: 25px;

    border-top: 1px solid rgba(70, 255, 140, .09);

    color: #657d71;

    text-align: center;

    font-size: .80rem;
}


/* ========================================================
   CELULAR
======================================================== */

@media (max-width: 800px) {

    .nav-links {
        display: none;
    }

    .logo {
        width: 70px;
        height: 70px;
    }

    .hero {
        padding: 50px 28px;

        min-height: 500px;
    }

    .hero::before {
        opacity: .35;

        right: -180px;
    }

    .hero::after {
        opacity: .30;

        right: -100px;
    }

    .section-title {
        font-size: 2rem;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# CABEÇALHO
# =========================================================

st.markdown(
    f"""
    <div class="navbar">

        <div class="brand">

            <img
                class="logo"
                src="data:image/png;base64,{logo}"
            >

            <div>

                <div class="brand-title">
                    Vig<span>IA</span> Goiás
                </div>

                <div class="brand-subtitle">
                    TECNOLOGIA E INTELIGÊNCIA A SERVIÇO DA COMUNIDADE
                </div>

            </div>

        </div>

        <div class="nav-links">
            INÍCIO PROJETO TECNOLOGIA
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HERO
# =========================================================

st.markdown(
    """
    <div class="hero">

        <div class="hero-content">

            <div class="eyebrow">
                VISÃO COMPUTACIONAL • VIGILÂNCIA AMBIENTAL
            </div>

            <h1>
                Tecnologia para um
                <br>
                <span>ambiente mais seguro.</span>
            </h1>

            <div class="hero-description">

                O VigIA Goiás utiliza Inteligência Artificial para
                reconhecer elementos presentes no ambiente e apoiar
                a identificação de condições relevantes à vigilância
                ambiental e em saúde.

            </div>

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
    """,
    unsafe_allow_html=True
)


# =========================================================
# ANÁLISE
# =========================================================

st.markdown(
    """
    <div class="section">

        <div class="section-label">
            ANÁLISE INTELIGENTE
        </div>

        <div class="section-title">
            Analise uma imagem do ambiente
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


col_info, col_upload = st.columns(
    [0.8, 1.2],
    gap="large"
)


with col_info:

    st.markdown(
        """
        <div class="analysis-info">

            <div class="analysis-icon">
                📷
            </div>

            <h3>
                Analisar ambiente
            </h3>

            <p>
                Envie uma fotografia para que o VigIA possa
                identificar elementos e condições ambientais
                relevantes.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


with col_upload:

    imagem_enviada = st.file_uploader(
        "Enviar imagem",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed"
    )


if imagem_enviada is not None:

    st.image(
        imagem_enviada,
        caption="Imagem enviada para análise",
        use_container_width=True
    )

    analisar = st.button(
        "✦ Iniciar análise com o VigIA",
        use_container_width=True
    )

    if analisar:

        st.info(
            "A interface está pronta. "
            "O modelo de Inteligência Artificial será conectado "
            "após a conclusão do treinamento."
        )


# =========================================================
# MÓDULOS
# =========================================================

st.markdown(
    """
    <div class="section">

        <div class="section-label">
            MÓDULOS DO SISTEMA
        </div>

        <div class="section-title">
            O que o VigIA identifica?
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


card1, card2, card3 = st.columns(
    3,
    gap="large"
)


# =========================================================
# CARD 1
# =========================================================

with card1:

    st.markdown(
        f"""
        <div
            class="future-card"
            style="
                background-image:
                    linear-gradient(
                        180deg,
                        rgba(0, 8, 5, .15) 0%,
                        rgba(0, 10, 6, .55) 45%,
                        rgba(0, 8, 5, .96) 100%
                    ),
                    url('data:image/jpeg;base64,{foto_cidade}');
            "
        >

            <div class="card-content">

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

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# CARD 2
# =========================================================

with card2:

    st.markdown(
        f"""
        <div
            class="future-card"
            style="
                background-image:
                    linear-gradient(
                        180deg,
                        rgba(0, 8, 5, .12) 0%,
                        rgba(0, 10, 6, .48) 45%,
                        rgba(0, 8, 5, .96) 100%
                    ),
                    url('data:image/jpeg;base64,{foto_natureza}');
            "
        >

            <div class="card-content">

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

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# CARD 3
# =========================================================

with card3:

    st.markdown(
        f"""
        <div
            class="future-card"
            style="
                background-image:
                    linear-gradient(
                        180deg,
                        rgba(0, 8, 5, .14) 0%,
                        rgba(0, 10, 6, .55) 45%,
                        rgba(0, 8, 5, .97) 100%
                    ),
                    url('data:image/jpeg;base64,{foto_cidade}');
            "
        >

            <div class="card-content">

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
                    ● EM DESENVOLVIMENTO
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# MISSÃO
# =========================================================

st.markdown(
    """
    <div class="mission">

        <strong>VigIA Goiás</strong>
        — tecnologia, Inteligência Artificial e dados ambientais
        para apoiar ambientes mais seguros, saudáveis e monitorados.

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# RODAPÉ
# =========================================================

st.markdown(
    """
    <div class="custom-footer">

        VigIA Goiás •
        Inteligência Artificial aplicada à vigilância ambiental

    </div>
    """,
    unsafe_allow_html=True
)
