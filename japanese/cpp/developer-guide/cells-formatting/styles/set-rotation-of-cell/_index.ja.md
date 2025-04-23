---
title: C++でセルの文字列を回転させる方法
linktitle: セルのテキストの回転方法
type: docs
weight: 80
url: /ja/cpp/how-to-rotate-text-of-cell/
description: Aspose.Cells for C++ APIを使用したC++コードでセルの文字列を回転させる例
keywords: C++でセルの文字列を回転させる、ワークブック内のセルの回転角度をプログラムで設定、Excelでセルの文字列を回転させる方法
---

## **Aspose.Cells でセルのテキストを回転する**

Aspose.Cellsは、Excelのスプレッドシートをプログラムで操作する強力なC++コンポーネントです。Aspose.Cellsの機能の一つにセルの回転があり、これによりテキストの向きを調整してデータの視覚的提示を向上させることができます。本資料では、Aspose.Cellsを使用したセルの回転方法について解説します。

## **Excel でセルのテキストを回転する方法**
Excel でセルを回転するには、次の手順を使用できます:
1. Excel を開き、回転させたいセルまたは範囲を選択します。
1. 選択したセルで右クリックし、コンテキストメニューから「セルの書式設定」を選択します。または、Excel リボンの「ホーム」タブで、「セル」グループの「書式」ドロップダウンをクリックし、「セルの書式設定」を選択します。
1. 「セルの書式設定」ダイアログボックスで、「配置」タブに移動します。
1. 「方向」セクションで、テキストの回転オプションが表示されます。『度』ボックスに、希望の回転角度を直接入力できます。正の値はテキストを反時計回りに、負の値は時計回りに回転させます。
<br>
![todo:image_alt_text](alignment.png)
1. 希望の回転を選択したら、「OK」をクリックして変更を適用します。選択したセルは、選択した回転角度または方向に基づいて回転されます。

## **Aspose.Cells APIを使用してセルのテキストを回転する方法**

[**Style.GetRotationAngle()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getrotationangle/)プロパティを使用すると、セルを回転させることが簡単になります。Aspose.Cellsでセルを回転させるには、次の手順に従う必要があります:
1. Excelワークブックをロードする
<br>
まず、Aspose.Cellsを使用してExcelワークブックをロードする必要があります。Workbookクラスを使用して既存のExcelファイルを開くか、新しいファイルを作成できます。 

1. ワークシートにアクセスする
<br>
ワークブックがロードされたら、セルを回転させたいワークシートにアクセスする必要があります。ワークシートはインデックスまたは名前でアクセスできます。 

1. セルのテキストを回転させる
<br>
ワークシートにアクセスできるようになったので、希望のセルのStyleオブジェクトを変更することでセルを回転させることができます。Styleオブジェクトを使用すると、回転を含むさまざまな書式設定オプションを設定できます。 

1. ワークブックを保存する
<br>
セルを回転させた後、変更されたワークブックをSaveメソッドを使用してファイルまたはストリームに保存できます。

## **C++サンプルコード**

以下のコードをご覧ください。これはワークブックオブジェクトを作成し、いくつかのセルに異なる回転角を設定しています。スクリーンショットはサンプルコードの実行後の結果を示しています。
<br>
<img src="rotation.png" width=80% />

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
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Row index of the cell
    int row = 0;
    // Column index of the cell
    int column = 0;

    // Get cell A1 and set its value
    Cell a1 = worksheet.GetCells().Get(row, column);
    a1.PutValue(u"a1 rotate text");
    Style a1Style = a1.GetStyle();

    // Set the rotation angle in degrees
    a1Style.SetRotationAngle(45);
    a1.SetStyle(a1Style);

    // Set column index to 1 for cell B1
    column = 1;
    Cell b1 = worksheet.GetCells().Get(row, column);
    b1.PutValue(u"b1 rotate text");
    Style b1Style = b1.GetStyle();

    // Set the rotation angle in degrees
    b1Style.SetRotationAngle(255);
    b1.SetStyle(b1Style);

    // Set column index to 2 for cell C1
    column = 2;
    Cell c1 = worksheet.GetCells().Get(row, column);
    c1.PutValue(u"c1 rotate text");
    Style c1Style = c1.GetStyle();

    // Set the rotation angle in degrees
    c1Style.SetRotationAngle(-90);
    c1.SetStyle(c1Style);

    // Set column index to 3 for cell D1
    column = 3;
    Cell d1 = worksheet.GetCells().Get(row, column);
    d1.PutValue(u"d1 rotate text");
    Style d1Style = d1.GetStyle();

    // Set the rotation angle in degrees
    d1Style.SetRotationAngle(-90);
    d1.SetStyle(d1Style);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
