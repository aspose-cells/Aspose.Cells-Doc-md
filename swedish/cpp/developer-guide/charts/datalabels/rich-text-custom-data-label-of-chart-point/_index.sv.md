---
title: Rik Text Anpassad datapunktetikett i diagram med C++
description: Lär dig hur du lägger till rik text anpassade datapunktetiketter till diagrampunkter i Aspose.Cells for C++. Vår guide visar hur du formaterar etiketter med olika teckensnitt, färger och justeringsalternativ för att förbättra utseendet och läsbarheten på dina diagram.
keywords: Aspose.Cells for C++, diagram, rik text, anpassade datapunktetiketter, teckensnitt, färger, justering, utseende, läsbarhet.
type: docs
weight: 10
url: /sv/cpp/rich-text-custom-data-label-of-chart-point/
---

{{% alert color="primary" %}}

Du kan använda Aspose.Cells för att skapa rik text anpassade datapunktetiketter för diagram. Aspose.Cells erbjuder metoden [DataLabels.Characters()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/characters/) för att returnera objektet [FontSetting](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/), vilket kan användas för att ställa in teckensnittsegenskaper för texten, såsom färg, fetstil etc.

{{% /alert %}}

## Anpassat riktmärke för diagram punkt

Följande kod kommer åt den första diagrampunkten i den första serien, ställer in dess text och sedan formaterar teckensnittet för de första 10 tecknen genom att ställa in dess färg till röd och fetstil till **true**.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a workbook from source Excel file
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the sheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Access the data label of first series first point
    DataLabels dlbls = chart.GetNSeries().Get(0).GetPoints().Get(0).GetDataLabels();

    // Set data label text
    dlbls.SetText(u"Rich Text Label");

    // Set the font setting of the first 10 characters
    FontSetting fntSetting = dlbls.Characters(0, 10);
    fntSetting.GetFont().SetColor(Color::Red());
    fntSetting.GetFont().SetIsBold(true);

    // Save the workbook
    workbook.Save(srcDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```
