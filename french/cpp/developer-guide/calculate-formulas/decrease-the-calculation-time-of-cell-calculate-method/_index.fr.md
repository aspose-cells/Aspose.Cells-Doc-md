---
title: Diminuer le temps de calcul de la méthode Cell.Calculate avec C++
linktitle: Diminuer le temps de calcul de Cell.Calculate
description: Cet article présente comment utiliser la bibliothèque Aspose.Cells pour réduire le temps de calcul de la méthode de calcul des cellules dans Microsoft Excel. En chargeant un fichier Excel existant ou en en créant un nouveau, nous pouvons utiliser les méthodes fournies par Aspose.Cells pour optimiser la méthode de calcul des cellules et améliorer ses performances. Finalement, nous enregistrons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, méthodes de calcul des cellules, optimisation, performances, réduction du temps de calcul
type: docs
weight: 100
url: /fr/cpp/decrease-the-calculation-time-of-cell-calculate-method/
---

## **Scénarios d'utilisation possibles**

Normalement, nous recommandons aux utilisateurs d'appeler la méthode [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) une fois, puis d'obtenir les valeurs calculées des cellules individuelles. Mais parfois, les utilisateurs ne veulent pas calculer tout le classeur. Ils souhaitent simplement calculer une seule cellule. Aspose.Cells fournit la propriété [**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getrecursive/) que vous pouvez définir sur **false** et cela réduira considérablement le temps de calcul des cellules individuelles. Parce que lorsque la propriété récursive est réglée sur **true**, tous les dépendants des cellules sont recalculés à chaque appel. Mais lorsque la propriété récursive est **false**, seules les cellules dépendantes sont calculées une fois et ne sont pas recalculées lors des appels suivants.

## **Diminuer le temps de calcul de la méthode Cell.Calculate()**

Le code d'exemple suivant illustre l'utilisation de la propriété [**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getrecursive/). Exécutez ce code avec le [fichier Excel d'exemple](5113710.xlsx) fourni et vérifiez sa sortie console. Vous verrez que le fait de définir la propriété récursive sur **false** a considérablement réduit le temps de calcul. Veuillez également lire les commentaires pour une meilleure compréhension de cette propriété.

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

## **Sortie console**

Ceci est la sortie console du code d'exemple ci-dessus lorsqu'il est exécuté avec le [fichier excel d'exemple](5113710.xlsx) sur notre machine. Veuillez noter que votre sortie peut différer, mais le temps écoulé après avoir défini la propriété récursive sur **false** sera toujours inférieur à celui lorsque cette propriété est sur **true**.

{{< highlight java >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
