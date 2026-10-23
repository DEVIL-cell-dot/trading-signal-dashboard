
import streamlit as st
from datetime import datetime, timezone

st.set_page_config(page_title="Trading Signals", page_icon="📈", layout="wide")

st.title("📈 Trading Signal Dashboard")
st.caption("Forex Live & OTC | Signal analysis only")

market = st.selectbox("Market", ["Live Forex", "OTC"])
pair = st.selectbox(
    "Currency Pair",
    ["EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "EUR/JPY"]
)
expiry = st.selectbox("Expiry", ["1 minute", "5 minutes", "15 minutes"])

st.info("Market: " + market)
st.write("Selected pair:", pair)
st.write("Expiry:", expiry)

st.warning(
    "Abhi live price feed connect nahi hai. "
    "CALL/PUT signal generate karne se pehle verified market data zaroori hai."
)

st.write("Dashboard time (UTC):", datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"))
st.caption("Auto-trading enabled nahi hai. Koi trade automatically place nahi hoga.")
