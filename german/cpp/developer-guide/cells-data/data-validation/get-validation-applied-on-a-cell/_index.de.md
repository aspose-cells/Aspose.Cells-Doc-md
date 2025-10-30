---
title: Validierung auf eine Zelle mit C++ abrufen
linktitle: Angewendete Validierung auf einer Zelle erhalten.
type: docs
weight: 200
url: /de/cpp/get-validation-applied-on-a-cell/
description: Dieser Artikel zeigt, wie man in C++ Validierungen auf eine Zelle anwendet.
keywords: Zellvalidierung in Excel mit C++ anwenden, Validierung auf eine Zelle in Excel mit C++ anwenden, Validierung in Excel mit C++, Zellvalidierung in Excel mit C++, C++ Zellvalidierung in Excel, C++ Validierung auf eine Zelle in Excel, C++ Zellvalidierung in Excel, C++ Zellvalidierung
---

{{% alert color="primary" %}}

Sie können Aspose.Cells verwenden, um die auf eine Zelle angewendete Validierung zu erhalten. Aspose.Cells bietet die [**Cell::GetValidation()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/) Methode für diesen Zweck. Wenn keine Validierung auf die Zelle angewendet wird, gibt sie null zurück.

Ebenso können Sie die [**Worksheet::Validations::GetValidationInCell**](https://reference.aspose.com/cells/cpp/aspose.cells/validationcollection/getvalidationincell/) Methode verwenden, um die auf eine Zelle angewendete Validierung durch Angabe ihrer Zeilen- und Spaltenindizes zu erhalten.

{{% /alert %}}

## C++ Code zum Erhalten der auf eine Zelle angewendeten Validierung

Der folgende Code zeigt, wie Validierungen auf eine Zelle angewendet werden.

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

## Verwandte Artikel

- [Datenüberprüfung](/cells/de/cpp/data-validation/)
{{< app/cells/assistant language="cpp" >}}
