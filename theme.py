import streamlit as st


def load_theme():

    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    *{
        font-family:'Inter',sans-serif;
    }

    /* --------------------------
       Hide Streamlit Default UI
    ---------------------------*/

    #MainMenu{
        visibility:hidden;
    }

    header{
        visibility:hidden;
    }

    footer{
        visibility:hidden;
    }

    /* --------------------------
       Background
    ---------------------------*/

    .stApp{

        background:
        linear-gradient(
        180deg,
        #FFFFFF 0%,
        #F8F5FF 40%,
        #EEF5FF 100%
        );

        color:#1F2937;

    }

    /* --------------------------
       Sidebar
    ---------------------------*/

    section[data-testid="stSidebar"]{

        background:#FFFFFF;

        border-right:1px solid #ECECEC;

    }

    section[data-testid="stSidebar"] *{

        color:#1F2937;

    }

    /* --------------------------
       Buttons
    ---------------------------*/

    .stButton>button{

        width:100%;

        height:56px;

        border-radius:16px;

        border:none;

        font-size:16px;

        font-weight:600;

        color:white;

        background:
        linear-gradient(
        90deg,
        #7C4DFF,
        #9F7AEA
        );

        transition:.3s;

        box-shadow:
        0 10px 20px
        rgba(124,77,255,.25);

    }

    .stButton>button:hover{

        transform:translateY(-3px);

        box-shadow:
        0 15px 30px
        rgba(124,77,255,.35);

    }

    /* --------------------------
       Text Input
    ---------------------------*/

    .stTextInput input{

        border-radius:15px;

        border:1px solid #E5E7EB;

        padding:12px;

    }

    .stTextArea textarea{

        border-radius:15px;

        border:1px solid #E5E7EB;

        padding:12px;

    }

    /* --------------------------
       Cards
    ---------------------------*/

    .card{

        background:white;

        border-radius:22px;

        padding:32px;

        border:1px solid #ECECEC;

        box-shadow:
        0 12px 35px
        rgba(0,0,0,.05);

        transition:.3s;

        margin-bottom:25px;

    }

    .card:hover{

        transform:translateY(-5px);

        box-shadow:
        0 20px 45px
        rgba(124,77,255,.15);

    }

    /* --------------------------
       Hero
    ---------------------------*/

    .hero{

        background:
        linear-gradient(
        135deg,
        #FFFFFF,
        #F5F0FF,
        #EEF6FF
        );

        padding:60px;

        border-radius:28px;

        border:1px solid #ECECEC;

        box-shadow:
        0 20px 50px
        rgba(0,0,0,.06);

        margin-bottom:35px;

    }

    .hero-badge{

        display:inline-block;

        padding:8px 20px;

        background:#EEE8FF;

        color:#6D4AFF;

        border-radius:30px;

        font-size:14px;

        font-weight:600;

        margin-bottom:25px;

    }

    .hero-title{

        font-size:60px;

        font-weight:800;

        color:#1F2937;

        line-height:1.15;

    }

    .gradient{

        color:#7C4DFF;

    }

    .hero-desc{

        margin-top:25px;

        color:#64748B;

        font-size:20px;

        line-height:1.8;

    }

    /* --------------------------
       Section Title
    ---------------------------*/

    .section-title{

        font-size:36px;

        font-weight:700;

        color:#1F2937;

        margin-top:20px;

        margin-bottom:25px;

    }

    /* --------------------------
       Recommendation Card
    ---------------------------*/

    .recommend-card{

        background:white;

        border-radius:20px;

        padding:28px;

        border:1px solid #ECECEC;

        box-shadow:
        0 10px 30px
        rgba(0,0,0,.05);

        margin-bottom:25px;

    }

    /* --------------------------
       Prompt Card
    ---------------------------*/

    .prompt-card{

        background:white;

        border-radius:20px;

        border:1px solid #ECECEC;

        padding:30px;

        box-shadow:
        0 10px 30px
        rgba(0,0,0,.05);

    }

    /* --------------------------
       Footer
    ---------------------------*/

    .footer{

        text-align:center;

        color:#64748B;

        padding:40px;

        margin-top:60px;

    }

    </style>
    """, unsafe_allow_html=True)