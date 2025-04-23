---
title: Couleurs personnalisées de tranche ou de secteur dans un graphique à secteurs avec C++
linktitle: Couleurs personnalisées de tranche ou de secteur dans le diagramme circulaire
description: Apprenez à utiliser Aspose.Cells for C++ pour personnaliser les couleurs des tranches et secteurs dans un graphique à secteurs. Notre guide montrera comment attribuer des couleurs uniques à chaque tranche, secteur ou légion pour une meilleure apparence visuelle et une meilleure représentation des données.
keywords: Aspose.Cells for C++, Graphique à secteurs, Couleurs personnalisées de tranches, Couleurs de secteurs, Appeal visuel, Représentation des données.
type: docs
weight: 60
url: /fr/cpp/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

Cet article explique comment ajouter des couleurs personnalisées aux tranches/secteurs d'un diagramme circulaire. Par défaut, les diagrammes circulaires utilisent le modèle par défaut de Microsoft Excel. Pour utiliser d'autres couleurs, redéfinissez les couleurs dans le diagramme.

{{% /alert %}}

Pour définir une couleur personnalisée pour les tranches ou secteurs individuels d'un diagramme circulaire :

1. Accédez à [**Series**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/) l'objet [**ChartPoint**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/).
1. Attribuez la couleur de votre choix en utilisant la propriété [**ChartPoint.GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/area/getforegroundcolor/).

Cet article explique également comment :

- Les données de catégorie d'un graphique.
- Un titre de graphique lié à une cellule.
- Les paramètres de police du titre du graphique.
- La position de la légende.

{{% alert color="primary" %}}

[**ChartPoint.GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/area/getforegroundcolor/) n'est pas spécifique aux diagrammes circulaires mais peut être utilisé pour tous les types de diagrammes.

{{% /alert %}}

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook object
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put the sample values used in a pie chart
    worksheet.GetCells().Get(u"C3").PutValue(u"India");
    worksheet.GetCells().Get(u"C4").PutValue(u"China");
    worksheet.GetCells().Get(u"C5").PutValue(u"United States");
    worksheet.GetCells().Get(u"C6").PutValue(u"Russia");
    worksheet.GetCells().Get(u"C7").PutValue(u"United Kingdom");
    worksheet.GetCells().Get(u"C8").PutValue(u"Others");

    // Put the sample values used in a pie chart
    worksheet.GetCells().Get(u"D2").PutValue(u"% of world population");
    worksheet.GetCells().Get(u"D3").PutValue(25);
    worksheet.GetCells().Get(u"D4").PutValue(30);
    worksheet.GetCells().Get(u"D5").PutValue(10);
    worksheet.GetCells().Get(u"D6").PutValue(13);
    worksheet.GetCells().Get(u"D7").PutValue(9);
    worksheet.GetCells().Get(u"D8").PutValue(13);

    // Create a pie chart with desired length and width
    int pieIdx = worksheet.GetCharts().Add(ChartType::Pie, 1, 6, 15, 14);

    // Access the pie chart
    Chart pie = worksheet.GetCharts().Get(pieIdx);

    // Set the pie chart series
    pie.GetNSeries().Add(u"D3:D8", true);

    // Set the category data
    pie.GetNSeries().SetCategoryData(u"=Sheet1!$C$3:$C$8");

    // Set the chart title that is linked to cell D2
    pie.GetTitle().SetLinkedSource(u"D2");

    // Set the legend position at the bottom
    pie.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set the chart title's font name and color
    pie.GetTitle().GetFont().SetName(u"Calibri");
    pie.GetTitle().GetFont().SetSize(18);

    // Access the chart series
    Series srs = pie.GetNSeries().Get(0);

    // Color the individual points with custom colors
    srs.GetPoints().Get(0).GetArea().SetForegroundColor(Color{0, 246, 22, 219});
    srs.GetPoints().Get(1).GetArea().SetForegroundColor(Color{0, 51, 34, 84});
    srs.GetPoints().Get(2).GetArea().SetForegroundColor(Color{0, 46, 74, 44});
    srs.GetPoints().Get(3).GetArea().SetForegroundColor(Color{0, 19, 99, 44});
    srs.GetPoints().Get(4).GetArea().SetForegroundColor(Color{0, 208, 223, 7});
    srs.GetPoints().Get(5).GetArea().SetForegroundColor(Color{0, 222, 69, 8});

    // Autofit all columns
    worksheet.AutoFitColumns();

    // Save the workbook
    U16String outputPath = outDir + u"output.out.xlsx";
    workbook.Save(outputPath, SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
}
```
