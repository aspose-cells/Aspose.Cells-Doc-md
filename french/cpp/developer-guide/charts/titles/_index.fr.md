---
title: Gérer les titres des graphiques Excel avec C++
linktitle: Titres
description: Apprenez comment utiliser Aspose.Cells for C++ pour ajouter et formater les titres de graphique et d axe dans Microsoft Excel. Notre guide montrera comment définir différents types de titres, ajuster leur apparence et modifier les titres des axes pour une meilleure représentation et clarté des données.
keywords: Aspose.Cells for C++, Titres de graphique, Titres d axe, Microsoft Excel, Représentation des données, Apparence.
type: docs
weight: 50
url: /fr/cpp/chart-and-axis-titles/
---

{{% alert color="primary" %}}

Dans les graphiques Excel, il existe 2 types de titres :
1. Titre du graphique 
1. Titres des axes

{{% /alert %}}

## **Options de titre**
Aspose.Cells permet également de gérer les titres de graphique en temps réel. Avec l'objet [Title](https://reference.aspose.com/cells/cpp/aspose.cells.charts/title/), vous pouvez changer le texte, la police et le format de remplissage des titres.

|![todo:image_alt_text](chart_title.png)|

## **Configuration des titres des graphiques ou des axes**
Vous pouvez utiliser Microsoft Excel pour définir les titres d’un graphique et de ses axes dans un environnement WYSIWYG. Aspose.Cells permet également aux développeurs de définir les titres d’un graphique et de ses axes en temps réel. Tous les graphiques et leurs axes contiennent une propriété [Title](https://reference.aspose.com/cells/cpp/aspose.cells.charts/title/) qui peut être utilisée pour définir leurs titres, comme illustré dans l'exemple ci-dessous.

Le code suivant montre comment définir des titres pour les graphiques et les axes.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

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

    // Setting the foreground color of the plot area
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::Blue());

    // Setting the foreground color of the chart area
    chart.GetChartArea().GetArea().SetForegroundColor(Color::Yellow());

    // Setting the foreground color of the 1st SeriesCollection area
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color::Red());

    // Setting the foreground color of the area of the 1st SeriesCollection point
    chart.GetNSeries().Get(0).GetPoints().Get(0).GetArea().SetForegroundColor(Color::Cyan());

    // Filling the area of the 2nd SeriesCollection with a gradient
    chart.GetNSeries().Get(1).GetArea().GetFillFormat().SetOneColorGradient(Color::Lime(), 1, GradientStyleType::Horizontal, 1);

    // Setting the title of a chart
    chart.GetTitle().SetText(u"Title");

    // Setting the font color of the chart title to blue
    chart.GetTitle().GetFont().SetColor(Color::Blue());

    // Setting the title of category axis of the chart
    chart.GetCategoryAxis().GetTitle().SetText(u"Category");

    // Setting the title of value axis of the chart
    chart.GetValueAxis().GetTitle().SetText(u"Value");

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sujets avancés**
- [Lire le sous-titre du graphique à partir du fichier ODS](/cells/fr/cpp/read-chart-subtitle-from-ods-file/)
{{< app/cells/assistant language="cpp" >}}
