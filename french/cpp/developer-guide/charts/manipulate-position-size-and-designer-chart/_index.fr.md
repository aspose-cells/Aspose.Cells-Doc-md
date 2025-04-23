---
title: Manipuler la taille, la position et le graphique de conception avec C++
linktitle: Manipuler la position, la taille et la conception du graphique
description: Apprenez comment utiliser Aspose.Cells for C++ pour manipuler efficacement la position, la taille et le graphique de conception dans Microsoft Excel. Notre guide démontrera comment ajuster ces propriétés pour une meilleure mise en page et visualisation.
keywords: Aspose.Cells for C++, Position, Taille, Graphique de conception, Microsoft Excel, Mise en page, Visualisation.
type: docs
weight: 45
url: /fr/cpp/manipulate-position-size-and-designer-chart/
---

## **Position et taille du graphique**
 Parfois, vous souhaitez changer la position ou la taille du graphique nouveau ou existant dans la feuille de calcul. Aspose.Cells offre la propriété [Chart.GetChartObject()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getchartobject/) pour réaliser cela. Vous pouvez utiliser ses sous-propriétés pour redimensionner le graphique avec une nouvelle **hauteur** et **largeur** ou le repositionner avec de nouvelles coordonnées **X** et **Y**.

### **Contrôle de la position et la taille du graphique**
Pour changer la position (coordonnées X, Y) ou la taille (hauteur, largeur) du graphique, utilisez ces propriétés :

1. [Chart.GetX()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getx/)
1. [Chart.GetY()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gety/)
1. [Chart.GetHeight()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getheight/)
1. [Chart.GetWidth()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getwidth/)

L'exemple suivant explique l'utilisation des API ci-dessus, il charge le classeur existant qui contient un graphique dans sa première feuille. Ensuite, il redimensionne et repositionne le graphique en utilisant Aspose.Cells.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"chart.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"chart.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(1);

    // Load the chart from the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Resize the chart
    chart.GetChartObject().SetWidth(400);
    chart.GetChartObject().SetHeight(300);

    // Reposition the chart
    chart.GetChartObject().SetX(250);
    chart.GetChartObject().SetY(150);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Chart resized and repositioned successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Manipulation des graphiques de concepteur**
Il y a des moments où vous avez besoin de manipuler ou de modifier des graphiques dans des fichiers de modèle de concepteur. Aspose.Cells prend en charge pleinement la manipulation des contenus et des éléments de graphique de concepteur. Les données, les contenus des graphiques, l'image de fond et les mises en forme peuvent être conservés avec précision.

### **Manipulation des graphiques de concepteur dans les fichiers de modèle**
Pour manipuler des graphiques de concepteur dans des fichiers de modèle, utilisez l'API liée au graphique. Par exemple, vous pouvez utiliser la propriété Worksheet.Charts pour obtenir la collection de graphiques existante dans le fichier de modèle.

#### **Création d'un graphique**
L'exemple suivant montre comment créer un graphique en forme de pyramide. Nous manipulerons ce graphique plus tard.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;

    int sheetIndex = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(4);
    worksheet.GetCells().Get(u"B2").PutValue(20);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    int chartIndex = worksheet.GetCharts().Add(ChartType::Pyramid, 5, 0, 15, 5);
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    chart.GetNSeries().Add(u"A1:B3", true);

    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Excel file created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Manipulation du graphique**
L'exemple suivant montre comment manipuler le graphique existant. Dans cet exemple, nous modifions le graphique créé précédemment. Dans la sortie générée, notez que l'étiquette de date d'un point de données a été définie sur 'Royaume-Uni, 30K'.

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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"piechart.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Open the existing file
    Workbook workbook(inputFilePath);

    // Get the designer chart in the second sheet
    Worksheet sheet = workbook.GetWorksheets().Get(1);
    Chart chart = sheet.GetCharts().Get(0);

    // Get the data labels in the data series of the third data point
    DataLabels datalabels = chart.GetNSeries().Get(0).GetPoints().Get(2).GetDataLabels();

    // Change the text of the label
    datalabels.SetText(u"Unided Kingdom, 400K ");

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Data label text updated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Manipulation d'un graphique linéaire dans le modèle de concepteur**
Dans cet exemple, nous manipulerons un graphique linéaire. Nous ajouterons des séries de données au graphique existant et changerons leurs couleurs de ligne.

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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the designer chart in the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Chart chart = worksheet.GetCharts().Get(0);

    // Add the third data series to it
    chart.GetNSeries().Add(U16String(u"{60, 80, 10}"), true);

    // Add another data series (fourth) to it
    chart.GetNSeries().Add(U16String(u"{0.3, 0.7, 1.2}"), true);

    // Plot the fourth data series on the second axis
    chart.GetNSeries().Get(3).SetPlotOnSecondAxis(true);

    // Change the Border color of the second data series
    chart.GetNSeries().Get(1).GetBorder().SetColor(Color::Green());

    // Change the Border color of the third data series
    chart.GetNSeries().Get(2).GetBorder().SetColor(Color::Red());

    // Make the second value axis visible
    chart.GetSecondValueAxis().SetIsVisible(true);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Chart modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
