---
title: Transpose Range
description: This article explains how to transpose or rotate data from rows to columns or vice versa in Excel files using Aspose.Cells for C++ with three different approaches.
linktitle: Transpose Range
url: /cpp/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
keywords: Aspose.Cells, C++ library, spreadsheet, transpose range, rotate data, transpose function, dynamic array formula, array formula, Excel TRANSPOSE, Rows to Columns
type: docs
weight: 80
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for C++ supports transposing (rotating) data so that rows become columns and columns become rows in three different ways. The first approach uses the in-place `Range.Transpose()` method and works on every Excel version, while the second uses `Cell.SetDynamicArrayFormula()` to write a modern dynamic array `=TRANSPOSE(...)` formula that spills automatically on Excel 365 or Excel 2021. The third approach uses `Cell.SetArrayFormula()` to write a classic Ctrl+Shift+Enter (CSE) array formula that is compatible with older Excel versions. This article walks through each approach with step-by-step instructions and complete code examples.
{{% /alert %}}

## **Introduction**
Transposing a range means rotating it so that what was a row becomes a column and what was a column becomes a row, effectively reflecting the data across its main diagonal. In Microsoft Excel, the worksheet function `TRANSPOSE` performs this operation, and the conceptual reference is documented at [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). This concept can be applied programmatically to a range of cells, which is useful in many business and reporting scenarios.
- Re-orienting quarterly or yearly sales reports where quarters normally run across the page and regions down the page, or vice versa.
- Swapping axis orientation in dashboards or charts so that a time series runs down the page instead of across.
- Reshaping data imported from external systems so that it matches the layout expected by downstream analysis or reporting templates.
To make the rest of the article concrete, every example uses the following small sales-by-region-by-quarter table. In the sample workbook this table occupies the range **A1:D5**, with **A1** left empty as the top-left corner, **B1:D1** holding the region headers, and **A2:A5** holding the quarter headers.
| Region            | Europe    | Asia      | North America |
|-------------------|-----------|-----------|---------------|
| Qtr 1             | 21704714  | 8774099   | 12094215      |
| Qtr 2             | 17987034  | 12214447  | 10873099      |
| Qtr 3             | 19485029  | 14356879  | 15689543      |
| Qtr 4             | 22567894  | 15763492  | 17456723      |
The article then presents three different ways to transpose this data using Aspose.Cells for C++, each suited to a different Excel version and use case.

## **Approach 1 — Transpose Range in Place (Range.Transpose)**
Use this approach whenever you want to transpose data without involving the `TRANSPOSE` worksheet function. It works on **every version of Excel** and has no dependency on dynamic arrays, which makes it the safest cross-version compatible option. It is ideal when you only need the final transposed output and do not need to keep the original `TRANSPOSE` formula in the workbook.

### **API used**
`Range.Transpose()` is an instance method on the `Aspose.Cells.Range` class. Calling it flips the range in place by swapping its rows and columns, so what was a row becomes a column and what was a column becomes a row. The method modifies the underlying cells directly without writing a formula.

### **Steps**
1. Open the source workbook with `LoadOptions` set to the `.xlsx` format by creating a `Workbook(srcFile, LoadOptions(LoadFormat::Xlsx))`.
2. Retrieve the first worksheet from the workbook using `workbook.GetWorksheets().Get(0)`.
3. Access the cells collection of the worksheet through `worksheet.GetCells()`.
4. Create the source range covering **A1:D5** by calling `cells.CreateRange(u"A1:D5")`.
5. Call `source.Transpose()` to rotate the range in place, swapping rows and columns.
6. Save the workbook with `workbook.Save(outputFile)`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    U16String srcFile(u"source.xlsx");
    U16String outputFile(u"transposed.xlsx");
    LoadOptions loadOptions(LoadFormat::Xlsx);
    Workbook workbook(srcFile, loadOptions);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    Range source = cells.CreateRange(u"A1:D5");
    source.Transpose();
    workbook.Save(outputFile);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Approach 2 — Transpose with a Dynamic Array Formula (Excel 365 / 2021)**
Use this approach when you want to preserve the `=TRANSPOSE(A1:D5)` formula as a live formula in the output workbook so the result updates automatically if the source data changes, and the target Excel file will be opened in **Excel 365 / Excel 2021 or later** where dynamic arrays and the spill operator are supported.

### **API used**
`Cell.SetDynamicArrayFormula(const char* formula, FormulaParseOptions options, bool calculateValue)` is a method on `Aspose.Cells.Cell` that sets the cell's formula as a **dynamic array formula**. Excel evaluates the formula once and automatically spills the result into the surrounding cells. The third parameter, when set to `true`, instructs Aspose.Cells to also calculate the resulting values at write time.

### **Steps**
1. Load the source workbook by constructing `Workbook(srcFile, LoadOptions(LoadFormat::Xlsx))`.
2. Retrieve the first worksheet via `workbook.GetWorksheets().Get(0)` and access its `Cells` collection through `worksheet.GetCells()`.
3. Place the dynamic array formula on cell **A6**, just below the source range, by calling `cells.Get(u"A6").SetDynamicArrayFormula(u"=TRANSPOSE(A1:D5)", nullptr, true)`.
4. The `nullptr` argument passes default `FormulaParseOptions`, and the third argument `true` tells Aspose.Cells to treat the formula as a dynamic array and to evaluate it so the spilled values are written to the workbook.
5. Save the workbook with `workbook.Save(outputFile)`.
Cell **A6** holds the formula `=TRANSPOSE(A1:D5)` and Excel spills the result automatically into the region **A6:D10**, a 5-row by 4-column block equal to the transposed data.

{{% alert color="primary" %}}
This approach works **only on Excel 365 / 2021 or later**. Older Excel versions will not spill dynamic array formulas correctly.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    std::string srcFile = "source.xlsx";
    std::string outFile = "output_transpose_dynamic.xlsx";
    LoadOptions loadOptions(LoadFormat::Xlsx);
    Workbook workbook(U16String(srcFile.c_str()), loadOptions);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    Cell cell = cells.Get(u"A6");
    FormulaParseOptions options;
    cell.SetDynamicArrayFormula(U16String("=TRANSPOSE(A1:D5)"), options, true);
    workbook.Save(U16String(outFile.c_str()), SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Approach 3 — Transpose with a Classic Array Formula (CSE)**
Use this approach when you want a `TRANSPOSE` formula preserved in the workbook but the target Excel file may be opened in **older Excel versions (pre-2021, including 2019, 2016, 2013, and so on)** where dynamic array spilling is not supported. The classic CSE (Ctrl+Shift+Enter) array formula is the legacy-compatible alternative that all Excel versions can evaluate.

### **API used**
`Cell.SetArrayFormula(const char* arrayFormula, int nRows, int nColumns)` is a method on `Aspose.Cells.Cell` that assigns a **classic array (CSE) formula** to the anchor cell and declares the dimensions of the resulting array. Aspose.Cells writes the multi-cell array-formula marker so Excel evaluates the formula as a single array expression that fills the declared range.

### **Steps**
2. Retrieve the first worksheet via `workbook.GetWorksheets().Get(0)` and access its `Cells` collection through `worksheet.GetCells()`.
3. Call `cells.Get(u"A6").SetArrayFormula(u"=TRANSPOSE(A1:D5)", 4, 5)`. The second argument `4` is the number of rows of the destination array and the third argument `5` is the number of columns.
4. Save the workbook with `workbook.Save(outputFile)`.
Cell **A6** is the anchor of the array formula and the evaluated array spans 4 rows by 5 columns starting at A6, matching the transposed dimensions of the A1:D5 source. Excel writes a single array-formula marker across the resulting range so older Excel versions evaluate it correctly.

{{% alert color="primary" %}}
CSE array formulas are the classic Excel way to evaluate a `TRANSPOSE` expression and this approach is universally compatible across Excel versions.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Load the source workbook with xlsx LoadOptions
    std::string srcFile = "source.xlsx";
    Workbook workbook(U16String(srcFile.c_str()), LoadOptions(LoadFormat::Xlsx));
    // Access the first worksheet and its Cells collection
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    // Set the classic CSE array formula on cell A6.
    // The formula =TRANSPOSE(A1:D5) rotates the 5-row x 4-column source range
    // into a 4-row x 5-column array. The second argument (4) is the number of rows
    // and the third argument (5) is the number of columns of the resulting array.
    // Aspose.Cells writes the CSE array-formula marker so Excel evaluates it as
    // a single multi-cell array formula, compatible with older Excel versions
    // (2019, 2016, 2013, etc.) that do not support dynamic array spilling.
    cells.Get(u"A6").SetArrayFormula(u"=TRANSPOSE(A1:D5)", 4, 5);
    // Save the workbook so the array-formula marker is persisted
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Comparison — When to Use Each Approach**
| Approach | API / Method | Excel Version | Source formula preserved? | Output range |
|----------|--------------|---------------|--------------------------|--------------|
| Approach 1 — In-place transpose | `Range.Transpose()` | All Excel versions | No (values only) | Initial anchor range, 5×4 |
| Approach 2 — Dynamic array formula | `Cell.SetDynamicArrayFormula` | Excel 365 / 2021+ | Yes (spills dynamically) | Spilled from anchor |
| Approach 3 — Classic array formula (CSE) | `Cell.SetArrayFormula` | All Excel versions | Yes (multi-cell array formula) | Explicit size, 4×5 |
Use **Approach 1** when you need a quick, cross-version transformation and only need the transposed values written to the file. Use **Approach 2** when modern Excel is guaranteed and you want the formula to stay live and update if the source changes. Use **Approach 3** when you need the widest compatibility with a preserved formula across every Excel version, including the older releases that do not support dynamic arrays.

## **Related Articles**
- [SmartMarker Single Cell Array Rendering | Aspose.Cells for C++](/cells/cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Inserting an Image into a Cell](/cells/cpp/inserting-an-image-into-a-cell/)
- [Splitting Excel Files into Multiple Files](/cells/cpp/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="" >}}