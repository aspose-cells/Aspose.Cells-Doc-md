---
title: Läs diagramundertext från ODS fil med C++
linktitle: Läs diagramrubriken från en ODS fil
description: Lär dig hur du använder Aspose.Cells for C++ för att läsa diagramets undertext från en OpenDocument Spreadsheet (ODS) fil. Vår guide visar hur man extraherar och får tillgång till diagramets undertext för vidare analys eller visning.
keywords: Aspose.Cells for C++, Läs diagramundertext, OpenDocument Spreadsheet, ODS fil, Diagramutvinning, Dataanalys.
type: docs
weight: 160
url: /sv/cpp/read-chart-subtitle-from-ods-file/
---

## **Läs diagramunderrubrik från ODS-fil**

Aspose.Cells ger dig möjlighet att läsa diagramrubriker i ODS-filer genom att använda egenskapen [**Chart.SubTitle**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getsubtitle/). Följande exempelkod laddar den [exempelfilen i ODS-format](89620481.ods) och läser diagramrubriken med [**Chart.SubTitle**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getsubtitle/)-egenskapen och skriver ut den i konsolfönstret. Se den givna konsoloutputen nedan för referens.

## **Exempelkod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load excel file containing charts
    Workbook workbook(srcDir + u"SampleChart.ods");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Print chart subtitle
    cout << "Chart Subtitle: " << chart.GetSubTitle().GetText().ToUtf8() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Konsoloutput**

{{< highlight java >}}

Chart Subtitle: Sample Chart Subtitle

{{< /highlight >}}
