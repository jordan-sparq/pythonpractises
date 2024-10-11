# Bigquery dry run

# This script shows how to write your own decorator which can be used in integration tests. This will dry run
# your bigquery SQL without returning a result. If the query fails it will raise an exception.

from functools import wraps
import pytest
from google.cloud import bigquery

class QuerySucceeded(Exception):
    """Exception raised for a successful query in the context of BigQuery testing.

    Attributes:
        message -- explanation of the exception
    """

    def __init__(self, message="Query succeeded."):
        self.message = message
        super().__init__(self.message)


def bq_dry_run(test_func):
    """Decorator that should be used on all BQ query integration tests.
    When making a `dry_run` query call, the query isn't actually made as a Job in the BQ backend,
    so calls of `.result()` or `.to_dataframe()` will return a `404 Not Found` error, as the job is
    not found. This happens _after any errors resulting from the query (say SQL format error) are_
    raised. So by wrapping all tests in an assertion that checks the `NotFound` is raised, we
    resolve this issue.
    If wanted to use other decorators on the test, e.g. `@pytest.mark.parametrize` calls, then you
    must put the @bq_dry_run decorator to apply first (most inward decorator).
    E.g.:

    >>> @pytest.mark.parametrize("package", [True, False])
    >>> @bq_dry_run
    >>> def test_validity_get_sql(package):
    >>> '''Test 'get' query is valid.'''
    >>> _ = bigquery.Client().query(active_hotels.get_sql(package=package)).to_dataframe()

    """

    @wraps(test_func)
    def test_wrapper(*args, **kwargs):
        with pytest.raises(QuerySucceeded):
            test_func(*args, *kwargs)
    return test_wrapper