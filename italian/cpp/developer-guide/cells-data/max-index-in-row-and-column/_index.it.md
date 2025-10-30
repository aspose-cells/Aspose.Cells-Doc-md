---
title: Trova il Max Indice di Colonna in Riga e il Max Indice di Riga in Colonna con C++
linktitle: Ottenere l Indice Massimo della Colonna nella Riga e l Indice Massimo della Riga nella Colonna
type: docs
weight: 600
url: /it/cpp/get-max-index-in-row-and-column/
description: Impara come ottenere il Max Indice di Colonna in Riga e il Max Indice di Riga in Colonna tramite l API Aspose.Cells for C++.
keywords: Ottieni l Indice della Colonna Massima nella Riga, Ottieni l Indice della Riga Massima nella Colonna, Ottieni l Indice della Colonna Dati Massima nella Riga, Ottieni l Indice della Riga Dati Massima nella Colonna.
---

## **Possibili Scenari di Utilizzo**
Quando hai bisogno di manipolare alcuni dati sulle righe o colonne, è importante conoscere l'intervallo di dati delle righe e colonne. Aspose.Cells offre questa funzione. Per ottenere l'indice massimo di colonna su una riga, puoi ottenere le proprietà [Row.GetLastCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastcell/) e [Row.GetLastDataCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/), quindi usare la proprietà [Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/) per ottenere l'indice massimo di colonna e l'indice massimo di colonna dei dati. Ma per ottenere l'indice massimo di riga e l'indice massimo di riga dei dati su una colonna, è necessario creare un intervallo sulla colonna, quindi scorrere l'intervallo per trovare l'ultima cella e infine usare l'attributo [Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/) sulla cella.

Aspose.Cells fornisce le seguenti proprietà e metodi per aiutarti a raggiungere i tuoi obiettivi.
- [**Row.GetLastCell()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastcell/)
- [**Row.GetLastDataCell()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/)
- [**Cell.GetColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/)
- [**Cell.GetRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/)

## **Ottieni l'Indice della Colonna Massima nella Riga e l'Indice della Riga Massima nella Colonna usando Aspose.Cells**
Questo esempio mostra come:

1. Caricare il [file di esempio](sample.xlsx).
1. Ottenere la riga che ha bisogno di ottenere l'indice massimo della colonna e l'indice massimo della colonna dei dati.
1. Ottieni l'attributo [Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/) sulla cella.
1. Creare un intervallo basato sulla colonna.
1. Ottenere l'iteratore e attraversare l'intervallo.
1. Ottieni l'attributo [Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/) sulla cella.

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String filePath = srcDir + u"sample.xlsx";

    Workbook workbook(filePath);
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    Row row = cells.CheckRow(1);
    if (row)
    {
        std::cout << "Max column index in row: " << row.GetLastCell().GetColumn() << std::endl;
        std::cout << "Max data column index in row: " << row.GetLastDataCell().GetColumn() << std::endl;
    }

    Range columnRange = cells.CreateRange(1, 1, true);
    auto colIter = columnRange.GetEnumerator();

    int maxRow = 0;
    int maxDataRow = 0;

    while (colIter.MoveNext())
    {
        Cell currCell = colIter.GetCurrent();
        if (!currCell.GetStringValue().IsEmpty())
        {
            maxDataRow = currCell.GetRow();
        }
        if (!currCell.GetStringValue().IsEmpty() || currCell.GetHasCustomStyle())
        {
            maxRow = currCell.GetRow();
        }
    }

    std::cout << "Max row index in Column: " << maxRow << std::endl;
    std::cout << "Max data row index in Column: " << maxDataRow << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
