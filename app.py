"""
✨ A Universe of Us ✨
A birthday surprise website built with Streamlit.

HOW TO RUN:
    pip install -r requirements.txt
    streamlit run app.py

Then open the local network URL on her phone (see README.md for details).
"""

import os
import random
import streamlit as st

# ============================================================
#  1. EDIT THIS SECTION — make it yours!
# ============================================================

GIRLFRIEND_NAME = "Dhivya!💖"          # her name
YOUR_NAME = "Ezhil"                  # your name (signs the letter)
SITE_TITLE = "A Universe of Us my love"   # site theme title
TAGLINE = "32 planets, one galaxy, and it's all because of you."

# Theme colors (hex). Try: pink/lavender, sunset orange, or ocean teal.
PRIMARY_COLOR = "#ce4257"     # headings, buttons
SECONDARY_COLOR = "#ce4257"   # accents, gradient
BG_TOP = "#74c69d"            # background gradient top
BG_BOTTOM = "#d8f3dc"         # background gradient bottom

# "Our Story" section
OUR_STORY_TITLE = "How It All Started ✨"
OUR_STORY_TEXT = """
One fine day, almost 15 years munnadi... Namma 6th standard
padikum  pothu, Gomathi  miss tution  la start aanathu.....
apotha na antha tution eh  join pannen... Na paatuku chumma
ukanthu irunthen... appo retta jedai potutu, poo vachitu...
Vidhya mandhir school dress la ne vantha...  na apotha unna
first time pakuren, paathathum enakula butterfly parakuthu,
kai kaal ellam nadunguthu... etho oru maari aagiduchu enaku
enanu solla therila, but enaku romba  pudichiruchu ethanala 
nu kuda therila enaku,  romba azhaga iruntha ne apo enakula
etho etho  solluchi iva  tha da  unaku nu thonuchu... enaku
apovey antha sec eh  thoniduchu ne tha en life la kuda vara
pora nu, apo enaku athu love nu kuda theriyala nejama enaku
apo ethumey therila love  na ennanu  theriyathu aana apovey
enaku nee tha nu thonuchu, aana na romba happy aagiten unna
paathathum... aprm ne vanthu en  front la ukantha na unnaye
tha paathutu irunthen enaku unkita ehtachu peasanum nu aasa
vanthuduchu  de... aprm  epadiyo  manasula  thairiyam  vara
vachitu peasalam nu try pannen aana enaku bayam peasala....
aprm again peasa try panen, intha time epdiyachu peasidanum
nu mudivu panni 'Hello' nu kupten ne thirumbala aprm  again
kupten ne thirumbi paatha... aiyo na apoveyy  flat  aagiten
enada iva ivalo azhaga iruka nu manasu solluthu, aprm scale
iruka nu keten short scale the iruku paravalaya nu ne ketta,
na ok nu solliten... aana unmaiyalumey short scale na enanu
kuda therila enaku na dabukunu ok solliten... ne kudutha na
suma kodu podra mari apdiye vachitu irunthen thirupi kuduka
manase varala aprm romba neram kalichi thirupi kuduklana ne
aprm enkita peasa matiyo nu thonuchu athanala hello nu unna
kupten... ne  athey mari  thirumbuna paahhh unnaye paathutu
irunthen Thanks nu solli kuduthen.. Ne its ok nu sonna aprm
apdiye unna sight adichitey irunthen.. unnaye tha  paathutu
irupen ne enna paakura apo la na unnaye tha paathutu irupen
romba  azhagana day anaiku  aana enaku date  tha correct ah
theriyala de sorry! antha day en life la ennaikumey marakave
maten...

That's where our love begins!!!💖💖💖"""

# Memory timeline captions — one per photo (edit all 30!)
# Photos should be placed in the /photos folder, named 1.jpg, 2.jpg ... 30.jpg
# (jpg, jpeg or png all work)
MEMORY_CAPTIONS = [
    "Ezhil & Dhivya💕 Forever",
    "Happiieee Birthday de Kunjiii💕",
] +  [f"Your Beautiful images My love 💕" for i in range(1, 42)]

# Couples quiz — only she should know these answers!
QUIZ = [
    {
        "question": "Namma entha standard padikirapo na unaku propose panna? ",
        "options": ["8", "9", "10", "11"],
        "answer": 1,
    },
    {
        "question": "Neeyu naanu first enga thaniya meet pannom??",
        "options": ["Pattanam", "Namakkal", "Mohanur", "Rasipuram"],
        "answer": 2,
    },
    {
        "question": "Namma entha kovil ku 1st ponom???",
        "options": ["Narasimmar Kovil", "Anjaneyar Kovil", "Malai Kottai"],
        "answer": 1,
    },
    {
        "question": "2025 la na ooruku vanthapo ethana days namma meet pannom?",
        "options": ["8", "10", "13", "15"],
        "answer": 3,  # index of correct option
    },
    {
        "question": "Maruthamalai Kovil la namma enna prasadham saptom???",
        "options": ["Lemon rice", "Puliyotharai", "Thakkali Sadham", "Thayir Sadham"],
        "answer": 1,
    },
{
        "question": "Sorry thango neriya questions kekalam nu irunthen time kammiya iruku de kunjiii sorryyy babe💕"
    },
]

# "Reasons I love you" generator — add as many as you like
#REASONS = [
 #   "Pudichiruku atha reason"
#]

# Final letter
FINAL_LETTER = f"""
Dear {GIRLFRIEND_NAME},

Write your closing message here. This is the big one — say the thing
you actually want her to remember from today.

Happy Birthday. I love you.

— {YOUR_NAME}
"""

# ---------- Login screen ----------
# These are the fallback credentials used when running locally.
# For hosted deployments, set these in .streamlit/secrets.toml instead
# (see README) so the real password isn't sitting in app.py / GitHub.
APP_USERNAME = "dhivya"
APP_PASSWORD = "24"

LOGIN_TITLE = "For You Ammuuu💌"
LOGIN_SUBTITLE = "This one's just between us. Enter the details to unlock it."

# ============================================================
#  2. APP CODE — no need to edit below unless you want to
# ============================================================

st.set_page_config(
    page_title=SITE_TITLE,
    page_icon="💖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ---------- Styling ----------
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Quicksand:wght@400;600;700&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Quicksand', sans-serif;
    }}

    .stApp {{
        background: linear-gradient(160deg, {BG_TOP} 0%, {BG_BOTTOM} 100%);
    }}

    h1, h2, h3, .headline {{
        font-family: 'Pacifico', cursive;
        color: {PRIMARY_COLOR};
    }}

    .subtitle {{
        text-align: center;
        color: #081c15;
        font-size: 1.05rem;
        margin-top: -0.5rem;
    }}

    .card {{
        background: rgba(255, 255, 255, 0.75);
        color: #081c15;
        border-radius: 20px;
        padding: 1.3rem 1.5rem;
        box-shadow: 0 8px 24px rgba(180, 120, 180, 0.15);
        margin-bottom: 1rem;
    }}

    div.stButton > button {{
        background: linear-gradient(135deg, {PRIMARY_COLOR}, {SECONDARY_COLOR});
        color: white;
        border: none;
        border-radius: 999px;
        padding: 0.55rem 1.4rem;
        font-weight: 600;
        width: 100%;
        transition: transform 0.15s ease;
    }}
    div.stButton > button:hover {{
        transform: scale(1.03);
        color: white;
    }}

    .progress-label {{
        text-align: center;
        color: #8b7a94;
        font-size: 0.9rem;
    }}

    .floating-hearts {{
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        pointer-events: none;
        overflow: hidden;
        z-index: 0;
    }}
    .heart {{
        position: absolute;
        bottom: -10%;
        font-size: 1.4rem;
        opacity: 0.55;
        animation: rise linear infinite;
    }}
    @keyframes rise {{
        0%   {{ transform: translateY(0) rotate(0deg); opacity: 0.6; }}
        100% {{ transform: translateY(-110vh) rotate(30deg); opacity: 0; }}
    }}

    /* ---- Nav bar: plain flex row, immune to Streamlit's column breakpoints ---- */
    .navbar {{
        display: flex;
        flex-direction: row;
        flex-wrap: nowrap;
        gap: 0.35rem;
        margin-bottom: 0.5rem;
    }}
    .navbtn {{
        flex: 1 1 0;
        text-align: center;
        text-decoration: none !important;
        background: linear-gradient(135deg, {PRIMARY_COLOR}, {SECONDARY_COLOR});
        color: white !important;
        border-radius: 999px;
        padding: 0.5rem 0.2rem;
        font-size: 1.15rem;
        line-height: 1;
    }}
    .navbtn.active {{
        outline: 2px solid white;
        outline-offset: -4px;
    }}
    </style>

    <div class="floating-hearts">
        <div class="heart" style="left:5%; animation-duration:14s;">💗</div>
        <div class="heart" style="left:25%; animation-duration:18s; animation-delay:2s;">💫</div>
        <div class="heart" style="left:45%; animation-duration:12s; animation-delay:4s;">💕</div>
        <div class="heart" style="left:65%; animation-duration:20s; animation-delay:1s;">✨</div>
        <div class="heart" style="left:85%; animation-duration:16s; animation-delay:3s;">💖</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- Session state ----------
if "page" not in st.session_state:
    st.session_state.page = "home"
if "memory_idx" not in st.session_state:
    st.session_state.memory_idx = 0
#if "reasons_shown" not in st.session_state:
#    st.session_state.reasons_shown = []
#if "current_reason" not in st.session_state:
#    st.session_state.current_reason = None
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False
if "finale_shown" not in st.session_state:
    st.session_state.finale_shown = False
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

PAGES = {
    "home": "🏠",
    "story": "📖",
    "memories": "📸",
    "quiz": "🧩",
    "letter": "💝",
}
LABELS = {
    "home": "Home",
    "story": "Story",
    "memories": "Memories",
    "quiz": "Quiz",
    "letter": "Letter",
}

# Let a nav link (?page=xxx) set the current page
_query_page = st.query_params.get("page")
if _query_page in PAGES:
    st.session_state.page = _query_page


def go(page):
    st.session_state.page = page


def get_credentials():
    """Read username/password from st.secrets if set (recommended for
    hosted deployments), otherwise fall back to the values in the config
    section above (fine for local/private use)."""
    try:
        return st.secrets["auth"]["username"], st.secrets["auth"]["password"]
    except Exception:
        return APP_USERNAME, APP_PASSWORD


def show_login():
    st.markdown(f"<h1 style='text-align:center;'>{LOGIN_TITLE}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='subtitle'>{LOGIN_SUBTITLE}</p>", unsafe_allow_html=True)
    st.write("")

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Unlock 💖")
    st.markdown("</div>", unsafe_allow_html=True)

    if submitted:
        real_username, real_password = get_credentials()
        if username == real_username and password == real_password:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("That's not quite it — try again 💭")

def find_photo(index):
    """Look for photos/{index}.jpg|.jpeg|.png, return path or None."""
    for ext in ("jpg", "jpeg", "png"):
        path = os.path.join("photos", f"{index}.{ext}")
        if os.path.exists(path):
            return path
    return None


if not st.session_state.authenticated:
    show_login()
    st.stop()

# ---------- Top navigation ----------
_nav_html = f"""
<style>
.navbar {{
    display: flex !important;
    flex-direction: row !important;
    flex-wrap: nowrap !important;
    gap: 0.3rem;
    margin-bottom: 0.5rem;
    width: 100%;
}}
.navbtn {{
    flex: 1 1 0;
    display: inline-block;
    text-align: center;
    text-decoration: none !important;
    background: linear-gradient(135deg, {PRIMARY_COLOR}, {SECONDARY_COLOR});
    color: white !important;
    border-radius: 999px;
    padding: 0.5rem 0.1rem;
    font-size: 1.1rem;
    line-height: 1;
    box-sizing: border-box;
}}
.navbtn.active {{
    outline: 2px solid white;
    outline-offset: -4px;
}}
</style>
<div class="navbar">
"""
for _key, _emoji in PAGES.items():
    _active = " active" if st.session_state.page == _key else ""
    _nav_html += f"<a href='?page={_key}' class='navbtn{_active}' title='{LABELS[_key]}'>{_emoji}</a>"
_nav_html += "</div>"
st.markdown(_nav_html, unsafe_allow_html=True)

st.write("")

# ============================================================
#  PAGES
# ============================================================

if st.session_state.page == "home":
    st.markdown(f"<h1 style='text-align:center; color: #081c15'>{SITE_TITLE}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='subtitle'>{TAGLINE}</p>", unsafe_allow_html=True)
    st.write("")
    st.markdown(
        f"""
        <div class="card" style="text-align:center;">
            <h2>Happy Birthday, {GIRLFRIEND_NAME} 🎂</h2>
            <p>I made you something for you Ammu💕</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    if st.button("Start the journey 💫"):
        st.balloons()
        go("story")

elif st.session_state.page == "story":
    st.markdown(f"<h1 style='text-align:center; color: #081c15''>{OUR_STORY_TITLE}</h1>", unsafe_allow_html=True)
    st.markdown(f"<div class='card'>{OUR_STORY_TEXT.replace(chr(10), '<br>')}</div>", unsafe_allow_html=True)
    if st.button("See our memories →"):
        go("memories")

elif st.session_state.page == "memories":
    total = len(MEMORY_CAPTIONS)
    idx = st.session_state.memory_idx
    st.markdown("<h1 style='text-align:center; color: #081c15''>Our Little Galaxy 📸</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='progress-label'>Memory {idx + 1} of {total}</p>", unsafe_allow_html=True)
    st.progress((idx + 1) / total)

    photo_path = find_photo(idx + 1)
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        if photo_path:
            st.image(photo_path, use_container_width=True)
        else:
            st.info(f"📷 Add photos/{idx + 1}.jpg to show your photo here")
        st.write(MEMORY_CAPTIONS[idx])
        st.markdown("</div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        if st.button("⬅ Previous", disabled=idx == 0):
            st.session_state.memory_idx -= 1
            st.rerun()
    with c2:
        if idx < total - 1:
            if st.button("Next ➡"):
                st.session_state.memory_idx += 1
                st.rerun()
        else:
            if st.button("On to the quiz 🧩"):
                go("quiz")

elif st.session_state.page == "quiz":
    st.markdown("<h1 style='text-align:center; color: #081c15''>Do You Know Us? 🧩</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p class='subtitle'>Chuma oru 5 questions crt aah answer pannidu</p>",
        unsafe_allow_html=True,
    )

    answers = []
    for i, q in enumerate(QUIZ):
        #st.markdown("<div class='card'>", unsafe_allow_html=True)
        choice = st.radio(q["question"], q["options"], key=f"q_{i}", index=None)
        answers.append(choice)
        #st.markdown("</div>", unsafe_allow_html=True)

    if st.button("Check my answers"):
        st.session_state.quiz_submitted = True

    if st.session_state.quiz_submitted:
        score = sum(
            1
            for i, q in enumerate(QUIZ)
            if answers[i] == q["options"][q["answer"]]
        )
        st.markdown("<div class='card' style='text-align:center; color: #081c15''>", unsafe_allow_html=True)
        if score == len(QUIZ):
            st.success(f"{score}/{len(QUIZ)} — Perfect score! You know us better than anyone. 💕")
        else:
            st.success(f"{score}/{len(QUIZ)} — Somehow you still win, because it's your birthday. 😄")
        st.markdown("</div>", unsafe_allow_html=True)
        if st.button("One more thing..."):
            go("letter")

#elif st.session_state.page == "reasons":
 #   st.markdown("<h1 style='text-align:center;'>Reasons I Love You 💌</h1>", unsafe_allow_html=True)
  #  st.markdown(
   #     "<p class='subtitle'>Tap the button — one reason at a time, forever refillable.</p>",
    #    unsafe_allow_html=True,
    #)

    #if st.session_state.current_reason is None:
     #   st.session_state.current_reason = random.choice(REASONS)

    #st.markdown(
     #   f"<div class='card' style='text-align:center; font-size:1.15rem;'>"
      #  f"“{st.session_state.current_reason}”</div>",
       # unsafe_allow_html=True,
   # )

    #if st.button("Give me another reason 💗"):
     #   remaining = [r for r in REASONS if r != st.session_state.current_reason]
      #  st.session_state.current_reason = random.choice(remaining) if remaining else random.choice(REASONS)
       # st.rerun()

   # st.write("")
    #if st.button("One more thing... →"):
     #   go("letter")

elif st.session_state.page == "letter":
    st.markdown("<h1 style='text-align:center; color: #081c15''>💝</h1>", unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="card" style="font-size:1.05rem; line-height:1.7; font-style:italic;">
        {FINAL_LETTER.replace(chr(10), '<br>')}
        </div>
        """,
        unsafe_allow_html=True,
    )
    if not st.session_state.finale_shown:
        st.balloons()
        st.session_state.finale_shown = True

    if st.button("Replay from the start"):
        st.session_state.memory_idx = 0
        st.session_state.quiz_submitted = False
        st.session_state.current_reason = None
        st.session_state.finale_shown = False
        go("home")
        st.rerun()