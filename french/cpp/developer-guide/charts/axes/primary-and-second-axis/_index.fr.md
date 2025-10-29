---
title: Axes principaux et secondaires avec C++
linktitle: Axe Principal et Secondaire
description: Apprenez à comprendre et à travailler avec les axes principaux et secondaires dans Aspose.Cells for C++. Notre guide vous aidera à comprendre les différences entre axes principaux et secondaires, et comment les configurer et les utiliser efficacement dans vos graphiques.
keywords: Aspose.Cells for C++, axes primaires, axes secondaires, compréhension, différences, configuration, utilisation.
type: docs
weight: 190
url: /fr/cpp/primary-and-second-axis/
---

## **Scénarios d'utilisation possibles**
Lorsque les nombres dans un graphique varient largement d'une série de données à une autre, ou lorsque vous avez des types de données mélangés (prix et volume), tracez une ou plusieurs séries de données sur un axe vertical (valeur) secondaire. L'échelle de l'axe vertical secondaire affiche les valeurs des séries de données associées. Un axe secondaire fonctionne bien dans un graphique qui montre une combinaison de graphiques en colonnes et en lignes.

## **Gérer les axes primaire et secondaire comme Microsoft Excel**
Veuillez voir le code d’exemple ci-dessous qui crée un nouveau fichier Excel et place les valeurs du graphique dans la première feuille. 
Ensuite, nous ajoutons un graphique et montrons le deuxième axe.

![todo:image_alt_text](excel.png)

## **Code d'exemple**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put the sample values used in a chart
    worksheet.GetCells().Get(u"A1").PutValue(u"Region");
    worksheet.GetCells().Get(u"A2").PutValue(u"Peking");
    worksheet.GetCells().Get(u"A3").PutValue(u"New York");
    worksheet.GetCells().Get(u"A4").PutValue(u"Paris");
    worksheet.GetCells().Get(u"B1").PutValue(u"Sales Volume");
    worksheet.GetCells().Get(u"C1").PutValue(u"Growth Rate");
    worksheet.GetCells().Get(u"B2").PutValue(100);
    worksheet.GetCells().Get(u"B3").PutValue(80);
    worksheet.GetCells().Get(u"B4").PutValue(140);
    worksheet.GetCells().Get(u"C2").PutValue(0.7);
    worksheet.GetCells().Get(u"C3").PutValue(0.8);
    worksheet.GetCells().Get(u"C4").PutValue(1.0);

    // Create a Scatter chart
    int pieIdx = worksheet.GetCharts().Add(ChartType::Scatter, 6, 6, 15, 11);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Add Series
    chart.GetNSeries().Add(u"B2:C4", true);

    // Set the category data
    chart.GetNSeries().SetCategoryData(u"=Sheet1!$A$2:$A$4");

    // Set the Second-Axis
    chart.GetNSeries().Get(1).SetPlotOnSecondAxis(true);

    // Show the Second-Axis
    chart.GetSecondValueAxis().SetIsVisible(true);

    // Set the second series ChartType to line
    chart.GetNSeries().Get(1).SetType(ChartType::Line);

    // Set the series name
    chart.GetNSeries().Get(0).SetName(u"Sales Volume");
    chart.GetNSeries().Get(1).SetName(u"Growth Rate");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the file
    workbook.Save(u"PrimaryandSecondaryAxis.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
