---
title: Obtenez la validation des cellules dans les fichiers ODS avec C++
linktitle: Obtenir la validation de la cellule dans les fichiers ODS
type: docs
weight: 180
url: /fr/cpp/get-cell-validation-in-ods-files/
description: Apprenez comment obtenir la validation des cellules dans les fichiers ODS en utilisant l API Aspose.Cells for C++.
keywords: Obtenir la validation de la cellule, obtenir la validation de la cellule 
---

## **Obtenir la validation de la cellule dans les fichiers ODS**

Avec l'API Aspose.Cells for C++, vous pouvez obtenir la validation appliquée à une cellule dans les fichiers ODS. L'API fournit la méthode [**GetValidation**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/) de la classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Le code suivant démontre l'utilisation de la méthode [**GetValidation**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/) en chargeant le fichier [source ODS](101089354.ods) et en lisant la validation de la cellule A9.

### **Code d'exemple**

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
