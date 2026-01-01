import streamlit as st

# --- 1. ページ設定 ---
st.set_page_config(
    page_title="Natual Wind Rie",
    page_icon="🌿",
    layout="centered"
)

# --- 2. デザインのカスタマイズ（CSS） ---
st.markdown("""
    <style>
    .stApp {
        background-color: #FFFAF0; /* 背景：温かみのある生成り色 */
        color: #4E342E;
    }
    /* インスタボタン専用のスタイル */
    .insta-btn {
        display: inline-block;
        background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%);
        color: white !important;
        padding: 10px 20px;
        text-decoration: none;
        border-radius: 30px;
        font-weight: bold;
        text-align: center;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .insta-btn:hover {
        opacity: 0.9;
        box-shadow: 0 6px 8px rgba(0,0,0,0.15);
    }
    /* 事例紹介のボックス装飾 */
    .case-box {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #FFAB91;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. メインヘッダー & インスタ誘導 ---
st.title("🌿 Natual Wind Rie")
st.caption("心と体を整える、隠れ家サロンへようこそ")

col1, col2 = st.columns([2, 1])
with col1:
    st.write("アニマルコミュニケーション & 耳つぼジュエリー")
    st.write("ペットも、飼い主様も。すべての魂に癒しを届けます。")

with col2:
    # インスタグラムへのリンクボタン
    st.markdown("""
        <a href="https://www.instagram.com/naturalwind2024?igsh=MWJ4eW82cTg5b296eA==/" target="_blank" class="insta-btn">
            📷 Instagramを見る
        </a>
    """, unsafe_allow_html=True)

st.image("3201fb7d-fb92-4ca2-abf4-93f87160d733.png")

st.markdown("---")

# --- 4. サービスメニュー（タブ切り替え） ---
tab1, tab2 = st.tabs(["🐾 アニマルコミュニケーション", "👂 耳つぼジュエリー"])

# === タブ1：アニマルコミュニケーション（ここを修正） ===
with tab1:
    st.header("🐾 ペットの声、届けます")
    st.write("""
    「どうしてこんな行動をするの？」
    「身体の調子はどうかな？」
    
    写真を通して、大切なご家族（ペット）の魂にアクセスし、
    飼い主様へのメッセージを通訳いたします。
    """)
    
    st.markdown("---")
    
    st.subheader("📖 過去のセッション事例")
    st.write("これまでにご相談いただいた事例の一部をご紹介します。")
    
    # 事例1
    with st.expander("Case 1：夜泣きが止まらないトイプードル（3歳・男の子）"):
        st.info("💡 **お悩み**：夜中になると急に吠え出し、ご近所迷惑が心配で眠れない日々が続いていました。")
        st.write("""
        **【ペットからのメッセージ】**
        「窓の外の街灯がチカチカして怖いの。ママを守らなきゃって思ってたんだよ」
        
        **【その後】**
        遮光カーテンに変えて、「守ってくれてありがとう、もう大丈夫だよ」と伝えたところ、その日から朝までぐっすり眠れるようになりました。
        """)

    # 事例2
    with st.expander("Case 2：急にご飯を食べなくなった猫（12歳・女の子）"):
        st.info("💡 **お悩み**：病院では異常なしと言われたが、食欲が戻らず元気がない。")
        st.write("""
        **【ペットからのメッセージ】**
        「いつものお皿の匂いが変わった気がするの。洗剤変えた？」
        
        **【その後】**
        食器用洗剤を無香料のものに戻したところ、嘘のように食欲が復活しました。猫ちゃんの敏感な嗅覚によるものでした。
        """)

    # 事例3
    with st.expander("Case 3：お空に旅立ったハムスターからの言葉"):
        st.info("💡 **お悩み**：最期に苦しまなかったか、もっとできたことがあったのではないかと後悔している。")
        st.write("""
        **【ペットからのメッセージ】**
        「僕の手を握って温めてくれたの、ちゃんと分かってたよ。すごくポカポカして幸せだった。ありがとう。」
        
        **【その後】**
        飼い主様の涙が止まり、前を向くきっかけになりました。
        """)
    
    st.caption("※個人の感想であり、効果を保証するものではありません。")


# === タブ2：耳つぼジュエリー（そのまま維持） ===
with tab2:
    st.header("👂 耳つぼジュエリー施術")
    st.write("""
    **「飼い主様が笑っていれば、ペットも幸せ」**
    
    耳には全身のツボが集まっています。
    スワロフスキーの輝きを楽しみながら、自律神経を整え、
    肩こり・腰痛・リフトアップへのアプローチを行います。
    """)
    
    col_ear1, col_ear2 = st.columns(2)
    with col_ear1:
        # 画像を変更したい場合はURLを差し替えてください
        st.image("https://images.unsplash.com/photo-1598150654641-a20464d26272?q=80&w=1000&auto=format&fit=crop", caption="耳つぼ施術イメージ")
    with col_ear2:
        st.markdown("""
        **【メニュー】**
        * **リフトアップコース:** 3,000円
        * **肩こり解消コース:** 3,000円
        * **自律神経調整コース:** 4,000円
        
        ※アニマルコミュニケーションとのセット割引もございます。
        """)
    
    st.warning("⚠️ 医療行為ではありません。リラクゼーションとしてご利用ください。")

st.markdown("---")

# --- 5. お問い合わせ ---
st.header("📩 ご予約・お問い合わせ")
st.write("InstagramのDM、または以下のフォームよりご連絡ください。")

with st.form("contact_form"):
    menu = st.multiselect("興味のあるメニュー", ["アニマルコミュニケーション", "耳つぼ", "両方"])
    name = st.text_input("お名前")
    message = st.text_area("ご相談・ご希望の日時")
    
    submitted = st.form_submit_button("送信する")
    if submitted:
        st.success("送信完了しました。InstagramのDMも合わせてご確認いただけますと幸いです。")