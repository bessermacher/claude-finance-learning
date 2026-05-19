TEST_ENTRIES = [
    # 1. Clean baseline
    "Posted 12,500 EUR to office supplies (acc 642100), cost center 4200, period March 2026.",

    # 2. Polish language mixed in
    "Księgowanie: 8.450,00 PLN na koszty marketingu, MPK 5100, marzec 2026, faktura FV/2026/03/127.",

    # 3. Number as words + missing CC
    "Charged twelve thousand euros to legal fees account 644200 for Q1 2026. Cost center TBD.",

    # 4. Negative/credit entry, revenue
    "Credit to revenue account 700100, -45,800 EUR, profit center PL_WARSAW, 2026-03-31.",

    # 5. European decimal/thousand separator
    "Travel expenses 1.234,56 EUR — acc 645300 — CC 4200 — period 03.2026.",

    # 6. Multi-line accrual
    "Accrual booking March close:\n- Account: 491000 (accrued expenses)\n- Amount: EUR 23 750\n- Cost center: 6100\n- Description: Q1 audit fees, KPMG",

    # 7. FX conversion needed
    "Reimbursement 5000 PLN at rate 4.32, posted to acc 645100, CC 4200, March 2026.",

    # 8. Ambiguous period
    "Office rent last month, 15k EUR, account 641100, cost center 4200.",

    # 9. Direction unclear (reversal)
    "Reversed marketing accrual, 8200 EUR, acc 491000, CC 5100, period 2026-03.",

    # 10. Polish accounting shorthand
    "WB 03/2026: opłata bankowa 127,50 EUR, konto 751000, MPK ogólny 9000.",
]