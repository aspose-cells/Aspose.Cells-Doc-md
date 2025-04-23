---
title: 在C++中添加带条件图标集的单元格文本
linktitle: 使用单元格文本添加条件图标集
type: docs
weight: 160
url: /zh/cpp/add-conditional-icons-set-with-the-cell-text/
description: 学习如何使用Aspose.Cells和C++在Excel中在单元格文本旁添加条件图标。
---

{{% alert color="primary" %}} 

有时，你希望在单元格中的文本旁添加条件图标，以使数据对读者更有意义。你可能想使用一些条件格式图标类型，但不希望对单元格应用条件格式。Aspose.Cells支持此功能。

{{% /alert %}} 

以下代码示例显示了如何在单元格文本旁添加条件图标设置。

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

    // Input date into the cells
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
