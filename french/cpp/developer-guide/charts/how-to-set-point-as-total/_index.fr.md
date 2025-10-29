---
title: Comment définir un point comme total avec C++
linktitle: Comment définir un point comme total
description: Dans certains graphiques Excel, par exemple, le graphique WaterFall, vous pouvez avoir besoin de définir un point comme total. Cet article décrit comment utiliser Aspose.Cells avec C++ pour le faire.
keywords: Graphique WaterFall, Point, Définir comme total.
type: docs
weight: 72
url: /fr/cpp/how-to-set-point-as-total/
---

## Qu'est-ce que "Définir le point comme total" dans un graphique Excel

Dans certains graphiques Excel, par exemple, le graphique WaterFall, certaines données de points sont la somme des points précédents, vous pouvez avoir besoin de "définir le point comme total". Nous montrerons le code d'exemple et l'illustration ci-dessous.

## Un graphique WaterFall doit "définir le point comme total" 

![todo:image_alt_text](set-as-total1.png)

Cette image montre un graphique WaterFall dans Excel. Nous pouvons voir qu'il y a quatre points de données commençant par "Total", et ils sont utilisés pour compter toutes les données précédentes.
Dans cette image, les réglages ne sont pas tout à fait corrects, lorsque nous sélectionnons un point "Total 2024" et que nous pouvons voir que l'option "Définir comme total" n'est pas cochée dans Excel.
Ci-dessous est joint le [fichier Excel exemple](SampleSheet.xlsx) qui doit être modifié, et nous utiliserons Aspose.Cells pour le configurer correctement.

## Utiliser Aspose.Cells pour "Définir le point comme total" 

Nous utilisons le code suivant pour configurer le fichier correctement :

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Initialize file path
    U16String filePath(u"");

    // Load the workbook
    Workbook wb(filePath + u"SampleSheet.xlsx");

    // Get the first worksheet
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Get the chart by name
    Chart chart = worksheet.GetCharts().Get(u"Graphiq5");

    // Set some points as total column
    // In this example, we set points 0, 4, 8, 12 as total
    Vector<int32_t> subtotals = {0, 4, 8, 12};
    chart.GetNSeries().Get(0).GetLayoutProperties().SetSubtotals(subtotals);

    // Save the workbook
    wb.Save(filePath + u"output.xlsx");

    std::cout << "Chart subtotals set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Vous pouvez obtenir le [fichier de sortie correct](output.xlsx) suivant

Comme le montre la figure ci-dessous, les quatre points de données "Total" sont correctement configurés, et vous pouvez voir la différence avec le graphique précédent.

![todo:image_alt_text](set-as-total2.png)
{{< app/cells/assistant language="cpp" >}}
