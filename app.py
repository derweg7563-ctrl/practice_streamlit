import streamlit as st

print("page reloaded")
st.set_page_config(
    page_title="포켓몬 도감",
    page_icon="./images/mon1.png"
)
st.markdown("""
<style>
img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    max-width: 100%; /* 부모 너비에 맞춤 */
    height: auto;
}

/* 2. Expander 내부의 모든 요소를 세로로 나열하고 가운데 정렬 */
[data-testid="stExpanderDetails"] div {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    font-size: 20px;
}

/* 3. 텍스트들(이름, 속성 등)도 가운데 정렬 강제 */
.stMarkdown {
    text-align: center;
}
[data-testid="stIconMaterial"]{
    visibility: hidden;
}
</style>         
""", unsafe_allow_html=True)


st.title("Streamlit 포켓몬 도감")
st.markdown("**포켓몬**을 하나씩 추가해서 도감을 채워보세요!")


type_emoji_dict = {
    '불꽃': '🔥',
    '물': '💧',
    '풀': '🌿',
    '전기': '⚡',
    '얼음': '❄️',
    '격투': '🥊',
    '독': '☠️',
    '땅': '🌍',
    '비행': '🕊️',
    '에스퍼': '🔮',
    '벌레': '🐛',
    '바위': '🪨',
    '고스트': '👻',
    '드래곤': '🐉',
    '악': '😈',
    '강철': '⚙️',
    '페어리': '🧚‍♀️'
}   

initial_pokemons = [

    {
        "name": "피카츄",
        "types": ["전기"],
        "image_url": "https://i.namu.wiki/i/JRwm0cCR84snXwMJpuDkEeQ1jE2H368Ssle1QtaPlDCHdkxmYjpgQrlLwUCHR4MLEdm8MN7TBObOYHAKdW6J4an-3rd48pqTrPxjGPBGDBYTS6LXZDREFh4YXHV2eyAVdoLdi8T-ky4JzhW4HZoZkg.webp"
    },
    
    {
        "name": "갸라도스",
        "types": ["물","비행"],
        "image_url": "https://i.namu.wiki/i/YL-AYn3eFQ3Nme9gSeqTHASseiUdzgp7POfICRPv6SrpcTjLHH8ZX9Nu3rlnshzmmoXNGiTEQlU9dt9CyMf5SsJpqmicxf9hpE6CSRajk3e0d6GpMxplggJq_yQl-2-4csCGv6WzwN6-WUVxoT68nw.webp"
    },

    {
        "name": "개굴닌자",
        "types": ["물","악"],
        "image_url": "https://i.namu.wiki/i/UDcwUH1TalXaSLISWrsb6ys1X5-Egt9ZeSG7fFPSVTISOeKZ3O2Ztf7vngfxs50Xr_TttihdV6EPDhSPRDDA6xYlBd9zkn5mIQOIJQlCsc6pkvUnq6tih7_2JFHbAorAhA7pk5Nqbdz8gq9SI6vbgg.webp"
    },

    {
        "name": "루카리오",
        "types": ["격투","강철"],
        "image_url": "https://i.namu.wiki/i/IkZB2oUCUD8L2tHcAw8oyg9ulTqvC4Vc3o-fcGT5D0wi4p3-YsEuH1XEoOs6jLe27cW9H3Wo6aWpueHDEnmMp7dmkPAnAjb1Bz9XzZcO97GP4Vvvus6QFPTW_-j-OZsK_-WbeEFO04QYJlzy8EoBgA.webp"
    },

    {
        "name": "에이스번",
        "types": ["불꽃"],
        "image_url": "https://i.namu.wiki/i/NVZ0Er-WYuJ_J_dTXBJcBmd6JsdQKBAJUVg2EjTvoV3rFJnZ_Olg0clbhQj6hAsf1OVHPTdXCuMwO2MdN11pDM4S_AzWWGDsCP1QQ-R6mOxrdon2O8bXQ5UvIM9BjxQhlIBMCEC4BQivBGC2b7jM_g.webp"
    },

    {
        "name": "누오",
        "types": ["물","땅"],
        "image_url": "https://i.namu.wiki/i/vaIohyQZVRE3cr3psCAP1bMbyz_YvA4EtApByKYxsrkhfiANmV1SJHEI7XWluNywDe9TiZupxfIWxZTRZ2bOsXNGqHqwc136hH1mCGEt0GSO6IIuTaknDAWdWOQWic2Kegx-00JZyXyTrRqeo8ojvw.webp"
    }

]

example_pokemon = {
    "name": "알로라 디그다",
    "types": ["땅","강철"],
    "image_url": "https://i.namu.wiki/i/L2Yfe9Z_6GecCYTj3ayNeiIMVXRbW9xVdvDk1BGERZzJHSZhTLb77UL0OW0-iadvEzlTWx7byvnGHdoDwmR682FwAoPH9XPPNqxLbDqRTaVS7eYfXuqsfWau7ZHn1ONIcKTaPfU6IY70npJ9rr25vA.webp"
}
if "pokemons" not in st.session_state:
    st.session_state.pokemons = initial_pokemons

auto_complete = st.toggle("예시 데이터로 체우기")
print("page reloaded, auto_complete:", auto_complete)

with st.form(key="form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input(
            label="포켓몬 이름",
            value=example_pokemon["name"] if auto_complete else ""
        )

    with col2:
        types = st.multiselect(
            label="포켓몬 속성",
            options=list(type_emoji_dict.keys()),
            max_selections=2,
            default=example_pokemon["types"] if auto_complete else []
        )
    image_url = st.text_input(
        label="포켓몬 이미지 URL",
        value=example_pokemon["image_url"] if auto_complete else ""
    )
    submit = st.form_submit_button(label="Submit")
    if submit:
        if not name:
            st.error("포켓몬 이름을 입력해주세요.")
        elif len(types) == 0:
            st.error("포켓몬 속성을 적어도 한개 선택해주세요.")
        else:
            st.success("포켓몬을 추가할 수 있습니다.")
            st.session_state.pokemons.append({
                "name": name,
                "types": types,
                "image_url": image_url if image_url else "./images/default.png"
            })
            
  


for i in range(0, len(st.session_state.pokemons),3):
    row_pokemons = st.session_state.pokemons[i:i+3]
    cols = st.columns(3)
    for j in range(len(row_pokemons)):
        with cols[j]:
            pokemon = row_pokemons[j]
            with st.expander(label=f"**{i+j+1}. {pokemon["name"]}**", expanded=True):
                st.image(pokemon["image_url"])
                emoji_types = [f"{type_emoji_dict[x]} {x}" for x in pokemon["types"]]
                st.text("/".join(emoji_types))
                delete_button = st.button("삭제", key=i+j, use_container_width=True)
                if delete_button:
                    print("delete button clicked!")
                    del st.session_state.pokemons[i+j]
                    st.rerun()
