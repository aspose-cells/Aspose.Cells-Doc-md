---
title: Gérer les DataLabels des graphiques Excel avec C++
linktitle: Étiquettes de données
type: docs
weight: 50
url: /fr/cpp/insert-datalabels-to-chart/
description: Apprenez comment gérer efficacement les étiquettes de données dans les graphiques Excel à l aide de Aspose.Cells for C++. Notre guide complet couvre diverses tâches de gestion, y compris l ajout, la suppression et la modification des étiquettes pour améliorer la lisibilité et l utilisabilité du graphique.
keywords: Aspose.Cells for C++, graphiques Excel, étiquettes de données, gestion, lisibilité, convivialité, ajout, suppression, modification.
---

{{% alert color="primary" %}}

Les DataLabels sont une partie importante d'un graphique. Nous pouvons facilement connaître la valeur, le pourcentage, etc. de chaque série.

{{% /alert %}}

## **Options d'étiquettes de données**
Aspose.Cells permet également de gérer les DataLabels du graphique en temps réel avec l'objet [DataLabels](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/). Il est simple de déplacer, mettre à jour et formater les étiquettes de données du graphique.

|![todo:image_alt_text](chart_datalabels.png)|

## **Gérer les étiquettes de données du graphique**
Il est simple de gérer les DataLabels du graphique avec Aspose.Cells [DataLabels](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/).

L'extrait de code suivant montre comment gérer DataLabels :

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
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(60);
    worksheet.GetCells().Get(u"B2").PutValue(32);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Show value labels
    chart.GetNSeries().Get(0).GetDataLabels().SetShowValue(true);

    // Show series name labels
    chart.GetNSeries().Get(1).GetDataLabels().SetShowSeriesName(true);

    // Move labels to center
    chart.GetNSeries().Get(1).GetDataLabels().SetPosition(LabelPositionType::Center);

    // Save the file
    workbook.Save(u"chart_datalabels.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Sujets avancés**
- [Ajouter des étiquettes personnalisées aux points de données de la série du graphique](/cells/fr/cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/)
- [Désactiver le retour à la ligne pour les étiquettes de données du graphique](/cells/fr/cpp/disable-text-wrapping-for-data-labels-of-the-chart/)
- [Redimensionner la forme de l'étiquette de données du graphique pour s'adapter au texte](/cells/fr/cpp/resize-chart-s-data-label-shape-to-fit-text/)
- [Étiquette de données personnalisée Rich Text du point de graphique](/cells/fr/cpp/rich-text-custom-data-label-of-chart-point/)
- [Définir le type de forme des étiquettes de données du graphique](/cells/fr/cpp/set-the-shape-type-of-data-labels-of-chart/)
- [Affichage de la plage de cellules sous forme d'étiquettes de données](/cells/fr/cpp/showing-cell-range-as-the-data-labels/)
{{< app/cells/assistant language="cpp" >}}
