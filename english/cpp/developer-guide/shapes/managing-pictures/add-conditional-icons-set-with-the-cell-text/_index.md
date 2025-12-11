---
title: Add Conditional Icons Set with Cell Text Using C++
linktitle: Add Conditional Icons Set with Cell Text
type: docs
weight: 160
url: /cpp/add-conditional-icons-set-with-the-cell-text/
description: Learn how to add conditional icons next to cell text in Excel using Aspose.Cells with C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Sometimes, you want to add conditional icons next to the text in a cell to make data more meaningful to readers. You may want to use some of the conditional formatting icon types without applying conditional formatting to cells. Aspose.Cells supports this feature.

{{% /alert %}} 

The following code sample shows how to add a conditional icons set with cell text.

```cpp
#include <iostream>
#include <memory>
#include <vector>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first worksheet (default worksheet) in the workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the cells
    Cells cells = worksheet.GetCells();

    // Set the columns widths (A, B and C)
    cells.SetColumnWidth(0, 24);
    cells.SetColumnWidth(1, 24);
    cells.SetColumnWidth(2, 24);

    // Input data into the cells
    cells.Get(u"A1").PutValue(u"KPIs");
    cells.Get(u"A2").PutValue(u"Total Turnover (Sales at List)");
    cells.Get(u"A3").PutValue(u"Total Gross Margin %");
    cells.Get(u"A4").PutValue(u"Total Net Margin %");
    cells.Get(u"B1").PutValue(u"UA Contract Size Group 4");
    cells.Get(u"B2").PutValue(19551794);
    cells.Get(u"B3").PutValue(11.8070745566204);
    cells.Get(u"B4").PutValue(11.858589818569);
    cells.Get(u"C1").PutValue(u"UA Contract Size Group 3");
    cells.Get(u"C2").PutValue(8150131.66666667);
    cells.Get(u"C3").PutValue(10.3168384396244);
    cells.Get(u"C4").PutValue(11.3326931937091);

    // Get the conditional icon's image data
    Vector<uint8_t> imagedata = ConditionalFormattingIcon::GetIconImageData(IconSetType::TrafficLights31, 0);
    // Add the picture to the cell based on the image data
    worksheet.GetPictures().Add(1, 1, imagedata);

    // Get the conditional icon's image data
    Vector<uint8_t> imagedata1 = ConditionalFormattingIcon::GetIconImageData(IconSetType::Arrows3, 2);
    // Add the picture to the cell based on the image data
    worksheet.GetPictures().Add(1, 2, imagedata1);

    // Get the conditional icon's image data
    Vector<uint8_t> imagedata2 = ConditionalFormattingIcon::GetIconImageData(IconSetType::Symbols3, 0);
    // Add the picture to the cell based on the image data
    worksheet.GetPictures().Add(2, 1, imagedata2);

    // Get the conditional icon's image data
    Vector<uint8_t> imagedata3 = ConditionalFormattingIcon::GetIconImageData(IconSetType::Stars3, 0);
    // Add the picture to the cell based on the image data
    worksheet.GetPictures().Add(2, 2, imagedata3);

    // Get the conditional icon's image data
    Vector<uint8_t> imagedata4 = ConditionalFormattingIcon::GetIconImageData(IconSetType::Boxes5, 1);
    // Add the picture to the cell based on the image data
    worksheet.GetPictures().Add(3, 1, imagedata4);

    // Get the conditional icon's image data
    Vector<uint8_t> imagedata5 = ConditionalFormattingIcon::GetIconImageData(IconSetType::Flags3, 1);
    // Add the picture to the cell based on the image data
    worksheet.GetPictures().Add(3, 2, imagedata5);

    // Save the Excel file
    U16String outputPath = outDir + u"outfile_cond_icons1.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "File saved successfully at: " << outputPath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
