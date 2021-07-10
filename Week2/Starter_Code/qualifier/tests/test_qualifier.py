# Import pathlib
from pathlib import Path

#Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators

# Import Filters
from qualifier.filters import credit_score
from qualifier.filters import debt_to_income
from qualifier.filters import loan_to_value
from qualifier.filters import max_loan_size

def test_save_csv():
    # @TODO: Your code here!
    # Use Path from pathlib to output the test csv to ./data/output/qualifying_loans.csv
    output_path = Path("tests/data/output/qualifying_loans.csv")
    test_data = [
        ['West Central Credit Union - Premier Option', '400000', '0.9', '0.35', '760', '2.7'], 
        ['FHA Fredie Mac - Premier Option', '600000', '0.9', '0.43', '790', '3.6'], 
        ['FHA Fannie Mae - Premier Option', '500000', '0.9', '0.47', '780', '3.6'], 
        ['General MBS Partners - Premier Option', '400000', '0.95', '0.35', '790', '3.0'], 
        ['iBank - Premier Option', '500000', '0.85', '0.46', '780', '3.15'], 
        ['Goldman MBS - Premier Option', '500000', '0.8', '0.4', '770', '3.6'], 
        ['Citi MBS - Premier Option', '400000', '0.9', '0.47', '780', '3.6'], 
        ['Prosper MBS - Premier Option', '400000', '0.85', '0.42', '750', '3.45'], 
        ['Bank of Stodge & Stiff - Premier Option', '500000', '0.9', '0.41', '790', '3.15']
    ]
    fileio.save_csv(output_path, test_data)
    read_data = fileio.load_csv(output_path)
    assert len(test_data) == len(read_data)
    for i in range(0, len(test_data)):
        for j in range(0, len(test_data[i])):
            assert test_data[i] == read_data[i]

def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

def test_filters():
    bank_data = fileio.load_csv(Path('./data/daily_rate_sheet.csv'))
    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000

    monthly_debt_ratio = 0.375

    loan_to_value_ratio = 0.84

    # @TODO: Test the new save_csv code!
    # YOUR CODE HERE!
    test_calculate_monthly_debt_ratio()
    test_calculate_loan_to_value_ratio()
    test_save_csv()

test_filters()
