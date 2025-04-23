---
title: C++でセルの書式を変更する方法
linktitle: セルの形式を変更
description: Aspose.CellsライブラリをC++で使用してセルのフォーマットを変更する方法（フォント、色、境界線など）について説明します。これらのプロパティを調整することで、セルの見た目や外観をより細かく制御できます。
keywords: Aspose.Cells、セル書式設定、C++、フォント、色、境界線
type: docs
weight: 20
url: /ja/cpp/how-to-change-format-of-cell/
---

## **可能な使用シナリオ**
特定のデータを強調表示したい場合、セルのスタイルを変更できます。

## **Excelのセルのフォーマットを変更する方法**

Excelの単一のセルのフォーマットを変更するには、次の手順に従います。

1. Excelを開き、セルのフォーマットを変更したいワークブックを開きます。

2. フォーマットを変更したいセルを見つけます。

3. セルを右クリックして、コンテキストメニューから"セルの書式設定"を選択します。または、セルを選択し、Excelリボンのホームタブに移動し、"セル"グループの"書式"ドロップダウンをクリックし、「セルの書式設定」を選択することもできます。

4. 「セルの書式設定」ダイアログボックスが表示されます。ここでは、選択したセルに適用するさまざまな書式オプションを選択できます。たとえば、フォントスタイル、フォントサイズ、フォントの色、数値形式、罫線、背景色などを変更できます。ダイアログボックスのさまざまなタブを探索して、さまざまな書式オプションにアクセスできます。

5. 所望の書式設定変更を行った後、「OK」ボタンをクリックして、選択したセルに書式を適用します。

## **C++を使用したセルのフォーマット変更方法**

Aspose.Cellsを使ってセルの書式を変更するには、以下の方法を使用できます：
1. [Cell.SetStyle(Style style)](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/)
2. [Cell.SetStyle(Style style, bool explicitFlag)](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/)
3. [Cell.SetStyle(Style style, StyleFlag flag)](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/)

## **サンプルコード**
この例では、Excelワークブックを作成し、いくつかのサンプルデータを追加し、最初のワークシートにアクセスし、2つのセル("A2"および"B3")を取得します。次に、セルのスタイルを取得し、さまざまな書式オプション(たとえば、フォントの色、太字)を設定し、セルの形式を変更します。最後に、作業ブックを新しいファイルに保存します。
![todo:image_alt_text](change-format.png)

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

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

    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cell a2 = worksheet.GetCells().Get(u"A2");
    Style style = a2.GetStyle();
    style.GetFont().SetColor(Color::Red());
    style.GetFont().SetIsBold(true);

    StyleFlag flag;
    flag.SetFontColor(true);
    a2.SetStyle(style, flag);

    Cell b3 = worksheet.GetCells().Get(u"B3");
    Style style2 = b3.GetStyle();
    style2.GetFont().SetColor(Color::Blue());
    style2.GetFont().SetIsItalic(true);
    b3.SetStyle(style2);

    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
}
```
