---
title: 使用C++实现工作表的自定义纸张大小以进行渲染
linktitle: 实现工作表的自定义纸张大小以进行渲染
type: docs
weight: 70
url: /zh/cpp/implement-custom-paper-size-of-worksheet-for-rendering/
description: 本文介绍了如何使用C++ API在将Excel文件渲染为PDF文件格式时，设置所需工作表的自定义纸张大小。
keywords: 在使用C++渲染Excel为PDF时设置自定义纸张大小
---

## **可能的使用场景**

在MS Excel中没有直接创建自定义纸张大小的选项；然而，在将Excel文件渲染为PDF文件格式时，可以设置工作表的自定义纸张大小。本文解释了如何使用Aspose.Cells API设置工作表的自定义纸张大小。

## **实现工作表的自定义纸张大小以进行渲染**

Aspose.Cells允许您实现工作表的自定义纸张大小。您可以使用[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)类的[**CustomPaperSize**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/custompapersize/)方法指定自定义页面大小。以下示例代码演示了如何为工作簿中的第一个工作表指定自定义纸张大小。请同时参考用以下代码生成的[输出PDF](45056028.pdf)。

## **屏幕截图**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **示例代码**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Set custom paper size in unit of inches
    ws.GetPageSetup().CustomPaperSize(6, 4);

    // Access cell B4
    Cell b4 = ws.GetCells().Get("B4");

    // Add the message in cell B4
    b4.PutValue(u"Pdf Page Dimensions: 6.00 x 4.00 in");

    // Save the workbook in pdf format
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    wb.Save(outputDir + u"outputCustomPaperSize.pdf");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
