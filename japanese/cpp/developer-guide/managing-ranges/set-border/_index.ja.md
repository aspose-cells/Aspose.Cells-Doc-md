---
title: C++を使った範囲境界線の設定
type: docs
weight: 600
url: /ja/cpp/set-range-border/
description: Aspose.Cellsを使用してC++で範囲境界線を設定する方法を学びます。
---

## **可能な使用シナリオ**
範囲の境界線を設定したい場合、各セルを個別に設定する必要はありません。範囲に境界線を設定できます。Aspose.Cellsはこの機能を提供します。この記事は、範囲境界線設定のためのサンプルコードを紹介します。

## **Excelで範囲のボーダーを設定する**
Excelで範囲のボーダーを設定するには、次の手順に従います:
1. ボーダーを適用する範囲のセルを選択します。
2. リボンの「ホーム」タブに移動し、「フォント」グループを検索します。
3. 「フォント」グループ内で、「ボーダー」ドロップダウンボタンをクリックします。
<br>
<img src="border.png" />
4. ドロップダウンメニュー内のオプションから適用するボーダーの種類を選択します。プリセットのボーダースタイルを選択するか、独自のボーダーをカスタマイズすることができます。
5. 希望のボーダースタイルを選択したら、そのボーダーが選択したセル範囲に適用されます。

## **Aspose.Cellsを使用して範囲のボーダーを設定する**
この例では、次のことができます:

1. ワークブックを作成する。
2. 最初のワークシートのセルにデータを追加します。
3. [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range)を作成します。
4. 範囲の内部境界線を設定します。
5. 範囲の外枠線を設定する。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new Workbook object
    Workbook workbook;

    // Obtain the reference of the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the value to the cells
    Cell cell = cells.Get("A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get("B1");
    cell.PutValue(u"Count");
    cell = cells.Get("C1");
    cell.PutValue(u"Price");

    cell = cells.Get("A2");
    cell.PutValue(u"Apple");
    cell = cells.Get("A3");
    cell.PutValue(u"Mango");
    cell = cells.Get("A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get("A5");
    cell.PutValue(u"Cherry");

    cell = cells.Get("B2");
    cell.PutValue(5);
    cell = cells.Get("B3");
    cell.PutValue(3);
    cell = cells.Get("B4");
    cell.PutValue(6);
    cell = cells.Get("B5");
    cell.PutValue(4);

    cell = cells.Get("C2");
    cell.PutValue(5);
    cell = cells.Get("C3");
    cell.PutValue(20);
    cell = cells.Get("C4");
    cell.PutValue(30);
    cell = cells.Get("C5");
    cell.PutValue(60);

    // Create a range (A1:C5)
    Range range = cells.CreateRange(u"A1", u"C5");

    // Set inner border of range
    CellsColor innerColor = workbook.CreateCellsColor();
    innerColor.SetColor(Color::Red());
    range.SetInsideBorders(BorderType::Vertical, CellBorderType::Thin, innerColor);
    innerColor.SetColor(Color::Green());
    range.SetInsideBorders(BorderType::Horizontal, CellBorderType::Thin, innerColor);

    // Set outer border of range
    CellsColor outerColor = workbook.CreateCellsColor();
    outerColor.SetColor(Color::Blue());
    range.SetOutlineBorders(CellBorderType::Thin, outerColor);

    // Save the Workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
