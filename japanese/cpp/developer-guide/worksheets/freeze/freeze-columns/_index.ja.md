---
title: C++を使用してExcelシートの最初の列を固定する
linktitle: 列を固定する
type: docs
weight: 190
url: /ja/cpp/how-to-freeze-columns-of-excel-worksheet
description: この記事では、Aspose.Cells APIを使用してプログラムmatically Excelワークシートの左側の列を固定する方法を学びます。
keywords: 左の列を固定、最初の列を固定、列をロックする
---

## **紹介**

この記事では、左の列を固定する方法を学びます。行に大量のデータがある場合、横にスクロールした際に左の列が見えなくなることがあります。最初の列を固定してロックすれば、残りのデータをスクロールしても固定された部分が見えるようになります。ヘッダーも簡単に確認できます。

## **Excelでの列の固定**

**![Excelで左列を固定する](freeze-columns.png)**

1. 左の列を固定したい場合、その列の下の列を最初に選択します。
2. 表示 > ウィンドウ枠の固定をクリックします。
3. ドロップダウンメニューから、「最初の列を固定」をクリックします。
4. 下にスクロールしても、最初の列は常に左側のビューに固定されます。

**![固定された列](frozen-columns.png)**

ご覧のとおり、最初の列が固定されており、横スクロールしても固定された部分は常にビューの上部にロックされています。

列の固定は、長いデータを確認しながら最初の列を保持するのに便利です。

## **Aspose.Cells for C++を使用した列の固定**
Aspose.Cells for C++を使えば、最初の列の固定は簡単です。 
選択した列に列を固定するには、[**Worksheet.FreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)メソッドを使用してください。
1. ファイルを開くためにワークブックを作成します。または空のファイルを作成します。
2. Worksheet.FreezePanes()メソッドを使って最初の列を固定します。
3. ファイルを保存します。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"Freeze.xlsx");

    // Freezing panes at the second column
    workbook.GetWorksheets().Get(0).FreezePanes(u"B1", 0, 1);

    // Saving the file
    workbook.Save(u"frozen.xlsx");

    std::cout << "Panes frozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

添付 [サンプルExcelファイル](Freeze.xlsx)。
