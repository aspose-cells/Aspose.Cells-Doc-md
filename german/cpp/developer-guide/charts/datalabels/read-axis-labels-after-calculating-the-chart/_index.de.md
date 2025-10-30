---
title: Achsenbeschriftungen nach der Berechnung des Diagramms mit C++ lesen
linktitle: Achsenbeschriftungen nach Berechnen des Diagramms lesen
description: Erfahren Sie, wie Sie Achsenbeschriftungen in Aspose.Cells for C++ nach der Diagrammberechnung lesen. Unser Leitfaden zeigt Ihnen, wie Sie Achsenbeschriftungen einschließlich Formatierung und Positionierung zugreifen und abrufen.
keywords: Aspose.Cells for C++, Diagramm, Achsenbeschriftungen, Berechnung, Lesen, Zugriff, Abrufen, Formatierung, Positionierung.
type: docs
weight: 90
url: /de/cpp/read-axis-labels-after-calculating-the-chart/
---

## **Mögliche Verwendungsszenarien**

Sie können die Achsenbeschriftungen Ihres Diagramms nach Berechnen seiner Werte mit der Methode [**Chart.Calculate()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/calculate/) lesen. Verwenden Sie für diesen Zweck die Methode [**Axis.GetAxisTexts()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/getaxistexts/), die die Liste der Achsenbeschriftungen zurückgibt.

## **Lesen Sie die Achsenbeschriftungen nach der Berechnung des Diagramms**

Siehe bitte den folgenden Beispielcode, der die [Beispieldatei für Excel](ReadAxisLabels.xlsx) lädt und die Kategorienachsenbeschriftungen des Diagramms im ersten Arbeitsblatt liest. Anschließend werden die Werte der Achsenbeschriftungen in der Konsole ausgegeben. Bitte sehen Sie sich die Konsolenausgabe des untenstehenden Beispielcodes als Referenz an.

## **Beispielcode**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook wb(srcDir + u"ReadAxisLabels.xlsx");

    Worksheet ws = wb.GetWorksheets().Get(0);

    Chart ch = ws.GetCharts().Get(0);

    ch.Calculate();

    Vector<U16String> lstLabels = ch.GetCategoryAxis().GetAxisTexts();

    std::wcout << L"Category Axis Labels: " << std::endl;
    std::wcout << L"---------------------" << std::endl;

    for (int32_t i = 0; i < lstLabels.GetLength(); ++i)
    {
        std::wcout << reinterpret_cast<const wchar_t*>(lstLabels[i].GetData()) << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Konsolenausgabe**

{{< highlight cpp >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
