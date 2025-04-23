---
title: 在将Excel转换为PDF时渲染Office加载项 with C++
linktitle: 转换Excel为PDF时呈现Office加载项
type: docs
weight: 100
url: /zh/cpp/render-office-add-ins-while-converting-excel-to-pdf/
description: 了解如何在将Excel文件转换为PDF时渲染Office加载项，使用Aspose.Cells for C++。
---

## **可能的使用场景**

之前，Aspose.Cells在将Excel文件保存为PDF时无法渲染Office加载项。现在，Aspose.Cells可以正确渲染。您无需使用任何特殊的方法或属性即可在输出PDF中渲染Office加载项。只需将您的Excel文件保存为PDF格式，它将自动渲染Office加载项。

## **在将Excel转换为PDF时呈现Office加载项**

以下示例代码保存了包含Office加载项的[示例Excel文件](60489769.xlsx)。请查看[之前版本（即17.11）生成的输出PDF](60489770.pdf)和[较新版本（即17.12及之后版本）生成的输出PDF](60489771.pdf)。之前版本的输出PDF为空白，但较新版本的输出PDF显示了Office加载项。

## **示例代码**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample Excel file containing Office Add-Ins
    U16String inputFilePath = u"sampleRenderOfficeAdd-Ins.xlsx";
    Workbook wb(inputFilePath);

    // Save it to Pdf format with version appended to the output filename
    U16String outputFilePath = u"output-" + CellsHelper::GetVersion() + u".pdf";
    wb.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "File saved successfully: " << outputFilePath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
