import streamlit as st
import base64
import os

# === 基本設定 ===
st.set_page_config(page_title="共有PDFビューア", page_icon="📄", layout="centered")
PDF_PATH = "uploaded.pdf"

st.title("📄 共有PDFビューア")
st.write("このサイトでは、アップロードしたPDFが全員に共有されます。")

# === PDFアップロード ===
uploaded_file = st.file_uploader("📤 PDFをアップロードしてください", type=["pdf"])

if uploaded_file:
    # ファイルを保存（上書き）
    with open(PDF_PATH, "wb") as f:
        f.write(uploaded_file.read())
    st.success("✅ PDFをアップロードしました！（全員に反映されます）")

# === PDF表示 ===
if os.path.exists(PDF_PATH):
    with open(PDF_PATH, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    pdf_display = f"""
    <iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="900" type="application/pdf"></iframe>
    """
    st.markdown(pdf_display, unsafe_allow_html=True)
else:
    st.info("まだPDFがアップロードされていません。")
