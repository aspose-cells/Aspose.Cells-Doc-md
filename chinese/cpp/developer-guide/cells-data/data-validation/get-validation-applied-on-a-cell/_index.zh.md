---
title: 用C++获取单元格验证
linktitle: 获取应用于单元格的验证
type: docs
weight: 200
url: /zh/cpp/get-validation-applied-on-a-cell/
description: 本文章介绍了如何用C++应用验证到单元格。
keywords: 用C++在Excel中应用单元格验证；在Excel中对单元格应用验证；在Excel中进行验证；Excel中的单元格验证；使用C++在Excel中应用单元格验证；用C++对Excel中的单元格进行验证；C++在Excel中的单元格验证；C++在Excel中应用验证。
---

{{% alert color="primary" %}}

您可以使用Aspose.Cells获取应用于单元格的验证。Aspose.Cells为此提供了[**Cell::GetValidation()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/)方法。如果单元格上没有应用验证，则返回null。

同样，您可以使用 [**Worksheet::Validations::GetValidationInCell**](https://reference.aspose.com/cells/cpp/aspose.cells/validationcollection/getvalidationincell/) 方法通过提供它的行和列索引来获取应用于单元格的验证。

{{% /alert %}}

## 用C++获取已应用到单元格的验证

下面的代码示例演示了如何获取应用到单元格的验证。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate the workbook from sample Excel file
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access its first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Cell C1 has the Decimal Validation applied on it. It can take only the values Between 10 and 20
    Cell cell = worksheet.GetCells().Get(u"C1");

    // Access the validation applied on this cell
    Validation validation = cell.GetValidation();

    // Read various properties of the validation
    std::cout << "Reading Properties of Validation" << std::endl;
    std::cout << "--------------------------------" << std::endl;
    std::cout << "Type: " << static_cast<int>(validation.GetType()) << std::endl;
    std::cout << "Operator: " << static_cast<int>(validation.GetOperator()) << std::endl;
    std::cout << "Formula1: " << validation.GetFormula1().ToUtf8() << std::endl;
    std::cout << "Formula2: " << validation.GetFormula2().ToUtf8() << std::endl;
    std::cout << "Ignore blank: " << validation.GetIgnoreBlank() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## 相关文章

- [数据有效性](/cells/zh/cpp/data-validation/)
