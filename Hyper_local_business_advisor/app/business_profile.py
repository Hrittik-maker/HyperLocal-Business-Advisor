class BusinessProfile:
    def __init__(
        self,
        business_type,
        location,
        capital,
        customers_per_day,
        average_price,
        variable_cost_per_customer,
        fixed_cost
    ):
        self.business_type = business_type
        self.location = location

        self.capital = capital

        self.customers_per_day = customers_per_day
        self.average_price = average_price
        self.variable_cost_per_customer = variable_cost_per_customer
        self.fixed_cost = fixed_cost

    def to_dict(self):
        """
        Convert the business profile into a dictionary.
        Useful later for databases, APIs and AI systems.
        """

        return {
            "business_type": self.business_type,
            "location": self.location,
            "capital": self.capital,
            "customers_per_day": self.customers_per_day,
            "average_price": self.average_price,
            "variable_cost_per_customer": self.variable_cost_per_customer,
            "fixed_cost": self.fixed_cost
        }