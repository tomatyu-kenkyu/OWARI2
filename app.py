import streamlit as st
from paddleocr import PaddleOCR
from PIL import Image
import numpy as np

st.title("PaddleOCR Web版")

# OCRモデル読み込み
@st.cache_resource
def load_ocr():
    return PaddleOCR(
        use_angle_cls=True,
        lang='japan'
    )

ocr = load_ocr()

# 画像アップロード
uploaded_file = st.file_uploader(
    "画像をアップロード",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    # 画像読み込み
    image = Image.open(uploaded_file).convert("RGB")
    img_array = np.array(image)

    st.image(image, caption="アップロード画像")

    # OCR実行
    with st.spinner("OCR解析中..."):
        result = ocr.ocr(img_array)

    st.subheader("認識結果")

    # 表示
    texts = []

    if result and result[0]:
        for line in result[0]:
            text = line[1][0]
            texts.append(text)

    output_text = "\n".join(texts)

    st.text_area(
        "抽出文字",
        output_text,
        height=300
    )
