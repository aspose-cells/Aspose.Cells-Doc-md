---
title: Gérer les axes des graphiques Excel avec C++
description: Apprenez à configurer les axes de graphiques dans Aspose.Cells for C++. Notre guide vous montrera comment ajuster les axes principaux et secondaires, définir leurs plages et modifier leurs propriétés pour améliorer vos graphiques.
keywords: Aspose.Cells for C++, axes de graphique, configuration, axes principaux, axes secondaires, plage, propriétés.
linktitle: Axes
type: docs
weight: 50
url: /fr/cpp/chart-axes/
---

{{% alert color="primary" %}}

Dans les graphiques Excel, il existe 3 types d'axes :
1. Axe horizontal (catégorie) : Axe X
1. Axe vertical (valeur) : Axe Y
1. Axe de profondeur (série) : Axe Z

{{% /alert %}}

## **Options d'Axe**
Aspose.Cells vous permet également de gérer les axes des graphiques en temps réel. Avec l'objet [Axis](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/), vous pouvez modifier toutes les options de l'axe comme dans Excel.

|![todo:image_alt_text](chart_axes.png)|

## **Gérer les axes des X et Y**

Dans les graphiques Excel, les axes horizontal et vertical sont les deux axes les plus populaires à utiliser.

Le fragment de code suivant montre comment définir les options des axes X et Y.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(u"Series1");
    worksheet.GetCells().Get(u"A2").PutValue(50);
    worksheet.GetCells().Get(u"A3").PutValue(100);
    worksheet.GetCells().Get(u"A4").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(u"Series2");
    worksheet.GetCells().Get(u"B2").PutValue(60);
    worksheet.GetCells().Get(u"B3").PutValue(32);
    worksheet.GetCells().Get(u"B4").PutValue(50);

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.SetChartDataRange(u"A1:B4", true);

    // Hiding X axis
    chart.GetCategoryAxis().SetIsVisible(false);

    // Setting max value of Y axis
    chart.GetValueAxis().SetMaxValue(200);

    // Setting major unit
    chart.GetValueAxis().SetMajorUnit(50);

    // Save the file
    workbook.Save(u"chart_axes.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Sujets avancés**
- [Changer la direction des étiquettes des graduations](/cells/fr/cpp/change-tick-label-direction/)
- [Déterminer quels axes existent dans le graphique](/cells/fr/cpp/determine-which-axis-exists-in-the-chart/)
- [Gérer les unités automatiques de l'axe du graphique comme dans Microsoft Excel](/cells/fr/cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/)
- [Lire les étiquettes des axes après le calcul du graphique](/cells/fr/cpp/read-axis-labels-after-calculating-the-chart/)
- [Comment définir l'axe des catégories dans un graphique Excel](/cells/fr/cpp/how-to-set-category-axis/)
