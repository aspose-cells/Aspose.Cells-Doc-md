---
title: Trois méthodes pour filtrer les données du graphique avec C++
linktitle: Trois méthodes pour filtrer les données du graphique
description: Apprenez comment filtrer les graphiques dans Excel en utilisant Aspose.Cells for C++. Notre guide complet vous montrera comment appliquer des filtres aux graphiques, personnaliser les éléments du graphique, et utiliser les outils d analyse de données pour de meilleures insights et une prise de décision éclairée.
keywords: Aspose.Cells for C++, Filtrer des graphiques dans Excel, Analyse de données, Prise de décisions, Visualisation.
type: docs
weight: 2210
url: /fr/cpp/filtering-charts-in-excel/
---


## **1. Filtrer les séries pour afficher un graphique**

### **Étapes pour filtrer les séries d'un graphique dans Excel**
Dans Excel, nous pouvons filtrer des séries spécifiques dans un graphique, ce qui empêche ces séries filtrées d'être affichées dans le graphique. Le graphique original est montré dans **Figure 1**. Cependant, lorsque nous filtrons **Testseries2** et **Testseries4**, le graphique apparaîtra comme dans **Figure 2**.

Dans Aspose.Cells, nous pouvons effectuer une opération similaire. Pour un fichier [exemple](seriesFiltered.xlsx) comme celui-ci, si nous voulons filtrer **Testseries2** et **Testseries4**, nous pouvons exécuter le code suivant. De plus, nous maintiendrons deux listes : une ([GetNSeries()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getnseries/)) pour stocker toutes les séries sélectionnées et une autre ([GetFilteredNSeries](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getfilterednseries/)) pour stocker les séries filtrées.

Veuillez **noter** qu'en code, lorsque nous définissons **chart->GetNSeries()->Get(0)->SetIsFiltered(true);**, la première série dans [GetNSeries()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getnseries/) sera supprimée et placée à la position appropriée dans [GetFilteredNSeries](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getfilterednseries/). Ensuite, le [NSeries[1]] précédent deviendra le nouvel élément en premier dans la liste, et toutes les séries suivantes décaleront vers l'avant de une position. Cela signifie que si nous exécutons alors **chart->GetNSeries()->Get(1)->SetIsFiltered(true);**, nous supprimons effectivement la troisième série d'origine. Cela peut parfois prêter à confusion, donc nous recommandons de suivre l'opération dans le code, qui supprime les séries du fin au début.

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **Code d'exemple**
Le code d'exemple suivant charge le [fichier Excel d'exemple](seriesFiltered.xlsx).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of existing Workbook
    Workbook workbook(u"seriesFiltered.xlsx");

    // Get filtered series list
    SeriesCollection nSeriesFiltered = workbook.GetWorksheets().Get(0).GetCharts().Get(u"Chart 1").GetFilteredNSeries();

    // Get selected series list
    SeriesCollection nSeries = workbook.GetWorksheets().Get(0).GetCharts().Get(u"Chart 1").GetNSeries();

    // Should be 0
    std::cout << "Filtered Series count: " << nSeriesFiltered.GetCount() << std::endl;

    // Should be 6
    std::cout << "Visible Series count: " << nSeries.GetCount() << std::endl;

    // Process from the end to the beginning
    nSeries.Get(1).SetIsFiltered(true);
    nSeries.Get(0).SetIsFiltered(true);

    // Should be 2
    std::cout << "Filtered Series count: " << nSeriesFiltered.GetCount() << std::endl;

    // Should be 4
    std::cout << "Visible Series count: " << nSeries.GetCount() << std::endl;

    // Save the workbook
    workbook.Save(u"seriesFiltered-out.xlsx");

    // Reload the workbook
    workbook = Workbook(u"seriesFiltered-out.xlsx");

    // Should be 2
    std::cout << "Filtered Series count: " << nSeriesFiltered.GetCount() << std::endl;

    // Should be 4
    std::cout << "Visible Series count: " << nSeries.GetCount() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **2. Filtrer les données et laisser le changement de graphique**

Filtrer vos données est une excellente façon de gérer les filtres de graphiques avec beaucoup de données. Lorsque vous filtrez les données, le graphique changera. Un problème que nous devrons résoudre est de faire en sorte que le graphique reste à l'écran. Lors du filtrage, des lignes masquées apparaissent, et parfois, le graphique sera dans ces lignes masquées.

![todo:image_alt_text](Figure3.png)

### **Étapes pour utiliser les filtres de données pour changer le graphique dans Excel**

1. Cliquez à l'intérieur de la plage de vos données.
2. Cliquez sur l'onglet **Données**, et activez les filtres en cliquant sur Filtres. Votre ligne d'en-tête aura des flèches déroulantes.
3. Créez un graphique en allant sur l'onglet **Insertion** et en sélectionnant un graphique à colonnes.
4. Filtrer maintenant vos données en utilisant les flèches déroulantes dans les données. N'utilisez pas les filtres de graphique.

### **Code d'exemple**
Le code d'exemple suivant montre la même fonctionnalité en utilisant Aspose.Cells.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Get the First sheet.
    Worksheet sheet = workbook.GetWorksheets().Get(u"Sheet1");

    // Add data into details cells.
    sheet.GetCells().Get(0, 0).PutValue(u"Fruits Name");
    sheet.GetCells().Get(0, 1).PutValue(u"Fruits Price");
    sheet.GetCells().Get(1, 0).PutValue(u"Apples");
    sheet.GetCells().Get(2, 0).PutValue(u"Bananas");
    sheet.GetCells().Get(3, 0).PutValue(u"Grapes");
    sheet.GetCells().Get(4, 0).PutValue(u"Oranges");
    sheet.GetCells().Get(1, 1).PutValue(5);
    sheet.GetCells().Get(2, 1).PutValue(2);
    sheet.GetCells().Get(3, 1).PutValue(1);
    sheet.GetCells().Get(4, 1).PutValue(4);

    // Add a chart to the worksheet
    int chartIndex = sheet.GetCharts().Add(ChartType::Column, 7, 7, 15, 15);

    // Access the instance of the newly added chart
    Chart chart = sheet.GetCharts().Get(chartIndex);

    // Set data range
    chart.SetChartDataRange(u"A1:B5", true);

    // Set AutoFilter range
    sheet.GetAutoFilter().SetRange(u"A1:B5");

    // Add filters for a filter column.
    sheet.GetAutoFilter().AddFilter(0, u"Bananas");
    sheet.GetAutoFilter().AddFilter(0, u"Oranges");

    // Apply the filters
    sheet.GetAutoFilter().Refresh();

    // Save the chart as an image
    chart.ToImage(u"Autofilter.png");

    // Save the workbook
    workbook.Save(u"Autofilter.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **3. Filtrer les données en utilisant un tableau et laisser le changement du graphique**

Utiliser un tableau est similaire à la Méthode 2, en utilisant une plage, mais vous avez des avantages avec les tableaux par rapport aux plages. Lorsque vous modifiez votre plage en un tableau et ajoutez des données, le graphique se met à jour automatiquement. Avec une plage, vous devrez modifier la source de données.

### **Format en tableau dans Excel**

Cliquez à l'intérieur de vos données et utilisez **CTRL + T** ou utilisez l'onglet Accueil, **Format en Tableau**

![todo:image_alt_text](Figure4.png)

### **Code d'exemple**
Le code d'exemple suivant charge le [fichier Excel d’exemple](TableFilters.xlsx) et montre la même fonctionnalité en utilisant Aspose.Cells.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Tables;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook
    Workbook workbook(u"TableFilters.xlsx");

    // Access first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Access the instance of the newly added chart
    int chartIndex = sheet.GetCharts().Add(ChartType::Column, 7, 7, 15, 15);
    Chart chart = sheet.GetCharts().Get(chartIndex);

    // Set data range
    chart.SetChartDataRange(u"A1:B7", true);

    // Convert the chart to image
    chart.ToImage(u"TableFilters.before.png");

    // Add a new List Object to the worksheet
    ListObject listObject = sheet.GetListObjects().Get(sheet.GetListObjects().Add(u"A1", u"B7", true));

    // Add default style to the table
    listObject.SetTableStyleType(TableStyleType::TableStyleMedium10);

    // Show Total
    listObject.SetShowTotals(false);

    // Add filters for a filter column
    listObject.GetAutoFilter().AddFilter(0, u"James");

    // Apply the filters
    listObject.GetAutoFilter().Refresh();

    // After adding new value the chart will change
    listObject.PutCellValue(7, 0, Object(u"Me"));
    listObject.PutCellValue(7, 1, Object(1000));

    // Check the changed images
    chart.ToImage(u"TableFilters.after.png");

    // Saving the Excel file
    workbook.Save(u"TableFilter.out.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
