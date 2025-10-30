---
title: Ställ in Värden Formatkod för diagramserien med C++
linktitle: Nummerformat
type: docs
weight: 100
url: /sv/cpp/set-the-values-format-code-of-chart-series/
description: Lär dig hur du ställer in värden formatkod för diagramserier i Aspose.Cells for C++. Vår guide hjälper dig att förstå hur du formaterar dina diagramdataserier med rätt formatkod för att presentera data noggrant och professionellt.
keywords: Aspose.Cells for C++, diagramserier, värden formatkod, formatering, datapresentation, noggrannhet, professionalism.
---

## **Möjliga användningsscenario**
Du kan ställa in värden formatkod för diagramserier med hjälp av [Series.GetValuesFormatCode()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/getvaluesformatcode/) egenskapen. Denna egenskap är inte bara användbar för serier baserade på området i kalkylbladet utan fungerar också bra för serier skapade med en array av värden.

## **Ställ in värdenas formatkod för diagramserier**
Följande exempel på kod lägger till en serie i det tomma diagrammet som inte hade några serier tidigare. Det lägger till serien med hjälp av en värde-array. När serien är tillagd formateras den med koden `$#,##0` med hjälp av <a href="https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/getvaluesformatcode/">Series.GetValuesFormatCode()</a> egenskapen och siffran `10000` blir `$10,000`. Skärmbilden visar effekten av koden på <a href="51740712.xlsx">exempel-Excel-filen</a> och <a href="51740713.xlsx">utdata-Excel-filen</a> efter körning.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Exempelkod**
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
    U16String inputFilePath = srcDir + u"51740712.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"51740713.xlsx";

    // Load the source Excel file
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Access first chart
    Chart ch = worksheet.GetCharts().Get(0);

    // Add series using an array of values
    ch.GetNSeries().Add(U16String(u"{10000, 20000, 30000, 40000}"), true);

    // Access the series and set its values format code
    Series srs = ch.GetNSeries().Get(0);
    srs.SetValuesFormatCode(U16String(u"$#,##0"));

    // Save the output Excel file
    wb.Save(outputFilePath);

    std::cout << "Chart series added and formatted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
