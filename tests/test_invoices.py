from datetime import date

from invoicing.models import Invoice, InvoiceLine


def test_total_sums_all_lines() -> None:
    invoice = Invoice("inv_0001", "cus_0001", date(2026, 10, 1), date(2026, 10, 31))
    invoice.lines.append(InvoiceLine("Day units", 11_250))
    invoice.lines.append(InvoiceLine("Night units", 4_380))
    invoice.lines.append(InvoiceLine("Standing charge", 1_200))

    assert invoice.total_pence() == 16_830


def test_invoice_without_lines_totals_zero() -> None:
    invoice = Invoice("inv_0002", "cus_0002", date(2026, 10, 1), date(2026, 10, 31))

    assert invoice.total_pence() == 0
