import streamlit as st
import datetime

# --- 1. ページ設定 ---
st.set_page_config(
    page_title="Natural Wind Rie",
    page_icon="🌿",
    layout="centered"
)

# --- 2. CSSデザイン（スマホで見やすく調整） ---
st.markdown("""
    <style>
    /* 全体の背景と文字色 */
    .stApp {
        background-color: #FFFAF0;
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
        width: 100%; /* スマホで押しやすく */
    }
    .insta-btn:hover {
        opacity: 0.9;
        box-shadow: 0 6px 8px rgba(0,0,0,0.15);
    }
    /* ボタンのスマホ対応：幅を広げる */
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background: linear-gradient(90deg, #FFAB91 0%, #FF8A65 100%);
        color: white;
        border: none;
        padding: 10px;
        font-weight: bold;
    }
    /* 事例紹介のボックス装飾 */
    .case-box {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #FFAB91;
        margin-bottom: 10px;
    }
    /* インプット欄の背景を白く */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. サイドバー：表示モード切り替え ---
with st.sidebar:
    st.header("⚙️ 表示設定")
    # スマホユーザー向けに画面をスッキリさせるスイッチ
    mode = st.radio("表示モード", ["通常モード", "スマホ用シンプルモード"])
    
    st.markdown("---")
    st.write("営業日: 土・日・祝")
    st.write("営業時間: 10:00 - 18:00")

# --- 4. メインコンテンツ ---

# シンプルモードなら、大きな画像を飛ばす
if mode == "通常モード":
    st.title("🌿 Natural Wind Rie")
    st.caption("心と体を整える、隠れ家サロンへようこそ")
    
    # 画像表示（指定されたファイル名に変更済み）
    # ※もしエラーが出る場合は、フォルダ内の画像名をこれに合わせてください
    st.image("3201fb7d-fb92-4ca2-abf4-93f87160d733.png", use_container_width=True)
else:
    # スマホモード用のコンパクトなヘッダー
    st.header("🌿 Natural Wind Rie")
    st.info("📱 スマホ用シンプルモードで表示中")

# インスタグラムへのリンクボタン（指定されたURLに変更済み）
col1, col2 = st.columns([2, 1])
with col1:
    st.write("アニマルコミュニケーション & 耳つぼジュエリー")
    st.write("ペットも、飼い主様も。すべての魂に癒しを届けます。")

with col2:
    st.markdown("""
        <a href="https://www.instagram.com/naturalwind2024?igsh=MWJ4eW82cTg5b296eA==/" target="_blank" class="insta-btn">
            📷 Instagramを見る
        </a>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- 5. サービスメニュー（タブ切り替え） ---
tab1, tab2 = st.tabs(["🐾 アニマルコミュニケーション", "👂 耳つぼジュエリー"])

# === タブ1：アニマルコミュニケーション ===
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


# === タブ2：耳つぼジュエリー ===
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
        # 画像URL（Unsplashのままにしていますが、必要あれば変更してください）
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

# --- 6. 予約システム（カレンダー機能付き） ---
st.header("📩 ご予約・お問い合わせ")
# st.write("InstagramのDM、または以下のフォームよりご連絡ください。") # 下のフォームと重複するのでコメントアウト

# 満席の日付リスト（手動設定例）
fully_booked_dates = [
    datetime.date(2026, 1, 10),
    datetime.date(2026, 1, 15),
    datetime.date(2026, 2, 1),
]

with st.form("contact_form"):
    # 1. メニュー選択
    menu = st.selectbox("ご希望メニュー", ["アニマルコミュニケーション", "耳つぼジュエリー", "両方"])
    
    # 2. 日付選択（今日より前は選べない設定）
    booking_date = st.date_input(
        "ご希望日",
        min_value=datetime.date.today()
    )
    
    # 3. 時間帯選択
    booking_time = st.selectbox("ご希望の時間帯", [
        "10:00 - 11:00",
        "11:00 - 12:00",
        "13:00 - 14:00",
        "14:00 - 15:00",
        "15:00 - 16:00",
        "16:00 - 17:00"
    ])

    name = st.text_input("お名前")
    email = st.text_input("メールアドレス")
    message = st.text_area("その他ご要望")
    
    submitted = st.form_submit_button("予約をリクエストする")

    if submitted:
        # 満席チェック
        if booking_date in fully_booked_dates:
            st.error(f"申し訳ありません。{booking_date} は既に満席となっております。別の日程をご選択ください。")
        # 入力漏れチェック
        elif not name or not email:
            st.warning("お名前とメールアドレスを入力してください。")
        else:
            st.balloons()
            st.success(f"""
            ✅ 送信完了しました！
            
            日時: {booking_date} {booking_time}
            メニュー: {menu}
            
            内容を確認次第、Instagram DM または {email} 宛にご連絡いたします。
            """)