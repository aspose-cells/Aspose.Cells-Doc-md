---
title: Shape Typ der Datenbeschriftungen im Diagramm mit C++ festlegen
linktitle: Legen Sie den Formtyp der Datenbeschriftungen des Diagramms fest
description: Erfahren Sie, wie Sie den Shape Typ der Datenbeschriftungen in Diagrammen mit Aspose.Cells for C++ festlegen. Unser Leitfaden erklärt die verfügbaren Shape Typen und zeigt, wie Sie den passenden Shape Typ für Ihre Datenbeschriftungen auswählen, um die Präsentation und Benutzerfreundlichkeit Ihrer Diagramme zu verbessern.
keywords: Aspose.Cells for C++, Diagrammerstellung, Datenbeschriftungen, Shape Typen, Präsentation, Benutzerfreundlichkeit.
type: docs
weight: 110
url: /de/cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **Mögliche Verwendungsszenarien**
Sie können den Shape-Typ der Datenbeschriftungen im Diagramm ändern, indem Sie die Eigenschaft `DataLabels.ShapeType` verwenden. Sie akzeptiert den Wert des `DataLabelShapeType`-Enums und ändert entsprechend den Shape-Typ der Datenbeschriftungen. Einige seiner Werte sind:

{{< highlight java >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}

## **Festlegen des Formtyps von Datenbeschriftungen des Diagramms**
Das folgende Beispiel ändert den Shape-Typ der Datenbeschriftungen im Diagramm auf `DataLabelShapeType.WedgeEllipseCallout`. Bitte beachten Sie die [Beispieldatei Excel](60489778.xlsx), die in diesem Beispiel verwendet wird, und die [Ausgabedatei Excel](60489779.xlsx), die daraus generiert wurde. Der Screenshot zeigt die Wirkung des Codes auf die Beispiel-Excel-Datei. 

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)

## **Beispielcode**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Load source Excel file
    U16String inputFilePath = u"sampleSetShapeTypeOfDataLabelsOfChart.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first chart
    Chart ch = ws.GetCharts().Get(0);

    // Access first series
    Series srs = ch.GetNSeries().Get(0);

    // Set the shape type of data labels i.e. Speech Bubble Oval
    srs.GetDataLabels().SetShapeType(DataLabelShapeType::WedgeEllipseCallout);

    // Save the output Excel file
    U16String outputFilePath = u"outputSetShapeTypeOfDataLabelsOfChart.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Shape type of data labels set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
