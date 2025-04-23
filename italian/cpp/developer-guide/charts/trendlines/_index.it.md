---
title: Ottieni il testo dell equazione della Trendline del Grafico con C++
linktitle: Retta di Tendenza
description: Impara come usare Aspose.Cells for C++ per recuperare il testo dell equazione di una trendline in un grafico creato in Microsoft Excel. La nostra guida dimostrerà come accedere ed estrarre l equazione di una trendline per ulteriori analisi o visualizzazione.
keywords: Aspose.Cells for C++, Trendline del grafico, Testo dell equazione, Microsoft Excel, Analisi dei dati, Visualizzazione.
type: docs
weight: 110
url: /it/cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

È possibile recuperare il Testo dell'Equazione della Retta di Tendenza utilizzando Aspose.Cells. Aspose.Cells fornisce proprietà [**Trendline.GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/gettext/) che restituisce il testo dell'equazione della retta di tendenza. Per utilizzare questa proprietà, sarà prima necessario chiamare il metodo [**Chart.Calculate()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/calculate/).

{{% /alert %}}

Lo screenshot seguente mostra il grafico con una Trendline e il suo testo dell’equazione mostrato in rosso. Recupereremo questo testo usando la proprietà [**Trendline.GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/gettext/) nel seguente esempio di codice.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## Codice C++ per ottenere il testo dell'equazione della trendline del grafico

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object from source Excel file
    Workbook workbook(srcDir + u"source.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Calculate the Chart first to get the Equation Text of Trendline
    chart.Calculate();

    // Access the Trendline
    Trendline trendLine = chart.GetNSeries().Get(0).GetTrendLines().Get(0);

    // Read the Equation Text of Trendline
    std::cout << "Equation Text: " << trendLine.GetDataLabels().GetText().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Output generato dal codice di esempio

Questo è l'output console del codice di esempio precedente.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
