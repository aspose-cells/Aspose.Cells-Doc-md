---
title: Ändra Tick Label riktning med C++
linktitle: Ändra riktning för ticketiketter
description: Lär dig hur du ändrar riktningen på klicketiketter i Aspose.Cells for C++. Vår guide hjälper dig att förstå hur du justerar orienteringen av klicketiketter på axlar, inklusive horisontella, vertikala och snedställda orienteringar.
keywords: Aspose.Cells for C++, klicketiketter, riktning, orientering, axlar, horisontell, vertikal, snedställd.
type: docs
weight: 170
url: /sv/cpp/change-tick-label-direction/
---

## **Ändra riktning för ticketiketter**

Aspose.Cells ger dig möjlighet att ändra riktningen på diagrammets ticketiketter genom att använda egenskapen [**TickLabels.GetDirectionType()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/ticklabels/getdirectiontype/). Egenskapen [**TickLabels.GetDirectionType()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/ticklabels/getdirectiontype/) accepterar värdet för [**ChartTextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextdirectiontype) ENUMERATION. ENUMERATION [**ChartTextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextdirectiontype) innehåller följande medlemmar:

- Horisontell
- Vertikal
- Rotera 90
- Rotera 270
- Staplad

Följande bild jämför källfilen och utdatafilen:

### **Källfilens bild**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **Utdatasfilens bild**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

Följande kodsnutt ändrar ticketikettens riktning från Rotera 90 till Horisontell.

## **Exempelkod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Directory source and output paths
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook and load the sample Excel file
    Workbook workbook(sourceDir + u"SampleChangeTickLabelDirection.xlsx");

    // Obtain the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Load the chart from the source worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Set the category axis tick labels direction to Horizontal
    chart.GetCategoryAxis().GetTickLabels().SetDirectionType(ChartTextDirectionType::Horizontal);

    // Output the modified workbook to a new file
    workbook.Save(outDir + u"outputChangeChartDataLableDirection.xlsx");

    std::cout << "Chart tick label direction changed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Käll- och utdatafilerna kan laddas ned från följande länkar.

[Källfil](105480221.xlsx)

[Utdatasfil](105480223.xlsx)
