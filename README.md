# FinalAssignment

The quarterpiapproximation.py Python script approximates the value of 1/4 of π using the Leibniz formula for π (https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80) and stores the results locally in a MySQL DB. It also submits the exact time of when the script started the execution and when it finished executing to a remote server using the Python socket module.

The qpiserver.py is a Python based TCP server script that receives incoming data about the script execution and saves it in a local file. 
