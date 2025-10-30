---
title: Trova il tipo di valori X e Y dei punti nella serie del grafico con C++
linktitle: Trova il tipo di valori X e Y dei punti nella serie del grafico
description: Scopri come determinare il tipo di valori X e Y nei punti della serie del grafico usando Aspose.Cells for C++. La nostra guida spiegherà i vari tipi di valori dei dati e mostrerà come accedervi e lavorarci all interno dei tuoi grafici.
keywords: Aspose.Cells for C++, grafici, valori X, valori Y, tipi di dati, accesso, lavoro con, serie del grafico.
type: docs
weight: 150
url: /it/cpp/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Possibili Scenari di Utilizzo**
A volte, vuoi conoscere il tipo di valori X e Y dei punti del grafico in una serie. Aspose.Cells fornisce i metodi `ChartPoint::get_XValueType` e `ChartPoint::get_YValueType` che possono essere usati a questo scopo. Nota che dovrai chiamare il metodo `Chart::Calculate()` prima di poter utilizzare efficacemente queste proprietà.

## **Trova il tipo di valori X e Y dei punti nella serie del grafico**
Il seguente esempio di codice carica il file Excel di esempio ([sample Excel file](64716905.xlsx)) e accede al primo grafico all’interno del primo foglio di lavoro. Successivamente chiama il metodo `Chart::Calculate()` e determina il tipo di valori X e Y del primo punto del grafico, stampandoli sulla console. Consulta l’output della console riportato di seguito come riferimento.

## **Codice di Esempio**
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

    // Load sample Excel file containing chart
    Workbook wb(srcDir + u"sampleFindTypeOfXandYValuesOfPointsInChartSeries.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first chart
    Chart ch = ws.GetCharts().Get(0);

    // Calculate chart data
    ch.Calculate();

    // Access first chart point in the first series
    ChartPoint pnt = ch.GetNSeries().Get(0).GetPoints().Get(0);

    // Print the types of X and Y values of chart point
    std::cout << "X Value Type: " << static_cast<int>(pnt.GetXValueType()) << std::endl;
    std::cout << "Y Value Type: " << static_cast<int>(pnt.GetYValueType()) << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Output della console**

{{< highlight java >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
