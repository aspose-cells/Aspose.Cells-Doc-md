---
title: Comment définir l axe de catégorie avec C++
linktitle: Comment définir l axe des catégories
description: Apprenez comment définir l axe de catégorie dans Aspose.Cells for C++. Notre guide vous aidera à comprendre comment définir la plage de l axe de catégorie, ajuster ses propriétés et formater ses étiquettes.
keywords: Aspose.Cells for C++, axe de catégorie, réglage, plage, propriétés, mise en forme.
type: docs
weight: 205
url: /fr/cpp/how-to-set-category-axis/
---

## **Scénarios d'utilisation possibles**
Après avoir créé un graphique dans une feuille de calcul, vous pouvez définir l'axe des catégories pour celui-ci. Dans cet article, nous vous montrerons comment définir l'axe des catégories pour un graphique Excel en utilisant Aspose.Cells avec un code d’exemple.

## **Les étapes dans le code d'exemple**

1. Créez un nouveau classeur.

2. Créez un nouveau graphique dans la première feuille de calcul.

3. Ajoutez quelques valeurs aux cellules de la première feuille de calcul.

4. Maintenant, vous pouvez définir l'axe de catégorie. Il existe deux méthodes : utiliser les données de cellule ou utiliser directement des chaînes, les deux sont illustrées dans l'exemple de code.

5. Définissez l'axe de valeur, enregistrez le classeur pour voir le résultat.

## **Code d'exemple**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    // Your local test path
    U16String path = u"";

    // Create a new workbook
    Workbook workbook;
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);
    worksheet.SetName(u"CHART");

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 8, 0, 20, 10);
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add some values to cells
    worksheet.GetCells().Get(u"A1").PutValue(u"Sales");
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"A4").PutValue(130);
    worksheet.GetCells().Get(u"A5").PutValue(160);
    worksheet.GetCells().Get(u"A6").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(u"Days");
    worksheet.GetCells().Get(u"B2").PutValue(1);
    worksheet.GetCells().Get(u"B3").PutValue(2);
    worksheet.GetCells().Get(u"B4").PutValue(3);
    worksheet.GetCells().Get(u"B5").PutValue(4);
    worksheet.GetCells().Get(u"B6").PutValue(5);

    // Some values in string
    U16String Sales = u"100,150,130,160,150";
    U16String Days = u"1,2,3,4,5";

    // Set Category Axis Data with string
    chart.GetNSeries().SetCategoryData(u"{" + Days + u"}");
    // Or you can set Category Axis Data with data in cells, try it!
    // chart.GetNSeries().SetCategoryData(u"B2:B6");

    // Add Series to the chart
    chart.GetNSeries().Add(u"Demand1", true);
    // Set value axis with string 
    chart.GetNSeries().Get(0).SetValues(u"{" + Sales + u"}");
    chart.GetNSeries().Add(u"Demand2", true);
    // Set value axis with data in cells
    chart.GetNSeries().Get(1).SetValues(u"A2:A6");

    // Set some Category Axis properties
    chart.GetCategoryAxis().GetTickLabels().SetRotationAngle(45);
    chart.GetCategoryAxis().GetTickLabels().GetFont().SetSize(8);
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Save the workbook to view the result file
    workbook.Save(path + u"Output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
