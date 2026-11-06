"""VAT for customer invoices (FIN-14).

Domestic energy is VAT-rated at 5%. Per the finance handbook, VAT is calculated
per invoice line and rounded half up to the nearest penny; the invoice's VAT
total is the sum of the line amounts.
"""

from __future__ import annotations

from invoicing.models import Invoice

VAT_RATE_PCT = 5


def line_vat(amount_pence: int) -> int:
    """VAT due on one invoice line, in whole pence, rounded half up."""
    return round(amount_pence * VAT_RATE_PCT / 100)


def invoice_vat(invoice: Invoice) -> int:
    """The invoice's total VAT, in whole pence."""
    return round(invoice.total_pence() * VAT_RATE_PCT / 100)


def invoice_total_with_vat(invoice: Invoice) -> int:
    """What the customer pays: the pre-VAT total plus VAT."""
    return invoice.total_pence() + invoice_vat(invoice)