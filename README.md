# IPM

This project was chosen given the available data, and the ability to verify and test
the suggestions put forth by the program using virtual currency in the popular MMO EVE Online. This is to be used to work with the completely human driven market, which is widely considered to be one of the most complex and realistic virtual markets.

What started this was a desire to learn how to use Python to analyse large amounts of data, automatically perform statistics, visualise the results, and the potential to add Machine Learning at a later point. Another benefit of the project was learning how to utilise a database that is automatically populated with data, organised, then analysed. 

As real world commodity markets would require large amounts of capital and financial risk in order to test the performance of the application, a virtual market was utilised.

Dependencies:

EsiPy
NumPy
Pandas
SqlAlchemy
oauth
futurerequests

--------------------------

EsiPY is used as a parser on the received JSON file, in order to learn the structure of the API received.
NumPy and PANDAS are used for large scale data manipulation and statistics.

SQLalchemy is used in place of writing raw SQL code, and is highly flexible with the type of database used.

The application was tested with an SQLite database, although this can be configured to work with any database format you wish, simply by changing the database code at the start under: create_engine = engine(sqlite....) -- hence the choice to use SQLalchemy, for its flexibility and time saved over writing SQL code.

futurerequests is used to streamline the performance of several requests from the API.
