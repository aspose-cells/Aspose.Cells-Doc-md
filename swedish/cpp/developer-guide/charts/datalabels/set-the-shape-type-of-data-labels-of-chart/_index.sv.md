---
title: Ställ in typer av datapunktetiketter för diagrammet med C++
linktitle: Ställ in datamärkenas formtyp i diagrammet
description: Lär dig hur du ställer in datapunktetikettens formtyp i diagram med Aspose.Cells for C++. Vår guide förklarar de olika tillgängliga formtyperna och visar hur du väljer rätt form för att förbättra presentationen och användbarheten av dina diagram.
keywords: Aspose.Cells for C++, diagram, datapunktetiketter, formtyper, presentation, användbarhet.
type: docs
weight: 110
url: /sv/cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **Möjliga användningsscenario**
Du kan ändra formtypen för datapunktetiketter i diagrammet med egenskapen `DataLabels.ShapeType`. Den tar värdet från `DataLabelShapeType`-enumerationen och ändrar formtypen för datapunkter därefter. Några av dess värden är:

{{< highlight java >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}

## **Ställ in datamärkenas formtyp i diagram**
Följande exempel ändrar formtypen för datalabels i diagrammet till `DataLabelShapeType.WedgeEllipseCallout`. Se gärna [exempel-Excel-filen](60489778.xlsx) som används i denna kod och den [utdata-Excel file](60489779.xlsx) som genereras av den. Skärmbilden visar hur koden påverkar exempel-Excel-filen. 

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)

## **Exempelkod**
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
