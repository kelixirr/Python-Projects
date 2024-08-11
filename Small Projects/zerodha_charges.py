import math
import matplotlib.pyplot as plt
def zerodha_charges(amount, type = "delivery", market = "NSE", intent = "buy"):
    if amount <= 0:
        print("Enter positive invested amount")

    brokerage = 0
    stamp = 0
    transaction =  0
    stt_ed, stt_id  = amount * 0.001, 0
    if intent == "sell":
        stt_id = amount * 0.00025
    if market == "NSE":
        transaction = amount * 0.0000322
    elif market == "BSE":
        transaction = amount * 0.0000375
    else:
        print("Valida Markets: NSE or BSE")

    dp_charges = 13 + 13 * 0.18 if type == "delivery" and intent == "sell" else 0
    if amount >= 10000000:
        sebi = 10 * math.floor(amount / 10000000)
    else:
        sebi = 0

    if type == "intraday":
        brokerage = min(amount * 0.0003, 20)
        stamp = min(amount * 0.00003, 300 * math.floor(amount / 10000000)) if intent == "buy" else 0

    elif type == "delivery":
        brokerage = 0
        stamp = min(amount * 0.00015, 1500 * math.floor(amount / 10000000)) if intent == "buy" else 0

    gst = 0.18 * (brokerage + sebi + transaction)
    charges = brokerage + (stt_ed if type == "delivery" else stt_id) + transaction + sebi + stamp + gst + dp_charges
    profit = amount - charges

    print(f"For your invested amount of {amount}, approximate final payout will be: {profit:.4f}")
    print(f"Your total charges will be:{charges:.4f}\n")
    print(f"Charges brekadown:")

    if type == "intraday":
        print(f"Brokerage:{brokerage:.4f}")
        print(f"STT/CTT:{stt_id:.4f}")
        print(f"Transaction:{transaction:.4f}")
        print(f"Stamp:{stamp:.4f}")
        print(f"Sebi:{sebi}")
        print(f"GST:{gst:.4f}")
    else:
        print(f"Brokerage:{brokerage:.4f}")
        print(f"STT/CTT:{stt_ed:.4f}")
        print(f"DP charges:{dp_charges}")
        print(f"Transaction:{transaction:.4f}")
        print(f"Stamp:{stamp:.4f}")
        print(f"Sebi:{sebi}")
        print(f"GST:{gst:.4f}")

    print("Note: Zerodha also charges Annual account maintaince fee which can go upto Rs 300 for Individuals")

if __name__ == "__main__":
    zerodha_charges(20000500, type = "intraday", market = "BSE", intent = "buy")
