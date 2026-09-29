import streamlit as st

from financial_engine import analyze_business_profile
from what_if_engine import run_scenario
from business_profile import BusinessProfile


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="HyperLocal Business Advisor",
    page_icon="📊",
    layout="wide"
)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("📊 HyperLocal Business Advisor")

st.write(
    "Analyze the basic financial feasibility of a business."
)


# --------------------------------------------------
# BUSINESS INFORMATION
# --------------------------------------------------

st.header("Business Information")

col1, col2 = st.columns(2)


with col1:

    business_type = st.text_input(
        "Business Type",
        placeholder="e.g. Dairy Shop"
    )

    location = st.text_input(
        "Location",
        placeholder="e.g. Meerut"
    )

    customers_per_day = st.number_input(
        "Expected Customers per Day",
        min_value=0,
        value=40
    )

    average_price = st.number_input(
        "Average Selling Price (₹)",
        min_value=0.0,
        value=80.0
    )


with col2:

    variable_cost = st.number_input(
        "Variable Cost per Customer (₹)",
        min_value=0.0,
        value=45.0
    )

    fixed_cost = st.number_input(
        "Fixed Monthly Cost (₹)",
        min_value=0.0,
        value=25000.0
    )

    capital = st.number_input(
        "Available Capital (₹)",
        min_value=0.0,
        value=200000.0
    )


# --------------------------------------------------
# ANALYZE BUTTON
# --------------------------------------------------

st.divider()

analyze_button = st.button(
    "🔍 Analyze Business",
    type="primary"
)


# --------------------------------------------------
# RUN INITIAL ANALYSIS
# --------------------------------------------------

if analyze_button:

    if not business_type:

        st.warning("Please enter the business type.")

    elif not location:

        st.warning("Please enter the location.")

    else:

        # Create a structured business profile
        business = BusinessProfile(
            business_type=business_type,
            location=location,
            capital=capital,
            customers_per_day=customers_per_day,
            average_price=average_price,
            variable_cost_per_customer=variable_cost,
            fixed_cost=fixed_cost
        )

        # Analyze the structured business profile
        result = analyze_business_profile(business)

        # Store both profile and analysis
        st.session_state["business_profile"] = business
        st.session_state["business_result"] = result

        # Clear any previous scenario
        st.session_state.pop("scenario_result", None)


# --------------------------------------------------
# DISPLAY BUSINESS ANALYSIS
# --------------------------------------------------

if "business_result" in st.session_state:

    result = st.session_state["business_result"]

    st.header("Business Analysis")


    # ----------------------------------------------
    # MAIN FINANCIAL METRICS
    # ----------------------------------------------

    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Monthly Revenue",
            f"₹{result['monthly_revenue']:,.0f}"
        )


    with col2:

        st.metric(
            "Monthly Cost",
            f"₹{result['monthly_total_cost']:,.0f}"
        )


    with col3:

        st.metric(
            "Monthly Profit",
            f"₹{result['monthly_profit']:,.0f}"
        )


    # ----------------------------------------------
    # SECONDARY METRICS
    # ----------------------------------------------

    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            "Profit Margin",
            f"{result['profit_margin']:.2f}%"
        )


    with col2:

        break_even = result[
            "break_even_customers_per_day"
        ]

        if break_even is not None:

            st.metric(
                "Break-even Customers / Day",
                f"{break_even:.1f}"
            )

        else:

            st.metric(
                "Break-even Customers / Day",
                "Not achievable"
            )


    # ----------------------------------------------
    # BASIC INTERPRETATION
    # ----------------------------------------------

    st.divider()

    st.subheader("Initial Interpretation")


    if result["monthly_profit"] > 0:

        st.success(
            "The current assumptions produce a positive "
            "estimated monthly profit."
        )

    elif result["monthly_profit"] == 0:

        st.warning(
            "The business is approximately at break-even "
            "under these assumptions."
        )

    else:

        st.error(
            "The current assumptions produce an estimated "
            "monthly loss."
        )


    # ==================================================
    # WHAT-IF SIMULATOR
    # ==================================================

    st.divider()

    st.header("🔬 What-If Simulator")

    st.write(
        "Explore how changing your business assumptions "
        "could affect financial performance."
    )


    # ----------------------------------------------
    # SCENARIO INPUTS
    # ----------------------------------------------

    st.subheader("Change Your Assumptions")

    col1, col2 = st.columns(2)


    with col1:

        customer_change = st.slider(
            "Change in Customers (%)",
            min_value=-50,
            max_value=50,
            value=0,
            step=5
        )

        price_change = st.slider(
            "Change in Selling Price (%)",
            min_value=-30,
            max_value=30,
            value=0,
            step=5
        )


    with col2:

        variable_cost_change = st.slider(
            "Change in Variable Cost (%)",
            min_value=-30,
            max_value=50,
            value=0,
            step=5
        )

        fixed_cost_change = st.slider(
            "Change in Fixed Cost (%)",
            min_value=-30,
            max_value=50,
            value=0,
            step=5
        )


    # ----------------------------------------------
    # RUN SCENARIO BUTTON
    # ----------------------------------------------

    run_scenario_button = st.button(
        "🚀 Run Scenario"
    )


    if run_scenario_button:

        scenario = run_scenario(

            customers_per_day=customers_per_day,

            average_price=average_price,

            variable_cost_per_customer=variable_cost,

            fixed_cost=fixed_cost,

            customer_change_percent=customer_change,

            price_change_percent=price_change,

            variable_cost_change_percent=variable_cost_change,

            fixed_cost_change_percent=fixed_cost_change
        )

        st.session_state["scenario_result"] = scenario


    # ----------------------------------------------
    # DISPLAY SCENARIO RESULTS
    # ----------------------------------------------

    if "scenario_result" in st.session_state:

        scenario = st.session_state["scenario_result"]


        st.subheader("Scenario Results")


        col1, col2, col3 = st.columns(3)


        with col1:

            revenue_change = (
                scenario["monthly_revenue"]
                - result["monthly_revenue"]
            )

            st.metric(
                "Scenario Revenue",
                f"₹{scenario['monthly_revenue']:,.0f}",
                delta=f"₹{revenue_change:,.0f}"
            )


        with col2:

            cost_change = (
                scenario["monthly_total_cost"]
                - result["monthly_total_cost"]
            )

            st.metric(
                "Scenario Cost",
                f"₹{scenario['monthly_total_cost']:,.0f}",
                delta=f"₹{cost_change:,.0f}"
            )


        with col3:

            profit_change = (
                scenario["monthly_profit"]
                - result["monthly_profit"]
            )

            st.metric(
                "Scenario Profit",
                f"₹{scenario['monthly_profit']:,.0f}",
                delta=f"₹{profit_change:,.0f}"
            )


        st.metric(
            "Scenario Profit Margin",
            f"{scenario['profit_margin']:.2f}%",
            delta=(
                f"{scenario['profit_margin'] - result['profit_margin']:.2f}%"
            )
        )