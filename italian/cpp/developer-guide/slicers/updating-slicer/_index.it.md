---
title: Aggiornare Slicer con C++
linktitle: Aggiornamento Slicer
type: docs
weight: 50
url: /it/cpp/updating-slicer/
description: Questo articolo mostra come aggiornare tabelle pivot collegate aggiornando lo slicer usando l API Aspose.Cells for C++.
keywords: Aspose.Cells C++ Aggiorna slicer, C++ come cambiare lo slicer, come regolare lo slicer in C++, come selezionare o deselezionare gli elementi dello slicer.
---

## **Possibili Scenari di Utilizzo**

Se vuoi aggiornare uno slicer in Microsoft Excel, seleziona o deseleziona gli elementi, quindi aggiornerà automaticamente la tabella dello slicer o la tabella pivot. Usa [**Slicer.GetSlicerCacheItems()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicercache/getslicercacheitems/) per selezionare o deselezionare gli elementi dello slicer con Aspose.Cells e poi chiama il metodo [**Slicer.Refresh()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/refresh/) per aggiornare la tabella dello slicer o la tabella pivot.

## **Come aggiornare il riquadro di selezione**

Il seguente codice di esempio carica il [file Excel di esempio](67338475.xlsx) che contiene un filtro esistente. Deseleziona il 2° e 3° elemento del filtro e aggiorna il filtro. Quindi salva il lavoro come [file Excel di output](67338476.xlsx). La seguente schermata mostra l'effetto del codice di esempio sul file Excel di esempio. Come puoi vedere nella schermata, l'aggiornamento del filtro con gli elementi selezionati ha anche aggiornato la tabella pivot di conseguenza.

![todo:image_alt_text](updating-slicer_1.png)

## **Codice di Esempio**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing slicer.
    U16String inputFilePath = u"sampleUpdatingSlicer.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet.
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access the first slicer inside the slicer collection.
    Slicer slicer = ws.GetSlicers().Get(0);

    // Access the slicer items.
    SlicerCacheItemCollection scItems = slicer.GetSlicerCache().GetSlicerCacheItems();

    SlicerCacheItemCollection items = slicer.GetSlicerCache().GetSlicerCacheItems();

    for (int i = 0; i < items.GetCount(); ++i)
    {
        SlicerCacheItem item = items.Get(i);
        if (item.GetValue() == u"Pink" || item.GetValue() == u"Green")
        {
            item.SetSelected(false);
        }
    }

    slicer.Refresh();

    // Save the modified workbook.
    U16String outputFilePath = u"out.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Slicer updated and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
