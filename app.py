import streamlit as st

st.set_page_config(page_title="AlertAid", layout="wide")

# Centered title
st.markdown(
    """
    <h1 style='text-align: center; color: #2E86C1;'>
        AlertAid
    </h1>
    """,
    unsafe_allow_html=True,
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "bot", "text": "Hello! I'm AlertAid. Ask me about Flood, Typhoon, Earthquake, Hurricane, Tornado or Fire safety."}
    ]

def add_message(role, text):
    st.session_state.messages.append({"role": role, "text": text})

# Display chat
for msg in st.session_state.messages:
    if msg["role"] == "bot":
        st.markdown(
            f"""
            <div style="background-color:#E8F8F5; padding: 10px; border-radius: 10px; margin: 5px;">
                <b>AlertAid:</b> {msg["text"]}
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div style="text-align:right; background-color:#F0F3F4; padding: 10px; border-radius: 10px; margin: 5px;">
                <b>You:</b> {msg["text"]}
            </div>
            """,
            unsafe_allow_html=True,
        )

# Input box at the bottom
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message here...", "")
    submit = st.form_submit_button("Send")

    if submit and user_input.strip() != "":
        add_message("user", user_input)

        # Disaster-specific responses
        text = user_input.lower()

        if "flood" in text:
            response = (
                "🚨 Flood Safety Tips:\n"
                " Move to higher ground immediately, "
                " Avoid walking/driving through flood waters, "
                " Turn off electricity if water enters your home, "
                " Prepare an emergency kit with water, food, and medicines."
            )

        elif "typhoon" in text:
            response = (
                "🌪️ Typhoon Safety Tips:\n"
                " Stay indoors and away from windows, "
                " Secure loose objects outside, "
                " Charge your phone and prepare emergency supplies, "
                " Listen to local updates and evacuation orders."
            )

        elif "earthquake" in text:
            response = (
                "🌏 Earthquake Safety Tips:\n"
                " DROP, COVER, and HOLD ON, "
                " Stay away from windows and heavy furniture, "
                " If outside, move to an open area, "
                " After shaking stops, check for injuries and damage."
            )

        elif "fire" in text:
            response = (
                "🔥 Fire Safety Tips:\n"
                " Get out immediately and call emergency services, "
                " Use stairs, not elevators, "
                " If smoke is present, stay low and cover your mouth, "
                " Have a fire extinguisher ready and know your exits."
            )
            
        elif "hurricane" in text:
            response = (
                "🌀 Hurricane Safety Tips:\n"
                " Secure doors and windows, "
                " Stock up on food, water, and supplies, "
                " Avoid coastal and flood-prone areas, "
                " Stay updated with weather alerts and evacuation orders."
            )

        elif "tornado" in text:
            response = (
                "🌪️ Tornado Safety Tips:\n"
                " Go to a basement or interior room without windows, "
                " Stay low and cover your head, "
                " Avoid staying in a mobile home, "
                " If driving, exit the vehicle and find a sturdy shelter."
            )

        else:
            response = (
                "I can help with Flood, Typhoon, Earthquake, Tornado, Hurricane and Fire preparedness. "
                "What would you like to know?"
            )

        add_message("bot", response)
