---
title: Ottieni la validazione delle celle nei file ODS con C++
linktitle: Ottieni la convalida della cella nei file ODS
type: docs
weight: 180
url: /it/cpp/get-cell-validation-in-ods-files/
description: Scopri come ottenere la validazione delle celle nei file ODS usando l API Aspose.Cells for C++.
keywords: Ottieni la convalida della cella, ottieni la convalida della cella 
---

## **Ottieni la Convalida Cellulare nei File ODS**

Con Aspose.Cells for C++, puoi ottenere la validazione applicata a una cella nei file ODS. L'API fornisce il metodo [**GetValidation**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/) della classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Il seguente esempio di codice dimostra come funziona il metodo [**GetValidation**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/) caricando il file [ODS di origine](101089354.ods) e leggendo la validazione della cella A9.

### **Codice di Esempio**

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
