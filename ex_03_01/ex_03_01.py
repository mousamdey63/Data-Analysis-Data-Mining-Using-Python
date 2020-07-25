hrs = input("Enter Hours:")
rate = input("Enter Rate:")
fhrs = float(hrs)
frate = float(rate)
if fhrs>40:
    reg = fhrs*frate
    otp = (fhrs-40.0)*(frate*0.5)
    xp = reg+otp
else:
    xp = fhrs*frate
print("Pay:",xp)
