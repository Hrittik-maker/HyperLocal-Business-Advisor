from app.financial_engine import analyze_business, analyze_business_profile
from app.what_if_engine import run_scenario
from app.business_profile import BusinessProfile


def test_basic_business_analysis():

    result = analyze_business(
        customers_per_day=40,
        average_price=80,
        variable_cost_per_customer=45,
        fixed_cost=25000
    )

    assert result["monthly_revenue"] == 96000
    assert result["monthly_variable_cost"] == 54000
    assert result["monthly_total_cost"] == 79000
    assert result["monthly_profit"] == 17000
    assert round(result["profit_margin"], 2) == 17.71


def test_business_with_loss():

    result = analyze_business(
        customers_per_day=20,
        average_price=80,
        variable_cost_per_customer=45,
        fixed_cost=25000
    )

    assert result["monthly_profit"] < 0


def test_impossible_break_even():

    result = analyze_business(
        customers_per_day=40,
        average_price=40,
        variable_cost_per_customer=50,
        fixed_cost=25000
    )

    assert result["break_even_customers_per_day"] is None


def test_customer_decline_scenario():

    result = run_scenario(
        customers_per_day=40,
        average_price=80,
        variable_cost_per_customer=45,
        fixed_cost=25000,
        customer_change_percent=-20
    )

    assert result["monthly_revenue"] == 76800
    assert result["monthly_profit"] == 8600


def test_business_profile_analysis():

    business = BusinessProfile(
        business_type="Cafe",
        location="Dehradun",
        capital=100000,
        customers_per_day=40,
        average_price=80,
        variable_cost_per_customer=45,
        fixed_cost=25000
    )

    result = analyze_business_profile(business)

    assert result["monthly_revenue"] == 96000
    assert result["monthly_profit"] == 17000