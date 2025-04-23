---
title: Trova il massimo numero di righe e colonne supportate dai formati XLS e XLSX con C++
linktitle: Trova il massimo numero di righe e colonne
type: docs
weight: 20
url: /it/cpp/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
description: Impara come trovare il massimo numero di righe e colonne supportate dai formati XLS e XLSX usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

Ci sono diversi numeri di righe e colonne supportati dai formati Excel. Per esempio, XLS supporta 65536 righe e 256 colonne mentre XLSX supporta 1048576 righe e 16384 colonne. Se vuoi sapere quante righe e colonne sono supportate da un determinato formato, puoi usare le proprietà [**GetMaxRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrow/) e [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/).

## **Trova il numero massimo di righe e colonne supportate dai formati XLS e XLSX**

Il codice di esempio seguente crea prima un workbook in formato XLS e poi in formato XLSX. Dopo la creazione, stampa i valori delle proprietà [**GetMaxRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxrow/) e [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/). Guarda l'output della console del codice sotto per riferimento.

## **Codice di Esempio**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Print message about XLS format.
    std::cout << "Maximum Rows and Columns supported by XLS format." << std::endl;

    // Create workbook in XLS format.
    Workbook wb(FileFormatType::Excel97To2003);

    // Print the maximum rows and columns supported by XLS format.
    int maxRows = wb.GetSettings().GetMaxRow() + 1;
    int maxCols = wb.GetSettings().GetMaxColumn() + 1;
    std::cout << "Maximum Rows: " << maxRows << std::endl;
    std::cout << "Maximum Columns: " << maxCols << std::endl;
    std::cout << std::endl;

    // Print message about XLSX format.
    std::cout << "Maximum Rows and Columns supported by XLSX format." << std::endl;

    // Create workbook in XLSX format.
    wb = Workbook(FileFormatType::Xlsx);

    // Print the maximum rows and columns supported by XLSX format.
    maxRows = wb.GetSettings().GetMaxRow() + 1;
    maxCols = wb.GetSettings().GetMaxColumn() + 1;
    std::cout << "Maximum Rows: " << maxRows << std::endl;
    std::cout << "Maximum Columns: " << maxCols << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Output della console**

{{< highlight java >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
