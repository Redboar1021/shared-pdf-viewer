import streamlit as st
from pdfminer.high_level import extract_text
import os

# ============ 基本設定 ============
st.set_page_config(page_title="共有PDF→HTMLビューア", page_icon="📘", layout="wide")
PDF_PATH = "uploaded.pdf"
TEXT_PATH = "uploaded.txt"

st.title("📘 PDF → HTML ビューア（AI参照対応）")
st.write("アップロードしたPDFをHTML化し、AIシステムからも読める形で公開します。")

# ============ PDFアップロード ============
uploaded_file = st.file_uploader("📤 PDFをアップロードしてください", type=["pdf"])

if uploaded_file:
    # ファイル保存（上書き）
    with open(PDF_PATH, "wb") as f:
        f.write(uploaded_file.read())
    st.success("✅ PDFをアップロードしました！内容を解析中...")

    # ============ PDF → テキスト抽出 ============
    try:
        text = extract_text(PDF_PATH)
        if not text.strip():
            st.warning("⚠️ テキストが抽出できませんでした（画像のみのPDFかもしれません）")
        else:
            # テキストを保存（永続化）
            with open(TEXT_PATH, "w", encoding="utf-8") as f:
                f.write(text)
            st.success("✅ テキスト抽出が完了しました！")
    except Exception as e:
        st.error(f"❌ 変換中にエラーが発生しました: {e}")

# ============ HTMLとして表示 ============
if os.path.exists(TEXT_PATH):
    st.markdown("### 📄 現在の共有PDF内容（HTML表示 / AI参照可）")
    with open(TEXT_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # HTMLとして直接埋め込み（AIクローラが読める）
    html_content = f"""
    <div style='font-family: Helvetica, sans-serif; line-height: 1.6; white-space: pre-wrap;'>
        {content}
    </div>
    """
    st.components.v1.html(html_content, height=900, scrolling=True)
else:
    st.info("まだPDFがアップロードされていません。")
