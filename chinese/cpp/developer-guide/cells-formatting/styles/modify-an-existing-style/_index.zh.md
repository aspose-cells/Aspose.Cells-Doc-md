---
title: 用C++修改现有样式
description: Aspose.Cells是一个用于处理电子表格文件的C++库，允许用户修改现有单元格样式。本文将介绍如何使用Aspose.Cells库修改现有单元格样式，以便用户根据需要改变单元格的外观。
keywords: 修改现有样式，自定义应用程序的外观，指南，教程，帮助文档，开发文档，API参考，示例代码，下载，支持。
type: docs
weight: 90
url: /zh/cpp/modify-an-existing-style/
---

{{% alert color="primary" %}}

要将相同的格式选项应用于单元格，请创建一个新的格式样式对象。格式样式对象是格式特性的组合，如字体、字体大小、缩进、数字、边框、模式等，命名并存储为一组。应用时，该样式中的所有格式都会被应用。

你还可以使用现有样式，将其保存与工作簿一起，并用其格式化具有相同属性的信息。

当单元格没有明确格式化时，将应用**普通**样式（工作簿的默认样式）。除了普通样式之外，Microsoft Excel还预定义了几种样式，包括逗号、货币和百分号。

Aspose.Cells允许修改任何这些样式或您使用所需属性定义的任何其他样式。

{{% /alert %}}

## **使用Microsoft Excel**

更新Microsoft Excel 97-2003中的样式：

1. 单击**格式**菜单上的**样式**。
1. 从**样式名称**列表中选择要修改的样式。
1. 单击**修改**。
1. 使用格式单元格对话框中的选项卡选择要使用的样式选项。
1. 点击**确定**。
1. 在**样式包括**下，指定您想要的样式特征。
1. 单击**确定**以保存样式并将其应用于所选范围。

## **使用Aspose.Cells**

以下示例演示了如何使用[**Style.Update**](https://reference.aspose.com/cells/cpp/aspose.cells/style/update/)方法。

### **创建和修改样式**

此示例创建一个[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)对象，将其应用于一范围的单元格，并修改[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)对象。所做的更改会自动应用到单元格及其所在范围的样式。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create a workbook.
    Workbook workbook;

    // Create a new style object.
    Style style = workbook.CreateStyle();

    // Set the number format.
    style.SetNumber(14);

    // Set the font color to red color.
    style.GetFont().SetColor(Color::Red());

    // Name the style.
    style.SetName(u"Date1");

    // Get the first worksheet cells.
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Specify the style (described above) to A1 cell.
    cells.Get(u"A1").SetStyle(style);

    // Create a range (B1:D1).
    Range range = cells.CreateRange(u"B1", u"D1");

    // Initialize styleflag object.
    StyleFlag flag;

    // Set all formatting attributes on.
    flag.SetAll(true);

    // Apply the style (described above) to the range.
    range.ApplyStyle(style, flag);

    // Modify the style (described above) and change the font color from red to black.
    style.GetFont().SetColor(Color::Black());

    // Done! Since the named style (described above) has been set to a cell and range,
    // The change would be reflected (new modification is implemented) to cell (A1) and range (B1:D1).
    style.Update();

    // Save the excel file.
    U16String dataDir(u"..\\Data\\02_OutputDirectory\\");
    workbook.Save(dataDir + u"book_styles.out.xls");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **修改现有样式**

此示例使用一个简单的模板Excel文件，其中已经应用了一个名为“Percent”的样式到一个范围中。该示例：

1. 获取样式，
1. 创建一个样式对象，并
1. 修改样式格式。

修改将自动应用于应用了样式的范围。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputPath = srcDir + u"book1.xlsx";

    /*
     * Create a workbook.
     * Open a template file. 
     * In the book1.xlsx file, we have applied Ms Excel's 
     * Named style i.e., "Percent" to the range "A1:C8".
    */
    Workbook workbook(inputPath);

    // We get the Percent style and create a style object.
    Style style = workbook.GetNamedStyle(u"Percent");

    // Change the number format to "0.00%".
    style.SetNumber(11);

    // Set the font color.
    Color redColor = Color::Red();
    style.GetFont().SetColor(redColor);

    // Update the style. so, the style of range "A1:C8" will be changed too.
    style.Update();

    // Save the excel file.	
    U16String outputPath = srcDir + u"book2.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
