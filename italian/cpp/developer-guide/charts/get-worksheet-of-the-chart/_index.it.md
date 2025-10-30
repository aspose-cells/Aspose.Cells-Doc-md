---
title: Ottieni il foglio di lavoro del grafico con C++
linktitle: Ottieni il foglio di lavoro del grafico
description: Impara come recuperare il foglio di lavoro associato a un grafico Excel usando Aspose.Cells for C++. La nostra guida ti mostrerà come accedere al foglio di lavoro e eseguire operazioni su di esso per manipolare i dati sottostanti del grafico.
keywords: Aspose.Cells for C++, grafici Excel, fogli di lavoro, manipolazione dati, dati sottostanti, operazioni.
type: docs
weight: 1000
url: /it/cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

A volte, vuoi accedere a un foglio di lavoro tramite il riferimento di un grafico. Aspose.Cells fornisce il metodo [**Chart::GetWorksheet**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getworksheet/) che restituisce il riferimento del foglio di lavoro che contiene il grafico.

{{% /alert %}}

Il seguente esempio mostra come usare il metodo [**Chart::GetWorksheet**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getworksheet/). Il codice prima stampa il nome del foglio di lavoro, poi accede al primo grafico sul foglio. Successivamente, stampa di nuovo il nome del foglio, usando il metodo [**Chart::GetWorksheet**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getworksheet/).

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

Di seguito viene riportato l'output della console che il codice di esempio produce. Come puoi vedere, stampa lo stesso nome del foglio di lavoro entrambe le volte.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
