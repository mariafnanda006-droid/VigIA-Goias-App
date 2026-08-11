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
# IMAGENS
# =========================================================

def b64(caminho):
    arquivo = Path(caminho)

    if not arquivo.exists():
        return ""

    return base64.b64encode(
        arquivo.read_bytes()
    ).decode("utf-8")


logo_b64 = b64("Logo Vigia Goias.png")
cidade_b64 = b64("Foto Cidade Goiania.jpg")
natureza_b64 = b64("Foto Natureza 1.jpg")


# =========================================================
# CSS
# =========================================================

st.markdown(
    f"""
<style>

* {{
    box-sizing: border-box;
}}

.stApp {{
    background:
        radial-gradient(circle at 85% 7%, rgba(0,255,130,.11), transparent 24%),
        radial-gradient(circle at 7% 88%, rgba(0,190,120,.08), transparent 26%),
        #010806;
    color: white;
}}

.block-container {{
    max-width: 1450px;
    padding-top: 1rem;
    padding-bottom: 3rem;
}}

#MainMenu {{
    visibility: hidden;
}}

footer {{
    visibility: hidden;
}}

header {{
    background: transparent !important;
}}


/* ======================================================
   TOPO
====================================================== */

.st-key-topo {{
    border: 1px solid rgba(56,255,140,.20) !important;
    border-radius: 28px !important;
    padding: 10px 22px !important;

    background:
        rgba(2,18,12,.88);

    box-shadow:
        0 18px 70px rgba(0,0,0,.26);
}}

.st-key-topo img {{
    filter:
        drop-shadow(0 0 20px rgba(51,255,139,.18));
}}


/* ======================================================
   HERO
====================================================== */

.st-key-hero {{
    margin-top: 22px;

    border: 1px solid rgba(64,255,141,.22) !important;

    border-radius: 30px !important;

    padding:
        60px 55px !important;

    background:
        radial-gradient(
            circle at 80% 45%,
            rgba(0,255,130,.15),
            transparent 22%
        ),
        linear-gradient(
            120deg,
            rgba(2,20,13,.97),
            rgba(1,10,7,.96)
        );

    box-shadow:
        0 30px 100px rgba(0,0,0,.42);
}}

.st-key-hero h1 {{
    font-size: clamp(3.2rem, 5vw, 5.2rem) !important;

    line-height: 1.00 !important;

    letter-spacing: -.055em !important;

    color: white !important;

    margin-bottom: 24px !important;
}}

.st-key-hero h3 {{
    color: #41f58a !important;

    font-size: .80rem !important;

    letter-spacing: .17em !important;
}}

.st-key-hero p {{
    color: #b2c7bb !important;

    font-size: 1.05rem !important;

    line-height: 1.75 !important;
}}

.st-key-hero img {{
    max-height: 430px;

    object-fit: contain;

    filter:
        drop-shadow(0 0 38px rgba(55,255,135,.18));
}}


/* ======================================================
   PILLS
====================================================== */

.st-key-pill1,
.st-key-pill2,
.st-key-pill3 {{
    border: 1px solid rgba(72,255,143,.25) !important;

    border-radius: 999px !important;

    background:
        rgba(7,44,26,.45);

    padding:
        3px 10px !important;
}}

.st-key-pill1 p,
.st-key-pill2 p,
.st-key-pill3 p {{
    color: #caffdc !important;

    font-size: .82rem !important;
}}


/* ======================================================
   TÍTULOS DAS SEÇÕES
====================================================== */

.section-label {{
    color: #45f58a;

    font-size: .75rem;

    font-weight: 800;

    letter-spacing: .18em;

    margin-top: 65px;

    margin-bottom: 4px;
}}

.section-title {{
    color: white;

    font-size: 2.5rem;

    font-weight: 800;

    letter-spacing: -.045em;

    margin-bottom: 24px;
}}


/* ======================================================
   PAINEL DE ANÁLISE
====================================================== */

.st-key-analise {{
    padding: 25px !important;

    border-radius: 26px !important;

    border:
        1px solid rgba(55,255,140,.26) !important;

    background:
        linear-gradient(
            140deg,
            rgba(4,31,21,.88),
            rgba(1,18,12,.94)
        );

    box-shadow:
        0 25px 75px rgba(0,0,0,.30);
}}

.st-key-analise h2 {{
    color: white !important;
}}

.st-key-analise p {{
    color: #a7bdb1 !important;
}}


/* Upload */

div[data-testid="stFileUploader"] {{
    min-height: 210px;

    display: flex;

    align-items: center;

    border-radius: 20px;

    border:
        1px dashed rgba(57,255,141,.48);

    background:
        rgba(1,16,10,.62);

    padding: 18px;
}}

div[data-testid="stFileUploader"] section {{
    background: transparent !important;
}}

div[data-testid="stFileUploader"] button {{
    background:
        linear-gradient(
            90deg,
            #087842,
            #20da70
        ) !important;

    color: white !important;

    border: none !important;

    border-radius: 12px !important;
}}


/* ======================================================
   CARDS
====================================================== */

.st-key-card-residuos,
.st-key-card-ambiente,
.st-key-card-urbano {{
    min-height: 410px;

    border-radius: 25px !important;

    padding: 28px !important;

    border:
        1px solid rgba(67,255,143,.28) !important;

    box-shadow:
        0 25px 70px rgba(0,0,0,.38);

    overflow: hidden;

    transition:
        transform .25s ease,
        border-color .25s ease;
}}


.st-key-card-residuos {{
    background:
        linear-gradient(
            180deg,
            rgba(1,10,6,.18),
            rgba(1,10,6,.65) 45%,
            rgba(1,8,5,.97) 100%
        ),
        url("data:image/jpeg;base64,{cidade_b64}");

    background-size: cover;

    background-position: center;
}}


.st-key-card-ambiente {{
    background:
        linear-gradient(
            180deg,
            rgba(1,10,6,.12),
            rgba(1,10,6,.58) 45%,
            rgba(1,8,5,.97) 100%
        ),
        url("data:image/jpeg;base64,{natureza_b64}");

    background-size: cover;

    background-position: center;
}}


.st-key-card-urbano {{
    background:
        linear-gradient(
            180deg,
            rgba(1,10,6,.14),
            rgba(1,10,6,.60) 45%,
            rgba(1,8,5,.97) 100%
        ),
        url("data:image/jpeg;base64,{cidade_b64}");

    background-size: cover;

    background-position: center;
}}


.st-key-card-residuos:hover,
.st-key-card-ambiente:hover,
.st-key-card-urbano:hover {{
    transform: translateY(-6px);

    border-color:
        rgba(68,255,143,.60) !important;
}}


.st-key-card-residuos h2,
.st-key-card-ambiente h2,
.st-key-card-urbano h2 {{
    color: white !important;

    text-shadow:
        0 3px 14px rgba(0,0,0,.95);
}}


.st-key-card-residuos p,
.st-key-card-ambiente p,
.st-key-card-urbano p {{
    color: #f2fff7 !important;

    text-shadow:
        0 2px 12px rgba(0,0,0,1);
}}


/* ======================================================
   MISSÃO
====================================================== */

.st-key-missao {{
    margin-top: 35px;

    padding: 20px 28px !important;

    border-radius: 22px !important;

    border:
        1px solid rgba(65,255,141,.22) !important;

    background:
        linear-gradient(
            90deg,
            rgba(4,45,28,.50),
            rgba(1,20,13,.66)
        );
}}

.st-key-missao p {{
    text-align: center;

    color: #c3dfcf !important;
}}


/* ======================================================
   BOTÕES
====================================================== */

div.stButton > button {{
    width: 100%;

    border-radius: 13px;

    background:
        linear-gradient(
            90deg,
            #087841,
            #22db70
        );

    color: white;

    border:
        1px solid rgba(80,255,150,.35);

    font-weight: 700;
}}


/* ======================================================
   MOBILE
====================================================== */

@media(max-width: 800px) {{

    .st-key-hero {{
        padding:
            35px 25px !important;
    }}

    .st-key-hero h1 {{
        font-size:
            3rem !important;
    }}

}}

</style>
""",
    unsafe_allow_html=True
)


# =========================================================
# TOPO
# =========================================================

with st.container(
    key="topo",
    border=True
):

    logo_col, menu_col = st.columns(
        [1.2, 4],
        vertical_alignment="center"
    )

    with logo_col:

        st.image(
            "Logo Vigia Goias.png",
            width=190
        )

    with menu_col:

        m1, m2, m3, m4 = st.columns(4)

        with m1:
            st.markdown("**⌂ Início**")

        with m2:
            st.markdown("Sobre o projeto")

        with m3:
            st.markdown("Como funciona")

        with m4:
            st.markdown("Tecnologias")


# =========================================================
# HERO
# =========================================================

with st.container(
    key="hero",
    border=True
):

    texto, identidade = st.columns(
        [1.15, .85],
        gap="large",
        vertical_alignment="center"
    )

    with texto:

        st.markdown(
            "### VISÃO COMPUTACIONAL • VIGILÂNCIA AMBIENTAL"
        )

        st.markdown(
            """
# Tecnologia para um
# :green[ambiente mais seguro.]
"""
        )

        st.write(
            """
O VigIA Goiás utiliza Inteligência Artificial para reconhecer
elementos presentes no ambiente e apoiar a identificação de
condições relevantes à vigilância ambiental e em saúde.
"""
        )

        p1, p2, p3 = st.columns(3)

        with p1:

            with st.container(
                key="pill1",
                border=True
            ):

                st.write(
                    "✦ Inteligência Artificial"
                )

        with p2:

            with st.container(
                key="pill2",
                border=True
            ):

                st.write(
                    "◉ Dados ambientais"
                )

        with p3:

            with st.container(
                key="pill3",
                border=True
            ):

                st.write(
                    "⌁ Visão computacional"
                )

    with identidade:

        st.image(
            "Logo Vigia Goias.png",
            use_container_width=True
        )


# =========================================================
# ANÁLISE
# =========================================================

st.markdown(
    '<div class="section-label">ANÁLISE INTELIGENTE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">Analise uma imagem do ambiente</div>',
    unsafe_allow_html=True
)


with st.container(
    key="analise",
    border=True
):

    info, upload = st.columns(
        [1, 1.3],
        gap="large",
        vertical_alignment="center"
    )

    with info:

        st.header(
            "▣ Analisar ambiente"
        )

        st.write(
            """
Envie uma fotografia para que o VigIA possa identificar
elementos e condições ambientais relevantes.
"""
        )

    with upload:

        imagem = st.file_uploader(
            "Selecione uma imagem",
            type=[
                "jpg",
                "jpeg",
                "png"
            ],
            label_visibility="collapsed"
        )


if imagem is not None:

    st.image(
        imagem,
        caption="Imagem enviada",
        use_container_width=True
    )

    if st.button(
        "✦ Iniciar análise com o VigIA",
        use_container_width=True
    ):

        st.info(
            "A interface está pronta para receber "
            "o modelo treinado do VigIA."
        )


# =========================================================
# CARDS
# =========================================================

st.markdown(
    '<div class="section-label">MÓDULOS DO SISTEMA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">O que o VigIA identifica?</div>',
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns(
    3,
    gap="large"
)


with col1:

    with st.container(
        key="card-residuos",
        border=True
    ):

        st.header(
            "♻ Recipientes e resíduos"
        )

        st.write(
            "✅ Pneus"
        )

        st.write(
            "✅ Baldes"
        )

        st.write(
            "✅ Garrafas plásticas"
        )

        st.write(
            "✅ Latas"
        )


with col2:

    with st.container(
        key="card-ambiente",
        border=True
    ):

        st.header(
            "🌱 Condições ambientais"
        )

        st.write(
            "✅ Vegetação"
        )

        st.write(
            "✅ Água parada"
        )

        st.write(
            "✅ Matéria orgânica"
        )


with col3:

    with st.container(
        key="card-urbano",
        border=True
    ):

        st.header(
            "🏙 Estrutura urbana"
        )

        st.write(
            """
Futuro módulo de análise de infraestrutura,
saneamento e condições urbanas.
"""
        )

        st.warning(
            "● Em desenvolvimento"
        )


# =========================================================
# MISSÃO
# =========================================================

with st.container(
    key="missao",
    border=True
):

    st.write(
        """
🛡️ **Nosso objetivo é apoiar a vigilância em saúde**
e promover ambientes mais seguros e saudáveis para todos.
"""
    )


# =========================================================
# RODAPÉ
# =========================================================

st.markdown("---")

st.caption(
    "🌿 VigIA Goiás • Tecnologia, ciência e meio ambiente"
)
