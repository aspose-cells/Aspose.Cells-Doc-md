---
title: Personnalisation des graphiques avec C++
linktitle: Personnalisation des graphiques
description: Apprenez comment personnaliser des graphiques dans Aspose.Cells for C++. Notre guide vous montrera comment modifier la mise en page du graphique, ajouter et formater des séries de données, ajuster les axes, et appliquer diverses options de mise en forme pour améliorer l apparence et la convivialité de vos graphiques.
keywords: Aspose.Cells for C++, graphiques, personnalisation, mises en page, séries de données, axes, mise en forme, apparence, convivialité.
type: docs
weight: 40
url: /fr/cpp/customizing-charts/
---

{{% alert color="primary" %}}

## **Création de graphiques personnalisés**

Jusqu'à présent, lorsque nous avons discuté de graphiques, nous avons examiné des graphiques standard avec leurs paramètres de mise en forme standards. Nous définissons simplement la source de données, réglons quelques propriétés, et le graphique est créé avec ses paramètres de format par défaut. Mais les API Aspose.Cells supportent également la création de graphiques personnalisés permettant aux développeurs de créer des graphiques avec leurs propres paramètres de format.

Les développeurs peuvent créer des graphiques personnalisés à l'exécution à l'aide d'Aspose.Cells.

Un graphique est composé d'une série de données. Chaque série de données dans Aspose.Cells est représentée par un objet [**Series**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/) tandis que l'objet [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/) sert de collection d'objets [**Series**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/). Lors de la création d'un graphique personnalisé, les développeurs ont la liberté d'utiliser différents types de graphiques pour différentes séries de données (collectées dans l'objet [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/)).

Le code d'exemple ci-dessous montre comment créer des graphiques personnalisés. Dans cet exemple, nous allons utiliser un graphique en colonnes pour la première série de données et un graphique linéaire pour la deuxième série. Le résultat est que nous ajoutons un graphique en colonnes, combiné à un graphique linéaire, à la feuille de calcul.

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

    // Obtain the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"A4").PutValue(110);
    worksheet.GetCells().Get(u"B1").PutValue(260);
    worksheet.GetCells().Get(u"B2").PutValue(12);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(100);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add NSeries (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.GetNSeries().Add(u"A1:B4", true);

    // Set the chart type of 2nd NSeries to display as line chart
    chart.GetNSeries().Get(1).SetType(ChartType::Line);

    // Save the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Actuellement, Aspose.Cells ne supporte que les graphiques personnalisés combinant pie, line, column, et column stack, mais d'autres graphiques seront supportés dans les futures versions.

{{% /alert %}}
