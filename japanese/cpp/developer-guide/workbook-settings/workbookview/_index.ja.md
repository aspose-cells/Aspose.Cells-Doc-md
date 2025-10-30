---
title: C++ でブックビューを制御する方法
linktitle: ワークブックビューの制御方法
type: docs
weight: 600
url: /ja/cpp/how-to-control-workbook-view/
description: Aspose.Cells for C++ API を使用してブックビューを制御する方法を学びます。
keywords: ワークブックビューの制御方法、Excelビューの設定、ワークブックビューの操作、ワークブックビューの設定、Excelビューの制御方法
---

## **可能な使用シナリオ**
Excelページの表示を調整する必要がある場合は、各モジュール（水平・垂直スクロールバー、Excelファイルの非表示など）を制御する方法を知る必要があります。 Aspose.Cells はこの機能を提供しています。これらの目的を達成するためのプロパティとメソッドを提供します。

- [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/)
- [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/)
- [**WorkbookSettings.IsHidden**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishidden/)
- [**WorkbookSettings.IsMinimized**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isminimized/)
- [**WorkbookSettings.GetWindowHeight()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getwindowheight/)
- [**WorkbookSettings.GetWindowWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getwindowwidth/)
- [**WorkbookSettings.GetWindowLeft()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getwindowleft/)
- [**WorkbookSettings.GetWindowTop()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getwindowtop/)

## **Aspose.Cells for C++ を使用したブックビュー制御方法**
この例では、次のことができます:

1. ワークブックを作成する。
1. 最初のワークシートのセルにデータを追加する。
1. ワークブックビューの水平および垂直のスクロールバーを非表示にする。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Set values to cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");
    cell = cells.Get(u"C1");
    cell.PutValue(u"Price");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");

    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);

    cell = cells.Get(u"C2");
    cell.PutValue(5);
    cell = cells.Get(u"C3");
    cell.PutValue(20);
    cell = cells.Get(u"C4");
    cell.PutValue(30);
    cell = cells.Get(u"C5");
    cell.PutValue(60);

    // Apply style to cell E10
    cell = cells.Get(u"E10");
    Style temp = workbook.CreateStyle();
    temp.GetFont().SetColor(Color::Red());
    cell.SetStyle(temp);

    // Hide horizontal and vertical scrollbars
    workbook.GetSettings().SetIsHScrollBarVisible(false);
    workbook.GetSettings().SetIsVScrollBarVisible(false);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```

結果ファイルのプレビュー:
<br>
<image src="result.png" width="70%" />
{{< app/cells/assistant language="cpp" >}}
