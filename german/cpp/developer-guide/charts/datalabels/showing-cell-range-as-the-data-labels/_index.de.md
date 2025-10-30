---
title: Zellenbereich als Datenbeschriftungen mit C++ anzeigen
linktitle: Anzeige des Zellenbereichs als Datenbeschriftungen
description: Erfahren Sie, wie Sie einen Zellbereich als Datenbeschriftungen in Diagrammen mit Aspose.Cells for C++ anzeigen. Unser Leitfaden zeigt, wie Sie die Beschriftungen mit Ihrer Datenquelle verknüpfen und formatieren, um genaue und aussagekräftige Informationen in Ihren Diagrammen bereitzustellen.
keywords: Aspose.Cells for C++, Diagrammerstellung, Datenbeschriftungen, Zellbereich, Datenquelle, Formatierung, Genauigkeit, aussagekräftige Informationen.
type: docs
weight: 130
url: /de/cpp/showing-cell-range-as-the-data-labels/
---

{{% alert color="primary" %}}

In Microsoft Excel 2013 können Sie einen Zellenbereich für Datenbeschriftungen anzeigen. Aspose.Cells unterstützt diese Funktion

{{% /alert %}}

## **Kontrollkästchen zum Anzeigen des Zellenbereichs als Datenbeschriftungen**

So zeigen Sie den Zellenbereich als Datenbeschriftungen in Microsoft Excel:

1. Wählen Sie die Seriendatenbeschriftungen aus und klicken Sie mit der rechten Maustaste, um das Kontextmenü zu öffnen.
1. Wählen Sie **Datenelemente formatieren** aus. Beschriftungsoptionen werden angezeigt.
1. Wählen oder deaktivieren Sie die Option **Beschriftung enthält - Wert aus Zellen**.

Der unten stehende Beispielcode greift auf die Beschriftungen von Diagrammserien zu und setzt die [**DataLabels.GetShowCellRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/getshowcellrange/)-Eigenschaft auf **true**, um die Option **Beschriftung enthält - Wert aus Zellen** auszuwählen.

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
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook from the source Excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Check the "Label Contains - Value From Cells"
    DataLabels dataLabels = chart.GetNSeries().Get(0).GetDataLabels();
    dataLabels.SetShowCellRange(true);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
