---
title: Setzen Sie den Text des Legendeneintrags im Diagramm auf Keine mit C++
linktitle: Setzen Sie den Text des Legendeneintrags im Diagramm auf Keine
description: Lernen Sie, wie man Aspose.Cells for C++ verwendet, um den Text des Legendeneintrags auf Keine zu setzen. Unser Leitfaden zeigt, wie man die Füllfarbe der Legenden Einträge in Microsoft Excel Diagrammen zur besseren Visualisierung und Anpassung ändert.
keywords: Aspose.Cells for C++, Diagramm Legenden Eintrag Füllung, Microsoft Excel, Visualisierung, Anpassung.
type: docs
weight: 320
url: /de/cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/
---

{{% alert color="primary" %}}

Wenn Sie den Text der Diagrammlegendeneintragsfüllung auf keine setzen möchten, sodass er nicht im Diagrammlegendenbereich angezeigt wird, setzen Sie bitte [**LegendEntry.IsTextNoFill**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/legendentry/istextnofill/) auf **true**.

{{% /alert %}}

Der folgende Beispielcode setzt den Text der zweiten Diagrammlegendeneintragsfüllung auf keine. Laden Sie bitte die [Beispieldatei Excel](5115219.xlsx) herunter, die in diesem Code verwendet wird, und die [Ausgabedatei Excel](5115217.xlsx), die von ihr generiert wird, zur Referenz.

Der folgende Screenshot hebt die Auswirkung dieses Codes auf die [Beispieldatei Excel](5115219.xlsx) hervor.

![todo:image_alt_text](set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells_1.png)

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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"ChartLegendEntry_out.xlsx";

    // Open the template file
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the sheet
    Chart chart = sheet.GetCharts().Get(0);

    // Set text of second legend entry fill to none
    chart.GetLegend().GetLegendEntries().Get(1).SetIsTextNoFill(true);

    // Save the workbook in xlsx format
    workbook.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Chart legend entry modified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
