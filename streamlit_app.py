import streamlit as st
from src.componets.banner import banner
from src.componets.chat import chat
from src.componets.sidebar import sidebar
from src.componets.statistics_banner import statistics_banner
from src.utils.env_config import load_config

sidebar(st)
banner(st)
chat(st)
statistics_banner(st)

load_config()
