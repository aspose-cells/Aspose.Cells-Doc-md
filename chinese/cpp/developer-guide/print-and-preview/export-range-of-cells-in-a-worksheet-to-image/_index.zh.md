---
title: 使用C++将工作表范围导出为图像
linktitle: 导出范围为图像
type: docs
weight: 60
url: /zh/cpp/export-range-of-cells-in-a-worksheet-to-image/
description: 了解如何使用Aspose.Cells和C++将工作表的特定范围导出为图像。
---

## **可能的使用场景**

您可以使用 Aspose.Cells 制作工作表的图像。但是，有时您只需将工作表中的一定范围的单元格导出为图像。本文解释了如何实现这一点。

## **导出工作表中的单元格范围为图像**

要对一个范围进行图像化处理，将打印区域设置为所需的范围，然后将所有边距设置为 0。还需将 [**ImageOrPrintOptions.GetOnePagePerSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getonepagepersheet/) 设置为 **true**。以下代码将图像化范围 D8:G16。以下是 [示例 Excel 文件](47153160.xlsx) 的屏幕截图，以及代码中使用的图像。您可以使用任何 Excel 文件尝试此代码。

## **示例 Excel 文件及其导出图像的屏幕截图**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

执行该代码仅创建范围 D8:G16 的图像。

**![todo:image_alt_text](Output-Image.png)**

## **示例代码**

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

    // Create workbook from source file
    Workbook workbook(srcDir + u"sampleExportRangeOfCellsInWorksheetToImage.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the print area with the desired range
    worksheet.GetPageSetup().SetPrintArea(u"D8:G16");

    // Set all margins to 0
    worksheet.GetPageSetup().SetLeftMargin(0);
    worksheet.GetPageSetup().SetRightMargin(0);
    worksheet.GetPageSetup().SetTopMargin(0);
    worksheet.GetPageSetup().SetBottomMargin(0);

    // Set OnePagePerSheet option as true
    ImageOrPrintOptions options;
    options.SetOnePagePerSheet(true);
    options.SetImageType(Aspose::Cells::Drawing::ImageType::Jpeg);
    options.SetHorizontalResolution(200);
    options.SetVerticalResolution(200);

    // Take the image of the worksheet
    SheetRender sr(worksheet, options);
    sr.ToImage(0, outDir + u"outputExportRangeOfCellsInWorksheetToImage.jpg");

    std::cout << "Worksheet image exported successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
