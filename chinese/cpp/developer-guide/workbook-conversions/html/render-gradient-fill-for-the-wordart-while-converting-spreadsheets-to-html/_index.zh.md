---
title: 在将电子表格转换为HTML的同时为WordArt渲染渐变填充，使用C++实现
linktitle: 在将电子表格转换为HTML格式时渲染文字艺术的渐变填充
type: docs
weight: 90
url: /zh/cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/
description: 学习在使用C++将电子表格转换为HTML时为WordArt渲染渐变填充。
---

## **可能的使用场景**
在Aspose.Cells 17.1之前, 当将Excel文件转换为HTML格式时, Aspose.Cells无法渲染字体艺术的渐变填充. 自Aspose.Cells 17.1发布以来, 字体艺术的渐变填充得到了支持. 以下截图比较了使用Aspose.Cells 17.1和旧版本转换Excel文件时的渐变填充效果.

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)
## **在将电子表格转换为HTML时渲染WordArt的渐变填充**
以下示例代码将[source excel file](22774111.xlsx)转换为[output HTML format](22774109.zip). 源Excel文件中包含如上截图所示的带有渐变填充的字体对象.
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
    U16String inputFilePath = srcDir + u"sourceGradientFill.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save workbook to HTML format
    workbook.Save(outDir + u"out_sourceGradientFill.html");

    std::cout << "Workbook saved successfully in HTML format!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
