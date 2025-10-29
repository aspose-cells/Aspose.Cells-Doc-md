---
title: Comment créer un graphique dynamique avec liste déroulante avec C++
linktitle: Créer un graphique dynamique avec liste déroulante
description: Apprenez comment créer un graphique dynamique qui se met à jour en fonction de la sélection dans une liste déroulante en utilisant Aspose.Cells for C++. Notre guide étape par étape démontrera comment intégrer une liste déroulante dans votre graphique pour une visualisation des données flexible.
keywords: Aspose.Cells for C++, graphique dynamique, liste déroulante, visualisation de données, intégration, visualisation flexible.
type: docs
weight: 76
url: /fr/cpp/create-dynamic-chart-with-dropdownlist/
---

## **Scénarios d'utilisation possibles**
Un graphique dynamique avec liste déroulante dans Excel est un outil puissant qui permet aux utilisateurs de créer des graphiques interactifs qui peuvent se mettre à jour dynamiquement en fonction des données sélectionnées. Cette fonctionnalité est particulièrement utile dans les situations où il est nécessaire d'analyser de multiples ensembles de données ou de comparer divers scénarios.

Une application courante d'un graphique dynamique avec liste déroulante est l'analyse financière. Par exemple, une entreprise peut avoir plusieurs ensembles de données financières pour différentes années ou départements. En utilisant une liste déroulante, les utilisateurs peuvent sélectionner l'ensemble de données spécifique qu'ils souhaitent analyser, et le graphique se mettra automatiquement à jour pour afficher les informations correspondantes. Cela permet de comparer facilement et d'identifier les tendances ou schémas.

Une autre application se trouve dans les ventes et le marketing. Une entreprise peut avoir des données de vente pour différents produits ou régions. Avec un graphique dynamique avec liste déroulante, les utilisateurs peuvent choisir un produit ou une région spécifique dans la liste déroulante, et le graphique se mettra à jour dynamiquement pour afficher les performances de vente pour l'option sélectionnée. Cela aide à identifier les zones ou produits les plus performants et à prendre des décisions basées sur les données.

En résumé, un graphique dynamique avec liste déroulante dans Excel offre un moyen flexible et interactif de visualiser et d'analyser les données. Il est précieux dans les situations où il est nécessaire de comparer plusieurs ensembles de données ou d'explorer différents scénarios, ce qui en fait un outil polyvalent pour l'analyse financière, les ventes et le marketing, et de nombreuses autres applications.

## **Utiliser Aspose Cells pour créer un graphique dynamique avec liste déroulante**
Dans les paragraphes suivants, nous vous montrerons comment créer un graphique dynamique avec liste déroulante en utilisant Aspose.Cells. Nous vous fournirons le code pour l’exemple ainsi que le fichier Excel créé avec ce code.

## **Code d'exemple**
Le code d'exemple suivant générera le [fichier Dynamic Chart with Dropdownlist](DynamicChartWithDropdownlist.xlsx).

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook and access the first worksheet.
    Workbook workbook;
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    // Populate the data for the chart. Add values to cells and set series names.
    sheet.GetCells().Get(u"A3").PutValue(u"Tea");
    sheet.GetCells().Get(u"A4").PutValue(u"Coffee");
    sheet.GetCells().Get(u"A5").PutValue(u"Sugar");

    // In this example, we will add 12 months of data
    sheet.GetCells().Get(u"B2").PutValue(u"Jan");
    sheet.GetCells().Get(u"C2").PutValue(u"Feb");
    sheet.GetCells().Get(u"D2").PutValue(u"Mar");
    sheet.GetCells().Get(u"E2").PutValue(u"Apr");
    sheet.GetCells().Get(u"F2").PutValue(u"May");
    sheet.GetCells().Get(u"G2").PutValue(u"Jun");
    sheet.GetCells().Get(u"H2").PutValue(u"Jul");
    sheet.GetCells().Get(u"I2").PutValue(u"Aug");
    sheet.GetCells().Get(u"J2").PutValue(u"Sep");
    sheet.GetCells().Get(u"K2").PutValue(u"Oct");
    sheet.GetCells().Get(u"L2").PutValue(u"Nov");
    sheet.GetCells().Get(u"M2").PutValue(u"Dec");

    int allMonths = 12;
    int iCount = 3;
    for (int i = 0; i < iCount; i++)
    {
        for (int j = 0; j < allMonths; j++)
        {
            int _row = i + 2;
            int _column = j + 1;
            sheet.GetCells().Get(_row, _column).PutValue(50 * (i % 2) + 20 * (j % 3) + 10 * (i / 3) + 10);
        }
    }

    // This is the Dropdownlist for Dynamic Data
    CellArea ca = CellArea::CreateCellArea(9, 0, 9, 0);
    int _index = sheet.GetValidations().Add(ca);
    Validation _va = sheet.GetValidations().Get(_index);
    _va.SetType(ValidationType::List);
    _va.SetInCellDropDown(true);
    _va.SetFormula1(u"=$B$2:$M$2");

    sheet.GetCells().Get(u"A9").PutValue(u"Current Month");
    sheet.GetCells().Get(u"A10").PutValue(u"Jan");

    Style _style = sheet.GetCells().Get(u"A10").GetStyle();
    _style.GetFont().SetIsBold(true);
    _style.SetPattern(BackgroundType::Solid);
    _style.SetForegroundColor(Color::Yellow());
    sheet.GetCells().Get(u"A10").SetStyle(_style);

    // Set the dynamic range for the chart's data source.
    int index = sheets.GetNames().Add(u"Sheet1!ChtMonthData");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)");

    // Set the dynamic range for the chart's data labels.
    index = sheets.GetNames().Add(u"Sheet1!ChtXLabels");
    sheets.GetNames().Get(index).SetRefersTo(u"=Sheet1!$A$3:$A$5");

    // Create a chart object and set its data source.
    int chartIndex = sheet.GetCharts().Add(ChartType::Column, 8, 2, 20, 8);
    Chart chart = sheet.GetCharts().Get(chartIndex);
    chart.GetNSeries().Add(u"month", true);
    chart.GetNSeries().Get(0).SetName(u"=Sheet1!$A$10");
    chart.GetNSeries().Get(0).SetValues(u"Sheet1!ChtMonthData");
    chart.GetNSeries().Get(0).SetXValues(u"Sheet1!ChtXLabels");

    // Save the workbook as an Excel file.
    workbook.Save(u"DynamicChartWithDropdownlist.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Remarques**
Dans le fichier généré, le graphique comptera dynamiquement les données pour le mois sélectionné. Cela est fait en utilisant la formule "OFFSET" dans le code d'exemple :

```cpp
"=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)"
```

Vous pouvez essayer de changer la valeur de la liste déroulante dans la cellule "Sheet1!$A$10", et vous verrez le changement dynamique du graphique. Nous avons maintenant créé avec succès un graphique dynamique avec liste déroulante en utilisant Aspose.Cells.
{{< app/cells/assistant language="cpp" >}}
