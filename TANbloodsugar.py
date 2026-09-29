TanPatient = {"ana":(80,50,150,90,140,160,40),
           "ben":(130,140,135,90,140,150,165),
           "Carlo":(90,100,95,140,180,95)}
high_count = 0
patientname = ""

for patient, readings in TanPatient.items():
    total = 0
    count = 0
    print("\nPatient: ", patient)

    for reading in readings:
        total += reading
        if reading > 120:
            print(reading, "- high")
            count = count + 1
        else:
            print(reading," - normal")

    avr = total / len(readings)
    diff = max(readings) - min(readings)
    print("NUMBER OF HIGH READINGS - ", count)
    print("MAX READING - ",max(readings))
    print("MINUMUM READING - ", min(readings))
    print(f"AVERAGE READING - {avr}")
    print("DIFFERENCE READING - ", diff)


    if count > high_count:
        high_count = count
        patientname = patient

print("\nThe patient who have the most high blood sugar count is ", patientname)