---
title: Wert des Gleichungstextes der Trendlinie im Diagramm mit C++ abrufen
linktitle: Trendlinien
description: Lernen Sie, wie Sie Aspose.Cells for C++ verwenden, um den Gleichungstext einer Trendlinie in einem in Microsoft Excel erstellten Diagramm abzurufen. Unser Leitfaden zeigt, wie Sie die Gleichung einer Trendlinie für weitere Analysen oder zur Anzeige zugreifen und extrahieren.
keywords: Aspose.Cells for C++, Diagramm Trendlinie, Gleichungstext, Microsoft Excel, Datenanalyse, Anzeige.
type: docs
weight: 110
url: /de/cpp/get-equation-text-of-chart-trendline/
---

{{% alert color="primary" %}}

Sie können den Gleichungstext der Diagramm-Trendlinie mithilfe von Aspose.Cells abrufen. Aspose.Cells bietet eine [**Trendline.GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/gettext/)-Eigenschaft, die den Gleichungstext der Diagrammtrendlinie zurückgibt. Um diese Eigenschaft zu nutzen, müssen Sie zunächst die Methode [**Chart.Calculate()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/calculate/) aufrufen.

{{% /alert %}}

Das folgende Bildschirmfoto zeigt das Diagramm mit einer Trendlinie, deren Gleichungstext in roter Farbe angezeigt wird. Wir werden diesen Text mit der [**Trendline.GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/gettext/)-Eigenschaft im folgenden Beispielcode abrufen.

![todo:image_alt_text](get-equation-text-of-chart-trendline_1.png)

## C++-Code zum Abrufen des Gleichungstextes der Chart-Trendlinie

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

## Ausgabe, die vom Beispielcode generiert wurde

Dies ist die Konsolenausgabe des obigen Beispiels.

{{< highlight java >}}

Equation Text: y = 8.1333x + 5

{{< /highlight >}}
