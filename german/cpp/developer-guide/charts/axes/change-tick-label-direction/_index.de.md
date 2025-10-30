---
title: Ändern Sie die Richtung der Tick Label mit C++
linktitle: Ändern Sie die Ausrichtung der Tickbeschriftung
description: Lernen Sie, wie man die Richtung der Tick Labels in Aspose.Cells for C++ ändert. Unser Leitfaden hilft Ihnen zu verstehen, wie Sie die Orientierung der Tick Labels auf Achsen anpassen, einschließlich horizontaler, vertikaler und schräger Ausrichtung.
keywords: Aspose.Cells for C++, Tick Labels, Richtung, Orientierung, Achsen, horizontal, vertikal, schräg.
type: docs
weight: 170
url: /de/cpp/change-tick-label-direction/
---

## **Ändern der Richtung der Markierungstexte**

Aspose.Cells bietet die Möglichkeit, die Richtung der Diagramm-Tick-Labels mit der [**TickLabels.GetDirectionType()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/ticklabels/getdirectiontype/) Eigenschaft zu ändern. Die [**TickLabels.GetDirectionType()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/ticklabels/getdirectiontype/) Eigenschaft akzeptiert den [**ChartTextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextdirectiontype) Enumeration-Wert. Das [**ChartTextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextdirectiontype) Enumeration bietet die folgenden Mitglieder:

- Horizontal
- Vertikal
- Drehen90
- Drehen270
- Gestapelt

Das folgende Bild vergleicht die Quell- und Ausgabedateien:

### **Quelldateibild**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **Ausgabedateibild**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

Der folgende Code-Schnipsel ändert die Richtung der Tickbeschriftung von Rotate90 auf Horizontal.

## **Beispielcode**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Directory source and output paths
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook and load the sample Excel file
    Workbook workbook(sourceDir + u"SampleChangeTickLabelDirection.xlsx");

    // Obtain the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Load the chart from the source worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Set the category axis tick labels direction to Horizontal
    chart.GetCategoryAxis().GetTickLabels().SetDirectionType(ChartTextDirectionType::Horizontal);

    // Output the modified workbook to a new file
    workbook.Save(outDir + u"outputChangeChartDataLableDirection.xlsx");

    std::cout << "Chart tick label direction changed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Die Quell- und Ausgabedateien können von den folgenden Links heruntergeladen werden.

[Quelldatei](105480221.xlsx)

[Ausgabedatei](105480223.xlsx)
{{< app/cells/assistant language="cpp" >}}
