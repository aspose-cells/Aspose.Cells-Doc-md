---
title: Création d un graphique en secteurs avec lignes de leader avec C++
linktitle: Graphique circulaire
description: Apprenez comment utiliser Aspose.Cells for C++ pour créer un graphique en secteurs avec lignes de leader dans Microsoft Excel. Notre guide démontrera comment ajouter des lignes de leader reliant les points de données à la légende et améliorer la clarté globale de votre graphique.
keywords: Aspose.Cells for C++, Graphique en secteurs, Lignes de leader, Microsoft Excel, Visualisation de données, Personnalisation du graphique.
type: docs
weight: 45
url: /fr/cpp/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

Cet article explique comment créer un graphique en secteurs avec lignes de leader à partir de zéro en utilisant l'API Aspose.Cells for C++. Dans Excel, l'option 'Afficher les lignes de leader' est activée par défaut, donc lorsque vous créez un graphique en secteurs dans Excel, les lignes de leader sont affichées. Cependant, lors de la création d'un graphique similaire avec l'API Aspose.Cells, vous devez définir explicitement la propriété [**Series.GetHasLeaderLines()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/gethasleaderlines/).

{{% /alert %}}

Pour démontrer l'utilisation de l'API Aspose.Cells for C++ pour créer un graphique en secteurs avec lignes de leader, nous créerons d'abord un nouveau [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) et entrerons quelques données qui serviront de source pour la série. Une fois les données en place, nous ajouterons un [**Chart**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/) de type [**ChartType.Pie**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/) à la collection de graphiques et définirons ses différents aspects pour obtenir la vue souhaitée du graphique.

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

    // Create an instance of Workbook in XLSX format
    Workbook workbook(FileFormatType::Xlsx);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add two columns of data
    worksheet.GetCells().Get(u"A1").PutValue(u"Retail");
    worksheet.GetCells().Get(u"A2").PutValue(u"Services");
    worksheet.GetCells().Get(u"A3").PutValue(u"Info & Communication");
    worksheet.GetCells().Get(u"A4").PutValue(u"Transport Equip");
    worksheet.GetCells().Get(u"A5").PutValue(u"Construction");
    worksheet.GetCells().Get(u"A6").PutValue(u"Other Products");
    worksheet.GetCells().Get(u"A7").PutValue(u"Wholesale");
    worksheet.GetCells().Get(u"A8").PutValue(u"Land Transport");
    worksheet.GetCells().Get(u"A9").PutValue(u"Air Transport");
    worksheet.GetCells().Get(u"A10").PutValue(u"Electric Appliances");
    worksheet.GetCells().Get(u"A11").PutValue(u"Securities");
    worksheet.GetCells().Get(u"A12").PutValue(u"Textiles & Apparel");
    worksheet.GetCells().Get(u"A13").PutValue(u"Machinery");
    worksheet.GetCells().Get(u"A14").PutValue(u"Metal Products");
    worksheet.GetCells().Get(u"A15").PutValue(u"Cash");
    worksheet.GetCells().Get(u"A16").PutValue(u"Banks");

    worksheet.GetCells().Get(u"B1").PutValue(10.4);
    worksheet.GetCells().Get(u"B2").PutValue(5.2);
    worksheet.GetCells().Get(u"B3").PutValue(6.4);
    worksheet.GetCells().Get(u"B4").PutValue(10.4);
    worksheet.GetCells().Get(u"B5").PutValue(7.9);
    worksheet.GetCells().Get(u"B6").PutValue(4.1);
    worksheet.GetCells().Get(u"B7").PutValue(3.5);
    worksheet.GetCells().Get(u"B8").PutValue(5.7);
    worksheet.GetCells().Get(u"B9").PutValue(3);
    worksheet.GetCells().Get(u"B10").PutValue(14.7);
    worksheet.GetCells().Get(u"B11").PutValue(3.6);
    worksheet.GetCells().Get(u"B12").PutValue(2.8);
    worksheet.GetCells().Get(u"B13").PutValue(7.8);
    worksheet.GetCells().Get(u"B14").PutValue(2.4);
    worksheet.GetCells().Get(u"B15").PutValue(1.8);
    worksheet.GetCells().Get(u"B16").PutValue(10.1);

    // Create a pie chart and add it to the collection of charts
    int id = worksheet.GetCharts().Add(ChartType::Pie, 3, 3, 23, 13);

    // Access newly created Chart instance
    Chart chart = worksheet.GetCharts().Get(id);

    // Set series data range
    chart.GetNSeries().Add(u"B1:B16", true);

    // Set category data range
    chart.GetNSeries().SetCategoryData(u"A1:A16");

    // Turn off legend
    chart.SetShowLegend(false);

    // Access data labels
    DataLabels dataLabels = chart.GetNSeries().Get(0).GetDataLabels();

    // Turn on category names
    dataLabels.SetShowCategoryName(true);

    // Turn on percentage format
    dataLabels.SetShowPercentage(true);

    // Set position
    dataLabels.SetPosition(LabelPositionType::OutsideEnd);

    // Set separator
    dataLabels.SetSeparatorType(DataLabelsSeparatorType::Comma);

    // Save the workbook
    workbook.Save(outDir + u"PieChart_out.xlsx");

    std::cout << "Pie chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Jusqu'à présent, nous avons créé un graphique circulaire et réglé ses différents aspects. Maintenant, nous allons activer les lignes de repère pour le graphique. Veuillez noter que pour afficher les lignes de repère, nous devons déplacer légèrement les étiquettes de données.

Le code suivant active les lignes de repère, actualise le graphique, puis calcule les positions des étiquettes de données pour les déplacer en conséquence.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook in XLSX format
    Workbook workbook(FileFormatType::Xlsx);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add two columns of data
    worksheet.GetCells().Get(u"A1").PutValue(u"Retail");
    worksheet.GetCells().Get(u"A2").PutValue(u"Services");
    worksheet.GetCells().Get(u"A3").PutValue(u"Info & Communication");
    worksheet.GetCells().Get(u"A4").PutValue(u"Transport Equip");
    worksheet.GetCells().Get(u"A5").PutValue(u"Construction");
    worksheet.GetCells().Get(u"A6").PutValue(u"Other Products");
    worksheet.GetCells().Get(u"A7").PutValue(u"Wholesale");
    worksheet.GetCells().Get(u"A8").PutValue(u"Land Transport");
    worksheet.GetCells().Get(u"A9").PutValue(u"Air Transport");
    worksheet.GetCells().Get(u"A10").PutValue(u"Electric Appliances");
    worksheet.GetCells().Get(u"A11").PutValue(u"Securities");
    worksheet.GetCells().Get(u"A12").PutValue(u"Textiles & Apparel");
    worksheet.GetCells().Get(u"A13").PutValue(u"Machinery");
    worksheet.GetCells().Get(u"A14").PutValue(u"Metal Products");
    worksheet.GetCells().Get(u"A15").PutValue(u"Cash");
    worksheet.GetCells().Get(u"A16").PutValue(u"Banks");

    worksheet.GetCells().Get(u"B1").PutValue(10.4);
    worksheet.GetCells().Get(u"B2").PutValue(5.2);
    worksheet.GetCells().Get(u"B3").PutValue(6.4);
    worksheet.GetCells().Get(u"B4").PutValue(10.4);
    worksheet.GetCells().Get(u"B5").PutValue(7.9);
    worksheet.GetCells().Get(u"B6").PutValue(4.1);
    worksheet.GetCells().Get(u"B7").PutValue(3.5);
    worksheet.GetCells().Get(u"B8").PutValue(5.7);
    worksheet.GetCells().Get(u"B9").PutValue(3);
    worksheet.GetCells().Get(u"B10").PutValue(14.7);
    worksheet.GetCells().Get(u"B11").PutValue(3.6);
    worksheet.GetCells().Get(u"B12").PutValue(2.8);
    worksheet.GetCells().Get(u"B13").PutValue(7.8);
    worksheet.GetCells().Get(u"B14").PutValue(2.4);
    worksheet.GetCells().Get(u"B15").PutValue(1.8);
    worksheet.GetCells().Get(u"B16").PutValue(10.1);

    // Create a pie chart and add it to the collection of charts
    int id = worksheet.GetCharts().Add(ChartType::Pie, 3, 3, 23, 13);

    // Access newly created Chart instance
    Chart chart = worksheet.GetCharts().Get(id);

    // Set series data range
    chart.GetNSeries().Add(u"B1:B16", true);

    // Set category data range
    chart.GetNSeries().SetCategoryData(u"A1:A16");

    // Turn off legend
    chart.SetShowLegend(false);

    // Access data labels
    DataLabels dataLabels = chart.GetNSeries().Get(0).GetDataLabels();

    // Turn on category names
    dataLabels.SetShowCategoryName(true);

    // Turn on percentage format
    dataLabels.SetShowPercentage(true);

    // Set position
    dataLabels.SetPosition(LabelPositionType::OutsideEnd);

    // Set separator
    dataLabels.SetSeparatorType(DataLabelsSeparatorType::Comma);

    // Turn on leader lines
    chart.GetNSeries().Get(0).SetHasLeaderLines(true);

    // Calculate chart
    chart.Calculate();

    // You need to move DataLabels a little leftward or rightward depending on their position to show leader lines
    int DELTA = 100;
    for (int i = 0; i < chart.GetNSeries().Get(0).GetPoints().GetCount(); i++)
    {
        int X = chart.GetNSeries().Get(0).GetPoints().Get(i).GetDataLabels().GetX();
        // If it is greater than 2000, then move the X position a little right otherwise move the X position a little left
        if (X > 2000)
            chart.GetNSeries().Get(0).GetPoints().Get(i).GetDataLabels().SetX(X + DELTA);
        else
            chart.GetNSeries().Get(0).GetPoints().Get(i).GetDataLabels().SetX(X - DELTA);
    }

    // Save the workbook
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
}
```

Enfin, le code suivant sauvegarde le graphique au format image et le classeur au format XLSX.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook in XLSX format
    Workbook workbook(FileFormatType::Xlsx);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add two columns of data
    worksheet.GetCells().Get(u"A1").PutValue(u"Retail");
    worksheet.GetCells().Get(u"A2").PutValue(u"Services");
    worksheet.GetCells().Get(u"A3").PutValue(u"Info & Communication");
    worksheet.GetCells().Get(u"A4").PutValue(u"Transport Equip");
    worksheet.GetCells().Get(u"A5").PutValue(u"Construction");
    worksheet.GetCells().Get(u"A6").PutValue(u"Other Products");
    worksheet.GetCells().Get(u"A7").PutValue(u"Wholesale");
    worksheet.GetCells().Get(u"A8").PutValue(u"Land Transport");
    worksheet.GetCells().Get(u"A9").PutValue(u"Air Transport");
    worksheet.GetCells().Get(u"A10").PutValue(u"Electric Appliances");
    worksheet.GetCells().Get(u"A11").PutValue(u"Securities");
    worksheet.GetCells().Get(u"A12").PutValue(u"Textiles & Apparel");
    worksheet.GetCells().Get(u"A13").PutValue(u"Machinery");
    worksheet.GetCells().Get(u"A14").PutValue(u"Metal Products");
    worksheet.GetCells().Get(u"A15").PutValue(u"Cash");
    worksheet.GetCells().Get(u"A16").PutValue(u"Banks");

    worksheet.GetCells().Get(u"B1").PutValue(10.4);
    worksheet.GetCells().Get(u"B2").PutValue(5.2);
    worksheet.GetCells().Get(u"B3").PutValue(6.4);
    worksheet.GetCells().Get(u"B4").PutValue(10.4);
    worksheet.GetCells().Get(u"B5").PutValue(7.9);
    worksheet.GetCells().Get(u"B6").PutValue(4.1);
    worksheet.GetCells().Get(u"B7").PutValue(3.5);
    worksheet.GetCells().Get(u"B8").PutValue(5.7);
    worksheet.GetCells().Get(u"B9").PutValue(3);
    worksheet.GetCells().Get(u"B10").PutValue(14.7);
    worksheet.GetCells().Get(u"B11").PutValue(3.6);
    worksheet.GetCells().Get(u"B12").PutValue(2.8);
    worksheet.GetCells().Get(u"B13").PutValue(7.8);
    worksheet.GetCells().Get(u"B14").PutValue(2.4);
    worksheet.GetCells().Get(u"B15").PutValue(1.8);
    worksheet.GetCells().Get(u"B16").PutValue(10.1);

    // Create a pie chart and add it to the collection of charts
    int id = worksheet.GetCharts().Add(ChartType::Pie, 3, 3, 23, 13);

    // Access newly created Chart instance
    Chart chart = worksheet.GetCharts().Get(id);

    // Set series data range
    chart.GetNSeries().Add(u"B1:B16", true);

    // Set category data range
    chart.GetNSeries().SetCategoryData(u"A1:A16");

    // Turn off legend
    chart.SetShowLegend(false);

    // Access data labels
    DataLabels dataLabels = chart.GetNSeries().Get(0).GetDataLabels();

    // Turn on category names
    dataLabels.SetShowCategoryName(true);

    // Turn on percentage format
    dataLabels.SetShowPercentage(true);

    // Set position
    dataLabels.SetPosition(LabelPositionType::OutsideEnd);

    // Set separator
    dataLabels.SetSeparatorType(DataLabelsSeparatorType::Comma);

    // In order to save the chart image, create an instance of ImageOrPrintOptions
    ImageOrPrintOptions anOption;

    // Set image format
    anOption.SetImageType(ImageType::Png);

    // Set resolution
    anOption.SetHorizontalResolution(200);
    anOption.SetVerticalResolution(200);

    // Render chart to image
    chart.ToImage(u"output_out.png", anOption);

    // Save the workbook to see chart inside the Excel
    workbook.Save(u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```

|**Diagramme circulaire résultant**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

## **Sujets avancés**
- [Couleurs de tranche personnalisées dans le diagramme circulaire](/cells/fr/cpp/custom-slice-or-sector-colors-in-pie-chart/)
- [Savoir si les points de données sont dans le deuxième diagramme circulaire ou dans une barre sur un diagramme de deux ou trois cercles ou sur un diagramme à barres de deux ou trois cercles](/cells/fr/cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## Articles Connexes

- [Création de graphiques](/cells/fr/cpp/creating-charts/)
- [Personnalisation des graphiques](/cells/fr/cpp/customizing-charts/)
- [Mise en forme des données dans les graphiques](/cells/fr/cpp/data-formatting-in-charts/)
- [Réglage de l’apparence du graphique](/cells/fr/cpp/setting-chart-appearance/)
