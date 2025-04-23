---
title: Définir l apparence du graphique avec C++
linktitle: Format de graphique
description: Apprenez à configurer l apparence des graphiques dans Aspose.Cells for C++. Notre guide vous montrera comment modifier les dispositions du graphique, les couleurs, les polices et les effets pour obtenir le style visuel souhaité et améliorer vos feuilles de calcul.
keywords: Aspose.Cells for C++, création de graphiques, apparence du graphique, dispositions, couleurs, polices, effets, feuilles de calcul.
type: docs
weight: 20
url: /fr/cpp/setting-chart-appearance/
---

## **Réglage de l’apparence du graphique**
Dans Comment créer un graphique, nous avons présenté brièvement les types de graphiques et d'objets de graphiques offerts par Aspose.Cells, et décrit comment en créer un. Cet article discute comment personnaliser l'apparence des graphiques en définissant leurs propriétés :

- Définir la zone du graphique.
- Définition des lignes du graphique.
- Application de thèmes.
- Définition des titres des graphiques et des axes.
- Travailler avec des lignes de repère.

### **Définition de la zone du graphique**
Il existe différents types de zones dans un graphique et Aspose.Cells offre la flexibilité de modifier l'apparence de chaque zone. Les développeurs peuvent appliquer différents paramètres de mise en forme à une zone en changeant sa couleur avant-plan, sa couleur d'arrière-plan et son format de remplissage, etc.

Dans l'exemple ci-dessous, nous avons appliqué différents paramètres de mise en forme sur différents types de zones d'un graphique. Ces zones comprennent :

- Zone de traçage
- Zone du graphique
Zone de SeriesCollection
- Zone d'un point unique dans une SeriesCollection

Le code suivant montre comment définir la zone du graphique.

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

    // Create workbook
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

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

### **Définition des lignes du graphique**
Les développeurs peuvent également appliquer différents styles sur les lignes ou les marqueurs de données de la [SeriesCollection](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/). L'extrait de code suivant montre comment définir les lignes du graphique en utilisant l'API Aspose.Cells.

```c++
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

    // Create workbook
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

    // Applying a dotted line style on the lines of a SeriesCollection
    chart.GetNSeries().Get(0).GetBorder().SetStyle(LineType::Dot);

    // Applying a triangular marker style on the data markers of a SeriesCollection
    chart.GetNSeries().Get(0).GetMarker().SetMarkerStyle(ChartMarkerType::Triangle);

    // Setting the weight of all lines in a SeriesCollection to medium
    chart.GetNSeries().Get(1).GetBorder().SetWeight(WeightType::MediumLine);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Application des thèmes Microsoft Excel 2007/2010 aux graphiques**
Les développeurs peuvent appliquer différents thèmes/couleurs Microsoft Excel sur la [SeriesCollection](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/) ou d'autres objets graphiques comme illustré dans l'exemple ci-dessous.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xlsx";

    // Instantiate the workbook to open the file that contains a chart
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(1);

    // Get the first chart in the sheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Specify the FillFormat's type to Solid Fill of the first series
    chart.GetNSeries().Get(0).GetArea().GetFillFormat().SetFillType(FillType::Solid);

    // Get the CellsColor of SolidFill
    CellsColor cc = chart.GetNSeries().Get(0).GetArea().GetFillFormat().GetSolidFill().GetCellsColor();

    // Create a theme in Accent style
    cc.SetThemeColor(ThemeColor(ThemeColorType::Accent6, 0.6));

    // Apply the theme to the series
    chart.GetNSeries().Get(0).GetArea().GetFillFormat().GetSolidFill().SetCellsColor(cc);

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Chart theme applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Configuration des titres des graphiques ou des axes**
Vous pouvez utiliser Microsoft Excel pour définir les titres d'un graphique et de ses axes dans un environnement WYSIWYG. Aspose.Cells permet également aux développeurs de définir ces titres en temps réel. Tous les graphiques et leurs axes contiennent une propriété [Title](https://reference.aspose.com/cells/cpp/aspose.cells.charts/title/) qui peut être utilisée pour définir leurs titres comme illustré dans l'exemple ci-dessous.

Le snippet de code suivant démontre comment définir des titres pour les graphiques et les axes.

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

    // Create workbook
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

### **Travailler avec les grandes lignes de la grille**
Il est possible de personnaliser l'apparence des grandes lignes de la grille. Masquer ou afficher les lignes de la grille, ou définir leur couleur et d'autres paramètres. Ci-dessous, nous montrons comment masquer les lignes de la grille et comment changer leur couleur.

#### **Masquer les grandes lignes de la grille**
Les développeurs peuvent contrôler la visibilité des lignes de grille principales en réglant la propriété [IsVisible](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/line/isvisible/) de l'objet [Line](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/line/) à **true** ou **false**.

Le code suivant montre comment masquer les grandes lignes de la grille. Après avoir masqué les grandes lignes de la grille, un graphique en colonnes sera ajouté à la feuille de calcul sans lignes de grille.

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

    // Create a workbook object
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

    // Hiding the major gridlines of Category Axis
    chart.GetCategoryAxis().GetMajorGridLines().SetIsVisible(false);

    // Hiding the major gridlines of Value Axis
    chart.GetValueAxis().GetMajorGridLines().SetIsVisible(false);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Changer les paramètres des grandes lignes de la grille**
Les développeurs peuvent non seulement contrôler la visibilité des grandes lignes de la grille, mais aussi d'autres propriétés comme sa couleur, etc.

Le code suivant montre comment changer la couleur des grandes lignes de la grille. Après avoir défini la couleur des grandes lignes de la grille, un graphique en colonnes sera ajouté à la feuille de calcul avec des lignes de grille modifiées.

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

    // Create a workbook object
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

    // Setting the color of Category Axis' major gridlines to silver
    chart.GetCategoryAxis().GetMajorGridLines().SetColor(Color::Silver());

    // Setting the color of Value Axis' major gridlines to red
    chart.GetValueAxis().GetMajorGridLines().SetColor(Color::Red());

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Chart created and formatted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sujets avancés**
- [Définir le code de format des valeurs de la série du graphique](/cells/fr/cpp/set-the-values-format-code-of-chart-series/)
- [Définir une image comme remplissage d'arrière-plan dans le graphique](/cells/fr/cpp/set-picture-as-background-fill-in-the-chart/)
