---
title: C++ でシートタブバーを制御する方法
linktitle: シートタブバーの制御方法
type: docs
weight: 600
url: /ja/cpp/how-to-control-sheet-tab-bar/
description: Aspose.Cells for C++ API を通じてシートタブバーを制御する方法を学びます。
keywords: シートタブバーの制御、シートタブバーの操作、シートタブバーの設定、シートタブバーの制御方法。 
---

## **可能な使用シナリオ**
Excelシートバーの表示を調整する必要がある場合は、シートタブバーの表示・非表示、幅の変更、最初に表示されるタブの指定などを制御する方法を知る必要があります。 Aspose.Cells はこれらの機能をサポートしています。これらの目的を達成するために役立つプロパティとメソッドを提供します。

- [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/)
- [**WorkbookSettings.GetSheetTabBarWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getsheettabbarwidth/)
- [**WorkbookSettings.GetFirstVisibleTab()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getfirstvisibletab/)

## **Aspose.Cells for C++ を使用したシートタブバーの制御方法**
この例では、次のことができます:

1. ワークブックを作成する。
1. 最初のワークシートのセルにデータを追加する。
1. シートタブを表示してタブバーの幅を設定します。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook object
    Workbook workbook;

    // Obtain the reference to the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the value to the cells
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

    // Display the sheet tab and set the width of the tab bar
    workbook.GetSettings().SetShowTabs(true);
    workbook.GetSettings().SetSheetTabBarWidth(150);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

結果ファイルのプレビュー:
<br>
<image src="result.png" width="70%" />

{{< app/cells/assistant language="cpp" >}}
