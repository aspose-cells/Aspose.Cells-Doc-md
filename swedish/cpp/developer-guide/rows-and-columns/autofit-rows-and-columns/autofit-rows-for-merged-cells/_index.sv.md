---
title: Automatisk anpassning av rader för sammanslagna celler med C++
linktitle: Automatisk anpassning av rader för sammanslagna celler
type: docs
weight: 120
url: /sv/cpp/autofit-rows-for-merged-cells/
description: Lär dig hur du autosvarar rader för sammanslagna celler i Excel med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Microsoft Excel har en funktion som låter dig automatiskt justera höjden på en cell enligt dess innehåll. Funktionen kallas automatisk anpassning av rader. Microsoft Excel tillämpar inte automatisk anpassning på sammanslagna celler som standard. Ibland blir funktionen viktig för en användare som verkligen behöver implementera automatisk anpassning av rader även på sammanslagna celler.

{{% /alert %}}

## **Hur man använder AutoFitMergedCellsType för att autofita rader**
Aspose.Cells stödjer den här funktionen genom API:et [**AutoFitterOptions.AutoFitMergedCellsType**](https://reference.aspose.com/cells/cpp/aspose.cells/autofitmergedcellstype/). Med detta API är det möjligt att auto-anpassa rader i ett kalkylblad inklusive sammanfogade celler. Här är en lista över alla möjliga typer av auto-anpassning av sammanfogade celler:

- Ingen
- Första raden
- Sista raden
- Varje rad

## **Autofit rader för sammanslagna celler**

Se följande kod, den skapar ett arbetsbok-objekt och lägger till flera arbetsblad. Använd olika metoder för autofit-operationer i varje blad. Skärmbilden visar resultaten efter körning av exempel-koden.

<br>
<img src="result.png" width=80% />

## **C++ exempel kod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet1 = workbook.GetWorksheets().Get(0);

    // Create a range A1:B2
    Range range = sheet1.GetCells().CreateRange(0, 0, 2, 2);

    // Merge the cells
    range.Merge();

    // Insert value to the merged cell A1
    sheet1.GetCells().Get(0, 0).SetValue(U16String(u"A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end"));

    // Create a style object
    Style style = sheet1.GetCells().Get(0, 0).GetStyle();

    // Set wrapping text on
    style.SetIsTextWrapped(true);

    // Apply the style to the cell
    sheet1.GetCells().Get(0, 0).SetStyle(style);

    // Create an object for AutoFitterOptions
    AutoFitterOptions options;

    // Only expands the height of the first row.
    options.SetAutoFitMergedCellsType(AutoFitMergedCellsType::FirstLine);

    // Autofit rows in the sheet (including the merged cells)
    sheet1.AutoFitRows(options);

    // Add a new worksheet
    int index = workbook.GetWorksheets().Add();
    Worksheet sheet2 = workbook.GetWorksheets().Get(index);
    sheet2.SetName(U16String(u"Sheet2"));

    // Create a range A1:B2
    Range range2 = sheet2.GetCells().CreateRange(0, 0, 2, 2);

    // Merge the cells
    range2.Merge();

    // Insert value to the merged cell A1
    sheet2.GetCells().Get(0, 0).SetValue(U16String(u"A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end"));

    // Create a style object
    Style style2 = sheet2.GetCells().Get(0, 0).GetStyle();

    // Set wrapping text on
    style2.SetIsTextWrapped(true);

    // Apply the style to the cell
    sheet2.GetCells().Get(0, 0).SetStyle(style2);

    // Create an object for AutoFitterOptions
    AutoFitterOptions options2;

    // Only expands the height of the last row.
    options2.SetAutoFitMergedCellsType(AutoFitMergedCellsType::LastLine);

    // Autofit rows in the sheet (including the merged cells)
    sheet2.AutoFitRows(options2);

    // Add another new worksheet
    index = workbook.GetWorksheets().Add();
    Worksheet sheet3 = workbook.GetWorksheets().Get(index);
    sheet3.SetName(U16String(u"Sheet3"));

    // Create a range A1:B2
    Range range3 = sheet3.GetCells().CreateRange(0, 0, 2, 2);

    // Merge the cells
    range3.Merge();

    // Insert value to the merged cell A1
    sheet3.GetCells().Get(0, 0).SetValue(U16String(u"A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end"));

    // Create a style object
    Style style3 = sheet3.GetCells().Get(0, 0).GetStyle();

    // Set wrapping text on
    style3.SetIsTextWrapped(true);

    // Apply the style to the cell
    sheet3.GetCells().Get(0, 0).SetStyle(style3);

    // Create an object for AutoFitterOptions
    AutoFitterOptions options3;

    // Only expands the height of each row.
    options3.SetAutoFitMergedCellsType(AutoFitMergedCellsType::EachLine);

    // Autofit rows in the sheet (including the merged cells)
    sheet3.AutoFitRows(options3);

    // Add another new worksheet
    index = workbook.GetWorksheets().Add();
    Worksheet sheet4 = workbook.GetWorksheets().Get(index);
    sheet4.SetName(U16String(u"Sheet4"));

    // Create a range A1:B2
    Range range4 = sheet4.GetCells().CreateRange(0, 0, 2, 2);

    // Merge the cells
    range4.Merge();

    // Insert value to the merged cell A1
    sheet4.GetCells().Get(0, 0).SetValue(U16String(u"A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end"));

    // Create a style object
    Style style4 = sheet4.GetCells().Get(0, 0).GetStyle();

    // Set wrapping text on
    style4.SetIsTextWrapped(true);

    // Apply the style to the cell
    sheet4.GetCells().Get(0, 0).SetStyle(style4);

    // Create an object for AutoFitterOptions
    AutoFitterOptions options4;

    // Ignore merged cells.
    options4.SetAutoFitMergedCellsType(AutoFitMergedCellsType::None);

    // Autofit rows in the sheet (not including the merged cells)
    sheet4.AutoFitRows(options4);

    // Save the Excel file
    workbook.Save(U16String(u"out.xlsx"));

    Aspose::Cells::Cleanup();
}
```
