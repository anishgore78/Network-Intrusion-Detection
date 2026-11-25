
import streamlit as st
import requests

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="NetGuard AI | Intrusion Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

API_URL = "https://network-intrusion-detection-0hoe.onrender.com/predict"
HEALTH_URL = "https://network-intrusion-detection-0hoe.onrender.com/health"


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>
.stApp {
    background-color: #0b1120;
    color: #e5e7eb;
}

[data-testid="stSidebar"] {
    background-color: #111c30;
}

.main-title {
    font-size: 36px;
    font-weight: 800;
    color: #ffffff;
}

.subtitle {
    color: #94a3b8;
    font-size: 16px;
}

.section-title {
    color: #60a5fa;
    font-size: 22px;
    font-weight: 700;
}

.status-card {
    background: #17243a;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #263957;
}

.result-normal {
    background: #12352c;
    border: 1px solid #22c55e;
    padding: 25px;
    border-radius: 12px;
    text-align: center;
}

.result-attack {
    background: #451d27;
    border: 1px solid #ef4444;
    padding: 25px;
    border-radius: 12px;
    text-align: center;
}

div.stButton > button {
    width: 100%;
    background-color: #2563eb;
    color: white;
    border-radius: 9px;
    border: none;
    padding: 12px;
    font-weight: bold;
}

div.stButton > button:hover {
    background-color: #1d4ed8;
    color: white;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# API CONNECTION
# --------------------------------------------------

api_online = False

try:
    health = requests.get(HEALTH_URL, timeout=10)

    if health.status_code == 200:
        api_online = True

except requests.RequestException:
    api_online = False


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.markdown("## 🛡️ NETGUARD AI")
    st.caption("Intelligent Network Security")

    st.divider()

    st.markdown("### System Status")

    if api_online:
        st.success("Backend API Online")
    else:
        st.error("Backend API Offline")

    st.divider()

    st.markdown("### Model Information")

    st.write("**Algorithm:** K-Nearest Neighbors")
    st.write("**Input Features:** 41")
    st.write("**Classification:** Binary")
    st.write("**Classes:** Normal / Attack")

    st.divider()

    st.markdown("### Navigation")

    page = st.radio(
        "Select Page",
        ["Dashboard", "About Model"]
    )

    st.divider()

    st.caption(
        "Experimental cybersecurity prototype"
    )


# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------

if page == "Dashboard":

    st.markdown(
        '<div class="main-title">🛡️ Network Intrusion Detection</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'AI-powered network traffic classification and threat analysis'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    if api_online:
        st.success("Connected to FastAPI backend")
    else:
        st.error("Backend unavailable. Please try again later.")

    # Dashboard metrics

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("ML Algorithm", "KNN")

    with col2:
        st.metric("Input Features", "41")

    with col3:
        st.metric("Prediction Classes", "2")

    st.divider()

    st.markdown(
        '<div class="section-title">Network Traffic Analysis</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Enter the details of a network connection "
        "to classify its traffic."
    )

    # --------------------------------------------------
    # DEFAULT VALUES
    # --------------------------------------------------

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

    features = {}

    # --------------------------------------------------
    # INPUT FORM
    # --------------------------------------------------

    with st.form("traffic_analysis_form"):

        st.markdown("### 🌐 Connection Details")

        col1, col2, col3 = st.columns(3)

        with col1:
            features["protocol_type"] = st.selectbox(
                "Protocol Type",
                ["tcp", "udp", "icmp"]
            )

        with col2:
            features["service"] = st.text_input(
                "Network Service",
                value="http"
            ).strip()

        with col3:
            features["flag"] = st.text_input(
                "Connection Flag",
                value="SF"
            ).strip()

        st.divider()

        # Basic traffic features

        with st.expander("📊 Basic Traffic Features", expanded=True):

            names = [
                "duration",
                "src_bytes",
                "dst_bytes",
                "land",
                "wrong_fragment",
                "urgent"
            ]

            cols = st.columns(3)

            for i, name in enumerate(names):
                with cols[i % 3]:
                    features[name] = st.number_input(
                        name,
                        value=float(numeric_defaults[name]),
                        format="%.4f",
                        key=f"basic_{name}"
                    )

        # Login and content features

        with st.expander("🔐 Login and Content Features"):

            names = [
                "hot",
                "num_failed_logins",
                "logged_in",
                "num_compromised",
                "root_shell",
                "su_attempted",
                "num_root",
                "num_file_creations",
                "num_shells",
                "num_access_files",
                "num_outbound_cmds",
                "is_host_login",
                "is_guest_login"
            ]

            cols = st.columns(3)

            for i, name in enumerate(names):
                with cols[i % 3]:
                    features[name] = st.number_input(
                        name,
                        value=float(numeric_defaults[name]),
                        format="%.4f",
                        key=f"content_{name}"
                    )

        # Connection traffic statistics

        with st.expander("📈 Connection Traffic Statistics"):

            names = [
                "count",
                "srv_count",
                "serror_rate",
                "srv_serror_rate",
                "rerror_rate",
                "srv_rerror_rate",
                "same_srv_rate",
                "diff_srv_rate",
                "srv_diff_host_rate"
            ]

            cols = st.columns(3)

            for i, name in enumerate(names):
                with cols[i % 3]:
                    features[name] = st.number_input(
                        name,
                        value=float(numeric_defaults[name]),
                        format="%.4f",
                        key=f"traffic_{name}"
                    )

        # Destination host statistics

        with st.expander("🖥️ Destination Host Statistics"):

            names = [
                "dst_host_count",
                "dst_host_srv_count",
                "dst_host_same_srv_rate",
                "dst_host_diff_srv_rate",
                "dst_host_same_src_port_rate",
                "dst_host_srv_diff_host_rate",
                "dst_host_serror_rate",
                "dst_host_srv_serror_rate",
                "dst_host_rerror_rate",
                "dst_host_srv_rerror_rate"
            ]

            cols = st.columns(3)

            for i, name in enumerate(names):
                with cols[i % 3]:
                    features[name] = st.number_input(
                        name,
                        value=float(numeric_defaults[name]),
                        format="%.4f",
                        key=f"host_{name}"
                    )

        st.divider()

        analyze = st.form_submit_button(
            "🔍 ANALYZE NETWORK TRAFFIC",
            type="primary",
            use_container_width=True
        )

    # --------------------------------------------------
    # PREDICTION
    # --------------------------------------------------

    if analyze:

        if not features["service"] or not features["flag"]:
            st.error(
                "Please enter both the service and connection flag."
            )

        elif not api_online:
            st.error(
                "Backend API is offline. Please try again later."
            )

        else:

            with st.spinner(
                "Analyzing network traffic using KNN..."
            ):

                try:

                    response = requests.post(
                        API_URL,
                        json={"features": features},
                        timeout=60
                    )

                    if response.status_code == 200:

                        result = response.json()

                        st.divider()

                        st.markdown(
                            "## 🎯 Analysis Result"
                        )

                        if result["class_label"] == "Attack":

                            st.markdown(
                                """
                                <div class="result-attack">
                                    <h1>🚨 ATTACK DETECTED</h1>
                                    <h3>Potential malicious traffic identified</h3>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

                        else:

                            st.markdown(
                                """
                                <div class="result-normal">
                                    <h1>✅ NORMAL TRAFFIC</h1>
                                    <h3>No attack was identified by the model</h3>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

                        st.write("")

                        st.info(result["message"])

                        col1, col2 = st.columns(2)

                        with col1:
                            st.metric(
                                "Predicted Class",
                                result["class_label"]
                            )

                        with col2:
                            st.metric(
                                "Prediction Code",
                                result["prediction"]
                            )

                        st.caption(
                            "This result is an ML classification, "
                            "not a guarantee that traffic is safe."
                        )

                    else:

                        st.error(
                            f"API Error {response.status_code}"
                        )

                        st.code(response.text)

                except requests.RequestException as error:

                    st.error(
                        f"Could not connect to backend: {error}"
                    )


# --------------------------------------------------
# ABOUT MODEL PAGE
# --------------------------------------------------

elif page == "About Model":

    st.markdown(
        '<div class="main-title">About the ML Model</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Understanding the machine learning system'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### 🤖 K-Nearest Neighbors (KNN)")

    st.write(
        """
        K-Nearest Neighbors is a supervised machine learning
        algorithm used for classification.

        It classifies a new network connection by comparing
        it with nearby examples in the training dataset.
        """
    )

    st.markdown("### ⚙️ Project Architecture")

    st.code(
        """
        User Input
             |
             v
        Streamlit Frontend
             |
             v
        FastAPI REST API
             |
             v
        KNN ML Pipeline
             |
             v
        Prediction
        (Normal / Attack)
        """,
        language="text"
    )

    st.markdown("### 📋 Model Details")

    st.write("**Algorithm:** K-Nearest Neighbors")
    st.write("**Dataset:** NSL-KDD")
    st.write("**Features:** 41")
    st.write("**Output:** Normal or Attack")
    st.write("**Preprocessing:** StandardScaler and OneHotEncoder")

    st.warning(
        """
        This project is an experimental machine learning prototype.
        It may misclassify network traffic and should not be used
        as a standalone production security system.
        """
    )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "NETGUARD AI | KNN + FastAPI + Streamlit | "
    "Experimental Network Security Prototype"
)
