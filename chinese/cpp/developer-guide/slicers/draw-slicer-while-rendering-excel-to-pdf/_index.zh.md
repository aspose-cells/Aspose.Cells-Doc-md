---
title: 在将Excel渲染为PDF时绘制切片器，使用C++
linktitle: 在将 Excel 渲染为 PDF 时绘制分析器
type: docs
weight: 60
url: /zh/cpp/draw-slicer-while-rendering-excel-to-pdf/
description: 使用Aspose.Cells和C++导出带切片器设置的Excel为PDF。
---

## **在将 Excel 渲染为 PDF 时绘制分析器**
如果你拥有一个应用切片器的Excel文件，并希望导出带切片器设置的PDF，Aspose.Cells现已支持此功能。只需将含切片器的Excel文件导出为PDF，生成的PDF将显示应用了切片器的状态。

以下示例代码加载了包含现有切片器的[sample Excel file](94044165.xlsx)。然后将工作簿保存为[output PDF file](94044166.pdf)。以下截图比较了源Excel文件和生成的PDF文件。

![todo:image_alt_text](draw-slicer-while-rendering-excel-to-pdf_1.jpg)

## **示例代码**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"SampleSlicerChart.xlsx";

    // Path of output pdf file
    U16String outputFilePath = outDir + u"SampleSlicerChart.pdf";

    // Create workbook from the excel file
    Workbook workbook(inputFilePath);

    // Save the workbook as a PDF file
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved as PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
