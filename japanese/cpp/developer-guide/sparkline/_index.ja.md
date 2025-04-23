---
title: C++でスパークラインを挿入
linktitle: スパークライン
type: docs
weight: 160
url: /ja/cpp/creating-sparklines/
description: Aspose.Cellsを使用してExcelのスパークラインをC++で作成
---

## **スパークラインを挿入する**
{{% alert color="primary" %}} 

スパークラインはセル内に配置される小さなグラフで、データの視覚的な表現を提供します。トレンド（季節ごとの増減、経済サイクルなど）や最大・最小値を示すために使用します。最大効果を得るために、データの近くに配置してください。スパークラインにはライン、コラム、積み上げの3タイプがあります。

{{% /alert %}} 

Aspose.Cellsを使用してスパークラインを簡単に作成することができます。以下はその例です。

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

## **高度なトピック**
- [スパークラインの使用と 3D フォーマットの設定](/cells/ja/cpp/using-sparklines-and-settings-3d-format/)
