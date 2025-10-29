---
title: Axe de date avec C++
linktitle: Axe de date
description: Apprenez comment gérer l’axe de date dans Aspose.Cells for C++. Notre guide vous aidera à comprendre comment travailler avec différents formats de date, échelles de temps et fréquences d’étiquettes de graduation.
keywords: Aspose.Cells for C++, axe de date, gérer, formats de date, échelles de temps, fréquences d’étiquettes de graduation.
type: docs
weight: 200
url: /fr/cpp/date-axis/
---

## **Scénarios d'utilisation possibles**
Lorsque vous créez un graphique à partir des données de la feuille de calcul utilisant des dates, et que ces dates sont tracées le long de l’axe horizontal (catégorie) dans le graphique, Aspose.Cells modifie automatiquement l’axe de catégorie en un axe de date (échelle de temps).
Un axe de date affiche les dates dans l'ordre chronologique à des intervalles ou unités de base spécifiques, tels que le nombre de jours, de mois ou d'années, même si les dates sur la feuille de calcul ne sont pas dans l'ordre séquentiel ou dans les mêmes unités de base.
Par défaut, Aspose.Cells détermine les unités de base pour l’axe de date en fonction de la plus petite différence entre deux dates dans les données de la feuille de calcul. Par exemple, si vous avez des données sur les prix des actions où la plus petite différence entre les dates est de sept jours, Aspose.Cells définit l’unité de base sur les jours, mais vous pouvez changer l’unité de base en mois ou en année si vous souhaitez voir la performance de l’action sur une période plus longue.

## **Gérez l'axe de date comme Microsoft Excel**
Veuillez voir le code d’exemple ci-dessous qui crée un nouveau fichier Excel et place les valeurs du graphique dans la première feuille. 
Ensuite, nous ajoutons un graphique et définissons le type du [**Axis**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/) 
à [**TimeScale**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/categorytype/) puis nous définissons les unités de base en jours.

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

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add the sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(u"Date");

    // 14 means datetime format
    Style style = worksheet.GetCells().GetStyle();
    style.SetNumber(14);

    // Put values to cells for creating chart
    worksheet.GetCells().Get(u"A2").SetStyle(style);
    worksheet.GetCells().Get(u"A2").PutValue(Date{2022, 6, 26, 0, 0, 0, 0});

    worksheet.GetCells().Get(u"A3").SetStyle(style);
    worksheet.GetCells().Get(u"A3").PutValue(Date{2022, 5, 22, 0, 0, 0, 0});

    worksheet.GetCells().Get(u"A4").SetStyle(style);
    worksheet.GetCells().Get(u"A4").PutValue(Date{2022, 8, 3, 0, 0, 0, 0});

    worksheet.GetCells().Get(u"B1").PutValue(u"Price");
    worksheet.GetCells().Get(u"B2").PutValue(40);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(60);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 9, 6, 21, 13);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.SetChartDataRange(u"A1:B4", true);

    // Set the Axis type to Date time
    chart.GetCategoryAxis().SetCategoryType(CategoryType::TimeScale);

    // Set the base unit for CategoryAxis to days
    chart.GetCategoryAxis().SetBaseUnitScale(TimeUnit::Days);

    // Set the direction for the axis text to be vertical
    chart.GetCategoryAxis().GetTickLabels().SetDirectionType(ChartTextDirectionType::Vertical);

    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Set max value of Y axis
    chart.GetValueAxis().SetMaxValue(70);

    // Set major unit
    chart.GetValueAxis().SetMajorUnit(10);

    // Save the file
    workbook.Save(u"DateAxis.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
