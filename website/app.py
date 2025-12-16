import streamlit as st
import re
import os

st.set_page_config(page_title="RadFest", layout="wide")

st.markdown(
    """
    <style>
    /* Kill all Streamlit background surfaces */
    html, body {
        background: transparent !important;
    }

    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    section.main,
    .stApp,
    .block-container,
    [data-testid="stHeader"],
    [data-testid="stToolbar"],
    [data-testid="stSidebar"] {
        background: transparent !important;
        box-shadow: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <style>
    body {
        background-image: url("img/RadFest.png");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# CSS: black background, section panels, and RadFest gradient for header text (from poster)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #fffafa !important;
    }
    .rainbow-panel-a { background: #ff5555; color: #fff !important; border-radius: 24px; padding: 22px 20px 16px 20px; margin-bottom: 32px; }
    .rainbow-panel-b { background: #ffc93c; color: #222 !important; border-radius: 24px; padding: 22px 20px 16px 20px; margin-bottom: 32px; }
    .rainbow-panel-c { background: #59e470; color: #222 !important; border-radius: 24px; padding: 22px 20px 16px 20px; margin-bottom: 32px; }
    .rainbow-panel-d { background: #52b8ff; color: #fff !important; border-radius: 24px; padding: 22px 20px 16px 20px; margin-bottom: 32px; }
    .rainbow-panel-e { background: #be6cff; color: #fff !important; border-radius: 24px; padding: 22px 20px 16px 20px; margin-bottom: 32px; }
    .rainbow-header-text {
        background: linear-gradient(90deg,
            #F8E877, /* yellow */
            #FFD89A, /* peach */
            #B8F6DB, /* mint */
            #74DDF8, /* sky blue */
            #EF933B, /* orange */
            #B887F4, /* lilac */
            #F7A6D1 /* pink */
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-fill-color: transparent;
        font-weight: bold;
        display: inline;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title (in a rainbow panel)
st.markdown('<h1 class="rainbow-header-text">Welcome to RadFest 2025</h1>', unsafe_allow_html=True)

# Media section

cols = st.columns(3)
with cols[0]:
    st.image("img/RadFest.png", caption="", width="content")

with cols[1]:
    st.video('img/placeholder.mov')
with cols[2]:
    st.image("img/three-ottters-map.jpg", caption="", width="content")
st.markdown('</div>', unsafe_allow_html=True)

# FAQ section
st.markdown('<h2 class="rainbow-header-text">FAQ</h2>', unsafe_allow_html=True)
fname = "README.md"
faq_pairs = []

if os.path.exists(fname):
    with open(fname, encoding="utf8") as f:
        in_faq = False
        for line in f:
            if line.strip().startswith('# FAQ'):
                in_faq = True
                continue
            if in_faq:
                if line.strip() == '':
                    continue
                if line.strip().startswith('#'):
                    break
                m = re.match(r'([^\t]+)\t(.+)', line)
                if m:
                    faq_pairs.append((m.group(1).strip(), m.group(2).strip()))

if not faq_pairs:
    st.info("FAQ will appear here soon! (No FAQ found in README.md)")
else:
    # Force black text
    st.markdown(
        """
        <style>
        .faq-text {
            color: black;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    for q, a in faq_pairs:
        with st.expander(q):
            st.markdown(
                f"<div class='faq-text'>{a}</div>",
                unsafe_allow_html=True
            )

# Registration section
st.markdown('<h2 class="rainbow-header-text">Registration</h2>', unsafe_allow_html=True)
st.warning("[Google Form Placeholder](https://docs.google.com/forms/d/1oCohTVmY_oEt6WpDcsgOVQ9-6TnGATQFt_1t_rPc_Yk/edit)")
st.markdown('</div>', unsafe_allow_html=True)

# Music section
st.markdown('<h2 class="rainbow-header-text">Featured Music</h2>', unsafe_allow_html=True)
st.components.v1.iframe(
    "https://w.soundcloud.com/player/?url=https%3A//soundcloud.com/vintagegold123&color=%23ff5500&auto_play=false",
    height=120,
)
st.markdown('</div>', unsafe_allow_html=True)
