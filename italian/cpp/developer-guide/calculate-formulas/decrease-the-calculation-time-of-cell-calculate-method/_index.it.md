---
title: Riduci il tempo di calcolo del metodo Cell.Calculate con C++
linktitle: Riduci il tempo di calcolo di Cell.Calculate
description: Questo articolo introduce come utilizzare la libreria Aspose.Cells per ridurre il tempo di calcolo dei metodi di calcolo delle celle in Microsoft Excel. Caricando un file Excel esistente o creandone uno nuovo, possiamo utilizzare i metodi forniti da Aspose.Cells per ottimizzare il metodo di calcolo delle celle e migliorare le prestazioni. Infine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, metodi di calcolo delle celle, ottimizzazione, prestazioni, riduzione del tempo di calcolo
type: docs
weight: 100
url: /it/cpp/decrease-the-calculation-time-of-cell-calculate-method/
---

## **Possibili Scenari di Utilizzo**

Normalmente, si raccomanda agli utenti di chiamare il metodo [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) una volta e poi ottenere i valori calcolati delle singole celle. Ma alcune volte, gli utenti non vogliono calcolare l'intero workbook. Vogliono semplicemente calcolare una singola cella. Aspose.Cells fornisce la proprietà [**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getrecursive/) che puoi impostare su **false** e questo ridurrà significativamente il tempo di calcolo delle singole celle. Perché quando la proprietà ricorsiva è impostata su **true**, allora tutti i dipendenti delle celle vengono ricalcolati ad ogni chiamata. Ma quando la proprietà ricorsiva è **false**, le celle dipendenti vengono calcolate una sola volta e non vengono ricalcolate nelle chiamate successive.

## **Ridurre il tempo di calcolo del metodo Cell.Calculate()**

Il seguente esempio di codice illustra l'uso della proprietà [**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getrecursive/). Esegui questo codice con il [file Excel di esempio](5113710.xlsx) fornito e verifica l'output sulla console. Troverai che impostare la proprietà ricorsiva su **false** ha ridotto significativamente il tempo di calcolo. Leggi anche i commenti per una migliore comprensione di questa proprietà.

```c++
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

void TestCalcTimeRecursive(bool isRecursive) {
    Workbook* workbook = new Workbook();
    CalculationOptions options;
    options.SetRecursive(isRecursive);

    auto start = std::chrono::high_resolution_clock::now();
    workbook->CalculateFormula(&options);
    auto end = std::chrono::high_resolution_clock::now();

    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();
    std::cout << "Time (recursive=" << isRecursive << "): " << duration << " ms" << std::endl;

    delete workbook;
}

int main() {
    Aspose::Cells::Startup();

    TestCalcTimeRecursive(true);
    TestCalcTimeRecursive(false);

    Aspose::Cells::Cleanup();
    return 0;
}
```

```cpp
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std::chrono;

void TestCalcTimeRecursive(bool rec) {
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook wb(srcDir + u"sample.xlsx");
    Worksheet ws = wb.GetWorksheets().Get(0);
    CalculationOptions opts;
    opts.SetRecursive(rec);

    auto start = high_resolution_clock::now();
    for (int i = 0; i < 1000000; i++) {
        ws.GetCells().Get(u"A1").Calculate(opts);
    }
    auto stop = high_resolution_clock::now();

    auto duration = duration_cast<milliseconds>(stop - start);
    long estimatedTime = duration.count() / 1000;
    std::cout << "Recursive " << rec << ": " << estimatedTime << " seconds" << std::endl;
}

int main() {
    Aspose::Cells::Startup();
    TestCalcTimeRecursive(true);
    TestCalcTimeRecursive(false);
    Aspose::Cells::Cleanup();
    return 0;

}
```

## **Output della console**

Questo è l'output sulla console del codice di esempio sopra quando eseguito con il [file Excel di esempio](5113710.xlsx) sul nostro sistema. Nota che l'output può differire, ma il tempo trascorso dopo aver impostato la proprietà ricorsiva su **false** sarà sempre inferiore rispetto ad averla impostata su **true**.

{{< highlight java >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
