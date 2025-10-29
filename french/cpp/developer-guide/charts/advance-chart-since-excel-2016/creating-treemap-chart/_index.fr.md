---
title: Comment créer un graphique TreeMap avec C++
description: Apprenez à créer un graphique Treemap dans Aspose.Cells for C++. Notre guide vous aidera à comprendre les différentes propriétés et options de mise en forme disponibles pour les graphiques Treemap, y compris les couleurs, les étiquettes et la représentation des données.
keywords: Aspose.Cells for C++, graphique en arbre, créer, propriétés, mise en forme, couleurs, étiquettes, représentation des données, graphique circulaire, graphique hiérarchique.
type: docs
weight: 161
url: /fr/cpp/creating-treemap-chart/
---

## **Scénarios d'utilisation possibles**
Un graphique à carte de chaleur fournit une vue hiérarchique de vos données et facilite la détection de schémas, tels que les articles les plus vendus d'un magasin. Les branches de l'arbre sont représentées par des rectangles et chaque sous-branche est présentée sous la forme d'un rectangle plus petit. Le graphique à carte de chaleur affiche les catégories par couleur et proximité et peut facilement montrer beaucoup de données qui seraient difficiles avec d'autres types de graphiques.

![todo:image_alt_text](sample.png)
## **Diagramme TreeMap**
Après avoir exécuté le code ci-dessous, vous verrez le diagramme TreeMap comme indiqué ci-dessous.

![todo:image_alt_text](result.png)
## **Code d'exemple**
Le code d'exemple suivant charge le [fichier Excel d'exemple](treemap.xlsx) et génère le [fichier Excel de sortie](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"treemap.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a Treemap chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::Treemap, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"TreeMap Chart");

    // Add series data range (D2:F13, actually)
    chart.GetNSeries().Add(u"D2:F13", true);

    // Set category data (A2:C13 is incorrect)
    chart.GetNSeries().SetCategoryData(u"A2:C13");

    // Show the DataLabels with category names
    chart.GetNSeries().Get(0).GetDataLabels().SetShowCategoryName(true);

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
