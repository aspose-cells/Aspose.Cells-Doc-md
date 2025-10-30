---
title: Aggiungi Connessione Pivot con C++
linktitle: Aggiungi connessione pivot
type: docs
weight: 30
url: /it/cpp/add-pivot-connection/
description: Impara come aggiungere una connessione pivot con la libreria Aspose.Cells usando C++.
keywords: Aggiungi connessione pivot senza Office 2013, Office 2016, Office 2019 e Office 365.
---

## **Possibili Scenari di Utilizzo**

Se si desidera associare lo slicer e la tabella pivot in Excel, è necessario fare clic con il pulsante destro dello slicer e selezionare l'elemento "Connettere i report...". Nell'elenco delle opzioni, è possibile operare sulla casella di controllo. Allo stesso modo, se si desidera associare lo slicer e la tabella pivot tramite Aspose.Cells API in modo programmato, si prega di utilizzare il metodo [**Slicer.AddPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/addpivotconnection/). Si assocerà lo slicer e la tabella pivot.

## **Associa Slicer e Tabella pivot**

Il seguente codice di esempio carica il [file Excel di esempio](add-pivot-connection.xlsx) che contiene un slicer esistente. Accede al Slicer e quindi associa Slicer e Tabella pivot. Infine, salva il workbook come [output Excel file](add-pivot-connection-out.xlsx). 

## **Codice di Esempio**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"add-pivot-connection.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"add-pivot-connection-out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access first worksheet
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);

    // Access the first PivotTable inside the PivotTable collection
    PivotTableCollection pivotTables = worksheet.GetPivotTables();
    PivotTable pivotTable = pivotTables.Get(0);

    // Access the first slicer inside the slicer collection
    SlicerCollection slicers = worksheet.GetSlicers();
    Slicer slicer = slicers.Get(0);

    // Add PivotTable connection
    slicer.AddPivotConnection(pivotTable);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "PivotTable connection added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
