from datetime import date

from invoicing.models import Invoice, InvoiceLine
from invoicing.vat import invoice_total_with_vat, invoice_vat, line_vat


def invoice(*lines: InvoiceLine) -> Invoice:
    inv = Invoice("inv_0001", "cus_0001", date(2026, 10, 1), date(2026, 10, 31))
    inv.lines.extend(lines)
    return inv


def test_line_vat_is_five_percent_rounded_to_the_penny() -> None:
    assert line_vat(200) == 10
    assert line_vat(125) == 6  # 6.25p rounds to 6p
    assert line_vat(333) == 17  # 16.65p rounds to 17p


def test_invoice_vat_total() -> None:
    inv = invoice(InvoiceLine("Day units", 200), InvoiceLine("Standing charge", 125))

    assert invoice_vat(inv) == 16  # 10 + 6
    assert invoice_total_with_vat(inv) == 341


def test_empty_invoice_has_no_vat() -> None:
    assert invoice_vat(invoice()) == 0
    assert invoice_total_with_vat(invoice()) == 0
