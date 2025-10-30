---
title: Modifica le Proprietà dello Slicer con C++
linktitle: Cambia proprietà Slicer
type: docs
weight: 70
url: /it/cpp/change-slicer-properties/
description: Modifica le proprietà di uno Slicer nei file Excel usando Aspose.Cells con C++.
---

## **Possibili Scenari di Utilizzo**

Potrebbero esserci situazioni in cui potresti voler modificare le proprietà del Slicer come posizionamento o altezza riga. Aspose.Cells ti offre l'opzione di aggiornare queste proprietà.

## **Modifica le proprietà dello slicer**

Si prega di vedere il seguente codice di esempio. Carica il [file Excel di esempio](sampleCreateSlicerToExcelTable.xlsx) che contiene una tabella. Quindi crea il slicer in base alla prima colonna e cambia le sue proprietà come altezza riga, larghezza, è stampabile, titolo, ecc. Salva il workbook come [outputChangeSlicerProperties.xlsx](outputChangeSlicerProperties.xlsx).

## **Codice di Esempio**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing a table.
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    Workbook workbook(sourceDir + u"sampleCreateSlicerToExcelTable.xlsx");

    // Access first worksheet.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first table inside the worksheet.
    ListObject table = worksheet.GetListObjects().Get(0);

    // Add slicer
    int32_t idx = worksheet.GetSlicers().Add(table, 0, u"H5");

    Slicer slicer = worksheet.GetSlicers().Get(idx);
    slicer.SetPlacement(PlacementType::FreeFloating);
    slicer.SetRowHeightPixel(50);
    slicer.SetWidthPixel(500);
    slicer.SetTitle(u"Aspose");
    slicer.SetAlternativeText(u"Alternate Text");
    slicer.SetIsPrintable(false);
    slicer.SetIsLocked(false);

    // Refresh the slicer.
    slicer.Refresh();

    // Save the workbook in output XLSX format.
    workbook.Save(outputDir + u"outputChangeSlicerProperties.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
