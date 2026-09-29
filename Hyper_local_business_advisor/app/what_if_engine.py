from financial_engine import analyze_business


def run_scenario(
    customers_per_day,
    average_price,
    variable_cost_per_customer,
    fixed_cost,
    customer_change_percent=0,
    price_change_percent=0,
    variable_cost_change_percent=0,
    fixed_cost_change_percent=0
):
    """
    Run a what-if scenario by modifying the business assumptions.
    """

    # Apply percentage changes
    new_customers = customers_per_day * (
        1 + customer_change_percent / 100
    )

    new_price = average_price * (
        1 + price_change_percent / 100
    )

    new_variable_cost = variable_cost_per_customer * (
        1 + variable_cost_change_percent / 100
    )

    new_fixed_cost = fixed_cost * (
        1 + fixed_cost_change_percent / 100
    )

    # Analyze the modified business
    scenario_result = analyze_business(
        customers_per_day=new_customers,
        average_price=new_price,
        variable_cost_per_customer=new_variable_cost,
        fixed_cost=new_fixed_cost
    )

    return scenario_result