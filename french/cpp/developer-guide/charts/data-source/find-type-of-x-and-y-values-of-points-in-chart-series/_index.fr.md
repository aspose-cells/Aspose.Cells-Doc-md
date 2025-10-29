---
title: Trouver le type des valeurs X et Y des points dans la série de graphiques avec C++
linktitle: Trouver le type de valeurs X et Y des points dans la série de graphique
description: Apprenez comment déterminer le type de valeurs X et Y dans les points de la série de graphiques en utilisant Aspose.Cells for C++. Notre guide expliquera les différents types de valeurs de données et vous montrera comment y accéder et les manipuler dans vos graphiques.
keywords: Aspose.Cells for C++, diagramme, valeurs X, valeurs Y, types de données, accès, manipulation, série de graphiques.
type: docs
weight: 150
url: /fr/cpp/find-type-of-x-and-y-values-of-points-in-chart-series/
---

## **Scénarios d'utilisation possibles**
Parfois, vous souhaitez connaître le type des valeurs X et Y des points dans une série de graphiques. Aspose.Cells fournit les méthodes `ChartPoint::get_XValueType` et `ChartPoint::get_YValueType` qui peuvent être utilisées à cette fin. Veuillez noter que vous devrez appeler la méthode `Chart::Calculate()` avant de pouvoir utiliser efficacement ces propriétés.

## **Trouver le type de valeurs X et Y des points dans la série de graphiques**
Le code d'exemple suivant charge le [fichier Excel d'exemple](64716905.xlsx) et accède au premier graphique dans la première feuille de calcul. Ensuite, il appelle la méthode `Chart::Calculate()` et détermine le type des valeurs X et Y du premier point de graphique, puis les affiche dans la console. Veuillez voir la sortie console ci-dessous pour référence.

## **Code d'exemple**
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

## **Sortie console**

{{< highlight java >}}

X Value Type: IsString

Y Value Type: IsNumeric

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
