---
title: Définir la source de données pour le graphique avec C++
linktitle: Source de données
type: docs
weight: 10
url: /fr/cpp/data-formatting-in-charts/
description: Découvrez les différentes sources de données supportées par Aspose.Cells for C++. Notre guide vous expliquera les différents types de sources de données disponibles et comment les connecter et en extraire des données pour remplir vos feuilles de calcul.
keywords: Aspose.Cells for C++, graphiques, formatage des données, étiquettes, couleurs, polices, apparence, convivialité.
---

Dans nos sujets précédents, nous avons déjà fourni de nombreux exemples pour démontrer comment vous pouvez définir une source de données pour votre graphique. Dans ce sujet, nous allons fournir plus de détails sur les types de données pouvant être configurés pour un graphique.

## **Définition des données du graphique**

Il existe deux types de données à manipuler lors de l'utilisation de graphiques avec Aspose.Cells, comme suit :

- Données du graphique.
- Données de catégorie.

### **Données du graphique**

Les données du graphique sont les données que nous utilisons comme source de données pour construire nos graphiques. Nous pouvons ajouter une plage de cellules (contenant des données de graphique) en appelant la méthode [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/add/) de l'objet [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/).

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Excel object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(170);
    worksheet.GetCells().Get(u"A4").PutValue(300);
    worksheet.GetCells().Get(u"B1").PutValue(160);
    worksheet.GetCells().Get(u"B2").PutValue(32);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(40);

    // Adding sample values to cells as category data
    worksheet.GetCells().Get(u"C1").PutValue(u"Q1");
    worksheet.GetCells().Get(u"C2").PutValue(u"Q2");
    worksheet.GetCells().Get(u"C3").PutValue(u"Y1");
    worksheet.GetCells().Get(u"C4").PutValue(u"Y2");

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.GetNSeries().Add(u"A1:B4", true);

    // Saving the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Chart added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Données de catégorie**

Les données de catégorie sont utilisées pour l'étiquetage des données du graphique et peuvent être ajoutées à [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/) en utilisant sa propriété [**GetCategoryData()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/getcategorydata/). Un exemple complet est donné ci-dessous pour démontrer l'utilisation des données du graphique et de catégorie. Après l'exécution du code d'exemple ci-dessus, un graphique à colonnes sera ajouté à la feuille de calcul comme indiqué ci-dessous.

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int sheetIndex = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(10);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(170);
    worksheet.GetCells().Get(u"A4").PutValue(200);
    worksheet.GetCells().Get(u"B1").PutValue(120);
    worksheet.GetCells().Get(u"B2").PutValue(320);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(40);

    // Add sample values to cells as category data
    worksheet.GetCells().Get(u"C1").PutValue(u"Q1");
    worksheet.GetCells().Get(u"C2").PutValue(u"Q2");
    worksheet.GetCells().Get(u"C3").PutValue(u"Y1");
    worksheet.GetCells().Get(u"C4").PutValue(u"Y2");

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.GetNSeries().Add(u"A1:B4", true);

    // Set the data source for the category data of SeriesCollection
    chart.GetNSeries().SetCategoryData(u"C1:C4");

    // Save the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Chart added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sujets avancés**
- [Changer la source de données du graphique vers la feuille de calcul de destination lors de la copie des lignes ou de la plage](/cells/fr/cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Créer des graphiques dynamiques](/cells/fr/cpp/create-dynamic-charts/)
- [Méthode simple pour configurer un graphique en utilisant la méthode Chart.SetChartDataRange](/cells/fr/cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Trouver le type de valeurs X et Y des points dans la série de graphiques](/cells/fr/cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)
{{< app/cells/assistant language="cpp" >}}
