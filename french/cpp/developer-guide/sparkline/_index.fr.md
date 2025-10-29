---
title: Insérer une Sparkline avec C++
linktitle: Minigraphiques
type: docs
weight: 160
url: /fr/cpp/creating-sparklines/
description: Créer une Sparkline pour Excel en utilisant Aspose.Cells avec C++.
---

## **Insérer un sparkline**
{{% alert color="primary" %}} 

Une Sparkline est un petit graphique dans une cellule de feuille de calcul qui fournit une représentation visuelle des données. Utilisez les sparklines pour montrer les tendances dans une série de valeurs, telles que des augmentations ou diminutions saisonnières, des cycles économiques, ou pour mettre en évidence les valeurs maximales et minimales. Positionnez une Sparkline près de ses données pour un impact maximal. Il existe trois types de Sparkline : Ligne, Colonne, et Empilé.

{{% /alert %}} 

Il est simple de créer un sparkline avec Aspose.Cells en utilisant les codes d'exemple suivants :

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook book;
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Set values in cells
    sheet.GetCells().Get(u"A1").PutValue(5);
    sheet.GetCells().Get(u"B1").PutValue(2);
    sheet.GetCells().Get(u"C1").PutValue(1);
    sheet.GetCells().Get(u"D1").PutValue(3);

    // Define the CellArea
    CellArea ca;
    ca.StartColumn = 4;
    ca.EndColumn = 4;
    ca.StartRow = 0;
    ca.EndRow = 0;

    // Add a sparkline group
    int idx = sheet.GetSparklineGroups().Add(SparklineType::Line, sheet.GetName() + u"!A1:D1", false, ca);

    // Get the sparkline group
    SparklineGroup group = sheet.GetSparklineGroups().Get(idx);
    group.GetSparklines().Add(sheet.GetName() + u"!A1:D1", 0, 4);

    // Customize Sparklines
    // Create CellsColor
    CellsColor clr = book.CreateCellsColor();
    clr.SetColor(Color::Orange());
    group.SetSeriesColor(clr);

    // Set the high points to green and low points to red
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    group.GetHighPointColor().SetColor(Color::Green());
    group.GetLowPointColor().SetColor(Color::Red());

    // Set line weight
    group.SetLineWeight(1.0);

    // Optionally, apply a preset style
    // group.SetPresetStyle(SparklinePresetStyleType::Style10);

    // Save the workbook
    book.Save(outDir + u"output.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Sujets avancés**
- [Utiliser les sparklines et les paramètres de format 3D](/cells/fr/cpp/using-sparklines-and-settings-3d-format/)
{{< app/cells/assistant language="cpp" >}}
