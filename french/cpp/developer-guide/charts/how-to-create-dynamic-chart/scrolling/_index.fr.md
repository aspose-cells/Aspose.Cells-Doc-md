---
title: Comment créer un graphique défilant dynamique avec C++
linktitle: Créer un graphique défilant dynamique
description: Apprenez comment créer un graphique défilant dynamique en utilisant Aspose.Cells for C++. Notre guide étape par étape vous démontrera comment mettre en œuvre des transitions de données fluides et un défilement automatique dans votre graphique pour un affichage continu et mis à jour.
keywords: Aspose.Cells for C++, Graphique défilant dynamique, Transitions de données, Défilement fluide, Affichage continu, Mise à jour de la visualisation.
type: docs
weight: 75
url: /fr/cpp/create-dynamic-scrolling-chart/
---

## **Scénarios d'utilisation possibles**
Un graphique dynamique déroulant est un type de représentation graphique utilisé pour afficher des données qui changent avec le temps. Il est conçu pour fournir une vue en temps réel des données, permettant aux utilisateurs de suivre les mises à jour et les tendances continues. Le graphique se met à jour en continu lorsque de nouvelles données sont ajoutées, et il défile automatiquement pour afficher les informations les plus récentes.

Les graphiques dynamiques déroulants sont couramment utilisés dans diverses industries, telles que la finance, l'analyse du marché boursier, le suivi météorologique et l'analyse des médias sociaux. Ils permettent aux utilisateurs de visualiser et d'analyser les motifs de données et de prendre des décisions éclairées en fonction des informations en temps réel.

Ces graphiques sont généralement interactifs, permettant à l'utilisateur de zoomer, de faire défiler les données historiques et d'ajuster les intervalles de temps. Ils prennent souvent en charge plusieurs séries de données, offrant une vue complète des différentes mesures et de leurs corrélations.

 Globalement, les graphiques dynamiques déroulants sont des outils précieux pour surveiller et analyser les données en séries chronologiques, faciliter la prise de décisions en temps réel et améliorer les capacités de visualisation des données.

## **Utilisez Aspose Cells pour créer un graphique défilant dynamique**
Dans les paragraphes suivants, nous vous montrerons comment créer un graphique défilant dynamique avec Aspose.Cells. Nous vous présenterons le code pour l'exemple, ainsi que le fichier Excel créé avec ce code.

## **Code d'exemple**
Le code d'exemple suivant générera le [Fichier de graphique dynamique déroulant](DynamicScrollingChart.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String localPath(u"");

    Workbook workbook;
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    sheet.GetCells().Get(u"A1").PutValue(u"Day");
    sheet.GetCells().Get(u"B1").PutValue(u"Sales");

    int allDays = 30;
    int showDays = 10;
    int currentDay = 1;

    Cells cells = sheet.GetCells();
    for (int i = 0; i < allDays; i++)
    {
        int row = i + 1;
        cells.Get(row, 0).PutValue(i + 1);
        cells.Get(row, 1).PutValue(50 * (i % 2) + 20 * (i % 3) + 10 * (i / 3));
    }

    sheet.GetCells().Get(u"G19").PutValue(u"Start Day");
    sheet.GetCells().Get(u"G20").PutValue(currentDay);
    sheet.GetCells().Get(u"H19").PutValue(u"Show Days");
    sheet.GetCells().Get(u"H20").PutValue(showDays);

    int index = sheets.GetNames().Add(u"Sheet1!ChtScrollData");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

    index = sheets.GetNames().Add(u"Sheet1!ChtScrollLabels");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$A$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

    ScrollBar bar = sheet.GetShapes().AddScrollBar(2, 0, 3, 0, 200, 30);
    bar.SetMin(0);
    bar.SetMax(allDays - showDays);
    bar.SetCurrentValue(currentDay);
    bar.SetLinkedCell(u"$G$20");

    int chartIndex = sheet.GetCharts().Add(ChartType::Line, 2, 4, 15, 10);
    Chart chart = sheet.GetCharts().Get(chartIndex);
    chart.GetNSeries().Add(u"Sales", true);
    chart.GetNSeries().Get(0).SetValues(u"Sheet1!ChtScrollData");
    chart.GetNSeries().Get(0).SetXValues(u"Sheet1!ChtScrollLabels");

    workbook.Save(localPath + u"DynamicScrollingChart.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Remarques**
Dans le fichier généré, vous pouvez agir sur la barre de défilement, tandis que le graphique compte dynamiquement les 10 derniers ensembles de données. Cela est fait en utilisant la formule "OFFSET" dans le code d'exemple:

```
"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)"
```

Vous pouvez essayer de changer le nombre "10" en "15" dans la cellule "Feuille1!$H$20", et le graphique dynamique comptera les 15 derniers ensembles de données. Nous avons maintenant créé avec succès un graphique dynamique déroulant en utilisant Aspose.Cells.
