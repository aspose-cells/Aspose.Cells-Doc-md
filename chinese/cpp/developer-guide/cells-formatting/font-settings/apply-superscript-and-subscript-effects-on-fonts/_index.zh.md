---
title: 在 C++ 中使用 Aspose.Cells for C++ API 对字体应用上标和下标效果
linktitle: 在字体上应用上标和下标效果
type: docs
weight: 80
url: /zh/cpp/apply-superscript-and-subscript-effects-on-fonts/
description: 使用 Aspose.Cells for C++ API，在 C++ 中对 Excel 中文本应用上标和下标效果的代码示例。
keywords: excel 上标 c++，excel 下标 c++，excel 上标和下标 c++，在 excel 中插入上标和下标 c++，向 excel 添加上标和下标，向 excel 添加上标和下标 c++，在 excel 中添加上标和下标，添加上标 c++，添加下标 c++
---

{{% alert color="primary" %}}

Aspose.Cells提供将文本应用上标（文本位于基线上方）和下标（文本位于基线下方）效果的功能。

{{% /alert %}}

## **处理上标和下标**

通过将[**Style.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/)对象的[**IsSuperscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issuperscript/)属性设置为**true**来应用上标效果。要应用下标效果，将[**Style.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/)对象的[**IsSubscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issubscript/)属性设置为**true**。

以下代码示例展示了如何将上标和下标应用于文本。

### 用 C++ 应用上标效果的代码

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Excel object
    workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Adding some value to the "A1" cell
    cell.PutValue(u"Hello");

    // Setting the font Superscript
    Style style = cell.GetStyle();
    style.GetFont().SetIsSuperscript(true);
    cell.SetStyle(style);

    // Saving the Excel file
    workbook.Save(outDir + u"Superscript_out.xls", SaveFormat::Auto);

    std::cout << "Excel file saved successfully with superscript text!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### 用 C++ 应用下标效果的代码

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello");

    // Set the font Subscript
    Style style = cell.GetStyle();
    style.GetFont().SetIsSubscript(true);
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"Subscript_out.xls", SaveFormat::Auto);

    std::cout << "File saved successfully with subscript text!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
