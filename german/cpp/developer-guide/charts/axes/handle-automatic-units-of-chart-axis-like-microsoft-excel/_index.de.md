---
title: Automatische Achsen Einheiten im Diagramm wie Microsoft Excel mit C++ verwalten
linktitle: Automatische Achsen Einheiten verwalten
description: Lernen Sie, wie man automatische Einheiten auf Diagrammachsen in Aspose.Cells for C++, ähnlich wie bei Microsoft Excel, handhabt. Unser Leitfaden zeigt, wie man automatische Einheiten konfiguriert und anpasst, einschließlich der Anzeige wissenschaftlicher Notation und der Skalierung.
keywords: Aspose.Cells for C++, Diagrammachsen, automatische Einheiten, Microsoft Excel, Konfiguration, Anpassung, wissenschaftliche Notation, Skalierung.
type: docs
weight: 120
url: /de/cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/
---

## **Mögliche Verwendungsszenarien**
Ältere Versionen von Aspose.Cells konnten die automatischen Einheiten der Diagrammachse nicht ordnungsgemäß behandeln, wenn das Diagramm in ein Bild oder PDF gerendert wurde. Jetzt unterstützt Aspose.Cells die Behandlung automatischer Einheiten der Diagrammachse. Es gibt keinen Codeänderung. Konvertieren Sie einfach Ihr Diagramm in ein Bild oder PDF und es wird die Diagrammachse genauso rendern, wie es Microsoft Excel rendert.

## **Behandeln Sie automatische Einheiten der Diagrammachse wie Microsoft Excel**
Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](61767755.xlsx) und generiert das [Ausgabe-PDF-Diagramm](61767752.pdf). Der Screenshot zeigt die automatischen Einheiten der Diagrammachse in roten Rechtecken und vergleicht auch das Beispiel-Excel-Dateidiagramm mit dem Ausgabe-PDF-Diagramm. Beide sind genau gleich.

![todo:image_alt_text](handle-automatic-units-of-chart-axis-like-microsoft-excel_1.png)

## **Beispielcode**
```c++
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

    // Load the sample Excel file
    U16String inputFilePath = srcDir + u"sampleHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    WorksheetCollection worksheets = wb.GetWorksheets();
    Worksheet ws = worksheets.Get(0);

    // Access first chart
    ChartCollection charts = ws.GetCharts();
    Chart ch = charts.Get(0);

    // Render chart to PDF
    U16String outputFilePath = outDir + u"outputHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.pdf";
    ch.ToPdf(outputFilePath);

    std::cout << "Chart rendered to PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
