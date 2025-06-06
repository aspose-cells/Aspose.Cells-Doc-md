---
title: How to Format Number as Currency with C++
linktitle: How to Format Number as Currency
type: docs
weight: 10
url: /cpp/format-number-to-currency/
description: This article will introduce how to format number to currency using Aspose.Cells for C++ API.
keywords: format number as currency, cell number settings, format number to currency, currency settings, currency format.
---

## **Possible Usage Scenarios**
Formatting numbers to currency in Excel is important for several reasons, particularly when working with financial data. Here's why currency formatting is beneficial:

1. **Clarifies Financial Values**: formatting a number as currency makes it clear that the value represents money. For example, instead of seeing 1000, which could mean anything, $1,000 clearly indicates that the value is a monetary amount.
1. **Includes Currency Symbols**: when dealing with international or multiple currencies, formatting numbers with the appropriate currency symbol (e.g., $, €, £) clarifies the type of currency being used, reducing confusion in multi-national financial reports or transactions.
1. **Enhances Professional Presentation**: well-formatted currency values appear polished and professional, which is especially important for reports, presentations, and business documents. $10,000.00 looks more credible and organized than a plain 10000.
1. **Improves Readability**: currency formatting adds commas as thousands separators and decimal places, making large numbers easier to read. For example, 1000000 becomes $1,000,000.00, which is more legible and easier to understand at a glance.
1. **Ensures Consistency**: By applying consistent currency formatting, you ensure all monetary values in a dataset are displayed in the same format. This consistency is important for financial accuracy and for professional communication, especially in large spreadsheets with many numbers.
1. **Shows Precision**: currency formatting typically includes two decimal places, making it easy to see exact monetary amounts. For example, $100.50 is clearly different from $100.00, which is important in financial reports where precision matters.
1. **Simplifies Financial Calculations**: when performing financial calculations (like adding totals or averaging costs), currency formatting helps Excel and users understand that the data is in monetary terms. It helps Excel apply appropriate formatting in formulas and functions, ensuring the results stay consistent.
1. **Reduces Misinterpretation**: without currency formatting, numbers could be misinterpreted as general numerical values rather than amounts of money. For example, 500 could be mistaken as a count of items or units, while $500.00 clearly represents a financial amount.
1. **Works with Accounting Features**: currency formatting aligns well with accounting functions in Excel, such as balance sheets or cash flow reports. It makes the values easier to use in financial statements where money is the primary focus.
<br>
In summary, formatting numbers as currency helps distinguish monetary values from other types of numbers, increases clarity, and makes data easier to interpret, especially in financial contexts.

## **How to Format Number to Currency in Excel**
To format numbers as currency in Excel, follow these steps:

### **Using the Currency Format Option**
1. Select the cells that you want to format as currency.
1. Go to the Home tab on the ribbon.
1. In the Number group, click the dropdown arrow next to the number format box (this might display "General" by default).
<br>
<img src="1.png" width=60% />
1. Choose Currency from the list.

### **Using the Format Cells Dialog Box**
1. Select the cells you want to format.
1. Right-click on the selected cells and choose Format Cells to open the Format Cells dialog box.
1. In the Number tab, select Currency from the list on the left.
<br>
<img src="2.png" width=60% />
1. You can customize the following: Decimal places, Symbol, Negative numbers.
1. Click OK to apply the formatting.

## **How to Format Number to Currency in Aspose.Cells**

To format numbers as currency in Aspose.Cells for C++ library for working with Excel files, you can apply currency formatting to cells programmatically. Here's how you can do it using C++ with Aspose.Cells:

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the cell where you want to apply the currency format
    Cell a1 = worksheet.GetCells().Get(u"A1");

    // Set a numeric value to the cell
    a1.PutValue(1234.56);

    // Create a style object to apply the currency format
    Style a1Style = a1.GetStyle();
    // "7" is the currency format in Excel
    a1Style.SetNumber(7);

    // Apply the style to the cell
    a1.SetStyle(a1Style);

    // Access the cell where you want to apply the currency format
    Cell a2 = worksheet.GetCells().Get(u"A2");

    // Set a numeric value to the cell
    a2.PutValue(3456.78);

    // Create a style object to apply the currency format
    Style a2Style = a2.GetStyle();
    // Custom format for dollar currency
    a2Style.SetCustom(u"$#,##0.00");

    // Apply the style to the cell
    a2.SetStyle(a2Style);

    // Save the workbook
    workbook.Save(u"CurrencyFormatted.xlsx");

    std::cout << "Workbook saved successfully with currency formatting!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```