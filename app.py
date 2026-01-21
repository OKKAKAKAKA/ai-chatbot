import streamlit as st

st.set_page_config(page_title="AlertAid", page_icon="🛑")

# ------------------- STYLING -------------------
st.markdown(
    """
    <style>
    body { background-color: #FFFFFF; }
    .title { text-align: center; font-size: 50px; font-weight: bold; margin-bottom: 20px; color: #2E3A59; }
    .chatbox { max-width: 700px; margin: 0 auto; padding: 20px; border-radius: 20px; }
    .user { text-align: right; background-color: #DCF8C6; padding: 12px; border-radius: 20px; width: fit-content; max-width: 70%; float: right; clear: both; margin: 5px 0; }
    .bot { text-align: left; background-color: #F1F0F0; padding: 12px; border-radius: 20px; width: fit-content; max-width: 70%; float: left; clear: both; margin: 5px 0; }
    .input-area { position: fixed; bottom: 0; width: 100%; background: white; padding: 10px 0; box-shadow: 0 -1px 8px rgba(0,0,0,0.1); }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title">AlertAid</div>', unsafe_allow_html=True)

# ------------------- DISASTER FUNCTIONS -------------------
def earthquake_info(): return "An earthquake is the sudden shaking of the ground caused by movements in the Earth's crust."
def typhoon_info(): return "A typhoon is a powerful tropical cyclone with strong winds and heavy rainfall."
def flood_info(): return "A flood occurs when water overflows onto normally dry land."
def fire_info(): return "Fire is a rapid chemical reaction that produces heat, light, and smoke."

def earthquake_before(): return "- Secure heavy furniture, Prepare emergency kit, Identify safe places in your home"
def earthquake_during(): return "- Drop, Cover, and Hold and Stay away from windows"
def earthquake_after(): return "- Check for injuries and Be alert for aftershocks"

def typhoon_before(): return "- Monitor weather updates and Secure loose objects"
def typhoon_during(): return "- Stay indoors and Avoid floodwaters"
def typhoon_after(): return "- Avoid fallen power lines"

def flood_before(): return "- Prepare evacuation routes and Elevate appliances"
def flood_during(): return "- Move to higher ground and Do not walk through floodwaters"
def flood_after(): return "- Clean and disinfect your home"

def fire_before(): return "- Check electrical wiring and Keep fire extinguishers ready"
def fire_during(): return "- Stay low to avoid smoke and Evacuate immediately"
def fire_after(): return "- Do not re-enter burned areas"

# ------------------- CHAT FUNCTION -------------------
def get_response(user_input):
    user_input = user_input.lower()

    if "what is" in user_input and "earthquake" in user_input:
        return earthquake_info()
    elif "what is" in user_input and "typhoon" in user_input:
        return typhoon_info()
    elif "what is" in user_input and "flood" in user_input:
        return flood_info()
    elif "what is" in user_input and "fire" in user_input:
        return fire_info()

    elif "earthquake" in user_input:
        if "before" in user_input: return earthquake_before()
        if "during" in user_input: return earthquake_during()
        if "after" in user_input: return earthquake_after()

    elif "typhoon" in user_input:
        if "before" in user_input: return typhoon_before()
        if "during" in user_input: return typhoon_during()
        if "after" in user_input: return typhoon_after()

    elif "flood" in user_input:
        if "before" in user_input: return flood_before()
        if "during" in user_input: return flood_during()
        if "after" in user_input: return flood_after()

    elif "fire" in user_input:
        if "before" in user_input: return fire_before()
        if "during" in user_input: return fire_during()
        if "after" in user_input: return fire_after()

    return "Sorry, I didn't understand."

# ------------------- CHAT STATE -------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "bot", "text": "Hi! I’m AlertAid 🤖\nI can help you with disaster information. Ask me anything!"}
    ]

# ------------------- CHAT DISPLAY -------------------
st.markdown('<div class="chatbox">', unsafe_allow_html=True)
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user">{msg["text"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot">{msg["text"]}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ------------------- INPUT AREA (BOTTOM) -------------------
st.markdown('<div class="input-area">', unsafe_allow_html=True)

col1, col2 = st.columns([4, 1])

# ❗ NO session_state used for input
user_input = col1.text_input("", placeholder="Type your message here...")

send = col2.button("Send")

if send and user_input.strip() != "":
    st.session_state.messages.append({"role": "user", "text": user_input})
    bot_response = get_response(user_input)
    st.session_state.messages.append({"role": "bot", "text": bot_response})

    # THIS IS THE KEY CHANGE:
    # We restart the app AFTER sending so the input clears safely
    st.experimental_rerun()
