import streamlit as st
from src.componets.banner import banner
from src.componets.chat import chat
from src.componets.sidebar import sidebar

sidebar(st)
banner(st)
chat(st)
