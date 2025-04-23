---
title: Inserisci Slicer con C++
linktitle: Slicer
type: docs
weight: 170
url: /it/cpp/create-slicer/
description: Gestisci gli slicer dei file Excel con Aspose.Cells usando C++.
---

## **Possibili Scenari di Utilizzo**

Uno slicer è usato per filtrare rapidamente i dati. Può essere usato per filtrare i dati sia in una tabella sia in una tabella pivot. Microsoft Excel ti permette di creare uno slicer selezionando una tabella o una tabella pivot e cliccando su *Inserisci > Slicer*. Aspose.Cells permette anche di creare uno slicer usando il metodo [**Worksheet.Slicers.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicercollection/add/).

## **Creare un selettore per una tabella pivot**

Si prega di vedere il seguente codice di esempio. Carica il [file Excel di esempio](67338470.xlsx) che contiene la tabella pivot. Crea quindi lo slicer in base al primo campo pivot di base. Infine, salva il libro di lavoro nel formato [XLSX di output](67338471.xlsx) e [XLSB di output](67338472.xlsb). Nella seguente schermata viene mostrato lo slicer creato da Aspose.Cells nel file Excel di output.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **Codice di Esempio**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
using namespace Aspose::Cells::Slicers;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleCreateSlicerToPivotTable.xlsx";

    // Path of output Excel files
    U16String outputFilePathXlsx = outDir + u"outputCreateSlicerToPivotTable.xlsx";
    U16String outputFilePathXlsb = outDir + u"outputCreateSlicerToPivotTable.xlsb";

    // Load sample Excel file containing pivot table
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first pivot table inside the worksheet
    PivotTable pt = ws.GetPivotTables().Get(0);

    // Add slicer relating to pivot table with first base field at cell B22
    int idx = ws.GetSlicers().Add(pt, u"B22", pt.GetBaseFields().Get(0));

    // Access the newly added slicer from slicer collection
    Slicer slicer = ws.GetSlicers().Get(idx);

    // Save the workbook in output XLSX format
    wb.Save(outputFilePathXlsx, SaveFormat::Xlsx);

    // Save the workbook in output XLSB format
    wb.Save(outputFilePathXlsb, SaveFormat::Xlsb);

    std::cout << "Slicer created and workbooks saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Creare un selettore per tabella di Excel**

Si prega di vedere il seguente codice di esempio. Carica il [file Excel di esempio](sampleCreateSlicerToExcelTable.xlsx) che contiene una tabella. Crea quindi lo slicer in base alla prima colonna. Infine, salva il libro di lavoro nel formato [XLSX di output](outputCreateSlicerToExcelTable.xlsx).

### **Codice di Esempio**

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

    // Load sample Excel file containing a table
    Workbook workbook(srcDir + u"sampleCreateSlicerToExcelTable.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first table inside the worksheet
    ListObject table = worksheet.GetListObjects().Get(0);

    // Add slicer
    int idx = worksheet.GetSlicers().Add(table, 0, u"H5");

    // Save the workbook in output XLSX format
    workbook.Save(outDir + u"outputCreateSlicerToExcelTable.xlsx", SaveFormat::Xlsx);

    std::cout << "Slicer added successfully to the Excel table!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Argomenti Avanzati**
- [Modifica le proprietà dello slicer](/cells/it/cpp/change-slicer-properties/)
- [Disegna lo slicer durante il rendering di Excel in PDF](/cells/it/cpp/draw-slicer-while-rendering-excel-to-pdf/)
- [Formattazione del selettore](/cells/it/cpp/formatting-slicer/)
- [Rimozione dello slicer](/cells/it/cpp/removing-slicer/)
- [Rendering dello slicer](/cells/it/cpp/rendering-slicer/)
- [Aggiornamento dello slicer](/cells/it/cpp/updating-slicer/)
