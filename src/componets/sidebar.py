def sidebar(st):
    languages = {
        "Español": "es",
        "English": "en"
    }

    selected_language = st.sidebar.selectbox("Selecciona el idioma / Select language", list(languages.keys()))

    if "language" not in st.session_state:
        st.session_state.language = languages[selected_language]

    if languages[selected_language] != st.session_state.language:
        st.session_state.language = languages[selected_language]

    if st.session_state.language == "es":
        flag_image = "https://flagicons.lipis.dev/flags/4x3/co.svg"
    else:
        flag_image = "https://flagicons.lipis.dev/flags/4x3/us.svg"

    st.logo(flag_image, icon_image=flag_image)

