---
title: Ottieni la validazione applicata a una cella con C++
linktitle: Ottenere la convalida applicata su una cella
type: docs
weight: 200
url: /it/cpp/get-validation-applied-on-a-cell/
description: Questo articolo mostra come applicare la validazione a una cella con C++.
keywords: applicare validazione della cella in Excel con C++, applicare validazione su una cella in Excel con C++, applicare validazione in Excel con C++, validazione della cella in Excel con C++, C++ applica validazione della cella in Excel, C++ applica validazione su una cella in Excel, validazione della cella in Excel con C++, validazione della cella in Excel con C++
---

{{% alert color="primary" %}}

È possibile utilizzare Aspose.Cells per ottenere la convalida applicata a una cella. Aspose.Cells fornisce il metodo [**Cell::GetValidation()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/) a tale scopo. Se sulla cella non è applicata alcuna convalida, restituisce null.

Allo stesso modo, è possibile utilizzare il metodo [**Worksheet::Validations::GetValidationInCell**](https://reference.aspose.com/cells/cpp/aspose.cells/validationcollection/getvalidationincell/) per acquisire la convalida applicata a una cella fornendo i suoi indici di riga e colonna.

{{% /alert %}}

## Codice C++ per ottenere la validazione applicata su una cella

Il seguente esempio di codice mostra come ottenere la validazione applicata a una cella.

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

## Articoli correlati

- [Convalida Dati](/cells/it/cpp/data-validation/)
{{< app/cells/assistant language="cpp" >}}
