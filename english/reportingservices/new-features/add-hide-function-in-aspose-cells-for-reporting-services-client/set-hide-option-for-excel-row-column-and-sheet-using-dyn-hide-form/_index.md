---
title: Set Hide Option for Excel Row, Column and Sheet using Dyn‑Hide Form
type: docs
weight: 20
url: /reportingservices/set-hide-option-for-excel-row-column-and-sheet-using-dyn-hide-form/
ai_search_scope: cells_reportingservices
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Overview  

Aspose.Cells for Reporting Services allows you to hide specific rows, columns, or entire worksheets in the Excel workbook that is generated from a report. This is achieved through the **Dyn‑Hide** form, which reads hide parameters supplied as report parameters.

> **Note**  
> The hide parameters are processed **only** when they are passed as **Reporting Services report parameters**. They are not evaluated when set directly in the workbook via code.

## Hide Parameters  

| Parameter | Description | Required | Example |
|-----------|-------------|----------|---------|
| **SheetName** | Name of the worksheet that contains the object to hide. | Yes (except when `Type = worksheet`) | `SalesData` |
| **Type** | Kind of object to hide. Acceptable values: `row`, `column`. | Yes | `row` |
| **Row/Column Index** | Index of the row or column to hide. For columns you can use the letter notation (A, B, …). Index starts at **1**. When `Type = worksheet` this value is ignored. | No (required for `row`/`column`) | `5` (row 5) or `C` (column C) |
| **HideState** | Determines the hide state. Accepts `true`, `false`, or a **valid Excel formula** that evaluates to TRUE/FALSE. | Yes | `true` or `=ISBLANK(A5)` |

**## Visual Guide -  Specifying hide options**  

![todo:image_alt_text](set-hide-option-for-excel-row-column-and-sheet-using-dyn-hide-form_1.png)
