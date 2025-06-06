# Import the QueryBase class
from .query_base import QueryBase

# Import dependencies needed for sql execution
# from the `sql_execution` module
from .sql_execution import QueryMixin
from typing import List, Tuple
import pandas as pd

# Define a subclass of QueryBase
# called Employee
class Employee(QueryBase):

    # Set the class attribute `name`
    # to the string "employee"
    name = "employee"

    # Define a method called `names`
    # that receives no arguments
    # This method should return a list of tuples
    # from an sql execution
    def names(self) -> List[Tuple[str, int]]:
        """
        Returns a list of employee full names and their IDs.
        """
        # Query 3
        # Write an SQL query
        # that selects two columns 
        # 1. The employee's full name
        # 2. The employee's id
        # This query should return the data
        # for all employees in the database
        query = """
            SELECT first_name || ' ' || last_name AS full_name, employee_id AS id
            FROM employee;
        """
        return self.query(query)

    # Define a method called `username`
    # that receives an `id` argument
    # This method should return a list of tuples
    # from an sql execution
    def username(self, id: int) -> List[Tuple[str]]:
        """
        Returns the full name of the employee with the given ID.
        """
        # Query 4
        # Write an SQL query
        # that selects an employees full name
        # Use f-string formatting and a WHERE filter
        # to only return the full name of the employee
        # with an id equal to the id argument
        query = f"""
            SELECT first_name || ' ' || last_name AS full_name
            FROM employee
            WHERE employee_id = {id};
        """
        return self.query(query)

    # Below is method with an SQL query
    # This SQL query generates the data needed for
    # the machine learning model.
    # Without editing the query, alter this method
    # so when it is called, a pandas dataframe
    # is returns containing the execution of
    # the sql query
    def model_data(self, id: int) -> pd.DataFrame:
        """
        Returns a pandas DataFrame of model training data
        (sum of positive and negative events) for the employee.
        """
        return self.pandas_query(f"""
            SELECT SUM(positive_events) positive_events,
                   SUM(negative_events) negative_events
            FROM employee
            JOIN employee_events
                USING(employee_id)
            WHERE employee.employee_id = {id}
        """)
