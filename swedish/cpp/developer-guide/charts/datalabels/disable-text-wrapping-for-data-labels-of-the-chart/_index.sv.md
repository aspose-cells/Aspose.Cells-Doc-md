---
title: Inaktivera Textomslag för datapunkter i Diagrammet med C++
linktitle: Inaktivera Textomslag för datamärkningar
description: Lär dig hur du inaktiverar textomslag för datamärkningar i diagram med Aspose.Cells for C++. Vår guide visar hur du förhindrar att långa etiketter överlappar och ger tydligare och mer läsbara diagram.
keywords: Aspose.Cells for C++, diagram, datamärken, textomslag, överlappning, läsbarhet, visningar.
type: docs
weight: 70
url: /sv/cpp/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

Microsoft Excel 2013 tillåter användare att vicka eller avvicka text inne i dataetiketterna för diagrammet. Som standard är texten inne i dataetiketterna för diagrammet i det vikta läget.

Aspose.Cells tillhandahåller en [**DataLabels.IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/istextwrapped/)-egenskap som du kan ställa in på True eller False för att aktivera eller inaktivera textvaggning för dataetiketterna respektive.

{{% /alert %}}

Nedanstående kodexempel visar hur du inaktiverar textvaggning för dataetiketterna i diagrammet.

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
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"Output_out.xlsx";

    // Load the sample Excel file inside the workbook object
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Disable the Text Wrapping of Data Labels in all Series
    chart.GetNSeries().Get(0).GetDataLabels().SetIsTextWrapped(false);
    chart.GetNSeries().Get(1).GetDataLabels().SetIsTextWrapped(false);
    chart.GetNSeries().Get(2).GetDataLabels().SetIsTextWrapped(false);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Text wrapping disabled successfully in data labels!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
