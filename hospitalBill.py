
def calculatedTreatmentBill(a, b, c):
    # Calculate total treatment bill
    total_bill = a + b + c
    return total_bill


def calculateMedicineBill(d, e):
    med_bill = d + e
    gst = med_bill * 5 / 100
    return med_bill + gst


def totalHospitalBill(a, b, c, d, e):
    treatment_bill = calculatedTreatmentBill(a, b, c)
    medicine_bill = calculateMedicineBill(d, e)
    total = treatment_bill + medicine_bill

    print("HOSPITAL BILL DETAILS")
    print("---------------------")
    print(f"Total Treatment Bill = {treatment_bill:.2f}")
    print(f"Total Medicine Bill = {medicine_bill:.2f}")
    print(f"Final payable amount = {total:.2f}")

    return total


totalHospitalBill(1000, 2000, 1500, 500, 300)
