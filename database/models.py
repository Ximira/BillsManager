class Bills:
    title = ''
    value = 0.0
    paid_out_at = None
    expiration = None
    bill_file = None
    receipt_file = None 
    bill_type = Payment()
    company = Conpany()
    description_bill = ''


class Payment:
    name_type = ''
    description_payment = ''


class Company:
    name_company = ''
    description_company = ''