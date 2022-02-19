import pytest
from src.sorting import sort_by

mock_jobs = [
    {"date_posted": "2021-05-05", "max_salary": 4000, "min_salary": 400},
    {"date_posted": "2021-03-03", "max_salary": 6000, "min_salary": 600},
    {"date_posted": "2021-01-01", "max_salary": 5000, "min_salary": 500},
    {"date_posted": "2021-12-12", "max_salary": 2000, "min_salary": 200},
    {"date_posted": "2021-08-08", "max_salary": 3000, "min_salary": 300},
    {"date_posted": "2021-06-06", "max_salary": 1000, "min_salary": 100},
]

mock_sorted_by_min_salary = [
  {"date_posted": "2021-06-06", "max_salary": 1000, "min_salary": 100},
  {"date_posted": "2021-12-12", "max_salary": 2000, "min_salary": 200},
  {"date_posted": "2021-08-08", "max_salary": 3000, "min_salary": 300},
  {"date_posted": "2021-05-05", "max_salary": 4000, "min_salary": 400},
  {"date_posted": "2021-01-01", "max_salary": 5000, "min_salary": 500},
  {"date_posted": "2021-03-03", "max_salary": 6000, "min_salary": 600},
]

mock_sorted_by_max_salary = [
  {"date_posted": "2021-03-03", "max_salary": 6000, "min_salary": 600},
  {"date_posted": "2021-01-01", "max_salary": 5000, "min_salary": 500},
  {"date_posted": "2021-05-05", "max_salary": 4000, "min_salary": 400},
  {"date_posted": "2021-08-08", "max_salary": 3000, "min_salary": 300},
  {"date_posted": "2021-12-12", "max_salary": 2000, "min_salary": 200},
  {"date_posted": "2021-06-06", "max_salary": 1000, "min_salary": 100},
]

mock_sorted_by_date_posted = [
  {"date_posted": "2021-12-12", "max_salary": 2000, "min_salary": 200},
  {"date_posted": "2021-08-08", "max_salary": 3000, "min_salary": 300},
  {"date_posted": "2021-06-06", "max_salary": 1000, "min_salary": 100},
  {"date_posted": "2021-05-05", "max_salary": 4000, "min_salary": 400},
  {"date_posted": "2021-03-03", "max_salary": 6000, "min_salary": 600},
  {"date_posted": "2021-01-01", "max_salary": 5000, "min_salary": 500},
]


def test_sort_by_criteria():
    sort_by(mock_jobs, "min_salary")
    assert mock_jobs == mock_sorted_by_min_salary

    sort_by(mock_jobs, 'max_salary')
    assert mock_jobs == mock_sorted_by_max_salary

    sort_by(mock_jobs, 'date_posted')
    assert mock_jobs == mock_sorted_by_date_posted

    criteria = 'job_type'
    with pytest.raises(ValueError):
        sort_by(mock_jobs, criteria)
