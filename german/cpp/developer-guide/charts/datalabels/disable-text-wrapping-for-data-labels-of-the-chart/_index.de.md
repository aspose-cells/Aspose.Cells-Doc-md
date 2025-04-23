---
title: Deaktivieren Sie Zeilenumbruch für Datenbeschriftungen des Diagramms mit C++
linktitle: Zeilenumbruch für Datenbeschriftungen deaktivieren
description: Erfahren Sie, wie Sie den Zeilenumbruch für Datenbeschriftungen in Diagrammen mit Aspose.Cells for C++ deaktivieren. Unser Leitfaden zeigt Ihnen, wie Sie lange Beschriftungen daran hindern, sich zu überschneiden, und klarere und besser lesbare Diagramm Anzeigen bieten.
keywords: Aspose.Cells for C++, Diagrammerstellung, Datenbeschriftungen, Textumbruch, Überlappung, Lesbarkeit, Anzeigen.
type: docs
weight: 70
url: /de/cpp/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

Microsoft Excel 2013 ermöglicht es Benutzern, Texte in den Datenbeschriftungen des Diagramms umzubrechen oder nicht umzubrechen. Standardmäßig ist der Text in den Datenbeschriftungen des Diagramms umgebrochen.

Aspose.Cells bietet eine [**DataLabels.IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/istextwrapped/)-Eigenschaft, die Sie auf TRUE oder FALSE setzen können, um den Textumbruch der Datenbeschriftungen entsprechend zu aktivieren oder deaktivieren.

{{% /alert %}}

Der folgende Codebeispiel zeigt, wie der Textumbruch für die Datenbeschriftungen des Diagramms deaktiviert wird.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"Output_out.xlsx";

    // Load the sample Excel file inside the workbook object
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Disable the Text Wrapping of Data Labels in all Series
    chart.GetNSeries().Get(0).GetDataLabels().SetIsTextWrapped(false);
    chart.GetNSeries().Get(1).GetDataLabels().SetIsTextWrapped(false);
    chart.GetNSeries().Get(2).GetDataLabels().SetIsTextWrapped(false);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Text wrapping disabled successfully in data labels!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
