---
title: Visar cellområde som datapunkter i diagram med C++
linktitle: Visar cellområdet som datamärken
description: Lär dig att visa ett cellområde som datapunkter i diagram med Aspose.Cells for C++. Vår guide visar hur du länkar etiketterna till din datakälla och formaterar dem för att ge korrekt och meningsfull information.
keywords: Aspose.Cells for C++, diagram, datapunktetiketter, cellområde, datakälla, formatering, noggrannhet, meningsfull information.
type: docs
weight: 130
url: /sv/cpp/showing-cell-range-as-the-data-labels/
---

{{% alert color="primary" %}}

I Microsoft Excel 2013 kan du visa ett cellområde för datamärken. Aspose.Cells stödjer denna funktion.

{{% /alert %}}

## **Kryssrutan för att visa cellområde som datamärken**

Att visa cellområdet som datamärken i Microsoft Excel:

1. Välj seriens datamärken och högerklicka för att öppna snabbmenyn.
1. Välj **Formatera datamärken**. Etikettalternativ visas.
1. Välj eller avmarkera alternativet **Etiketten innehåller - Värde från celler**.

Exempelkoden nedan använder ett diagramseriedatamärken och ställer in [**DataLabels.GetShowCellRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/getshowcellrange/)-egenskapen till **true** för att välja alternativet **Etikett innehåller - Värde från celler**.

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
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook from the source Excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Check the "Label Contains - Value From Cells"
    DataLabels dataLabels = chart.GetNSeries().Get(0).GetDataLabels();
    dataLabels.SetShowCellRange(true);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
