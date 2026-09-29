from app.business_profile import BusinessProfile


def test_business_profile():

    business = BusinessProfile(
        business_type="Cafe",
        location="Dehradun",
        capital=100000,
        customers_per_day=40,
        average_price=80,
        variable_cost_per_customer=45,
        fixed_cost=25000
    )

    assert business.business_type == "Cafe"
    assert business.location == "Dehradun"
    assert business.capital == 100000
    assert business.customers_per_day == 40
    assert business.average_price == 80
    assert business.variable_cost_per_customer == 45
    assert business.fixed_cost == 25000


def test_business_profile_dictionary():

    business = BusinessProfile(
        business_type="Cafe",
        location="Dehradun",
        capital=100000,
        customers_per_day=40,
        average_price=80,
        variable_cost_per_customer=45,
        fixed_cost=25000
    )

    data = business.to_dict()

    assert data["business_type"] == "Cafe"
    assert data["location"] == "Dehradun"
    assert data["capital"] == 100000