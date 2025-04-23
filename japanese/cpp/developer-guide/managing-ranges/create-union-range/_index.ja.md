---
title: C++を使ったユニオン範囲の作成
linktitle: ユニオン範囲の作成
type: docs
weight: 360
url: /ja/cpp/create-union-range/
description: Aspose.Cellsを使用してC++でExcelファイルに結合範囲を作成する。
---

## **ユニオン範囲の作成**
Aspose.Cellsは[CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/)メソッドを使用して結合範囲を作成する機能を提供します。[CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/)メソッドは、結合範囲を作成するためのアドレスとワークシートのインデックスの2つのパラメータを受け取ります。 [CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/)メソッドは[UnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/unionrange/)オブジェクトを返します。

以下のコードスニペットは[CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/)メソッドを使用して結合範囲を作成する例を示しています。コードによって生成された出力ファイルは参考のために添付されています。

- [出力ファイル](106364952.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook object
    Workbook workbook;

    // Create union range
    UnionRange unionRange = workbook.GetWorksheets().CreateUnionRange(u"sheet1!A1:A10,sheet1!C1:C10", 0);

    // Put value "ABCD" in the range
    unionRange.SetValue(u"ABCD");

    // Save the output workbook
    workbook.Save(u"CreateUnionRange_out.xlsx");

    std::cout << "Union range created and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
