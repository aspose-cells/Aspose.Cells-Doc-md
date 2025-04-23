---
title: Ottieni ID unico del Foglio di Lavoro con C++
linktitle: Ottieni ID unico del Foglio di Lavoro
type: docs
weight: 190
url: /it/cpp/get-worksheet-unique-id/
description: Questo articolo mostra come ottenere l ID unico del foglio Excel utilizzando la libreria e l API C++ programmaticamente.
keywords: ID univoco del foglio Excel C++, ID univoco del foglio C++
---

## **Ottieni ID unico del Foglio di Lavoro**

Aspose.Cells fornisce la capacità di ottenere l'ID univoco di un foglio usando il metodo [**GetUniqueId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getuniqueid/). Il seguente frammento di codice dimostra l'uso del metodo [**GetUniqueId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getuniqueid/) per stampare l'ID univoco di un foglio di lavoro. Il seguente frammento di codice utilizza questo [file Excel di esempio](105480213.xlsx).

### Codice Sorgente

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source Excel file
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Print Unique Id
    std::cout << "Unique Id: " << worksheet.GetUniqueId().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```
