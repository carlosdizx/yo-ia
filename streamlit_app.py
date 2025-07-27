import streamlit as st
from src.componets.banner import banner
from src.componets.chat import chat
from src.componets.sidebar import sidebar
from src.componets.statistics_banner import statistics_banner
from src.services.gemini_service import GeminiService

sidebar(st)
banner(st)
client = GeminiService(st.session_state.language)
chat(st, client)
statistics_banner(st)
