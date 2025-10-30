---
title: C++を使用してMicrosoft Excelの数式監視ウィンドウにセルを追加
linktitle: 数式の監視ウィンドウにセルを追加
description: Excelの数式監視ウィンドウにセルを追加するためにAspose.Cells for C++を使う方法を学びます。Excelファイルをロードまたは作成し、セルを操作し、数式を設定し、変更したファイルを保存します。
keywords: Aspose.Cells、Excel、数式監視ウィンドウ、セルの追加、C++
type: docs
weight: 60
url: /ja/cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **可能な使用シナリオ**

Microsoft Excelの監視ウィンドウは、セルの値や数式をウィンドウで便利に監視できるツールです。Microsoft Excelで*数式 > 監視ウィンドウ*をクリックして*監視ウィンドウ*を開くことができます。このウィンドウには*監視の追加*ボタンがあり、監視するセルを追加できます。同様に、Aspose.Cells APIの[**Worksheet.CellWatches.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellwatchcollection/add/)メソッドを使用してセルを*監視ウィンドウ*に追加できます。

## **Microsoft Excelフォーミュラ計算エンジンのAspose.Cells**

次のサンプルコードは、セルC1とE1の数式を設定し、それらを監視ウィンドウに追加します。その後、ワークブックを[出力Excelファイル](67338481.xlsx)として保存します。出力Excelファイルを開き、*監視ウィンドウ*を見ると、両方のセルがこのスクリーンショットのように表示されます。

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **サンプルコード**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Put some integer values in cell A1 and A2
    ws.GetCells().Get(u"A1").PutValue(10);
    ws.GetCells().Get(u"A2").PutValue(30);

    // Access cell C1 and set its formula
    Cell c1 = ws.GetCells().Get(u"C1");
    c1.SetFormula(u"=Sum(A1,A2)");

    // Add cell C1 into cell watches by name
    ws.GetCellWatches().Add(c1.GetName());

    // Access cell E1 and set its formula
    Cell e1 = ws.GetCells().Get(u"E1");
    e1.SetFormula(u"=A2*A1");

    // Add cell E1 into cell watches by its row and column indices
    ws.GetCellWatches().Add(e1.GetRow(), e1.GetColumn());

    // Save workbook to output XLSX format
    wb.Save(u"outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
