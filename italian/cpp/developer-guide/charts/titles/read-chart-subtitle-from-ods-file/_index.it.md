---
title: Leggi il sottotitolo del grafico dal file ODS con C++
linktitle: Leggi il sottotitolo del grafico dal file ODS
description: Impara come usare Aspose.Cells for C++ per leggere il sottotitolo del grafico da un file OpenDocument Spreadsheet (ODS). La nostra guida dimostrerà come estrarre e accedere al sottotitolo di un grafico per ulteriori analisi o visualizzazione.
keywords: Aspose.Cells for C++, Leggi sottotitolo del grafico, OpenDocument Spreadsheet, file ODS, estrazione grafico, analisi dati.
type: docs
weight: 160
url: /it/cpp/read-chart-subtitle-from-ods-file/
---

## **Leggi il sottotitolo del grafico dal file ODS**

Aspose.Cells ti offre la possibilità di leggere i sottotitoli del grafico nei file ODS utilizzando la proprietà [**Chart.SubTitle**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getsubtitle/). Il seguente codice di esempio carica il [file ODS di esempio](89620481.ods) e legge il sottotitolo del grafico utilizzando la proprietà [**Chart.SubTitle**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getsubtitle/) e lo stampa nella finestra della console. Si prega di vedere l'output della console del codice qui sotto per maggiori dettagli.

## **Codice di Esempio**

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

## **Output della console**

{{< highlight java >}}

Chart Subtitle: Sample Chart Subtitle

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
