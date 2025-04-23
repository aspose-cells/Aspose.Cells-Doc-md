---
title: Obtenez la validation appliquée à une cellule avec C++
linktitle: Obtenir la validation appliquée sur une cellule
type: docs
weight: 200
url: /fr/cpp/get-validation-applied-on-a-cell/
description: Cet article montre comment appliquer une validation à une cellule avec C++.
keywords: appliquer la validation de cellule dans excel avec c++, appliquer une validation sur une cellule dans excel avec c++, appliquer validation dans excel avec c++, validation de cellule dans excel avec c++, c++ appliquer la validation de cellule dans excel, c++ appliquer la validation sur une cellule dans excel, validation de cellule c++ dans excel, validation de cellule c++
---

{{% alert color="primary" %}}

Vous pouvez utiliser Aspose.Cells pour obtenir la validation appliquée à une cellule. Aspose.Cells fournit la méthode [**Cell::GetValidation()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/) à cet effet. S'il n'y a aucune validation appliquée sur la cellule, elle renvoie null.

De même, vous pouvez utiliser la méthode [**Worksheet::Validations::GetValidationInCell**](https://reference.aspose.com/cells/cpp/aspose.cells/validationcollection/getvalidationincell/) pour acquérir la validation appliquée à une cellule en fournissant ses indices de ligne et de colonne.

{{% /alert %}}

## Code C++ pour obtenir la validation appliquée à une cellule

Le code ci-dessous vous montre comment obtenir la validation appliquée à une cellule.

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

## Articles Connexes

- [Validation des données](/cells/fr/cpp/data-validation/)
