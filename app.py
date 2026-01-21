import streamlit as st

st.set_page_config(page_title="AlertAid", page_icon="🛑")

# ------------------- STYLING -------------------
st.markdown(
    """
    <style>
    body {
        background-color: #FFFFFF;
    }
    .title {
        text-align: center;
        font-size: 50px;
        font-weight: bold;
        margin-bottom: 20px;
        color: #2E3A59;
        font-family: 'Arial', sans-serif;
    }
    .chatbox {
        max-width: 700px;
        margin: 0 auto;
        padding: 20px;
        border-radius: 20px;
    }
    .user {
        text-align: right;
        background-color: #DCF8C6;
        padding: 12px;
        border-radius: 20px;
        width: fit-content;
        max-width: 70%;
        float: right;
        clear: both;
        margin: 5px 0;
    }
    .bot {
        text-align: left;
        background-color: #F1F0F0;
        padding: 12px;
        border-radius: 20px;
        width: fit-content;
        max-width: 70%;
        float: left;
        clear: both;
        margin: 5px 0;
    }
    .input-area {
        position: fixed;
        bottom: 0;
        width: 100%;
        background: white;
        padding: 10px 0;
        box-shadow: 0 -1px 8px rgba(0,0,0,0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------- TITLE -------------------
st.markdown('<div class="title">AlertAid</div>', unsafe_allow_html=True)

# ------------------- DISASTER FUNCTIONS -------------------
def earthquake_before():
    return "🌍 EARTHQUAKE – BEFORE\n- Secure heavy furniture\n- Prepare emergency kit\n- Identify safe places in your home"

def earthquake_during():
    return "🌍 EARTHQUAKE – DURING\n- Drop, Cover, and Hold On\n- Stay away from windows"

def earthquake_after():
    return "🌍 EARTHQUAKE – AFTER\n- Check for injuries\n- Be alert for aftershocks"

def earthquake_info():
    return "An earthquake is the sudden shaking of the ground caused by movements in the Earth's crust."

def typhoon_before():
    return "🌪️ TYPHOON – BEFORE\n- Monitor weather updates\n- Secure loose objects"

def typhoon_during():
    return "🌪️ TYPHOON – DURING\n- Stay indoors\n- Avoid floodwaters"

def typhoon_after():
    return "🌪️ TYPHOON – AFTER\n- Avoid fallen power lines"

def typhoon_info():
    return "A typhoon is a powerful tropical cyclone with strong winds and heavy rainfall."

def flood_before():
    return "🌊 FLOOD – BEFORE\n- Prepare evacuation routes\n- Elevate appliances"

def flood_during():
    return "🌊 FLOOD – DURING\n- Move to higher ground\n- Do not walk through floodwaters"

def flood_after():
    return "🌊 FLOOD – AFTER\n- Clean and disinfect your home"

def flood_info():
    return "A flood occurs when water overflows onto normally dry land."

def fire_before():
    return "🔥 FIRE – BEFORE\n- Check electrical wiring\n- Keep fire extinguishers ready"

def fire_during():
    return "🔥 FIRE – DURING\n- Stay low to avoid smoke\n- Evacuate immediately"

def fire_after():
    return "🔥 FIRE – AFTER\n- Do not re-enter burned areas"

def fire_info():
    return "Fire is a rapid chemical reaction that produces heat, light, and smoke."

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
        if "before" in user_input:
            return earthquake_before()
        elif "during" in user_input:
            return earthquake_during()
        elif "after" in user_input:
            return earthquake_after()

    elif "typhoon" in user_input:
        if "before" in user_input:
            return typhoon_before()
        elif "during" in user_input:
            return typhoon_during()
        elif "after" in user_input:
            return typhoon_after()

    elif "flood" in user_input:
        if "before" in user_input:
            return flood_before()
        elif "during" in user_input:
            return flood_during()
        elif "after" in user_input:
            return flood_after()

    elif "fire" in user_input:
        if "before" in user_input:
            return fire_before()
        elif "during" in user_input:
            return fire_during()
        elif "after" in user_input:
            return fire_after()

    return "Sorry, I didn't understand."

# ------------------- CHAT STATE -------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "bot", "text": "Hi! I’m AlertAid 🤖\nI can help you with disaster info."}
    ]

# Initialize input value
if "input_value" not in st.session_state:
    st.session_state.input_value = ""

# ------------------- CHAT DISPLAY -------------------
st.markdown('<div class="chatbox">', unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user">{msg["text"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot">{msg["text"]}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ------------------- INPUT AREA -------------------
st.markdown('<div class="input-area">', unsafe_allow_html=True)

with st.form(key="chat_form"):
    col1, col2 = st.columns([4, 1])
    with col1:
        user_input = st.text_input("", key="input_value")
    with col2:
        submit = st.form_submit_button("Send")

    if submit and user_input:
        st.session_state.messages.append({"role": "user", "text": user_input})
        bot_response = get_response(user_input)
        st.session_state.messages.append({"role": "bot", "text": bot_response})

        # CLEAR INPUT AFTER SEND
        st.session_state.input_value = ""
        st.experimental_rerun()

st.markdown('</div>', unsafe_allow_html=True)
