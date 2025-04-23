---
title: Aggiornare e calcolare la tabella pivot con elementi calcolati con C++
linktitle: Aggiorna e calcola la tabella pivot con elementi calcolati
type: docs
weight: 40
url: /it/cpp/refresh-and-calculate-pivot-table-having-calculated-items/
description: Aggiorna e calcola la tabella pivot con elementi calcolati usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Aspose.Cells ora supporta l'aggiornamento e il calcolo della tabella pivot con elementi calcolati. Si prega di utilizzare [**PivotTable.RefreshData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/refreshdata/) e [**PivotTable.CalculateData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/) come di consueto per eseguire questa funzione.

{{% /alert %}}

## **Aggiornare e calcolare la tabella pivot con elementi calcolati**

 Il seguente esempio di codice carica il [file Excel di origine](5115238.xlsx) che contiene una tabella pivot con tre elementi calcolati come "add", "div", "div2". Per prima cosa cambiamo il valore della cella D2 a 20, poi aggiorniamo e calcoliamo la tabella pivot utilizzando le API di Aspose.Cells e salviamo il workbook in formato PDF. I risultati nel [PDF di output](5115229.pdf) mostrano che Aspose.Cells ha aggiornato e calcolato con successo la tabella pivot con elementi calcolati. Puoi verificarlo manualmente inserendo il valore 20 in cella D2 e aggiornando la tabella pivot tramite il tasto rapido Alt+F5 o cliccando sul pulsante di aggiornamento della tabella pivot.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source Excel file containing a pivot table having calculated items
    U16String sampleFilePath = srcDir + u"sample.xlsx";
    Workbook workbook(sampleFilePath);

    // Access first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Change the value of cell D2
    sheet.GetCells().Get(u"D2").PutValue(20);

    // Refresh and calculate all the pivot tables inside this sheet
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    for (int32_t i = 0; i < pivotTables.GetCount(); ++i)
    {
        PivotTable pt = pivotTables.Get(i);
        pt.RefreshData();
        pt.CalculateData();
    }

    // Save the workbook in output PDF
    U16String outputFilePath = srcDir + u"RefreshAndCalculateItems_out.pdf";
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
