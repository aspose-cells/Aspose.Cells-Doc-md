---
title: C++でワークシートのユニークIDを取得
linktitle: ワークシートのユニークIDを取得
type: docs
weight: 190
url: /ja/cpp/get-worksheet-unique-id/
description: この記事では、C++ライブラリとAPIを使用してExcelワークシートのユニークIDをプログラム的に取得する方法を示します。
keywords: ユニークID Excelワークシート C++、ユニークIDワークシート C++
---

## **ワークシートのユニークIDを取得**

Aspose.Cellsは、[**GetUniqueId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getuniqueid/) メソッドを使ってワークシートのユニークIDを取得する機能を提供します。以下のコードスニペットは、[**GetUniqueId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getuniqueid/) メソッドを使用してワークシートのユニークIDを出力する例です。このコードは、[サンプルExcelファイル](105480213.xlsx)を使用しています。

### ソースコード

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source Excel file
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Print Unique Id
    std::cout << "Unique Id: " << worksheet.GetUniqueId().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```
