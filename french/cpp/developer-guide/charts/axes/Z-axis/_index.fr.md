---
title: Axe Z avec C++
linktitle: Axe Z
description: Apprenez à travailler avec l axe Z dans Aspose.Cells for C++. Notre guide vous aidera à comprendre comment configurer et personnaliser l axe Z, y compris sa gamme et ses étiquettes, pour améliorer vos graphiques.
keywords: Aspose.Cells for C++, axe Z, création de graphiques, configuration, personnalisation, échelle, étiquettes.
type: docs
weight: 210
url: /fr/cpp/z-axis/
---

## **Scénarios d'utilisation possibles**
Pour certains graphiques 3D tels que les colonnes en 3D, les cônes en 3D ou les pyramides en 3D qui ont un axe de profondeur (série), également appelé axe Z, que vous pouvez modifier. Vous pouvez spécifier l'intervalle entre les marques de graduation, les étiquettes des axes et d'autres opérations.

## **Gérer les axes primaire et secondaire comme Microsoft Excel**
Veuillez voir le code d'exemple suivant qui crée un nouveau fichier Excel et met les valeurs du graphique dans la première feuille. Ensuite, nous ajoutons un graphique et fixons le type de graphique à Colonne3D, ainsi vous pouvez également voir l'axe Z appelé aussi Axe de profondeur. 

![todo:image_alt_text](excel.png)

## **Code d'exemple**
```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put values to cells for creating chart
    worksheet.GetCells().Get(u"A1").PutValue(u"A");
    worksheet.GetCells().Get(u"B1").PutValue(u"B");
    worksheet.GetCells().Get(u"C1").PutValue(u"C");
    worksheet.GetCells().Get(u"A2").PutValue(2);
    worksheet.GetCells().Get(u"A3").PutValue(1);
    worksheet.GetCells().Get(u"B2").PutValue(2);
    worksheet.GetCells().Get(u"B3").PutValue(3);
    worksheet.GetCells().Get(u"C2").PutValue(2);
    worksheet.GetCells().Get(u"C3").PutValue(3);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column3D, 9, 6, 25, 16);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Calculate the chart
    chart.Calculate();

    // Add SeriesCollection (chart data source) to the chart ranging from "A2" cell to "C3"
    chart.SetChartDataRange(u"A2:C3", true);

    // Hide the CategoryAxis axis
    chart.GetCategoryAxis().SetIsVisible(false);

    // Hide the ValueAxis axis
    chart.GetValueAxis().SetIsVisible(false);

    // Save the file
    workbook.Save(u"ZAxis.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
