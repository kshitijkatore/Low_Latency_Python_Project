import streamlit as st
import string

st.set_page_config(page_title="Text Utility", layout="centered")

st.title("📝 Real-Time Text Utility Web App")

# Input Text
text_input = st.text_area("Paste or type your text here:", height=200)

# Options
clean_punct = st.checkbox("Remove punctuation")
to_lower = st.checkbox("Convert to lowercase")
to_title = st.checkbox("Convert to title case")
remove_short = st.checkbox("Remove short words (less than 3 letters)")

def clean_text(text):
    words = text.split()

    # Clean punctuation
    if clean_punct:
        words = list(filter(lambda w: all(ch not in string.punctuation for ch in w), words))

    # Remove short words
    if remove_short:
        words = list(filter(lambda w: len(w) >= 3, words))

    # Lowercase or Title case
    if to_lower:
        words = list(map(lambda w: w.lower(), words))
    elif to_title:
        words = list(map(lambda w: w.title(), words))

    return ' '.join(words)

# Live Stats
if text_input:
    cleaned = clean_text(text_input)

    st.subheader("📊 Stats")
    st.write(f"Word Count: {len(cleaned.split())}")
    st.write(f"Character Count: {len(cleaned)}")
    st.write(f"Estimated Reading Time: {round(len(cleaned.split()) / 200, 2)} minutes")

    st.subheader("🧹 Cleaned Output")
    st.text_area("Result:", value=cleaned, height=150)

    # Export
    st.download_button("📥 Download Cleaned Text", data=cleaned, file_name="cleaned_text.txt", mime="text/plain")
