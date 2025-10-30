---
title: Inserisci Timeline con C++
linktitle: Timeline
type: docs
weight: 170
url: /it/cpp/create-timeline/
description: Impara come creare una linea temporale con Aspose.Cells usando C++.
---

## **Possibili Scenari di Utilizzo**

Invece di regolare i filtri per mostrare le date, puoi usare una Timeline PivotTable—un'opzione di filtro dinamico che ti permette di filtrare facilmente per data/ora e ingrandire il periodo desiderato con un controllo a cursore. Microsoft Excel ti permette di creare una timeline selezionando una tabella pivot e cliccando su *Inserisci > Timeline*. Aspose.Cells ti permette anche di creare una timeline usando il metodo [**Worksheet.Timelines.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.timelines/timelinecollection/add/).

## **Creare una timeline per una tabella pivot**

Si prega di consultare il codice di esempio seguente. Carica il [file di Excel di esempio](input.xlsx) contenente la tabella pivot. Crea quindi la timeline basata sul primo campo pivot di base. Infine, salva il workbook nel formato [XLSX di output](output.xlsx). La seguente schermata mostra la timeline creata da Aspose.Cells nel file Excel di output.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Codice di Esempio**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing pivot table
    U16String inputFilePath = u"input.xlsx";
    Workbook wb(inputFilePath);

    // Access second worksheet (index 1)
    Worksheet sheet = wb.GetWorksheets().Get(1);

    // Access first pivot table inside the worksheet
    PivotTable pivot = sheet.GetPivotTables().Get(0);

    // Add timeline relating to pivot table
    int index = sheet.GetTimelines().Add(pivot, 15, 1, u"Ship Date");

    // Access the newly added timeline from timeline collection
    Timeline timeline = sheet.GetTimelines().Get(index);

    // Save the modified workbook
    U16String outputFilePath = u"output.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Timeline added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
