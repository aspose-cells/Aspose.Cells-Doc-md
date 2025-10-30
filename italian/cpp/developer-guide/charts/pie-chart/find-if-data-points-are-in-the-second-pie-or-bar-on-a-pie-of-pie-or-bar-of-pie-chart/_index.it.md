---
title: Determina se i punti dati sono nella seconda fetta o barra di un grafico a torta di fetta o barra di fetta con C++
linktitle: Trova se i punti dati sono nel secondo grafico a torta o a barre su un grafico a torta di torta o a barre. Trova come usare Aspose.Cells for .NET per trovare se i punti dati sono nel secondo grafico a torta o barre su un grafico a torta di torta o a barre. La nostra guida dimostrerà come identificare e accedere al secondo grafico a torta o a barre su un grafico composito, consentendoti di analizzare e manipolare i dati in modo efficace.
description: Impara come usare Aspose.Cells for C++ per scoprire se i punti dati sono nella seconda fetta o barra di un grafico a torta di fetta o di barra. La nostra guida dimostrerà come identificare e accedere alla fetta o barra secondaria in un grafico composito, consentendoti di analizzare e manipolare efficacemente i dati.
keywords: Aspose.Cells for C++, Grafico Torta di Fetta, Barra di Fetta, Fetta Secondaria, Barra Secondaria, Analisi dei Dati, Manipolazione dei Dati.
type: docs
weight: 180
url: /it/cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **Possibili Scenari di Utilizzo**
Puoi trovare se i punti dati di una serie sono nella seconda fetta di un *Grafico Torta di Fetta* o nella barra di un *Grafico Barra di Fetta* usando Aspose.Cells. Utilizza la proprietà [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/isinsecondaryplot/) per determinarlo.

Si prega di scaricare il [file excel di esempio](5115193.xlsx) utilizzato nel seguente codice di esempio e vedere il suo output sulla console. Se si apre il [file excel di esempio](5115193.xlsx), si noterà che tutti i punti dati inferiori a 10 sono all'interno del grafico a barre di *Grafico a Barre di Torta* come mostrato anche dall'output sulla console.

## **Verifica se i punti dati sono nel secondo grafico a torta o a barre su un grafico di torta o barre di un grafico a torta**
Il seguente codice di esempio mostra come trovare se i punti dati sono nel secondo grafico a torta o a barre su un grafico *Torta di torte* o *Barra di torte*.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = srcDir + u"PieBars.xlsx";
    Workbook workbook(inputFilePath);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Chart chart = worksheet.GetCharts().Get(0);
    chart.Calculate();

    Series series = chart.GetNSeries().Get(0);

    int pointCount = series.GetPoints().GetCount();
    for (int i = 0; i < pointCount; ++i)
    {
        ChartPoint chartPoint = series.GetPoints().Get(i);

        if (chartPoint.Get_YValue().IsNull())
            continue;

        std::cout << "Value: " << chartPoint.Get_YValue().ToDouble() << std::endl;
        std::cout << "IsInSecondaryPlot: " << (chartPoint.IsInSecondaryPlot() ? "true" : "false") << std::endl;
        std::cout << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Output della console**
Guarda la seguente output sulla console generata dopo l'esecuzione del codice di esempio con il [file Excel di esempio](5115193.xlsx). Se [IsInSecondaryPlot](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/isinsecondaryplot/) è **falso**, il punto dati è all'interno della torta, se è **vero**, allora il punto dati è all'interno della barra.

{{< highlight java >}}

 Value: 15

IsInSecondaryPlot: False

Value: 9

IsInSecondaryPlot: True

Value: 2

IsInSecondaryPlot: True

Value: 40

IsInSecondaryPlot: False

Value: 5

IsInSecondaryPlot: True

Value: 4

IsInSecondaryPlot: True

Value: 25

IsInSecondaryPlot: False

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
