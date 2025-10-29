---
title: Comment créer un graphique en cascade avec C++
linktitle: Comment créer un diagramme en cascade
type: docs
weight: 160
url: /fr/cpp/creating-waterfall-chart/
description: Créez des graphiques en cascade dans Excel avec C++ et l’API Aspose.Cells for C++.
keywords: C++ créer un graphique en cascade dans Excel, C++ créer un graphique en cascade dans Excel, création d’un graphique en cascade dans Excel avec C++, créer un graphique en cascade dans Excel avec C++, créer un graphique en cascade dans Excel C++, créer un graphique en cascade dans Excel de manière programmatique, comment créer un graphique en cascade dans Excel avec C++
---

{{% alert color="primary" %}}

Un diagramme en cascade est un type spécial de diagramme qui est normalement utilisé pour démontrer comment la position de départ augmente ou diminue. Microsoft Excel propose de nombreux types de graphiques prédéfinis, y compris les colonnes, les lignes, les secteurs, les barres, le radar, etc. mais le diagramme en cascade va au-delà des graphiques de base et peut être créé à l'aide des types de graphiques existants avec peu ou beaucoup de personnalisation.

{{% /alert %}}

Les API Aspose.Cells permettent de créer un diagramme en cascade à l'aide du diagramme linéaire. L'API permet également de personnaliser l'apparence du graphique pour lui donner la forme de la cascade en définissant les propriétés [**Series.GetUpBars()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/getupbars/) & [**Series.GetDownBars()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/getdownbars/).

Le code ci-dessous montre comment utiliser l’API Aspose.Cells for C++ pour créer un graphique en cascade depuis zéro.

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

    // Create an instance of Workbook
    Workbook workbook;

    // Retrieve the first Worksheet in Workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Retrieve the Cells of the first Worksheet
    Cells cells = worksheet.GetCells();

    // Input some data which chart will use as source
    cells.Get(U16String(u"A1")).PutValue(U16String(u"Previous Year"));
    cells.Get(U16String(u"A2")).PutValue(U16String(u"January"));
    cells.Get(U16String(u"A3")).PutValue(U16String(u"March"));
    cells.Get(U16String(u"A4")).PutValue(U16String(u"August"));
    cells.Get(U16String(u"A5")).PutValue(U16String(u"October"));
    cells.Get(U16String(u"A6")).PutValue(U16String(u"Current Year"));

    cells.Get(U16String(u"B1")).PutValue(8.5);
    cells.Get(U16String(u"B2")).PutValue(1.5);
    cells.Get(U16String(u"B3")).PutValue(7.5);
    cells.Get(U16String(u"B4")).PutValue(7.5);
    cells.Get(U16String(u"B5")).PutValue(8.5);
    cells.Get(U16String(u"B6")).PutValue(3.5);

    cells.Get(U16String(u"C1")).PutValue(1.5);
    cells.Get(U16String(u"C2")).PutValue(4.5);
    cells.Get(U16String(u"C3")).PutValue(3.5);
    cells.Get(U16String(u"C4")).PutValue(9.5);
    cells.Get(U16String(u"C5")).PutValue(7.5);
    cells.Get(U16String(u"C6")).PutValue(9.5);

    // Add a Chart of type Waterfall in same worksheet as of data
    int idx = worksheet.GetCharts().Add(ChartType::Waterfall, 4, 4, 25, 13);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(idx);

    // Add Series
    chart.GetNSeries().Add(U16String(u"$B$1:$C$6"), true);

    // Add Category Data
    chart.GetNSeries().SetCategoryData(U16String(u"$A$1:$A$6"));

    // Series has Up Down Bars
    chart.GetNSeries().Get(0).SetHasUpDownBars(true);

    // Set the colors of Up and Down Bars
    chart.GetNSeries().Get(0).GetUpBars().GetArea().SetForegroundColor(Color::Green());
    chart.GetNSeries().Get(0).GetDownBars().GetArea().SetForegroundColor(Color::Red());

    // Make both Series Lines invisible
    chart.GetNSeries().Get(0).GetBorder().SetIsVisible(false);
    chart.GetNSeries().Get(1).GetBorder().SetIsVisible(false);

    // Set the Plot Area Formatting Automatic
    chart.GetPlotArea().GetArea().SetFormatting(FormattingType::Automatic);

    // Delete the Legend
    chart.GetLegend().GetLegendEntries().Get(0).SetIsDeleted(true);
    chart.GetLegend().GetLegendEntries().Get(1).SetIsDeleted(true);

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```

## Articles Connexes

- [Création de graphiques](/cells/fr/cpp/creating-charts/)
- [Personnalisation des graphiques](/cells/fr/cpp/customizing-charts/)
{{< app/cells/assistant language="cpp" >}}
