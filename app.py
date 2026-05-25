import streamlit as st
import plotly.express as px
from crypto_data import get_crypto_data

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Crypto Tracker Dashboard",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------
# Load Data
# -----------------------------
df = get_crypto_data()



# -----------------------------
# Header
# -----------------------------
st.title("🚀 Cryptocurrency Tracker Dashboard")
st.markdown(
    "Track live cryptocurrency prices, market capitalization, and top gainers in real time."
)

st.divider()

# -----------------------------
# Search Box
# -----------------------------
st.subheader("🔍 Search Cryptocurrency")

search = st.text_input(
    "Enter Cryptocurrency Name",
    placeholder="Example: Bitcoin"
)

if search:
    filtered_df = df[
        df["name"].str.contains(search, case=False, na=False)
    ]
else:
    filtered_df = df

# -----------------------------
# Key Metrics
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Coins",
        len(df)
    )

with col2:
    st.metric(
        "Highest Price Coin",
        df.loc[df["current_price"].idxmax(), "name"]
    )

with col3:
    st.metric(
        "Top Market Cap",
        df.loc[df["market_cap"].idxmax(), "name"]
    )

st.divider()

# -----------------------------
# Cryptocurrency Table
# -----------------------------
st.subheader("📋 Live Cryptocurrency Data")

st.dataframe(
    filtered_df[
        [
            "name",
            "symbol",
            "current_price",
            "market_cap",
            "total_volume",
            "price_change_percentage_24h"
        ]
    ],
    use_container_width=True
)

# -----------------------------
# Top Gainers
# -----------------------------
st.subheader("🔥 Top 5 Gainers (24 Hours)")

top_gainers = df.sort_values(
    by="price_change_percentage_24h",
    ascending=False
).head(5)

st.dataframe(
    top_gainers[
        [
            "name",
            "current_price",
            "price_change_percentage_24h"
        ]
    ],
    use_container_width=True
)

st.divider()

# -----------------------------
# Charts
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    fig_price = px.bar(
        df.head(10),
        x="name",
        y="current_price",
        title="📊 Top 10 Cryptocurrency Prices"
    )

    st.plotly_chart(
        fig_price,
        use_container_width=True
    )

with col2:
    fig_market = px.bar(
        df.head(10),
        x="name",
        y="market_cap",
        title="💰 Top 10 Market Capitalization"
    )

    st.plotly_chart(
        fig_market,
        use_container_width=True
    )

# -----------------------------
# Download Button
# -----------------------------
st.divider()

csv = df.to_csv(index=False)

st.download_button(
    label="⬇ Download Cryptocurrency Data",
    data=csv,
    file_name="data/crypto_data.csv",
    mime="text/csv"
)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption(
    "Built with Python, Streamlit, Plotly, Pandas & CoinGecko API"
)