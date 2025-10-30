---
title: Arbeitsblatt des Diagramms mit C++ abrufen
linktitle: Arbeitsblatt des Diagramms abrufen
description: Erfahren Sie, wie Sie mit Aspose.Cells for C++ das zu einem Excel Diagramm gehörende Arbeitsblatt abrufen. Unser Leitfaden zeigt, wie Sie auf das Arbeitsblatt zugreifen und Operationen auf ihm ausführen, um die zugrunde liegenden Daten des Diagramms zu manipulieren.
keywords: Aspose.Cells for C++, Excel Diagramme, Arbeitsblätter, Datenmanipulation, zugrunde liegende Daten, Operationen.
type: docs
weight: 1000
url: /de/cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Manchmal möchten Sie auf ein Arbeitsblatt über eine Referenz eines Diagramms zugreifen. Aspose.Cells bietet die [**Chart::GetWorksheet**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getworksheet/) Methode, die die Referenz des Arbeitsblatts zurückgibt, das das Diagramm enthält.

{{% /alert %}}

Das folgende Beispiel zeigt, wie die [**Chart::GetWorksheet**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getworksheet/) Methode verwendet wird. Der Code gibt zuerst den Namen des Arbeitsblatts aus, greift dann auf das erste Diagramm auf dem Arbeitsblatt zu und gibt anschließend den Namen des Arbeitsblatts erneut aus, wobei die [**Chart::GetWorksheet**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getworksheet/) Methode verwendet wird.

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

    // Create workbook from sample Excel file
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access first worksheet of the workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Print worksheet name
    cout << "Sheet Name: " << worksheet.GetName().ToUtf8() << endl;

    // Access the first chart inside this worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Access the chart's sheet and display its name again
    cout << "Chart's Sheet Name: " << chart.GetWorksheet().GetName().ToUtf8() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

Unten ist die Konsolenausgabe, die das Beispiel des Codes ergibt. Wie Sie sehen können, druckt es den Arbeitsblattnamen beide Male gleich aus.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
