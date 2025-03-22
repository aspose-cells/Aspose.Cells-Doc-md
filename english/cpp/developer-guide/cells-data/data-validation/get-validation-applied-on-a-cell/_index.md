---
title: Get Validation Applied on a Cell with C++
linktitle: Get Validation Applied on a Cell
type: docs
weight: 200
url: /cpp/get-validation-applied-on-a-cell/
description: This article shows how to apply validation on a Cell with C++.
keywords: apply cell validation in excel with c++, apply validation on a cell in excel with c++, apply validation in excel with c++, cell validation in excel with c++, c++ apply cell validation in excel, c++ apply validation on a cell in excel, c++ cell validation in excel, c++ cell validation
---

{{% alert color="primary" %}}

You can use Aspose.Cells to get the validation applied to a cell. Aspose.Cells provides the [**Cell::GetValidation()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/) method for this purpose. If there is no validation applied on the cell, it returns null.

Similarly, you can use [**Worksheet::Validations::GetValidationInCell**](https://reference.aspose.com/cells/cpp/aspose.cells/validationcollection/getvalidationincell/) method to acquire the validation applied to a cell by providing its row and column indices.

{{% /alert %}}

## C++ code to get the validation applied on a Cell

Below code sample shows you how to get validation applied on a cell.

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
    std::cout << "Type: " << validation.GetType() << std::endl;
    std::cout << "Operator: " << validation.GetOperator() << std::endl;
    std::cout << "Formula1: " << validation.GetFormula1().ToUtf8() << std::endl;
    std::cout << "Formula2: " << validation.GetFormula2().ToUtf8() << std::endl;
    std::cout << "Ignore blank: " << validation.GetIgnoreBlank() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## Related Articles

- [Data Validation](/cells/cpp/data-validation/)