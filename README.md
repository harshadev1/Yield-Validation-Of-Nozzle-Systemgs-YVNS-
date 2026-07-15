Yield Validation of Nozzle Systems (YVNS)
Video Demo: https://www.youtube.com/watch?v=F24i1TkhmxQ
Description
Yield Validation of Nozzle Systems (YVNS) is a Python-based engineering application developed as my final project for Harvard University's CS50's Introduction to Programming with Python (CS50P).

The primary objective of this project is to analyze fuel flow distribution inside a 12-nozzle gas turbine fuel manifold. Uniform fuel distribution is one of the most important factors affecting combustion efficiency, emissions, flame stability, and overall gas turbine performance. Even small pressure differences caused by changes in elevation can influence the amount of fuel delivered through individual nozzles. This software simulates these effects and provides engineers with an easy way to validate the performance of a nozzle system before operation.

Rather than performing repetitive engineering calculations manually, YVNS automates the complete analysis process. The user only needs to enter the required manifold parameters(Flow rate and nozzle choice), after which the software calculates nozzle pressures, pressure drops, individual nozzle flow rates, average values, and overall flow distribution statistics.

Project Idea
The idea for this project came from my father, who shared a real-world challenge he encountered while validating fuel distribution in gas turbine fuel manifolds.

His experience inspired me to develop a Python application that automates these repetitive engineering calculations, making the validation process faster, more efficient, and less prone to manual errors.

Features
YVNS performs several engineering calculations in a single execution.

The software is capable of:

Accepting user-defined manifold pressure
Computing static elevation pressure losses
Calculating effective pressure available at every nozzle
Determining pressure drop across each nozzle
Solving the fuel flow equation
Computing the individual flow rate of all twelve nozzles
Producing a complete engineering report
Computing average pressure
Computing average pressure drop
Computing average flow rate
Calculating overall percentage flow imbalance
Calculating deviation of each nozzle from the mean flow
Displaying all results in a clean tabular format
Engineering Principle
The project is based on a simple engineering principle.

Pressure decreases with elevation due to the hydrostatic relationship

Static Elevation Pressure = Density × Gravity × Height

The available pressure at every nozzle becomes

Available Pressure = Manifold Pressure − Static Elevation Pressure

The pressure drop across each nozzle is then determined, after which the nozzle flow equation is solved to determine fuel flow rate.

Because every nozzle sits at a unique elevation, each nozzle experiences a slightly different pressure and therefore a slightly different flow rate.

Project Structure
The project is organized into multiple functions, each responsible for a specific engineering calculation to make it way easier.

main()
Acts as the controller of the application.

It:

Displays the program banner
Collects user input
Calls all engineering calculation functions
Stores the results
Prints the engineering report
Handles unexpected errors gracefully
static_elevation(height)
This function calculates the pressure loss caused by static elevation.

Every nozzle has a predefined elevation value.

Using the hydrostatic equation, the function computes how much pressure is lost before the fuel reaches that nozzle.

This pressure loss is later subtracted from the inlet manifold pressure.

end_result(pressure_drop)
This function converts pressure drop into nozzle fuel flow.

The engineering relationship between pressure drop and flow rate follows the square-root law.

Internally the function computes

Flow Rate = C × sqrt(Pressure Drop)

where C is the experimentally selected discharge coefficient used for the nozzle model.

The square-root relationship closely represents real fluid flow behaviour through an orifice.

convert_hour(value)
This function converts the input flow rate from (pounds/sec) to (pounds/hour).

This conversion is very important as engineers generally measure flow in (pounds/sec) but calculations and everything is easier and fastly done in (pounds/hour)

flow_nozzles(pressure)
This function uses the engineering formula where flow through each nozzle = 100 * sqrt(pressure).

It returns the values to the function where its stored and displayed later.

Input Validation
The software validates all user input before calculations begin.

Examples include:

Numeric pressure values only
Prevention of invalid calculations
Exception handling using try/except
Protection against unexpected program crashes
These validation checks improve software robustness and usability.

Flow Distribution Analysis
After calculating all twelve nozzle flow rates, the software performs additional statistical analysis which turns out to be very helpful for engineers.

It computes

Average nozzle pressure
Average pressure drop
Average nozzle flow rate
Percentage flow imbalance
Flow deviation for every individual nozzle
These statistics allow engineers to evaluate how uniformly fuel is distributed throughout the manifold.

A perfectly balanced manifold would produce nearly identical flow rates across all nozzles.

Dictionary Storage
Nozzle elevations are stored inside a dictionary.

This allows each nozzle number to be associated directly with its elevation while keeping the code clean and readable.

Functions
Rather than placing all calculations inside one large block, every engineering calculation is separated into reusable functions.

This improves readability, testing, and future expansion.

Lists
Calculation results are stored inside a list of dictionaries.

Each dictionary represents one nozzle and stores

nozzle number
elevation
pressure
pressure drop
flow rate
This structure simplifies report generation and statistical calculations.

Mathematical Libraries
The project imports

math
sympy
pyfiglet
math

Used for square-root calculations required by the nozzle flow equation.

sympy

Used wherever symbolic mathematical solving is required.

pyfiglet

Provides the large ASCII title banner (Yield Validation of Nozzle Systems) displayed when the application starts, giving the software a professional command-line interface.

Report Generation
One of the major goals of the project was producing a report that engineers can interpret immediately.

Instead of printing only raw numbers, the software generates a structured report containing every calculated parameter, followed by summary statistics.

This makes the program significantly more useful than a simple calculator.

Challenges During Development
Developing this project required solving several challenges.

The biggest challenge was organizing multiple engineering calculations into clean, reusable Python functions while keeping the program readable.

Another challenge was ensuring every nozzle calculation remained independent while still allowing the software to generate overall manifold statistics.

Careful input validation and exception handling were also implemented to improve reliability.

Conclusion
Yield Validation of Nozzle Systems demonstrates how Python can be applied to solve practical engineering problems beyond traditional programming exercises.

The project combines engineering principles, mathematical calculations, data processing, and software design into a single application capable of performing meaningful analysis of a gas turbine fuel manifold.

Developing this project strengthened my understanding of Python programming, modular software design, input validation, mathematical computation, and engineering automation. It also showed how programming can simplify complex calculations that would otherwise require significant manual effort.

This project represents my successful completion of Harvard University's CS50P Final Project and demonstrates the application of Python to a real-world engineering problem.
