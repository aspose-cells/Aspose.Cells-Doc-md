---
title: ODSファイルのセル検証をC++で取得
linktitle: ODSファイルでのセル検証の取得
type: docs
weight: 180
url: /ja/cpp/get-cell-validation-in-ods-files/
description: Aspose.Cells for C++を使用して、ODSファイル内のセルに適用された検証を取得する方法を学びます。
keywords: セル検証を取得し、セル検証を取得します 
---

## **ODS ファイルでのセル検証を取得**

Aspose.Cells for C++を用いて、ODSファイルのセルに適用された検証を取得できます。APIは [**GetValidation**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/) メソッドを提供しています。

以下のコードサンプルは、[**GetValidation**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/) メソッドを使用して、[ソースODS](101089354.ods)ファイルを読み込み、セルA9の検証を取得する例です。

### **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source Excel file
    U16String inputFilePath = srcDir + u"SampleBook1.ods";
    Workbook workbook(inputFilePath);

    // Access first worksheet
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);

    // Access cell A9
    Cells cells = worksheet.GetCells();
    Cell cell = cells.Get(U16String(u"A9"));

    // Check validation existence
    Validation validation = cell.GetValidation();
    if (validation.IsNull() == false)
    {
        std::cout << "Validation type: " << static_cast<int>(validation.GetType()) << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
