import pytest
from employee import Employee

@pytest.fixture
def sample_employee():
    return Employee("Test", "User", 50000)

def test_give_default_raise(sample_employee):
    sample_employee.give_raise()
    assert sample_employee.annual_salary == 55000

def test_give_custom_raise(sample_employee):
    sample_employee.give_raise(8000)
    assert sample_employee.annual_salary == 58000
