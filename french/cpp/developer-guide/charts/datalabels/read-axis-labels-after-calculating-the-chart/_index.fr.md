---
title: Lire les étiquettes d axe après le calcul du graphique avec C++
linktitle: Lire les étiquettes d axe après avoir calculé le graphique
description: Apprenez comment lire les étiquettes d axe dans Aspose.Cells for C++ après avoir calculé le graphique. Notre guide vous montrera comment accéder et récupérer les étiquettes d axe, y compris leur mise en forme et leur positionnement.
keywords: Aspose.Cells for C++, graphique, étiquettes d axe, calcul, lecture, accès, récupération, mise en forme, positionnement.
type: docs
weight: 90
url: /fr/cpp/read-axis-labels-after-calculating-the-chart/
---

## **Scénarios d'utilisation possibles**

Vous pouvez lire les étiquettes d'axe de votre graphique après avoir calculé ses valeurs en utilisant la méthode [**Chart.Calculate()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/calculate/). Veuillez utiliser la méthode [**Axis.GetAxisTexts()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/getaxistexts/) à cette fin qui renverra la liste des étiquettes d'axe.

## **Lire les étiquettes des axes après le calcul du graphique**

Veuillez consulter le code d'exemple suivant qui charge le fichier Excel d'exemple et lit les étiquettes d'axe de catégorie du graphique dans la première feuille de calcul. Il imprime ensuite les valeurs des étiquettes d'axe sur la console. Veuillez consulter la sortie de la console du code d'exemple ci-dessous pour une référence.

## **Code d'exemple**

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

## **Sortie console**

{{< highlight cpp >}}

 Category Axis Labels:

\---------------------

Iran

China

USA

Brazil

England

{{< /highlight >}}
