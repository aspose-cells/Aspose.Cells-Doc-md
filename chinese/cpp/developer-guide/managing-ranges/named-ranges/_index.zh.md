---
title: 用C++创建工作簿和工作表作用域命名范围
linktitle: 命名范围
type: docs
weight: 40
url: /zh/cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: 学习如何使用Aspose.Cells和C++创建工作簿和工作表作用域的命名范围。
---

{{% alert color="primary" %}} 

Microsoft Excel 允许用户定义具有两种不同范围（工作簿（也称为全局范围）和工作表）的命名范围。

- 具有工作簿范围的命名范围可以通过简单地使用其名称从工作簿内的任何工作表中访问。
- 具有工作表范围的命名范围是通过在其创建的特定工作表的引用中访问的。

Aspose.Cells 提供了与 Microsoft Excel 相同的功能，用于添加工作簿和工作表范围的命名范围。创建工作表范围的命名范围时，应使用工作表引用来将其指定为工作表范围的命名范围。

{{% /alert %}} 

## **使用工作簿范围添加命名范围**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    //Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a new Workbook object
    Workbook workbook;

    // Get the first worksheet of the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get worksheet's cells collection
    Cells cells = sheet.GetCells();

    // Create a range of Cells from Cell A1 to C10
    Range workbookScope = cells.CreateRange(u"A1", u"C10");

    // Assign the name to workbook scope named range
    workbookScope.SetName(u"workbookScope");

    // Save the workbook
    workbook.Save(srcDir + u"WorkbookScope.out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **使用工作表范围添加命名范围**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create a new Workbook object
    Workbook workbook;

    // Get the first worksheet of the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get worksheet's cells collection
    Cells cells = sheet.GetCells();

    // Create a range of Cells
    Range localRange = cells.CreateRange(u"A1", u"C10");

    // Assign name to range with sheet reference
    localRange.SetName(u"Sheet1!local");

    // Save the workbook
    U16String outputFilePath = u"..\\Data\\02_OutputDirectory\\output.out.xls";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **高级主题**
- [创建访问和复制命名区域](/cells/zh/cpp/create-access-and-copy-named-ranges/)
- [格式和修改命名区域](/cells/zh/cpp/format-and-modify-named-ranges/)
- [获取带有外部链接的范围](/cells/zh/cpp/get-range-with-external-links/)
- [实现非连续范围](/cells/zh/cpp/implementing-non-sequential-ranges/)

