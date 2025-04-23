---
title: Gérer la légende des graphiques Excel avec C++
linktitle: Légende
description: Apprenez comment utiliser Aspose.Cells for C++ pour exploiter efficacement et personnaliser les légendes des graphiques dans Microsoft Excel. Notre guide complet explique la fonctionnalité de la légende, comment y accéder et la modifier, ainsi que comment améliorer la visualisation et la compréhension des données avec des légendes.
keywords: Aspose.Cells for C++, Légendes de graphiques, Microsoft Excel, Visualisation, Compréhension des données.
type: docs
weight: 50
url: /fr/cpp/chart-legend/
---

## **Options de légende**
Aspose.Cells permet également de gérer la légende d'un graphique en cours d'exécution. Avec l'objet [Legend](https://reference.aspose.com/cells/cpp/aspose.cells.charts/legend/), la légende peut être déplacée, mise à jour et formatée.

|![todo:image_alt_text](chart_legend.png)|

## **Définir la légende du graphique**
 Il est simple de gérer la légende d'un graphique avec Aspose.Cells [Legend](https://reference.aspose.com/cells/cpp/aspose.cells.charts/legend/).

L'extrait de code suivant montre comment gérer la légende :

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
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

    // Setting the title of a chart
    chart.GetTitle().SetText(u"Title");

    // Setting the font color of the chart title to blue
    chart.GetTitle().GetFont().SetColor(Color::Blue());

    // Move the legend to left
    chart.GetLegend().SetPosition(LegendPositionType::Left);

    // Set font color of the legend
    chart.GetLegend().GetFont().SetColor(Color::Blue());

    // Save the file
    workbook.Save(u"chart_legend.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Sujets avancés**
- [Définir le texte de l'entrée de la légende du graphique à aucun en utilisant Aspose.Cells](/cells/fr/cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/)
