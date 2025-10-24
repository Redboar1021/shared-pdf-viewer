import streamlit as st
from pdfminer.high_level import extract_text
import os

st.set_page_config(page_title="PDF→HTMLビューア", page_icon="📘", layout="wide")

PDF_PATH = "uploaded.pdf"
HTML_PATH = "uploaded.html"

st.title("📘 PDF → HTML ビューア")
st.write("アップロードされたPDFをHTML化してWeb上で表示します。")

# === アップロード ===
uploaded_file = st.file_uploader("📤 PDFをアップロードしてください", type=["pdf"])

if uploaded_file:
    # 保存
    with open(PDF_PATH, "wb") as f:
        f.write(uploaded_file.read())
    st.success("✅ PDFをアップロードしました！HTMLに変換します...")

    # === PDF → テキスト抽出 ===
    text = extract_text(PDF_PATH)

    # === HTML化 ===
    html_content = f"""
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{
                font-family: 'Helvetica', sans-serif;
                line-height: 1.6;
                margin: 40px;
                white-space: pre-wrap;
            }}
        </style>
    </head>
    <body>{text}</body>
    </html>
    """

    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(html_content)

    st.success("✅ HTML変換が完了しました！")

# === HTML表示 ===
if os.path.exists(HTML_PATH):
    st.components.v1.html(open(HTML_PATH, encoding="utf-8").read(), height=900, scrolling=True)
else:
    st.info("まだPDFがアップロードされていません。")
