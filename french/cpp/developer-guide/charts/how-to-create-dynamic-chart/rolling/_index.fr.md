---
title: Comment créer un graphique roulant dynamique avec C++
linktitle: Comment créer un graphique dynamique roulant
description: Apprenez à créer un graphique roulant dynamique en utilisant Aspose.Cells for C++. Notre guide vous montrera comment implémenter des transitions de données fluides et des moyennes mobiles dans votre graphique pour une visualisation continue et mise à jour.
keywords: Aspose.Cells for C++, graphique roulant dynamique, transitions de données, moyennes mobiles fluides, affichage continu, mise à jour de la visualisation.
type: docs
weight: 74
url: /fr/cpp/create-dynamic-rolling-chart/
---

## **Scénarios d'utilisation possibles**
Un graphique dynamique roulant se réfère à une représentation graphique qui affiche des points de données constamment en mouvement et se met à jour au fil du temps. Il s'agit d'un type de graphique qui se met continuellement à jour, présentant une fenêtre roulante des points de données les plus récents tout en éliminant les anciens points de données au fur et à mesure que de nouveaux arrivent.

Les graphiques dynamiques roulants sont couramment utilisés pour visualiser les tendances et les motifs dans les données en temps réel ou en continu. Ils sont particulièrement utiles dans des scénarios où les aspects temporels et les changements au fil du temps sont critiques, comme l'analyse du marché boursier, la surveillance météorologique ou le suivi des performances en direct.

Ces graphiques utilisent généralement des mécanismes d'animation ou de défilement automatique pour garantir que les informations les plus récentes sont toujours présentées. La longueur de la fenêtre roulante peut être personnalisée pour afficher une période de temps spécifique, comme la dernière heure, le jour ou la semaine.

En résumé, un graphique dynamique roulant est une représentation graphique continuellement mise à jour qui affiche les derniers points de données tout en éliminant les anciens, permettant aux utilisateurs d'observer les tendances et les motifs en temps réel.

## **Utilisez Aspose Cells pour créer un graphique dynamique roulant**
Dans les prochains paragraphes, nous vous montrerons comment créer un graphique dynamique roulant en utilisant Aspose.Cells. Nous vous montrerons le code de l'exemple, ainsi que le fichier Excel créé avec ce code.

## **Code d'exemple**
Le code d'exemple suivant générera le [fichier Dynamic Rolling Chart](DynamicRollingChart.xlsx).

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Your local test path
    U16String LocalPath = u"";

    // Create a new workbook and access the first worksheet.
    Workbook workbook;
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    // Populate the data for the chart. Add values to cells and set series names.
    sheet.GetCells().Get(u"A1").PutValue(u"Month");
    sheet.GetCells().Get(u"A2").PutValue(1);
    sheet.GetCells().Get(u"A3").PutValue(2);
    sheet.GetCells().Get(u"A4").PutValue(3);
    sheet.GetCells().Get(u"A5").PutValue(4);
    sheet.GetCells().Get(u"A6").PutValue(5);
    sheet.GetCells().Get(u"A7").PutValue(6);
    sheet.GetCells().Get(u"A8").PutValue(7);

    sheet.GetCells().Get(u"B1").PutValue(u"Sales");
    sheet.GetCells().Get(u"B2").PutValue(50);
    sheet.GetCells().Get(u"B3").PutValue(45);
    sheet.GetCells().Get(u"B4").PutValue(55);
    sheet.GetCells().Get(u"B5").PutValue(60);
    sheet.GetCells().Get(u"B6").PutValue(55);
    sheet.GetCells().Get(u"B7").PutValue(65);
    sheet.GetCells().Get(u"B8").PutValue(70);

    // Set the dynamic range for the chart's data source.
    int index = sheets.GetNames().Add(u"Sheet1!ChtData");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$B$1,COUNT(Sheet1!$B:$B),0,-5,1)");

    // Set the dynamic range for the chart's data labels.
    index = sheets.GetNames().Add(u"Sheet1!ChtLabels");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)");

    // Create a chart object and set its data source.
    int chartIndex = sheet.GetCharts().Add(ChartType::Line, 10, 3, 25, 10);
    Chart chart = sheet.GetCharts().Get(chartIndex);
    chart.GetNSeries().Add(u"Sales", true);
    chart.GetNSeries().Get(0).SetValues(u"Sheet1!ChtData");
    chart.GetNSeries().Get(0).SetXValues(u"Sheet1!ChtLabels");

    // Save the workbook as an Excel file.
    workbook.Save(LocalPath + u"DynamicRollingChart.xlsx");

    std::cout << "Dynamic rolling chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Remarques**
Dans le fichier généré, vous pouvez continuer à ajouter des données dans les colonnes A et B, tandis que le graphique comptera dynamiquement les 5 ensembles de données les plus récents. Cela est fait en utilisant la formule "OFFSET" dans le code d'exemple :

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

Vous pouvez essayer de modifier le nombre "-5" en "-10" dans la formule, et le graphique dynamique comptera les 10 derniers ensembles de données. Nous avons maintenant créé avec succès un graphique roulant dynamique en utilisant Aspose.Cells.
