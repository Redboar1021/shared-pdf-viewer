import streamlit as st
import os

# === 基本設定 ===
st.set_page_config(page_title="共有PDFビューア", page_icon="📄", layout="centered")
PDF_PATH = "uploaded.pdf"

st.title("📄 共有PDFビューア")
st.write("このページでは、最新のPDFをアップロード＆共有できます。")

# === PDFアップロード ===
uploaded_file = st.file_uploader("📤 PDFをアップロードしてください", type=["pdf"])

if uploaded_file:
    # 保存（既存ファイルを上書き）
    with open(PDF_PATH, "wb") as f:
        f.write(uploaded_file.read())
    st.success("✅ PDFをアップロードしました！（全員に反映されます）")

# === PDF表示 ===
if os.path.exists(PDF_PATH):
    st.write("👇 現在の共有PDF:")
    with open(PDF_PATH, "rb") as f:
        base64_pdf = f.read()
    st.download_button("📥 PDFをダウンロード", base64_pdf, file_name="shared.pdf")
    st.components.v1.html(
        f'<iframe src="data:application/pdf;base64,{base64_pdf.decode("latin1")}" width="700" height="900" type="application/pdf"></iframe>',
        height=900,
    )
else:
    st.info("まだPDFがアップロードされていません。")
