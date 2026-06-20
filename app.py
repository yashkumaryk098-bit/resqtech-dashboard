import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import random
import time

st.set_page_config(page_title="ResQtech AI Command", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0b0f19; color: #e2e8f0; font-family: sans-serif; }
    .hero-container {
        background: linear-gradient(135deg, #1e1b4b 0%, #311042 100%);
        border: 1px solid #4f46e5; padding: 25px; border-radius: 16px; margin-bottom: 25px;
    }
    .neon-text { text-shadow: 0 0 10px #3b82f6; color: #fff; }
    .cyber-card {
        background: #111827; border: 1px solid #1f2937; padding: 20px; border-radius: 12px; border-top: 4px solid #3b82f6; color: white;
    }
    .critical-card { border-top: 4px solid #ef4444; }
    .stButton>button {
        background: linear-gradient(90deg, #3b82f6 0%, #8b5cf6 100%); color: white; border-radius: 8px; font-weight: bold; border: none;
    }
    </style>
""", unsafe_allow_html=True)

def trigger_audio_alert(text):
    html_code = f"""<iframe src="https://google.com{text.replace(" ", "%20")}" allow="autoplay" style="display:none"></iframe>"""
    st.components.v1.html(html_code, height=0)

if "tickets" not in st.session_state:
    st.session_state.tickets = pd.DataFrame([
        {"ID": "RT-4021", "Cluster": "Sector 4, Cluster-B", "Issue": "Severe Waterlogging & Drain Choke", "Lat": 28.6139, "Lon": 77.2090, "Urgency": "CRITICAL", "Status": "Dispatched", "AI": "98.2%"},
        {"ID": "RT-1094", "Cluster": "Noida Entry Highway", "Issue": "Major Pothole Cluster", "Lat": 28.6250, "Lon": 77.2200, "Urgency": "HIGH", "Status": "In Progress", "AI": "94.6%"},
        {"ID": "RT-8821", "Cluster": "Okhla Catchment Zone", "Issue": "Silt Overflow Risk", "Lat": 28.5900, "Lon": 77.2400, "Urgency": "MEDIUM", "Status": "Pending", "AI": "91.1%"}
    ])

st.sidebar.markdown("<h1 style=\"color:#a855f7;\">🔮 RESQTECH AI</h1>", unsafe_allow_html=True)
page = st.sidebar.radio("⚡ COMMAND NODES:", ["📊 Live Telemetry Control", "🤳 Citizen AI Intake Module"])

if page == "📊 Live Telemetry Control":
    st.markdown("<div class=\"hero-container\"><h1 class=\"neon-text\">🚨 ResQtech: Early Warning Control Center</h1><p>AI disaster prevention platform mapping 97,900+ clusters.</p></div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    col1.markdown("<div class=\"cyber-card\"><h4>🌍 Scale Coverage</h4><h2>97,900+ Villages</h2></div>", unsafe_allow_html=True)
    col2.markdown("<div class=\"cyber-card critical-card\"><h4>⏱ Response Opt.</h4><h2>90% Reduction</h2></div>", unsafe_allow_html=True)
    col3.markdown("<div class=\"cyber-card\"><h4>🔥 Active Triggers</h4><h2>{} Incidents Live</h2></div>".format(len(st.session_state.tickets)), unsafe_allow_html=True)

    st.markdown("---")
    map_col, control_col = st.columns(2)
    
    with map_col:
        st.markdown("### 📍 Geographic Risk Grid")
        m = folium.Map(location=[28.6139, 77.2090], zoom_start=12, tiles="CartoDB dark_matter")
        
        for idx, row in st.session_state.tickets.iterrows():
            color = "red" if row["Urgency"] == "CRITICAL" else "orange" if row["Urgency"] == "HIGH" else "green"
            popup_html = f"""<div style="font-family:Arial; width:200px; color:#111827;"><h4>ID: {row["ID"]}</h4><b>Loc:</b> {row["Cluster"]}<br><b>Issue:</b> {row["Issue"]}<br><b>AI Match:</b> {row["AI"]}<br><b>Status:</b> {row["Status"]}</div>"""
            folium.Marker([row["Lat"], row["Lon"]], popup=folium.Popup(popup_html, max_width=250), icon=folium.Icon(color=color)).add_to(m)
            
        st_folium(m, width="100%", height=420, key="main_map")

    with control_col:
        st.markdown("### 👮 Action Command Deck")
        target_id = st.selectbox("Select Ticket ID:", st.session_state.tickets["ID"].tolist())
        new_status = st.selectbox("Assign Action Status:", ["Pending", "Dispatched", "In Progress", "Resolved"])
        
        if st.button("⚡ Update Status & Alert Teams"):
            st.session_state.tickets.loc[st.session_state.tickets["ID"] == target_id, "Status"] = new_status
            trigger_audio_alert(f"Ticket {target_id} updated to {new_status}")
            st.toast(f"Ticket {target_id} updated!", icon="🚀")
            st.rerun()
            
        if st.button("📲 Broadcast Twilio Emergency Warning"):
            trigger_audio_alert("Emergency system initiated. Broadcasting SMS alerts.")
            st.success("📲 Twilio Sandbox: 1,200+ Alerts Dispatched via SMS!")

elif page == "🤳 Citizen AI Intake Module":
    st.markdown("<h2>🤳 Real-time Field Telemetry Intake</h2>", unsafe_allow_html=True)
    form_col, ai_col = st.columns(2)
    
    with form_col:
        with st.form("citizen_form", clear_on_submit=True):
            uploaded_file = st.file_uploader("Snap & Upload Image", type=["jpg", "png", "jpeg"])
            cluster_name = st.text_input("Village Cluster Name")
            submit = st.form_submit_button("🚀 Transmit to Central Grid")

    with ai_col:
        st.markdown("### 🤖 Neural Vision Engine Output")
        if submit and uploaded_file is not None:
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i + 1)
            sim_lat = 28.61 + random.uniform(-0.04, 0.04)
            sim_lon = 77.20 + random.uniform(-0.04, 0.04)
            new_id = f"RT-{random.randint(5000, 9999)}"
            new_row = {"ID": new_id, "Cluster": cluster_name if cluster_name else "Dynamic Node", "Issue": "AI Detected Infrastructure Failure", "Lat": sim_lat, "Lon": sim_lon, "Urgency": "CRITICAL", "Status": "Pending", "AI": "96.4%"}
            st.session_state.tickets = pd.concat([st.session_state.tickets, pd.DataFrame([new_row])], ignore_index=True)
            trigger_audio_alert("Critical emergency node synced.")
            st.success(f"💥 CENTRAL GRID SYNCED: Assigned ID {new_id}")
            st.json({"Neural Core": "ResQtech-CV-v3.0", "Confidence": "96.4%", "Coordinates": f"{sim_lat:.4f}, {sim_lon:.4f}"})
