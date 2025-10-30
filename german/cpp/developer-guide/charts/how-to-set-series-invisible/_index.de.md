---
title: So setzen Sie eine Serie mit C++ unsichtbar
linktitle: Wie man Serien unsichtbar macht
description: In Excel Diagrammen müssen Sie möglicherweise Serien unsichtbar machen. Dieser Artikel beschreibt, wie man Aspose.Cells mit C++ dafür nutzt.
keywords: Excel Diagramm, Series, Unsichtbar, Gefiltert.
type: docs
weight: 74
url: /de/cpp/how-to-set-series-invisible/
---

## Wie man Serien in Excel-Diagrammen unsichtbar macht

In Excel-Diagrammen können Sie mit einem Rechtsklick auf das Diagramm "Daten auswählen" wählen und im Popup-Fenster festlegen, ob eine Serie sichtbar sein soll, indem Sie sie an- oder abwählen. Sie können die folgende [Beispieldatei](SeriesFiltered.xlsx) herunterladen und in Excel öffnen, um diese Funktion wie in der Abbildung gezeigt zu erreichen. Anschließend erklären wir, wie man dies mit der Aspose.Cells-Bibliothek umsetzt.

![todo:image_alt_text](series-invisible.png)

## Wie man Serien mit Aspose.Cells unsichtbar macht 

Wir verwenden den folgenden Code, um Serien mit Aspose.Cells unsichtbar zu machen:

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

Sie können die folgende [Inputdatei](SeriesFiltered.xlsx) und [Ausgabedatei](output.xlsx) erhalten.

Wie in der Abbildung unten gezeigt, sind die ersten beiden Serien, die ursprünglich sichtbar waren, in der Ausgabedatei unsichtbar geworden.  
![todo:image_alt_text](output.png)
{{< app/cells/assistant language="cpp" >}}
