---
title: Diagrammunterschrift aus ODS Datei mit C++ lesen
linktitle: Lese Diagramm Untertitel aus ODS Datei
description: Lernen Sie, wie man Aspose.Cells for C++ verwendet, um die Diagrammunterschrift aus einer OpenDocument Spreadsheet (ODS) Datei zu lesen. Unser Leitfaden zeigt, wie man die Unterüberschrift eines Diagramms extrahiert und zugänglich macht.
keywords: Aspose.Cells for C++, Diagrammtitel lesen, OpenDocument Spreadsheet, ODS Datei, Diagrammauszug, Datenanalyse.
type: docs
weight: 160
url: /de/cpp/read-chart-subtitle-from-ods-file/
---

## **Diagramm-Untertitel aus ODS-Datei lesen**

Aspose.Cells bietet Ihnen die Möglichkeit, Diagramm-Untertitel in ODS-Dateien mit der Eigenschaft [**Chart.SubTitle**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getsubtitle/) zu lesen. Im folgenden Beispielcode wird die [Beispiel ODS-Datei](89620481.ods) geladen, der Diagramm-Untertitel mit der Eigenschaft [**Chart.SubTitle**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getsubtitle/) gelesen und im Konsolenfenster ausgegeben. Bitte beachten Sie die Konsolenausgabe des untenstehenden Codes als Referenz.

## **Beispielcode**

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

## **Konsolenausgabe**

{{< highlight java >}}

Chart Subtitle: Sample Chart Subtitle

{{< /highlight >}}
