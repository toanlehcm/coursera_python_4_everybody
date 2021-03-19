def computepay(fh,fr):
    if fh > 40:
        reg = fh * fr
        otp = (fh - 40) * (fr * 0.5)
        return reg + otp
    else: 
        return fh * fr

hours = input("Enter Hours: ")
rates = input("Enter rate: ")
try:
    fhours = float(hours)
    frates = float(rates)
except:
    print("Error, please enter numeric input!")
    quit()

p = computepay(fhours, frates)
print("Pay",p)