import streamlit as st

st.set_page_config(
    page_title="VigIA Goiás",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================
# ESTILO
# =========================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 85% 10%, rgba(0,255,140,.10), transparent 25%),
        linear-gradient(135deg, #020807 0%, #04110c 50%, #020706 100%);
    color: white;
}

.block-container {
    max-width: 1300px;
    padding-top: 1.2rem;
    padding-bottom: 3rem;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {background: transparent !important;}

h1, h2, h3 {
    color: white !important;
}

.hero-box {
    background:
        radial-gradient(circle at 80% 45%, rgba(0,255,130,.14), transparent 20%),
        linear-gradient(120deg, rgba(3,18,12,.98), rgba(2,10,7,.92));
    border: 1px solid rgba(80,255,145,.18);
    border-radius: 28px;
    padding: 3rem;
    box-shadow: 0 20px 70px rgba(0,0,0,.35);
}

.glow {
    color: #50f58c;
}

.small-label {
    color: #48f58e;
    letter-spacing: .14em;
    font-size: .75rem;
    font-weight: 800;
}

.card {
    background: linear-gradient(
        145deg,
        rgba(8,29,20,.90),
        rgba(3,15,10,.88)
    );
    border: 1px solid rgba(70,255,140,.18);
    border-radius: 22px;
    padding: 1.4rem;
    min-height: 280px;
    box-shadow: 0 18px 55px rgba(0,0,0,.25);
}

.card:hover {
    border-color: rgba(70,255,140,.4);
}

div[data-testid="stFileUploader"] {
    background: rgba(7,25,18,.72);
    border: 1px dashed rgba(72,255,140,.35);
    border-radius: 18px;
    padding: 1rem;
}

div[data-testid="stFileUploader"] button {
    background: linear-gradient(90deg, #0b7b43, #20d76e) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
}

div.stButton > button {
    width: 100%;
    border-radius: 12px;
    background: linear-gradient(90deg, #0a7b42, #22d96d);
    color: white;
    border: none;
    font-weight: 700;
}

hr {
    border-color: rgba(70,255,140,.10);
}

</style>
""", unsafe_allow_html=True)

# =========================
# TOPO
# =========================

top1, top2 = st.columns([1, 5])

with top1:
    st.image("Logo Vigia Goias.png", width=95)

with top2:
    st.markdown("## VigIA Goiás")
    st.caption("Inteligência Artificial • Vigilância Ambiental")

st.divider()

# =========================
# HERO
# =========================

st.markdown('<div class="hero-box">', unsafe_allow_html=True)

st.markdown('<div class="small-label">VISÃO COMPUTACIONAL • VIGILÂNCIA AMBIENTAL</div>', unsafe_allow_html=True)

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
    st.success("✦ Inteligência Artificial")

with p2:
    st.success("◉ Dados ambientais")

with p3:
    st.success("⌁ Visão computacional")

st.markdown('</div>', unsafe_allow_html=True)

# =========================
# ANÁLISE
# =========================

st.markdown("### ANÁLISE INTELIGENTE")
st.header("Analise uma imagem do ambiente")

col1, col2 = st.columns([1, 1.4], gap="large")

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📷 Analisar ambiente")
    st.write(
        """
        Envie uma fotografia para que o VigIA possa identificar
        elementos e condições ambientais relevantes.
        """
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
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

    if st.button("✦ Iniciar análise com o VigIA"):
        st.info(
            "O modelo de Inteligência Artificial será conectado "
            "após a conclusão do treinamento."
        )

# =========================
# MÓDULOS
# =========================

st.markdown("### MÓDULOS DO SISTEMA")
st.header("O que o VigIA identifica?")

c1, c2, c3 = st.columns(3, gap="large")

with c1:
    st.image("Foto Cidade Goiania.jpg", use_container_width=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("♻️ Recipientes e resíduos")
    st.write("✓ Pneus")
    st.write("✓ Baldes")
    st.write("✓ Garrafas plásticas")
    st.write("✓ Latas")
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.image("Foto Natureza 1.jpg", use_container_width=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🌱 Condições ambientais")
    st.write("✓ Vegetação")
    st.write("✓ Água parada")
    st.write("✓ Matéria orgânica")
    st.markdown('</div>', unsafe_allow_html=True)

with c3:
    st.image("Foto Cidade Goiania.jpg", use_container_width=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🏙️ Estrutura urbana")
    st.write(
        """
        Futuro módulo de análise de infraestrutura,
        saneamento e condições urbanas.
        """
    )
    st.warning("Em desenvolvimento")
    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# FINAL
# =========================

st.divider()

st.success(
    "VigIA Goiás — tecnologia, Inteligência Artificial e dados "
    "ambientais para apoiar ambientes mais seguros e monitorados."
)

st.caption(
    "VigIA Goiás • Inteligência Artificial aplicada à vigilância ambiental"
)
