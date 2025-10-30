---
title: Popola i dati prima per riga poi per colonna con C++
linktitle: Popola prima i dati per riga e poi per colonna
type: docs
weight: 1000
url: /it/cpp/populate-data-first-by-row-then-by-column/
description: Impara come popolare i dati prima per riga poi per colonna tramite l API Aspose.Cells for C++.
keywords: Popola prima i dati per riga e poi per colonna, Inserisci prima i dati per riga e poi per colonna, Aggiungi prima i dati per riga e poi per colonna, Inserimento dati ad alte prestazioni, Aggiunta dati ad alte prestazioni
---

{{% alert color="primary" %}} 

Popolare un foglio di calcolo con i dati prima per riga e poi per colonna migliora le prestazioni complessive.

{{% /alert %}} 

Inserire i dati nella sequenza A1, B1, A2, B2 è più veloce rispetto a A1, A2, B1, B2. Se ci sono molte celle in un foglio di lavoro e si segue la seconda sequenza, ovvero si riempiono i dati riga per riga, questo suggerimento può rendere il programma molto più veloce.

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
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook
    Workbook workbook;

    // Populate Data into Cells
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();
    cells.Get(u"A1").PutValue(U"data1");
    cells.Get(u"B1").PutValue(U"data2");
    cells.Get(u"A2").PutValue(U"data3");
    cells.Get(u"B2").PutValue(U"data4");

    // Save workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
