---
title: Mostra l opzione Pagina filtro report con C++
linktitle: Mostra l opzione di visualizzazione delle pagine del filtro del report
type: docs
weight: 110
url: /it/cpp/show-report-filter-pages-option/
description: Impara come abilitare l opzione "Mostra pagine del filtro del report" nelle tabelle pivot utilizzando Aspose.Cells for C++.
---

## **Mostra l'opzione di visualizzazione delle pagine del filtro del report**
Excel supporta la creazione di tabelle pivot, l'aggiunta di filtri report e l'abilitazione dell'opzione "Mostra pagine del filtro del report". Aspose.Cells supporta anche questa funzione per attivare l'opzione "Mostra pagine del filtro del report" sulla tabella pivot creata. Di seguito un screenshot che mostra l'opzione "Mostra pagine del filtro del report" in Excel.

![todo:image_alt_text](show-report-filter-pages-option_1.png)

Il file di origine e i file di output di esempio possono essere scaricati da qui per testare il codice di esempio:

` `[File Excel di origine](81920786.xlsx) 

[File Excel di output](81920787.xlsx)

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

    // Load template file
    Workbook wb(srcDir + u"samplePivotTable.xlsx");

    // Get first pivot table in the worksheet
    PivotTable pt = wb.GetWorksheets().Get(1).GetPivotTables().Get(0);

    // Set pivot field
    pt.ShowReportFilterPage(pt.GetPageFields().Get(0));

    // Set position index for showing report filter pages
    pt.ShowReportFilterPageByIndex(pt.GetPageFields().Get(0).GetPosition());

    // Set the page field name
    pt.ShowReportFilterPageByName(pt.GetPageFields().Get(0).GetName());

    // Save the output file
    wb.Save(outDir + u"outputSamplePivotTable.xlsx");

    std::cout << "Pivot table report filter pages set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
