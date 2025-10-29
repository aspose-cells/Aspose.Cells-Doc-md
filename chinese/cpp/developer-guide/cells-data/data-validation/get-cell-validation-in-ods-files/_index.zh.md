---
title: 用C++获取ODS文件中的单元格验证
linktitle: 获取ODS文件中的单元格验证
type: docs
weight: 180
url: /zh/cpp/get-cell-validation-in-ods-files/
description: 学习如何使用Aspose.Cells for C++ API获取ODS文件中的单元格验证。
keywords: 获取单元格验证，获得单元格验证 
---

## **获取ODS文件中的单元格验证**

利用Aspose.Cells for C++ API，可以获取应用于ODS文件中单元格的验证。该API提供 [**GetValidation**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/) 方法和 [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) 类。

以下示例代码演示了如何使用 [**GetValidation**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/) 方法，通过加载 [源ODS文件](101089354.ods) 并读取单元格A9的验证信息。

### **示例代码**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source Excel file
    U16String inputFilePath = srcDir + u"SampleBook1.ods";
    Workbook workbook(inputFilePath);

    // Access first worksheet
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);

    // Access cell A9
    Cells cells = worksheet.GetCells();
    Cell cell = cells.Get(U16String(u"A9"));

    // Check validation existence
    Validation validation = cell.GetValidation();
    if (validation.IsNull() == false)
    {
        std::cout << "Validation type: " << static_cast<int>(validation.GetType()) << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
