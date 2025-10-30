---
title: Hur man skapar dynamiskt rullande diagram med C++
linktitle: Hur man skapar dynamiskt rullande diagram
description: Lär dig att skapa ett dynamiskt rullande diagram med Aspose.Cells for C++. Vår guide visar hur du implementerar smidiga dataövergångar och glidande medelvärden i ditt diagram för kontinuerlig och uppdaterad visning.
keywords: Aspose.Cells for C++, Dynamiskt rullande diagram, Dataövergångar, Smidiga medelvärden, Kontinuerlig visning, Uppdaterad visualisering.
type: docs
weight: 74
url: /sv/cpp/create-dynamic-rolling-chart/
---

## **Möjliga användningsscenario**
Ett dynamiskt rullande diagram syftar till en grafisk representation som visar data punkter som konstant förskjuts och uppdateras över tiden. Det är en typ av diagram som kontinuerligt uppdaterar sig själv och visar ett rullande fönster av de senaste datapunkterna samtidigt som äldre datapunkter kastas bort när nya kommer in.

Dynamiska rullande diagram används vanligen för att visualisera trender och mönster i realtid eller strömningsdata. De är särskilt användbara i scenarier där tidsmässiga aspekter och förändringar över tid är avgörande, såsom analys av aktiemarknaden, väderövervakning eller spårning av liveprestanda.

Dessa diagram använder vanligtvis animation eller automatisk rullning för att säkerställa att den mest aktuella informationen alltid presenteras. Längden på det rullande fönstret kan anpassas för att visa en specifik tidsperiod, såsom den senaste timmen, dagen eller veckan.

Sammanfattningsvis är ett dynamiskt rullande diagram en kontinuerligt uppdaterad grafisk representation som visar de senaste datapunkterna samtidigt som äldre kastas bort, vilket gör att användarna kan observera trender och mönster i realtid.

## **Använd Aspose Cells för att skapa dynamiskt rullande diagram**
I de följande styckena kommer vi att visa dig hur du skapar ett dynamiskt rullande diagram med hjälp av Aspose.Cells. Vi kommer att visa koden för exemplet, liksom Excel-filen skapad med denna kod.

## **Exempelkod**
Följande provkod kommer att generera [Dynamic Rolling Chart File](DynamicRollingChart.xlsx).

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Your local test path
    U16String LocalPath = u"";

    // Create a new workbook and access the first worksheet.
    Workbook workbook;
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    // Populate the data for the chart. Add values to cells and set series names.
    sheet.GetCells().Get(u"A1").PutValue(u"Month");
    sheet.GetCells().Get(u"A2").PutValue(1);
    sheet.GetCells().Get(u"A3").PutValue(2);
    sheet.GetCells().Get(u"A4").PutValue(3);
    sheet.GetCells().Get(u"A5").PutValue(4);
    sheet.GetCells().Get(u"A6").PutValue(5);
    sheet.GetCells().Get(u"A7").PutValue(6);
    sheet.GetCells().Get(u"A8").PutValue(7);

    sheet.GetCells().Get(u"B1").PutValue(u"Sales");
    sheet.GetCells().Get(u"B2").PutValue(50);
    sheet.GetCells().Get(u"B3").PutValue(45);
    sheet.GetCells().Get(u"B4").PutValue(55);
    sheet.GetCells().Get(u"B5").PutValue(60);
    sheet.GetCells().Get(u"B6").PutValue(55);
    sheet.GetCells().Get(u"B7").PutValue(65);
    sheet.GetCells().Get(u"B8").PutValue(70);

    // Set the dynamic range for the chart's data source.
    int index = sheets.GetNames().Add(u"Sheet1!ChtData");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$B$1,COUNT(Sheet1!$B:$B),0,-5,1)");

    // Set the dynamic range for the chart's data labels.
    index = sheets.GetNames().Add(u"Sheet1!ChtLabels");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)");

    // Create a chart object and set its data source.
    int chartIndex = sheet.GetCharts().Add(ChartType::Line, 10, 3, 25, 10);
    Chart chart = sheet.GetCharts().Get(chartIndex);
    chart.GetNSeries().Add(u"Sales", true);
    chart.GetNSeries().Get(0).SetValues(u"Sheet1!ChtData");
    chart.GetNSeries().Get(0).SetXValues(u"Sheet1!ChtLabels");

    // Save the workbook as an Excel file.
    workbook.Save(LocalPath + u"DynamicRollingChart.xlsx");

    std::cout << "Dynamic rolling chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Anteckningar**
I den genererade filen kan du fortsätta att lägga till data i kolumnerna A och B, samtidigt som diagrammet dynamiskt räknar de senaste 5 datamängderna. Detta görs med hjälp av "OFFSET"-formeln i provkoden:

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

Du kan prova att ändra numret "-5" till "-10" i formeln, och det dynamiska diagrammet kommer att räkna de senaste 10 datamängderna. Nu har vi skapat ett dynamiskt rullande diagram med hjälp av Aspose.Cells framgångsrikt.
{{< app/cells/assistant language="cpp" >}}
