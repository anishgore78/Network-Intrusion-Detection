
import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="Network Intrusion Detection",
    page_icon="🛡️",
    layout="wide"
)

API_URL = "https://network-intrusion-detection-0hoe.onrender.com/predict"

# Header
st.title("🛡️ Network Intrusion Detection System")
st.markdown(
    "Machine Learning-based network traffic classification "
    "using K-Nearest Neighbors."
)

st.info(
    "Prototype application: predictions are experimental "
    "and should not be used as the sole basis for security decisions."
)

# API status
try:
    health = requests.get(
        "https://network-intrusion-detection-0hoe.onrender.com/health",
        timeout=3
    )
    if health.status_code == 200:
        st.success("Backend API connected")
    else:
        st.error("Backend API is unavailable")
except requests.RequestException:
    st.error("Cannot connect to FastAPI. Start the backend first.")

st.divider()

st.subheader("Network Traffic Input")
st.write("Enter the 41 features of a network connection.")

# Categorical features
st.markdown("### Categorical Features")

col1, col2, col3 = st.columns(3)

with col1:
    protocol_type = st.selectbox(
        "Protocol Type",
        ["tcp", "udp", "icmp"]
    )

with col2:
    service = st.text_input(
        "Service",
        value="http"
    )

with col3:
    flag = st.text_input(
        "Connection Flag",
        value="SF"
    )

# Numerical features
st.markdown("### Numerical Features")

numeric_defaults = {
    "duration": 0,
    "src_bytes": 181,
    "dst_bytes": 5450,
    "land": 0,
    "wrong_fragment": 0,
    "urgent": 0,
    "hot": 0,
    "num_failed_logins": 0,
    "logged_in": 1,
    "num_compromised": 0,
    "root_shell": 0,
    "su_attempted": 0,
    "num_root": 0,
    "num_file_creations": 0,
    "num_shells": 0,
    "num_access_files": 0,
    "num_outbound_cmds": 0,
    "is_host_login": 0,
    "is_guest_login": 0,
    "count": 9,
    "srv_count": 9,
    "serror_rate": 0.0,
    "srv_serror_rate": 0.0,
    "rerror_rate": 0.0,
    "srv_rerror_rate": 0.0,
    "same_srv_rate": 1.0,
    "diff_srv_rate": 0.0,
    "srv_diff_host_rate": 0.0,
    "dst_host_count": 9,
    "dst_host_srv_count": 9,
    "dst_host_same_srv_rate": 1.0,
    "dst_host_diff_srv_rate": 0.0,
    "dst_host_same_src_port_rate": 0.11,
    "dst_host_srv_diff_host_rate": 0.0,
    "dst_host_serror_rate": 0.0,
    "dst_host_srv_serror_rate": 0.0,
    "dst_host_rerror_rate": 0.0,
    "dst_host_srv_rerror_rate": 0.0
}

features = {
    "protocol_type": protocol_type,
    "service": service.strip(),
    "flag": flag.strip()
}

# Display numerical inputs in columns
numeric_names = list(numeric_defaults.keys())

columns = st.columns(3)

for index, name in enumerate(numeric_names):
    with columns[index % 3]:
        value = st.number_input(
            name,
            value=float(numeric_defaults[name]),
            format="%.4f"
        )
        features[name] = value

st.divider()

# Prediction
if st.button("🔍 Analyze Network Traffic", type="primary"):
    if not features["service"] or not features["flag"]:
        st.error("Service and connection flag cannot be empty.")

    else:
        try:
            response = requests.post(
                API_URL,
                json={"features": features},
                timeout=30
            )

            if response.status_code == 200:
                result = response.json()

                st.subheader("Prediction Result")

                if result["class_label"] == "Attack":
                    st.error("🚨 ATTACK DETECTED")
                else:
                    st.success("✅ NORMAL TRAFFIC")

                st.write(result["message"])

                st.metric(
                    "Predicted Class",
                    result["class_label"]
                )

            else:
                st.error(
                    f"API Error {response.status_code}: "
                    f"{response.text}"
                )

        except requests.RequestException as error:
            st.error(f"Could not connect to API: {error}")

st.divider()

st.caption(
    "Network Intrusion Detection System | "
    "KNN + FastAPI + Streamlit | Experimental prototype"
)
