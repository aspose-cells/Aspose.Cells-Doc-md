---
title: Rimuovere Connessione Pivot con C++
linktitle: Rimuovere la connessione pivot
type: docs
weight: 30
url: /it/cpp/remove-pivot-connection/
description: Impara come rimuovere la connessione pivot con la libreria Aspose.Cells usando C++.
keywords: Rimuovere la connessione pivot senza office 2013, office 2016, office 2019 e office 365.
---

## **Possibili Scenari di Utilizzo**

Se desideri dissociare lo slicer e la tabella pivot in Excel, devi fare clic con il pulsante destro sullo slicer e selezionare l'elemento "Connessioni rapporto...". Nell'elenco delle opzioni, puoi operare sulla casella di controllo. Allo stesso modo, se desideri dissociare lo slicer e la tabella pivot utilizzando l'API di Aspose.Cells in modo programmatico, utilizza il metodo [**Slicer.RemovePivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/removepivotconnection/). Dissocerà lo slicer e la tabella pivot.

## **Dissociare lo slicer e la tabella pivot**

Il seguente codice di esempio carica il [file di Excel di esempio](remove-pivot-connection.xlsx) che contiene uno slicer esistente. Accede agli slicer e quindi dissocia lo slicer e la tabella pivot. Infine, salva il workbook come [file di Excel di output](remove-pivot-connection-out.xlsx). 

## **Codice di Esempio**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing slicer
    U16String inputFilePath = u"remove-pivot-connection.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access the first PivotTable inside the PivotTable collection
    PivotTable pivottable = ws.GetPivotTables().Get(0);

    // Access the first slicer inside the slicer collection
    Slicer slicer = ws.GetSlicers().Get(0);

    // Remove PivotTable connection
    slicer.RemovePivotConnection(pivottable);

    // Save the workbook in output XLSX format
    U16String outputFilePath = u"remove-pivot-connection-out.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Pivot connection removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
