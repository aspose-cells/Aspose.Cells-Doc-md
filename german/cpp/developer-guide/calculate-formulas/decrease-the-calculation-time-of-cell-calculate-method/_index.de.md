---
title: Verringerung der Berechnungszeit der Cell.Calculate Methode mit C++
linktitle: Verringerung der Berechnungszeit der Cell.Calculate
description: In diesem Artikel wird erläutert, wie die Aspose.Cells Bibliothek verwendet werden kann, um die Berechnungszeit der Zellberechnungsmethoden in Microsoft Excel zu reduzieren. Durch Laden einer vorhandenen Excel Datei oder Erstellen einer neuen können wir die von Aspose.Cells bereitgestellten Methoden nutzen, um die Zellberechnungsmethode zu optimieren und die Leistung zu verbessern. Schließlich speichern wir die modifizierte Excel Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, Methoden zur Zellberechnung, Optimierung, Leistung, Verkürzung der Berechnungszeit
type: docs
weight: 100
url: /de/cpp/decrease-the-calculation-time-of-cell-calculate-method/
---

## **Mögliche Verwendungsszenarien**

 Normalerweise empfehlen wir den Benutzern, die Methode [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) einmal aufzurufen und dann die berechneten Werte der einzelnen Zellen zu erhalten. Manchmal möchten die Benutzer jedoch nicht die gesamte Arbeitsmappe berechnen. Sie möchten nur eine einzelne Zelle berechnen. Aspose.Cells bietet die Eigenschaft [**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getrecursive/), die Sie auf **false** setzen können, was die Berechnungszeit der einzelnen Zellen erheblich verringert. Wenn die rekursive Eigenschaft auf **true** gesetzt ist, werden alle Abhängigkeiten der Zellen bei jedem Aufruf neu berechnet. Wenn die rekursive Eigenschaft jedoch **false** ist, werden abhängige Zellen nur einmal berechnet und nicht erneut bei nachfolgenden Aufrufen.

## **Verringerung der Berechnungszeit der Cell.Calculate() Methode**

 Der folgende Beispielcode zeigt die Verwendung der Eigenschaft [**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getrecursive/). Führen Sie diesen Code mit der bereitgestellten [Beispiel-Excel-Datei](5113710.xlsx) aus und prüfen Sie die Konsolenausgabe. Sie werden feststellen, dass das Setzen der rekursiven Eigenschaft auf **false** die Berechnungszeit erheblich verkürzt hat. Lesen Sie auch die Kommentare für ein besseres Verständnis dieser Eigenschaft.

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

## **Konsolenausgabe**

 Dies ist die Konsolenausgabe des oben genannten Beispielcodes, wenn er mit der bereitgestellten [Beispiel-Excel-Datei](5113710.xlsx) auf unserer Maschine ausgeführt wird. Beachten Sie, dass Ihre Ausgabe unterschiedlich sein kann, aber die nach der Einstellung der rekursiven Eigenschaft auf **false** verstrichene Zeit immer kürzer ist als bei **true**.

{{< highlight java >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
