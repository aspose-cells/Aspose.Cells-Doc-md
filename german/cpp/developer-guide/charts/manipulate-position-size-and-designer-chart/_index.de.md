---
title: Position, Größe und Designer Diagramm mit C++ bearbeiten
linktitle: Position, Größe und Designer des Diagramms manipulieren
description: Erfahren Sie, wie Sie Aspose.Cells for C++ effektiv nutzen, um die Position, Größe und das Designer Diagramm in Microsoft Excel zu manipulieren. Unser Leitfaden zeigt, wie man diese Eigenschaften für eine verbesserte Anordnung und Visualisierung anpasst.
keywords: Aspose.Cells for C++, Position, Größe, Designer Diagramm, Microsoft Excel, Layout, Visualisierung.
type: docs
weight: 45
url: /de/cpp/manipulate-position-size-and-designer-chart/
---

## **Chart-Position und Größe**
Manchmal möchten Sie die Position oder Größe des neuen oder vorhandenen Diagramms innerhalb des Arbeitsblatts ändern. Aspose.Cells bietet die Eigenschaft [Chart.GetChartObject()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getchartobject/), um dies zu erreichen. Sie können seine Untereigenschaften verwenden, um das Diagramm mit neuer **Höhe** und **Breite** neu zu dimensionieren oder mit neuen **X**- und **Y**-Koordinaten neu zu positionieren.

### **Steuerung der Diagrammposition und -größe**
Um die Position (X, Y-Koordinaten) oder Größe (Höhe, Breite) des Diagramms zu ändern, verwenden Sie diese Eigenschaften:

1. [Chart.GetX()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getx/)
1. [Chart.GetY()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gety/)
1. [Chart.GetHeight()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getheight/)
1. [Chart.GetWidth()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getwidth/)

Das folgende Beispiel erläutert die Verwendung der obigen APIs. Es lädt die vorhandene Arbeitsmappe, die ein Diagramm im ersten Arbeitsblatt enthält. Dann ändert es die Größe und Position des Diagramms mit Aspose.Cells neu.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"chart.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"chart.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(1);

    // Load the chart from the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Resize the chart
    chart.GetChartObject().SetWidth(400);
    chart.GetChartObject().SetHeight(300);

    // Reposition the chart
    chart.GetChartObject().SetX(250);
    chart.GetChartObject().SetY(150);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Chart resized and repositioned successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Manipulation von Designer-Diagrammen**
Es gibt Zeiten, in denen Sie Diagramminhalte und -elemente in Designer-Vorlagendateien manipulieren oder ändern müssen. Aspose.Cells unterstützt die vollständige Manipulation von Designer-Diagramminhalten und -elementen. Die Daten, Diagramminhalte, Hintergrundbild und Formatierungen können mit Genauigkeit beibehalten werden.

### **Manipulation von Designer-Diagrammen in Vorlagendateien**
Verwenden Sie die diagrammbezogene API, um Designer-Diagramme in Vorlagendateien zu manipulieren. Sie können beispielsweise die Eigenschaft Worksheet.Charts verwenden, um die vorhandene Diagrammsammlung in der Vorlagendatei zu erhalten.

#### **Erstellen eines Diagramms**
Das folgende Beispiel zeigt, wie man ein Pyramiden-Diagramm erstellt. Wir werden dieses Diagramm später bearbeiten.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;

    int sheetIndex = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(4);
    worksheet.GetCells().Get(u"B2").PutValue(20);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    int chartIndex = worksheet.GetCharts().Add(ChartType::Pyramid, 5, 0, 15, 5);
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    chart.GetNSeries().Add(u"A1:B3", true);

    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Excel file created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Manipulation des Diagramms**
Das folgende Beispiel zeigt, wie man das vorhandene Diagramm manipuliert. In diesem Beispiel ändern wir das oben erstellte Diagramm. In der generierten Ausgabe beachten Sie, dass das Datumslabel eines Datenpunkts auf 'Vereinigtes Königreich, 30K' gesetzt wurde.

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
    U16String inputFilePath = srcDir + u"piechart.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Open the existing file
    Workbook workbook(inputFilePath);

    // Get the designer chart in the second sheet
    Worksheet sheet = workbook.GetWorksheets().Get(1);
    Chart chart = sheet.GetCharts().Get(0);

    // Get the data labels in the data series of the third data point
    DataLabels datalabels = chart.GetNSeries().Get(0).GetPoints().Get(2).GetDataLabels();

    // Change the text of the label
    datalabels.SetText(u"Unided Kingdom, 400K ");

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Data label text updated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Manipulation eines Liniendiagramms in der Designer-Vorlage**
In diesem Beispiel werden wir ein Liniendiagramm manipulieren. Wir werden einige Datenreihen zu dem vorhandenen Diagramm hinzufügen und deren Linienfarben ändern.

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the designer chart in the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Chart chart = worksheet.GetCharts().Get(0);

    // Add the third data series to it
    chart.GetNSeries().Add(U16String(u"{60, 80, 10}"), true);

    // Add another data series (fourth) to it
    chart.GetNSeries().Add(U16String(u"{0.3, 0.7, 1.2}"), true);

    // Plot the fourth data series on the second axis
    chart.GetNSeries().Get(3).SetPlotOnSecondAxis(true);

    // Change the Border color of the second data series
    chart.GetNSeries().Get(1).GetBorder().SetColor(Color::Green());

    // Change the Border color of the third data series
    chart.GetNSeries().Get(2).GetBorder().SetColor(Color::Red());

    // Make the second value axis visible
    chart.GetSecondValueAxis().SetIsVisible(true);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Chart modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
