"""
Создайте класс с описанием любой компании.
К примеру тошиба или глобал лоджик. Company.
"""


class Company:
    def __init__(self,
                 name: str,
                 head_name: str,
                 foundation_year: int,
                 budget: int,
                 employees_amount: int,
                 industry: str
                 ):
        self.name = name
        self.head_name = head_name
        self.foundation_year = foundation_year
        self.budget = budget
        self.employees_amount = employees_amount
        self.industry = industry


Toshiba: Company = Company("Toshiba", "Satoshi Tsunakawa", 1875, 1000000000,
                           188000, "Electronics")


if __name__ == '__main__':
    print(Toshiba.name, Toshiba.head_name, Toshiba.foundation_year,
          Toshiba.budget, Toshiba.employees_amount, Toshiba.industry)

# Good but I can change name of company from anyware
# Toshiba.name = "Global Logic"
# You should hide your fields which should not be changed from outside of class -2 points
# I see state in this class but does not see methods which modify it -2 points
