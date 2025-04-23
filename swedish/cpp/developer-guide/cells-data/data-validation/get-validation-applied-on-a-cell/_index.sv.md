---
title: Hämta validering tillämpad på en cell med C++
linktitle: Få validering som tillämpats på en cell
type: docs
weight: 200
url: /sv/cpp/get-validation-applied-on-a-cell/
description: Denna artikel visar hur man tillämpar validering på en cell med C++.
keywords: tillämpa cellvalidering i Excel med C++, tillämpa validering på en cell i Excel med C++, tillämpa validering i Excel med C++, cellvalidering i Excel med C++, C++ tillämpning av cellvalidering i Excel, C++ tillämpning av validering på en cell i Excel, C++ cellvalidering i Excel, C++ cellvalidering
---

{{% alert color="primary" %}}

Du kan använda Aspose.Cells för att få valideringen som tillämpas på en cell. Aspose.Cells tillhandahåller [**Cell::GetValidation()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/) metoden för detta ändamål. Om det inte finns någon validering som tillämpas på cellen returneras null.

På liknande sätt kan du använda metod [**Worksheet::Validations::GetValidationInCell**](https://reference.aspose.com/cells/cpp/aspose.cells/validationcollection/getvalidationincell/) för att få validering som har tillämpats på en cell genom att ange dess rad- och kolumnindex.

{{% /alert %}}

## C++-kod för att hämta validering tillämpad på en cell

Nedan visas exempel på kod som visar hur du hämtar validering som är tillämpad på en cell.

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

## Relaterade artiklar

- [Data validering](/cells/sv/cpp/data-validation/)
