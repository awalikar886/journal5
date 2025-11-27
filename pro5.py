import sys

if len(sys.argv) == 4:
    script_name = sys.argv[0]
    principal = float(sys.argv[1])
    rate = float(sys.argv[2])
    time = float(sys.argv[3])
    print("User provided input values:")
else:
    script_name = sys.argv[0]
    principal = 10000.0   
    rate = 5.0            
    time = 2.0           
    print("No input given — using default values:")

 
simple_interest = (principal * rate * time) / 100

 
print("\n--- Simple Interest Calculation ---")
print("Script Name:", script_name)
print("Principal Amount:", principal)
print("Rate of Interest (%):", rate)
print("Time Period (years):", time)
print("Simple Interest:", simple_interest)