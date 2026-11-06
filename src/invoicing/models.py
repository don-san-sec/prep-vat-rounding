"""Invoice and invoice-line models."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date


@dataclass
class InvoiceLine:
    """A chargeable line on an invoice.

    Produced by the monthly billing run: day units, night units, the standing
    charge, occasional adjustments. Amounts are whole pence.
    """

    description: str
    amount_pence: int


@dataclass
class Invoice:
    """One customer's monthly invoice. All amounts are whole pence."""

    id: str
    customer_id: str
    period_start: date
    period_end: date
    lines: list[InvoiceLine] = field(default_factory=list)

    def total_pence(self) -> int:
        """The pre-VAT invoice total."""
        return sum(line.amount_pence for line in self.lines)