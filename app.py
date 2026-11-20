
import streamlit as st

# --------------------------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="FinSorIQ | Credit Risk Assessment",
    page_icon="🏦",
    layout="wide"
)

# --------------------------------------------------
# 2. APPLICATION HEADER
# --------------------------------------------------

st.title("🏦 FinSorIQ")
st.subheader("AI-Powered Corporate Credit Risk Assessment")

st.markdown(
    """
    Welcome to FinSorIQ.

    Your intelligent platform for corporate financial analysis,
    credit risk assessment and indicative credit rating.
    """
)

st.divider()

# --------------------------------------------------
# 3. SIDEBAR NAVIGATION
# --------------------------------------------------

st.sidebar.title("FinSorIQ Navigation")

st.sidebar.info(
    "Your corporate credit analysis workspace."
)

selected_module = st.sidebar.radio(
    "Select a Module",
    [
        "Home Dashboard",
        "Document Intelligence",
        "Financial Analysis",
        "Financial Ratios",
        "Credit Risk Assessment",
        "PD Modelling",
        "Peer Analysis",
        "Market Intelligence",
        "Credit Rating",
        "Generate Report"
    ]
)

# --------------------------------------------------
# 4. DASHBOARD OVERVIEW
# --------------------------------------------------

st.header("Dashboard Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Companies Analysed",
        value="0"
    )

with col2:
    st.metric(
        label="Reports Generated",
        value="0"
    )

with col3:
    st.metric(
        label="Risk Assessments",
        value="0"
    )

st.divider()

# --------------------------------------------------
# 5. MODULE STATUS
# --------------------------------------------------

st.header("Application Modules")

modules = [
    ("Document Intelligence", "Upload and extract annual reports."),
    ("Financial Analysis", "Analyse historical financial performance."),
    ("Financial Ratios", "Calculate liquidity, leverage and profitability."),
    ("Credit Risk Assessment", "Identify business and financial risks."),
    ("PD Modelling", "Develop and validate default prediction models."),
    ("Peer Analysis", "Compare companies against industry peers."),
    ("Market Intelligence", "Monitor industry and company developments."),
    ("Credit Rating", "Generate an indicative credit risk assessment."),
    ("Report Generation", "Export professional PDF and Excel reports.")
]

for module, description in modules:
    with st.container(border=True):
        st.subheader(module)
        st.write(description)
        st.caption("Development status: Coming soon")

st.divider()

# --------------------------------------------------
# 6. SELECTED MODULE INFORMATION
# --------------------------------------------------

st.header("Workspace")

if selected_module == "Home Dashboard":
    st.success("Welcome to your FinSorIQ home dashboard!")

else:
    st.info(
        f"{selected_module} will be developed in a future phase."
    )

# --------------------------------------------------
# 7. FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "FinSorIQ | Corporate Credit Risk Assessment Platform | "
    "Educational and analytical project"
)
