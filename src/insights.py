from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    jobs_list = read(path)
    unique_job_types = list(set([job['job_type'] for job in jobs_list]))
    return unique_job_types


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    filtred_jobs = list(
        filter(lambda job: job['job_type'] == job_type, jobs)
    )
    return filtred_jobs


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    jobs_list = read(path)
    industries = list(set([job['industry'] for job in jobs_list]))
    unique_industries = list(filter(None, industries))
    return unique_industries


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    filtred_jobs = list(
        filter(lambda job: job['industry'] == industry, jobs)
    )
    return filtred_jobs


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    jobs_list = read(path)
    max_salary_list = list(set([job['max_salary'] for job in jobs_list]))
    max_salary_list = list(filter(None, max_salary_list))
    max_salary_list = list(
        filter(lambda salary: salary != 'invalid', max_salary_list)
    )
    max_salary_list = list(map(int, max_salary_list))
    max_salary = max(max_salary_list)
    return max_salary


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs_list = read(path)
    min_salary_list = list(set([job['min_salary'] for job in jobs_list]))
    min_salary_list = list(filter(None, min_salary_list))
    min_salary_list = list(
        filter(lambda salary: salary != 'invalid', min_salary_list)
    )
    min_salary_list = list(map(int, min_salary_list))
    min_salary = min(min_salary_list)
    return min_salary


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if 'min_salary' not in job or 'max_salary' not in job:
        raise ValueError

    min = job['min_salary']
    max = job['max_salary']
    if type(salary) != int or type(min) != int or type(max) != int:
        raise ValueError

    if min > max:
        raise ValueError

    if min <= salary <= max:
        return True
    return False


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    def validate_values(job):
        min = job['min_salary']
        max = job['max_salary']
        if type(salary) != int or type(min) != int or type(max) != int:
            return False
        if min <= salary <= max:
            return job

    filtred_jobs = list(
        filter(validate_values, jobs)
    )
    return filtred_jobs
