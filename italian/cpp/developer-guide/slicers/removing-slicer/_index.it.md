---
title: Rimuovere Slicer con C++
linktitle: Rimozione del filtro
type: docs
weight: 30
url: /it/cpp/removing-slicer/
description: Impara come rimuovere slicer nei file Excel programmaticamente usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

Se vuoi rimuovere un slicer in Microsoft Excel, selezionalo e premi il pulsante *Elimina*. Allo stesso modo, se vuoi rimuoverlo usando l'API di Aspose.Cells programmaticamente, utilizza il metodo [**Worksheet.Slicers.Remove()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicercollection/remove/). Rimuoverà il slicer dal foglio di lavoro.

## **Rimozione dello slicer**

Il seguente codice di esempio carica il [file Excel di esempio](67338478.xlsx) che contiene un filtro esistente. Accede ai filtri e li rimuove. Infine, salva il lavoro come [file Excel di output](67338477.xlsx). La seguente schermata mostra il filtro che verrà rimosso dopo l'esecuzione del codice di esempio.

![todo:image_alt_text](removing-slicer_1.png)

## **Codice di Esempio**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing slicer.
    U16String inputFilePath(u"sampleRemovingSlicer.xlsx");
    Workbook wb(inputFilePath);

    // Access first worksheet.
    WorksheetCollection worksheets = wb.GetWorksheets();
    Worksheet ws = worksheets.Get(0);

    // Access the first slicer inside the slicer collection.
    SlicerCollection slicers = ws.GetSlicers();
    Slicer slicer = slicers.Get(0);

    // Remove slicer.
    slicers.Remove(slicer);

    // Save the workbook in output XLSX format.
    U16String outputFilePath(u"outputRemovingSlicer.xlsx");
    wb.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Slicer removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
