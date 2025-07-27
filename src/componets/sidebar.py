def sidebar(st):
    languages = {
        "Español": "es",
        "English": "en"
    }

    lang_code = st.query_params.get("lang", "es")

    st.session_state.language = lang_code

    language_label = list(languages.keys())[
        list(languages.values()).index(lang_code)
    ]

    selected_language_label = st.sidebar.selectbox(
        "Selecciona el idioma / Select language",
        list(languages.keys()),
        index=list(languages.keys()).index(language_label),
        key="selected_language"
    )

    selected_language_code = languages[selected_language_label]

    if selected_language_code != lang_code:
        st.query_params.update(lang=selected_language_code)
        st.session_state.language = selected_language_code
        st.session_state.messages = []
        st.markdown("""
            <script>
                window.location.reload();
            </script>
        """, unsafe_allow_html=True)

    flag_image = (
        "https://flagicons.lipis.dev/flags/4x3/co.svg"
        if st.session_state.language == "es"
        else "https://flagicons.lipis.dev/flags/4x3/us.svg"
    )
    st.logo(flag_image, icon_image=flag_image)

    messages = {
        "es": {"title_links": "Enlaces rápidos"},
        "en": {"title_links": "Quick Links"},
    }

    text = messages[st.session_state.language]["title_links"]

    st.sidebar.markdown(f"### {text}")
    st.sidebar.markdown("[Linkedin](https://www.linkedin.com/in/carlos-ernesto-diaz-basante/)")
    st.sidebar.markdown("[GitHub](https://github.com/carlosdizx)")
