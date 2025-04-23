---
title: Come impostare una Serie come invisibile con C++
linktitle: Come impostare la serie come invisibile
description: In Excel, nel grafico potresti aver bisogno di rendere invisiva una serie. Questo articolo descrive come usare Aspose.Cells con C++ per farlo.
keywords: Grafico Excel, Serie, Invisibile, ÈFiltrato.
type: docs
weight: 74
url: /it/cpp/how-to-set-series-invisible/
---

## Come impostare le serie come invisibili nel grafico Excel

In Excel, puoi cliccare con il tasto destro su un grafico, cliccare su "Seleziona dati", e nella finestra popup puoi impostare se una serie è visibile spuntando o deselezionando l'opzione. Puoi scaricare il seguente [file di esempio](SeriesFiltered.xlsx) e operarlo in Excel come mostrato nella figura per ottenere questa funzione. Successivamente, ti spiegheremo come farlo usando la libreria Aspose.Cells.

![todo:image_alt_text](series-invisible.png)

## Come impostare le serie come invisibili usando Aspose.Cells 

Usiamo il seguente codice per impostare le serie come invisibili usando Aspose.Cells:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // File path for the input and output Excel files
    U16String filePath(u"..\\Data\\01_SourceDirectory\\");

    // Open an existing Excel file
    Workbook workbook(filePath + u"SeriesFiltered.xlsx");

    // Access the charts collection of the first worksheet
    ChartCollection charts = workbook.GetWorksheets().Get(0).GetCharts();

    // Access a specific chart by name
    Chart chart = charts.Get(u"Chart 1");

    // Access filtered and non-filtered series collections
    SeriesCollection nSeriesFiltered = chart.GetFilteredNSeries();
    SeriesCollection nSeries = chart.GetNSeries();

    // Set the visibility of the first two series to be filtered
    nSeries.Get(1).SetIsFiltered(true);
    nSeries.Get(0).SetIsFiltered(true);

    // Save the modified Excel file
    workbook.Save(filePath + u"output.xlsx");

    std::cout << "Series filtered successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Puoi ottenere il seguente [File di input](SeriesFiltered.xlsx) e [file di output](output.xlsx).

Come mostrato nella figura sotto, le prime due serie, che erano visibili originariamente, sono diventate invisibili nel file di output.  
![todo:image_alt_text](output.png)
