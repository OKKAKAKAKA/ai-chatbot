print("========================================")
print("🆘 Disaster Information AI Chatbot 🆘")
print("Use keywords: before, during, after")
print("Use 'what is <disaster>' for information")
print("Type 'exit' to end the chat.")
print("========================================")

# -------- EARTHQUAKE --------
def earthquake_before():
    return """
🌍 EARTHQUAKE – BEFORE
- Secure heavy furniture
- Prepare emergency kit
- Identify safe places in your home
"""

def earthquake_during():
    return """
🌍 EARTHQUAKE – DURING
- Drop, Cover, and Hold On
- Stay away from windows
"""

def earthquake_after():
    return """
🌍 EARTHQUAKE – AFTER
- Check for injuries
- Be alert for aftershocks
"""

def earthquake_info():
    return """
🌍 WHAT IS AN EARTHQUAKE?
An earthquake is the sudden shaking of the ground caused by movements in the Earth's crust.
"""

# -------- TYPHOON --------
def typhoon_before():
    return """
🌪️ TYPHOON – BEFORE
- Monitor weather updates
- Secure loose objects
"""

def typhoon_during():
    return """
🌪️ TYPHOON – DURING
- Stay indoors
- Avoid floodwaters
"""

def typhoon_after():
    return """
🌪️ TYPHOON – AFTER
- Avoid fallen power lines
"""

def typhoon_info():
    return """
🌪️ WHAT IS A TYPHOON?
A typhoon is a powerful tropical cyclone with strong winds and heavy rainfall.
"""

# -------- FLOOD --------
def flood_before():
    return """
🌊 FLOOD – BEFORE
- Prepare evacuation routes
- Elevate appliances
"""

def flood_during():
    return """
🌊 FLOOD – DURING
- Move to higher ground
- Do not walk through floodwaters
"""

def flood_after():
    return """
🌊 FLOOD – AFTER
- Clean and disinfect your home
"""

def flood_info():
    return """
🌊 WHAT IS A FLOOD?
A flood occurs when water overflows onto normally dry land.
"""

# -------- FIRE --------
def fire_before():
    return """
🔥 FIRE – BEFORE
- Check electrical wiring
- Keep fire extinguishers ready
"""

def fire_during():
    return """
🔥 FIRE – DURING
- Stay low to avoid smoke
- Evacuate immediately
"""

def fire_after():
    return """
🔥 FIRE – AFTER
- Do not re-enter burned areas
"""

def fire_info():
    return """
🔥 WHAT IS A FIRE?
Fire is a rapid chemical reaction that produces heat, light, and smoke.
"""

# -------- CHAT LOOP --------
while True:
    user_input = input("\nYou: ").lower()

    if user_input == "exit":
        print("Chatbot: Stay safe! 👋")
        break

    # INFORMATION (STRICT "WHAT IS")
    elif "what is" in user_input and "earthquake" in user_input:
        print(earthquake_info())

    elif "what is" in user_input and "typhoon" in user_input:
        print(typhoon_info())

    elif "what is" in user_input and "flood" in user_input:
        print(flood_info())

    elif "what is" in user_input and "fire" in user_input:
        print(fire_info())

    # EARTHQUAKE ACTIONS
    elif "earthquake" in user_input:
        if "before" in user_input:
            print(earthquake_before())
        elif "during" in user_input:
            print(earthquake_during())
        elif "after" in user_input:
            print(earthquake_after())

    # TYPHOON ACTIONS
    elif "typhoon" in user_input:
        if "before" in user_input:
            print(typhoon_before())
        elif "during" in user_input:
            print(typhoon_during())
        elif "after" in user_input:
            print(typhoon_after())

    # FLOOD ACTIONS
    elif "flood" in user_input:
        if "before" in user_input:
            print(flood_before())
        elif "during" in user_input:
            print(flood_during())
        elif "after" in user_input:
            print(flood_after())

    # FIRE ACTIONS
    elif "fire" in user_input:
        if "before" in user_input:
            print(fire_before())
        elif "during" in user_input:
            print(fire_during())
        elif "after" in user_input:
            print(fire_after())

    else:
        print("Chatbot: Please ask using 'before', 'during', 'after', or 'what is <disaster>'.")
