from business_profile import BusinessProfile


def calculate_revenue(customers_per_day, average_price, days=30):
    """
    Calculate estimated monthly revenue.
    """
    return customers_per_day * average_price * days


def calculate_variable_cost(
    customers_per_day,
    variable_cost_per_customer,
    days=30
):
    """
    Calculate estimated monthly variable cost.
    """
    return customers_per_day * variable_cost_per_customer * days


def calculate_total_cost(fixed_cost, variable_cost):
    """
    Calculate total monthly cost.
    """
    return fixed_cost + variable_cost


def calculate_profit(revenue, total_cost):
    """
    Calculate estimated monthly profit.
    """
    return revenue - total_cost


def calculate_profit_margin(profit, revenue):
    """
    Calculate profit margin as a percentage.
    """
    if revenue == 0:
        return 0

    return (profit / revenue) * 100


def calculate_break_even_customers(
    fixed_cost,
    average_price,
    variable_cost_per_customer,
    days=30
):
    """
    Calculate the number of customers required per day
    to cover fixed costs.
    """

    contribution_per_customer = (
        average_price - variable_cost_per_customer
    )

    if contribution_per_customer <= 0:
        return None

    monthly_customers = fixed_cost / contribution_per_customer

    return monthly_customers / days


def analyze_business(
    customers_per_day,
    average_price,
    variable_cost_per_customer,
    fixed_cost
):
    """
    Perform a complete basic financial analysis.
    """

    revenue = calculate_revenue(
        customers_per_day,
        average_price
    )

    variable_cost = calculate_variable_cost(
        customers_per_day,
        variable_cost_per_customer
    )

    total_cost = calculate_total_cost(
        fixed_cost,
        variable_cost
    )

    profit = calculate_profit(
        revenue,
        total_cost
    )

    profit_margin = calculate_profit_margin(
        profit,
        revenue
    )

    break_even_customers = calculate_break_even_customers(
        fixed_cost,
        average_price,
        variable_cost_per_customer
    )

    return {
        "monthly_revenue": revenue,
        "monthly_variable_cost": variable_cost,
        "monthly_fixed_cost": fixed_cost,
        "monthly_total_cost": total_cost,
        "monthly_profit": profit,
        "profit_margin": profit_margin,
        "break_even_customers_per_day": break_even_customers
    }


def analyze_business_profile(business: BusinessProfile):
    """
    Analyze a complete BusinessProfile.

    This connects the structured business profile
    to the existing financial analysis engine.
    """

    return analyze_business(
        customers_per_day=business.customers_per_day,
        average_price=business.average_price,
        variable_cost_per_customer=business.variable_cost_per_customer,
        fixed_cost=business.fixed_cost
    )