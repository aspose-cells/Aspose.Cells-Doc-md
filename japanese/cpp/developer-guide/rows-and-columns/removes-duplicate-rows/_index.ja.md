---
title: C++でワークシートの重複行を削除する
linktitle: ワークシート内の重複行を削除する
type: docs
weight: 370
url: /ja/cpp/remove-duplicate-rows-in-a-worksheet/
description: Aspose.Cells for C++を使ってワークシートの重複行を削除する方法を学びます。
---

{{% alert color="primary" %}}

重複行の削除はMicrosoft Excelの多くの便利な機能のひとつです。ワークシート内の重複行を削除でき、どの列を重複チェック対象にするか選択できます。

Aspose.Cellsはこの目的のために`Cells::RemoveDuplicates()`メソッドを提供しています。また、`startRow`、`startColumn`、`endRow`、`endColumn`を設定して列を選択できます。

これがこの機能のテストにダウンロードできるサンプルファイルです。

[removeduplicates.xlsx](removeduplicates.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook book(u"removeduplicates.xlsx");

    // Remove duplicates from the first worksheet
    book.GetWorksheets().Get(0).GetCells().RemoveDuplicates(0, 0, 5, 3);

    // Save the result
    book.Save(u"removeduplicates-result.xlsx");

    std::cout << "Duplicates removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% /alert %}}
