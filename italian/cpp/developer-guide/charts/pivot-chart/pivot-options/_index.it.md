---
title: Come gestire PivotChart con PivotOptions in C++
linktitle: Opzioni Pivot
type: docs
weight: 10
url: /it/cpp/how-to-manage-pivotchart-with-pivotoptions/
description: Come gestire PivotChart con PivotOptions utilizzando C++.
keywords: PivotChart
---

## Cosa è un PivotChart

Un PivotChart in Excel è una rappresentazione grafica dei dati creata da una tabella pivot. Consente agli utenti di visualizzare e analizzare dinamicamente i dati riassumendo e visualizzando le informazioni in forma di grafico. I PivotCharts sono interattivi e possono essere facilmente modificati per mostrare diverse prospettive dei dati, rendendoli uno strumento potente per l'analisi e la presentazione dei dati in Excel.

## Come gestire PivotChart con PivotOptions

Utilizzando Aspose.Cells, è possibile utilizzare [**PivotOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/pivotoptions/) per gestire il PivotChart.

File di esempio e codice:  
[File di esempio](Sample.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path for the sample Excel file
    U16String path = u"..\\Data\\01_SourceDirectory\\";

    // Create a Workbook object from the sample file
    Workbook book(path + u"Sample.xlsx");

    // Get the first chart from the first worksheet
    Chart chart = book.GetWorksheets().Get(0).GetCharts().Get(0);

    // Get the PivotOptions from the chart
    PivotOptions opt = chart.GetPivotOptions();

    // Hide ZoneFilter in PivotChart
    opt.SetDropZoneFilter(false); // HideZoneFilter

    // You can set more properties, try them!
    // opt.SetDropZoneCategories(false);  // HideZoneCategories
    // opt.SetDropZoneData(false);        // HideZoneData
    // opt.SetDropZoneSeries(false);      // HideZoneSeries
    // opt.SetDropZonesVisible(false);    // Hide All

    // Save the modified file to see the effect
    book.Save(path + u"HideZoneFilter.xlsx");

    std::cout << "Pivot chart updated and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Con il codice di esempio sopra, è possibile controllare il file di risultato con l'effetto seguente, come mostrato nella figura:

**![Output](Output.png)**
