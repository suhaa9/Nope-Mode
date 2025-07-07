import streamlit as st

# Predefined creepy keywords (can expand or replace with NLP later)
CREEP_KEYWORDS = [
    "babe", "send pic", "hot", "sexy", "alone?", "miss your body", "horny", "naughty",
    "boobs", "cute smile", "strip", "video call now", "legs", "what are you wearing"
]

# Smart response options
RESPONSES = [
    "I'm not comfortable with this conversation.",
    "Let's keep this respectful.",
    "Please stop. This is inappropriate.",
    "Goodbye."
]

# Function to calculate "creep score"
def creep_score(message):
    message_lower = message.lower()
    score = 0
    flagged_words = []

    for word in CREEP_KEYWORDS:
        if word in message_lower:
            score += 10
            flagged_words.append(word)

    return min(score, 100), flagged_words


# ----- Streamlit UI -----
st.set_page_config(page_title="NopeMode | Anti-Creep Chat Scanner", page_icon="🚫")

st.title("🚫 NopeMode")
st.subheader("Smart AI-powered tool to detect creepy chat messages and help set boundaries.")

st.markdown("Enter a message or copy-paste a chat to check if it's **creepy or inappropriate**.")

user_input = st.text_area("💬 Paste message here:", height=150)

if st.button("🔍 Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        score, flagged = creep_score(user_input)

        st.markdown(f"### 🚨 Creep Score: `{score}/100`")
        if score > 0:
            st.error("⚠️ Red flag detected.")
            st.markdown("**🔴 Problematic Words Found:**")
            st.code(", ".join(flagged), language="text")

            st.markdown("#### 🧠 Suggested Responses:")
            for r in RESPONSES:
                st.write(f"• {r}")
        else:
            st.success("✅ This message seems respectful.")

st.markdown("---")
st.caption("Built with ❤️ by Suha | NopeMode v1.0")
