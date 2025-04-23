---
title: 書式設定範囲 with C++
linktitle: 範囲の書式設定
type: docs
weight: 105
url: /ja/cpp/how-to-format-a-range/
description: Aspose.Cellsを使用してC++でExcelの範囲を書式設定する方法を学びます。スタイル、フォント、色をプログラムでセル範囲に適用します。
---

## **可能な使用シナリオ**
範囲にスタイルを適用する必要がある場合は、範囲の書式設定を使用できます。

## **Excelでの範囲の書式設定方法**

Excelで範囲の書式を設定するには、Excelが提供する組み込みの書式設定オプションを使用します。Excelで範囲の書式を設定する方法は以下の通りです:

1. Excelを開き、書式を設定したい範囲が含まれているワークブックを開きます。

2. 書式を設定したい範囲を選択します。範囲を選択するには、範囲をクリックしてドラッグするか、ショートカットキーであるシフト+矢印キーを使用して選択を拡張することができます。

3. 範囲が選択されたら、選択した範囲を右クリックし、コンテキストメニューから「セルの書式設定」を選択します。または、Excelリボンのホームタブに移動し、「セル」グループの「書式」ドロップダウンをクリックし、「セルの書式設定」を選択します。

4. 「セルの書式設定」ダイアログボックスが表示されます。ここで、選択した範囲に適用するさまざまな書式設定オプションを選択できます。たとえば、フォントスタイル、フォントサイズ、フォント色、数値形式、罫線、背景色などを変更できます。 ダイアログボックス内の異なるタブを探索して、さまざまな書式設定オプションにアクセスできます。

5.所望の書式設定を行った後、選択した範囲に書式を適用するには、「OK」ボタンをクリックします。

## **C++を使用して範囲を書式設定する方法**

Aspose.Cellsを使って範囲を書式設定するには、次のメソッドを使用できます：
1. [Range.ApplyStyle(Style style, StyleFlag flag)](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/)
2. [Range.SetStyle(Style style)](https://reference.aspose.com/cells/cpp/aspose.cells/range/setstyle/)

## **サンプルコード**
この例では、Excelワークブックを作成し、サンプルデータを追加し、最初のワークシートにアクセスし、2つの範囲（"A1:C3"および"A4:C5"）を定義します。次に、新しいスタイルを作成し、さまざまな書式設定オプション（例：フォント色、太字）を設定し、そのスタイルを範囲に適用します。最後に、ワークブックを新しいファイルとして保存します。
<br>
![todo:image_alt_text](format-range.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
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

    Range range = worksheet.GetCells().CreateRange(u"A1:C3");
    Style style = workbook.CreateStyle();
    style.GetFont().SetColor(Color::Red());
    style.GetFont().SetIsBold(true);

    StyleFlag flag;
    flag.SetFont(true);
    range.ApplyStyle(style, flag);

    Range range2 = worksheet.GetCells().CreateRange(u"A4:C5");
    Style style2 = workbook.CreateStyle();
    style2.GetFont().SetColor(Color::Blue());
    style2.GetFont().SetIsItalic(true);
    range2.SetStyle(style2);

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
