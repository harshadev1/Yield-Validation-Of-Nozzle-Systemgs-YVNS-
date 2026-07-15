from math import sqrt
import sympy as solver
from pyfiglet import Figlet
from statistics import median
import sys

figlet = Figlet()
figlet.getFonts()
figlet.setFont(font="big")


def main():
 try:
        print(f"""
YVNS v1.0
        {(figlet.renderText("Yield Validation of Nozzle Systems"))}\n
=====================================================
-Gas Turbine Fuel Manifold Flow Distribution Software-
=====================================================
-> Built for 12 nozzle manifold systems\n

              """)
        print("""Assumptions made:
    * Nozzles are placed symmetrically on a hexagonal manifold.
    * Flow Capacity(Cv) = 100
    * Friction losses in the pipe are ignored for time being.
    * Pressure losses in the fuel nozzle is only considered.
    * Height difference between farthest nozzles is 10ft.
    * Incompressible fuel and Uniform fuel properties.
    * Constant pipe diameter and smooth commercial pipe.
              """)
#many nozzles at once. got to store them and then print em out.
        heights ={ 1: 10,2: 9,3: 6.5,4: 3.5,5: 1,6: 0,7: 0,8: 1,9: 3.5,10: 6.5,11: 9,12: 10}
        operation = int(input("What would you like to do?\n1.Inspect all nozzles\n2.Inspect a specific nozzle\nEnter(1/2): "))
        if operation == 1:
            print("--This tool numbers the nozzles from the top as 1 and goes around the manifold\nin anticlockwise direction and numbers the nozzles accordingly--")
            flow = float(input("Enter the Flow rate(lb/s): "))
            unit = convert_hour(flow)

            MP = solver.symbols("MP")
            flowrate = []
            for height in heights.values():
                PDE = static_elevation(height)
                PD = MP - PDE -14.5
                FLOW = flow_nozzles(PD)
                flowrate.append(FLOW)

            TF = solver.Eq(sum(flowrate), unit)
            guess = 14.5 + ((unit / 12) / 100) ** 2
            result = solver.nsolve(TF, MP, guess)
            results = []
            for nozzle,height in heights.items():
                P = float(result)
                PSE = static_elevation(height)
                P = float(result) - PSE
                PD = P - 14.5
                RATE = end_result(PD)
                results.append({
                "nozzle": nozzle,
                "height": height,
                "pressure": P,
                "pressure_drop": PD,
                "flow": RATE
            })

            print(f"""
--------------------------------------------------------------------
Nozzle   Elevation    Pressure       Pressure Drop     Flow rate
--------------------------------------------------------------------
              """)
            for result1 in results:
                print(
                    f"{result1['nozzle']:>2} "
                    f"{result1['height']:>10} ft"
                    f"{result1['pressure']:>10.2f} Psi"
                    f"{result1['pressure_drop']:>14.2f} Psid"
                    f"{result1['flow']:>12.2f} lb/hr"
                )

            verify = input("Do you want an System Report?(y/n) ")
            if verify.strip() ==  "y":
                    results = []
                    for nozzle,height in heights.items():
                                    P = float(result)
                                    PSE = static_elevation(height)
                                    P = float(result) - PSE
                                    PD = P - 14.5
                                    RATE = end_result(PD)
                                    results.append({
                                    "nozzle": nozzle,
                                    "height": height,
                                    "pressure": P,
                                    "pressure_drop": PD,
                                    "flow": RATE
                                })
        #system report
                    PAVG = sum(_["pressure"] for _ in results)/ 12
                    PDAVG = sum(_["pressure_drop"] for _ in results) / 12
                    AFLOW = sum(_["flow"]for _ in results)/12
                    FLOWS = [_["flow"] for _ in results]
                    Maxf = max(FLOWS)
                    Minf = min(FLOWS)
                    FIMBALANCE = ((Maxf - Minf)/AFLOW)*100
                    MEDF = median(FLOWS)
                    FUNIFORM = (Minf/Maxf)*100
                    print(f"""
==================== SYSTEM REPORT ====================

Average Pressure         : {round(PAVG,2)} psi
Average Pressure Drop    : {round(PDAVG,2)} psid
Average Flow Rate        : {round(AFLOW,2)} lb/hr

Maximum FLow             : {round(Maxf,2)} lb/hr
Minimum Flow             : {round(Minf,2)} lb/hr

Flow Imbalance           : {round(FIMBALANCE,2)}%
Median Flow              : {round(MEDF,2)} lb/hr

Flow Uniformity          : {round(FUNIFORM,2)}%

=======================================================
                  """)

            else:
                 sys.exit(1)

        elif operation == 2:
            print("---This tool numbers the nozzles from the top as 1 and goes around the manifold\nin anticlockwise direction and numbers the nozzles accordingly.---")
            flow = float(input("Enter the Flow rate(lb/s): "))
            unit = convert_hour(flow)
            nozzle_ = int(input("Which nozzle would you like to inspect(1-12): "))


    # MP = Manifold Pressure
    # PDE = Pressure due to Elevation = PSE = pressure due to static elevation
    # PD = Pressure Drop
    # TF = Total Flow
    # P = Pressure at nozzle


            if nozzle_ not in heights:
                print("Enter a valid Nozzle Number")
                return
            else:
                PSE = static_elevation(heights[nozzle_])

            MP = solver.symbols("MP")
            flowrate = []
            for height in heights.values():
                PDE = static_elevation(height)
                PD = MP - PDE -14.5
                FLOW = flow_nozzles(PD)
                flowrate.append(FLOW)

            TF = solver.Eq(sum(flowrate), unit)
            guess = 14.5 + ((unit / 12) / 100) ** 2
            result = solver.nsolve(TF, MP, guess)
            P = float(result)
            PSE = static_elevation(heights[nozzle_])
            P = float(result) - PSE
            PD = P - 14.5
            RATE = end_result(PD)

            print(f"""
    ==============================
    1. Nozzle: {nozzle_}
    2. Pressure: {round(P,2)}Psi
    3. Pressure Drop: {round(PD,2)}Psid
    4. Flow rate through nozzle: {round(RATE,2)}lb/hr
    ==============================
                    """)

#import results
            verify = input("Do you want an System Report?(y/n) ")
            if verify.strip() ==  "y":
                    results = []
                    for nozzle,height in heights.items():
                                    P = float(result)
                                    PSE = static_elevation(height)
                                    P = float(result) - PSE
                                    PD = P - 14.5
                                    RATE = end_result(PD)
                                    results.append({
                                    "nozzle": nozzle,
                                    "height": height,
                                    "pressure": P,
                                    "pressure_drop": PD,
                                    "flow": RATE
                                })
        #system report
                    PAVG = sum(_["pressure"] for _ in results)/ 12
                    PDAVG = sum(_["pressure_drop"] for _ in results) / 12
                    AFLOW = sum(_["flow"]for _ in results)/12
                    FLOWS = [_["flow"] for _ in results]
                    Maxf = max(FLOWS)
                    Minf = min(FLOWS)
                    FIMBALANCE = ((Maxf - Minf)/AFLOW)*100
                    MEDF = median(FLOWS)
                    FUNIFORM = (Minf/Maxf)*100
                    print(f"""
==================== SYSTEM REPORT ====================

Average Pressure         : {round(PAVG,2)} psi
Average Pressure Drop    : {round(PDAVG,2)} psid
Average Flow Rate        : {round(AFLOW,2)} lb/hr

Maximum FLow             : {round(Maxf,2)} lb/hr
Minimum Flow             : {round(Minf,2)} lb/hr

Flow Imbalance           : {round(FIMBALANCE,2)}%
Median Flow              : {round(MEDF,2)} lb/hr

Flow Uniformity          : {round(FUNIFORM,2)}%

=======================================================
                  """)

            else:
                 sys.exit(1)

 except ValueError:
    print("Given Flow rate is too less which results in the fuel not reaching the upper nozzles.\n" \
    "So, please enter a valid Flow rate.")




def convert_hour(value):
    return float(value) * 3600


def static_elevation(n):
    P = 850*9.81*n*0.3048
    return (P/6894.76)



def flow_nozzles(pressure):
    return 100*solver.sqrt(pressure)

def end_result(x):
    value = solver.sqrt(x)
    return (value)*100


if __name__ == "__main__":
    main()
