---
title: Hantera automatiska enheter för diagramaxeln som Microsoft Excel med C++
linktitle: Hantera automatiska enheter för diagramaxeln
description: Lär dig hur du hanterar automatiska enheter på diagramaxlar i Aspose.Cells for C++, liknande Microsoft Excel. Vår guide visar hur du konfigurerar och anpassar automatiska enheter på en diagramaxel, inklusive visning av vetenskaplig notation och justering av skalan.
keywords: Aspose.Cells for C++, diagramaxlar, automatiska enheter, Microsoft Excel, konfiguration, anpassning, vetenskaplig notation, skalning.
type: docs
weight: 120
url: /sv/cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/
---

## **Möjliga användningsscenario**
Tidigare versioner av Aspose.Cells kunde inte hantera automatiska enheter för diagramaxeln korrekt när diagrammet renderades till bild eller PDF. Nu stöder Aspose.Cells hanteringen av automatiska enheter för diagramaxeln. Det krävs ingen kodändring. Konvertera bara ditt diagram till bild eller PDF så kommer det att rendera diagramaxeln på samma sätt som Microsoft Excel gör.

## **Hantera automatiska enheter för diagramaxeln som Microsoft Excel**
Följande exempelkod laddar den [provisoriska Excelfilen](61767755.xlsx) och genererar [utdatan till PDF-diagrammet](61767752.pdf). Screenshoten visar de automatiska enheterna på diagramaxeln i röda rektanglar och jämför även det provisoriska Excelfilens diagram med utdatan till PDF-diagrammet. Båda är exakt likadana.

![todo:image_alt_text](handle-automatic-units-of-chart-axis-like-microsoft-excel_1.png)

## **Exempelkod**
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
