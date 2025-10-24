import streamlit as st
from pdfminer.high_level import extract_text
import os

st.set_page_config(page_title="AI対応PDF→HTMLビューア", page_icon="📘", layout="wide")

PDF_PATH = "uploaded.pdf"
TEXT_PATH = "uploaded.txt"

st.title("📘 PDF → HTML ビューア（AI参照対応・iframeなし）")
st.write("アップロードされたPDFの内容をHTMLとして直接ページに埋め込みます。AIクローラからも参照可能です。")

# ===== PDFアップロード =====
uploaded_file = st.file_uploader("📤 PDFをアップロードしてください", type=["pdf"])

if uploaded_file:
    # ファイルを保存
    with open(PDF_PATH, "wb") as f:
        f.write(uploaded_file.read())
    st.success("✅ PDFをアップロードしました。内容を変換中...")

    try:
        # PDF → テキスト抽出
        text = extract_text(PDF_PATH)

        if not text.strip():
            st.warning("⚠️ テキストが抽出できませんでした。画像のみのPDFかもしれません。")
        else:
            with open(TEXT_PATH, "w", encoding="utf-8") as f:
                f.write(text)
            st.success("✅ テキスト抽出が完了しました！")
    except Exception as e:
        st.error(f"❌ 変換中にエラーが発生しました: {e}")

# ===== HTML直接出力（iframeなし） =====
if os.path.exists(TEXT_PATH):
    st.markdown("### 📄 現在の共有PDF内容（AI参照可・HTML直埋め込み）")

    with open(TEXT_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # HTMLとしてページ本文に直接出力（AIが参照できる）
    st.markdown(
        f"""
        <div style='font-family: Helvetica, sans-serif; line-height: 1.6; white-space: pre-wrap;'>
        {content}
        </div>
        """,
        unsafe_allow_html=True  # ← これが重要！！
    )
else:
    st.info("まだPDFがアップロードされていません。")
