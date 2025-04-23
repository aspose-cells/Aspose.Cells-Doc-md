---
title: Ottieni tutti gli indici delle righe nascoste dopo aver aggiornato il filtro automatico con C++
linktitle: Ottieni tutti gli indici delle righe nascoste dopo l aggiornamento dell AutoFiltro
type: docs
weight: 320
url: /it/cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: Scopri come ottenere tutti gli indici delle righe nascoste dopo aver aggiornato il filtro automatico usando l API Aspose.Cells for C++.
keywords: Ottieni tutti gli indici delle righe nascoste dopo l aggiornamento dell AutoFiltro, Ottieni tutti gli indici delle righe nascoste dopo l aggiornamento dell AutoFiltro, Recupera tutti gli indici delle righe nascoste dopo l aggiornamento dell AutoFiltro
---

## **Possibili Scenari di Utilizzo**

Quando si applica l'autofiltro sulle celle del foglio di lavoro, alcune righe vengono nascoste automaticamente. Ma potrebbe essere il caso che alcune righe siano già state nascoste manualmente dall'utente finale di Excel e non sono nascoste da un autofiltro. Ciò rende difficile sapere quali delle righe sono nascoste dall'autofiltro e quali sono nascoste manualmente dall'utente finale di Excel. Aspose.Cells affronta questo problema utilizzando il metodo int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/refresh/). Questo metodo restituisce gli indici di riga di tutte le righe nascoste dall'autofiltro e non manualmente dall'utente finale di Excel.

## **Ottenere tutti gli indici delle righe nascoste dopo l'aggiornamento dell'autofiltro**

Si prega di vedere il seguente codice di esempio che carica il [file Excel di esempio](64716909.xlsx) che contiene alcune delle righe nascoste manualmente dall'utente finale di Excel. Il codice applica l'autofiltro e lo aggiorna utilizzando il metodo int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/refresh/) che restituisce gli indici di riga di tutte le righe nascoste dall'autofiltro. Poi stampa gli indici delle righe nascoste sulla console insieme ai nomi e ai valori delle celle.

## **Codice di Esempio**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = srcDir + U16String(u"sampleGetAllHiddenRowsIndicesAfterRefreshingAutoFilter.xlsx");
    Workbook workbook(inputFilePath);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    AutoFilter autoFilter = worksheet.GetAutoFilter();
    autoFilter.AddFilter(0, u"Orange");

    Vector<int32_t> rowIndices = autoFilter.Refresh(true);

    std::cout << "Printing Rows Indices, Cell Names and Values Hidden By AutoFilter." << std::endl;
    std::cout << "--------------------------" << std::endl;

    for (int32_t i = 0; i < rowIndices.GetLength(); i++)
    {
        int32_t r = rowIndices[i];
        Cell cell = worksheet.GetCells().Get(r, 0);
        std::cout << r << "\t" << cell.GetName().ToUtf8() << "\t" << cell.GetStringValue().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Output della console**

{{< highlight java >}}

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.

\--------------------------

1       A2      Apple

2       A3      Apple

3       A4      Apple

6       A7      Apple

7       A8      Apple

11      A12     Pear

12      A13     Pear

{{< /highlight >}}
