import streamlit as st
import os

st.set_page_config(page_title="File Utility Web App", layout="centered")
st.title("📁 File Utility Web App")

# Filename input
filename = st.text_input("📂 Enter filename (with .txt):")

# Operation selection
operation = st.selectbox("Select operation:", ["Read", "Write", "Append", "Count Word"])

if filename:
    try:
        if operation == "Read":
            if st.button("📖 Read File"):
                with open(filename, 'r') as f:
                    content = f.read()
                    st.text_area("📄 File Content:", value=content, height=200)

        elif operation == "Write":
            new_text = st.text_area("📝 Enter text to WRITE (overwrites file):")
            if st.button("💾 Save File"):
                with open(filename, 'w') as f:
                    f.write(new_text + '\n')
                st.success("✅ File written successfully!")

        elif operation == "Append":
            append_text = st.text_input("➕ Text to append:")
            if st.button("📌 Append Line"):
                with open(filename, 'a') as f:
                    f.write(append_text + '\n')
                st.success("✅ Text appended successfully!")

        elif operation == "Count Word":
            search_word = st.text_input("🔍 Word to count:")
            if st.button("🔍 Count Now"):
                with open(filename, 'r') as f:
                    content = f.read().lower()
                    count = content.count(search_word.lower())
                    st.info(f"'{search_word}' appears {count} times in '{filename}'")

    except FileNotFoundError:
        st.error("❌ File not found.")
    except PermissionError:
        st.error("❌ You don't have permission to access this file.")
    except Exception as e:
        st.error(f"⚠️ An unexpected error occurred: {e}")
else:
    st.info("🔑 Please enter a filename to proceed.")
