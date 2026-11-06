# VAT on invoices

VAT on Brightwatt Energy customer invoices: calculating it, rounding it, and
showing it on the bill.

## Context

Brightwatt Energy is an app-first UK domestic energy supplier. About 180,000
customers pay a monthly bill. Each invoice has one or more lines — day units,
night units, the standing charge, occasional adjustments — and every amount is
stored in whole pence.

Domestic energy is VAT-rated at 5%, so every customer invoice carries VAT.

The ticket for this work is FIN-14:

> "Show VAT on every customer invoice at 5%, following the finance handbook's
> rounding rules."

## The finance handbook's VAT rules

These come from the finance team's billing handbook. The invoice our systems
produce must match it exactly, or month-end reconciliation against the finance
ledger fails.

1. VAT is **5%** of the line amount.
2. VAT is calculated **per invoice line** and rounded **half up** to the nearest
   penny. A half penny always rounds up, never down.
3. The invoice's VAT total is the **sum of the line VAT amounts**. It is not
   recalculated on the invoice's pre-VAT total.
4. All arithmetic is done in **whole pence**: calculate with integers, and round
   only where the rules say to round.

Worked examples from the handbook:

- A line of 50p carries 2.5p of VAT, which rounds up to **3p**.
- An invoice with three lines of 10p each carries 0.5p of VAT per line — 1p each
  after rounding — so its VAT total is **3p**.
- A line of 125p carries 6.25p of VAT, which rounds to **6p**.

## How it works

```
src/invoicing/
  models.py           Invoice, InvoiceLine; invoice totals
tests/
```

VAT itself isn't implemented yet. The monthly billing run (not part of this
service) creates invoices; this service owns the invoice model and the
calculations shown on the bill.

## Running locally

```
uv sync
uv run pytest -q
```

## Your task

A colleague has opened a PR: https://github.com/don-san-sec/prep-vat-rounding/pull/1. You are the owner of this feature. Review the PR and decide whether to accept or reject it, and explain why.
