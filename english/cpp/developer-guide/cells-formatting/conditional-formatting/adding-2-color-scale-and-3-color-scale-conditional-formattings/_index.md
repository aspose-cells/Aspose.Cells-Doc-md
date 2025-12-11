---
title: Adding 2-Color Scale and 3-Color Scale Conditional Formatting with C++
linktitle: Adding 2-Color Scale and 3-Color Scale Conditional Formatting
description: How to use the Aspose.Cells library in C++ to add conditional formatting for two‑color scales and three‑color scales. By adjusting these criteria, you have more control over how cells look and appear.
keywords: Aspose.Cells, Conditional Formatting, C++, Color Scale, Two Color Scale, Three Color Scale
type: docs
weight: 20
url: /cpp/adding-2-color-scale-and-3-color-scale-conditional-formattings/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

**2-Color Scale** and **3-Color Scale** Conditional Formatting are added in the same way except they differ by the [**FormatCondition.GetIs3ColorScale()**](https://reference.aspose.com/cells/cpp/aspose.cells/colorscale/getis3colorscale/) property. This property is **false** for a 2‑Color Scale and **true** for a 3‑Color Scale Conditional Formatting.

{{% /alert %}}

The following sample code adds 2‑Color and 3‑Color Scale Conditional Formatting. It generates the [output Excel file](5115058.xlsx).

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add some data in cells
    worksheet.GetCells().Get(u"A1").PutValue(u"2-Color Scale");
    worksheet.GetCells().Get(u"D1").PutValue(u"3-Color Scale");

    for (int i = 2; i <= 15; i++)
    {
        int row = i - 1;
        worksheet.GetCells().Get(row, 0).PutValue(i); // Column A (0)
        worksheet.GetCells().Get(row, 3).PutValue(i); // Column D (3)
    }

    // Adding 2-Color Scale Conditional Formatting
    CellArea ca = CellArea::CreateCellArea(u"A2", u"A15");

    int idx = worksheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcc = worksheet.GetConditionalFormattings().Get(idx);
    fcc.AddCondition(FormatConditionType::ColorScale);
    fcc.AddArea(ca);

    FormatCondition fc = worksheet.GetConditionalFormattings().Get(idx).Get(0);
    fc.GetColorScale().SetIs3ColorScale(false);
    fc.GetColorScale().SetMaxColor(Color::LightBlue());
    fc.GetColorScale().SetMinColor(Color::LightGreen());

    // Adding 3-Color Scale Conditional Formatting
    ca = CellArea::CreateCellArea(u"D2", u"D15");

    idx = worksheet.GetConditionalFormattings().Add();
    fcc = worksheet.GetConditionalFormattings().Get(idx);
    fcc.AddCondition(FormatConditionType::ColorScale);
    fcc.AddArea(ca);

    fc = worksheet.GetConditionalFormattings().Get(idx).Get(0);
    fc.GetColorScale().SetIs3ColorScale(true);
    fc.GetColorScale().SetMaxColor(Color::LightBlue());
    fc.GetColorScale().SetMidColor(Color::Yellow());
    fc.GetColorScale().SetMinColor(Color::LightGreen());

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
