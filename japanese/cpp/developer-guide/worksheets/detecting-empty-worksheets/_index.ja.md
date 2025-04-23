---
title: 空のワークシートを検出（C++）
linktitle: 空のワークシートを検出する
type: docs
weight: 410
url: /ja/cpp/detecting-empty-worksheets/
description: このコードは、Aspose.Cells ライブラリを使用して C++ API でExcelワークブックの空のワークシートをプログラム的に検出する方法を示しています。
keywords: 空のワークシートを検出（C++）、空のExcelワークシートを見つける（C++）
---

## **空の初期化されたセルのチェック**

ワークシートには値が入力されたセルが1つ以上存在します。値はシンプル（テキスト、数字、日付/時刻）または数式、または数式に基づく値です。その場合、特定のワークシートが空かどうかを検出することは容易です。確認する必要があるのは [**Cells.MaxDataRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/) もしくは [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/) プロパティです。これらのプロパティがゼロまたは正の値を返せば、1つ以上のセルが値で埋まっています。いずれかのプロパティが -1 を返した場合、そのワークシートには値が入力されたセルが存在しないことを意味します。

{{% alert color="primary" %}}

行と列のコレクションはゼロベースのインデックスです。したがって、行0、列0のセルはワークシートの最初のセル（A1）を意味します。

{{% /alert %}}

## **空の初期化されたセルのチェック**

値が設定されているすべてのセルは自動的に初期化されます。ただし、シートに書式のみが適用されたセルが存在する可能性もあります。その場合、[**Cells.MaxDataRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/) や [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/) プロパティは -1 を返し、値が入力されていないことを示します。ただし、セルの書式設定による初期化セルはこの方法では検出できません。空の初期化セルがあるかどうかを確認するには、[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) コレクションから取得した列挙子の `MoveNext` メソッドを使用してください。`MoveNext` が true を返す場合、そのシートには1つ以上の初期化セルがあります。

## **図形のチェック**

特定のシートに値が入力されていなくても、コントロール、チャート、画像などの図形やオブジェクトが含まれている場合があります。その場合、[**ShapeCollection.Count**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/getcount/) プロパティを調査することで、そのシートに図形が含まれているかどうかを確認できます。正の値は図形の存在を示します。

## **プログラミングサンプル**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create an instance of Workbook and load an existing spreadsheet
    Workbook book(srcDir + u"sample.xlsx");

    // Loop over all worksheets in the workbook
    WorksheetCollection sheets = book.GetWorksheets();
    for (int i = 0; i < sheets.GetCount(); i++)
    {
        Worksheet sheet = sheets.Get(i);

        // Check if worksheet has populated cells
        if (sheet.GetCells().GetMaxDataRow() != -1)
        {
            cout << sheet.GetName().ToUtf8() << " is not empty because one or more cells are populated" << endl;
        }
        // Check if worksheet has shapes
        else if (sheet.GetShapes().GetCount() > 0)
        {
            cout << sheet.GetName().ToUtf8() << " is not empty because there are one or more shapes" << endl;
        }
        // Check if worksheet has empty initialized cells
        else
        {
            Range range = sheet.GetCells().GetMaxDisplayRange();
            auto rangeIterator = range.GetEnumerator();
            if (rangeIterator.MoveNext())
            {
                cout << sheet.GetName().ToUtf8() << " is not empty because one or more cells are initialized" << endl;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
