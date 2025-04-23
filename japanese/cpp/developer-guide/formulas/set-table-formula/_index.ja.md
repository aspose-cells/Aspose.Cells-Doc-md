---
title: 新しい行にデータを入力する際に、表やリストオブジェクト内の数式を自動的に伝播させる方法（C++）
linktitle: テーブルの数式を設定する
type: docs
weight: 260
url: /ja/cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: 新しいデータを入力するときに表やリストオブジェクトの数式を自動的に伝播させる方法を学びます。Aspose.Cells for C++を使用します。
---

## **可能な使用シナリオ**
時々、表やリストオブジェクト内の数式が新しい行に自動的に伝播することを望むことがあります。これはMicrosoft Excelの既定の動作です。Aspose.Cellsで同じ機能を実現するには、[ListColumn::GetFormula](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listcolumn/getformula/)メソッドを使用します。

## **新しい行にデータを入力する際に、表やリストオブジェクトの式を自動的に伝播させる**
次のサンプルコードは、列Bの数式が新しいデータを入力すると自動的に新しい行に伝播するように表またはリストオブジェクトを作成します。このコードで生成された[出力エクセルファイル](5115469.xlsx)を確認してください。セルA3に数字を入力すると、セルB2の数式が自動的にセルB3に伝播するのが分かります。

```c++
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

    // Create workbook object
    Workbook book;

    // Access first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Add column headings in cell A1 and B1
    sheet.GetCells().Get(0, 0).PutValue(u"Column A");
    sheet.GetCells().Get(0, 1).PutValue(u"Column B");

    // Add list object, set its name and style
    ListObject listObject = sheet.GetListObjects().Get(sheet.GetListObjects().Add(0, 0, 1, sheet.GetCells().GetMaxColumn(), true));
    listObject.SetTableStyleType(TableStyleType::TableStyleMedium2);
    listObject.SetDisplayName(u"Table");

    // Set the formula of second column so that it propagates to new rows automatically while entering data
    listObject.GetListColumns().Get(1).SetFormula(u"=[Column A] + 1");

    // Save the workbook in xlsx format
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
