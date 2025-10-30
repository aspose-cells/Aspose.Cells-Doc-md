---
title: Hur man skapar en Sunburst diagram med C++
description: Lär dig hur man skapar ett sunburst diagram i Aspose.Cells for C++, ett diagram som visar data i en cirkel. Vår guide hjälper dig att ställa in olika egenskaper och formatering av ditt diagram, inklusive datamärkning, legend, färger och mer.
keywords: Aspose.Cells for C++, sunburst diagram, skapa, ställ in egenskaper, datamärkning, legend, format, färg, cirkel, data rendering.
type: docs
weight: 162
url: /sv/cpp/creating-sunburst-chart/
---

## **Möjliga användningsscenario**
Treemaps-diagram är bra för att jämföra proportioner inom hierarkin, men treemaps är inte optimala för att visa hierarkiska nivåer mellan de största kategorierna och varje datapunkt. En sunburst-diagram är mycket bättre för att visa detta. Sunburst-diagram är idealiskt för att visa hierarkiska data. Varje nivå i hierarkin representeras av en ring eller cirkel, där den innersta ringen är toppen av hierarkin. Ett sunburst-diagram utan hierarkiska data (en nivå av kategorier) ser ut som en donut. Men ett sunburst-diagram med flera nivåer av kategorier visar hur de yttre ringarna är relaterade till de inre ringarna. Sunburst-diagram är mest effektiva för att visa hur en ring är uppdelad i dess bidragande delar, medan en annan typ av hierarkiskt diagram, treemaps-diagram, är ideal för att jämföra relativa storlekar.

![todo:image_alt_text](sample.png)
## **Solfjäderdiagram**
Efter att ha kört koden nedan kommer du att se solfjäderdiagrammet som visas nedan.

![todo:image_alt_text](result.png)
## **Exempelkod**
Följande exempelkod läser in [provkalkylbladet](sunburst.xlsx) och genererar [utmatningskalkylbladet](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"sunburst.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a Treemap chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::Sunburst, 5, 6, 25, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"Sunburst Chart");

    // Add series data range
    chart.GetNSeries().Add(u"D2:D16", true);

    // Set category data (A2:A16 is incorrect, as hierarchical category)
    chart.GetNSeries().SetCategoryData(u"A2:C16");

    // Show the DataLabels with category names
    chart.GetNSeries().Get(0).GetDataLabels().SetShowCategoryName(true);

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
