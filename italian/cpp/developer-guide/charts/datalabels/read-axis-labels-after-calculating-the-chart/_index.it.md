---
title: Leggi le etichette dell asse dopo aver calcolato il grafico con C++
linktitle: Leggere le etichette dell asse dopo il calcolo del grafico
description: Scopri come leggere le etichette dell’asse in Aspose.Cells for C++ dopo aver calcolato il grafico. La nostra guida ti mostrerà come accedere e recuperare le etichette dell’asse, inclusa la loro formattazione e posizionamento.
keywords: Aspose.Cells for C++, grafico, etichette dell asse, calcolo, lettura, accesso, recupero, formattazione, posizionamento.
type: docs
weight: 90
url: /it/cpp/read-axis-labels-after-calculating-the-chart/
---

## **Possibili Scenari di Utilizzo**

È possibile leggere le etichette degli assi del grafico dopo aver calcolato i valori utilizzando il metodo [**Chart.Calculate()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/calculate/). Si prega di utilizzare il metodo [**Axis.GetAxisTexts()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/getaxistexts/) a tale scopo che restituirà l'elenco delle etichette degli assi.

## **Leggere le etichette dell'asse dopo il calcolo del grafico**

Si prega di vedere il seguente codice di esempio che carica il file Excel di esempio e legge le etichette dell'asse delle categorie del grafico nel primo foglio di lavoro. Stampa quindi i valori delle etichette degli assi sulla console. Si prega di vedere l'output della console del codice di esempio riportato di seguito per un riferimento.

## **Codice di Esempio**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook wb(srcDir + u"ReadAxisLabels.xlsx");

    Worksheet ws = wb.GetWorksheets().Get(0);

    Chart ch = ws.GetCharts().Get(0);

    ch.Calculate();

    Vector<U16String> lstLabels = ch.GetCategoryAxis().GetAxisTexts();

    std::wcout << L"Category Axis Labels: " << std::endl;
    std::wcout << L"---------------------" << std::endl;

    for (int32_t i = 0; i < lstLabels.GetLength(); ++i)
    {
        std::wcout << reinterpret_cast<const wchar_t*>(lstLabels[i].GetData()) << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Output della console**

{{< highlight cpp >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
