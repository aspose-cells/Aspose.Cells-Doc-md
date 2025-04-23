---
title: C++を使用してセルに適用された検証を取得する方法
linktitle: セルに適用された検証を取得
type: docs
weight: 200
url: /ja/cpp/get-validation-applied-on-a-cell/
description: この記事では、C++を使ってセルに検証を適用する方法を紹介します。
keywords: C++を使用してExcelにセル検証を適用、セルに検証を行う、C++でExcelのセル検証を適用、C++でExcelのセル検証、C++でExcelのセル検証を行う、C++でセルの検証をExcelに適用、C++でExcelのセル検証を行う
---

{{% alert color="primary" %}}

Aspose.Cellsを使用して、セルに適用された検証を取得できます。Aspose.Cellsはこの目的のために[**Cell::GetValidation()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/)メソッドを提供します。セルに検証が適用されていない場合、nullを返します。

同様に、[**Worksheet::Validations::GetValidationInCell**](https://reference.aspose.com/cells/cpp/aspose.cells/validationcollection/getvalidationincell/)メソッドを使用して、行と列のインデックスを指定してセルに適用された検証を取得できます。

{{% /alert %}}

## C++でセルに適用された検証を取得するコード例

以下のコード例は、検証をセルに取得する方法を示しています。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate the workbook from sample Excel file
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access its first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Cell C1 has the Decimal Validation applied on it. It can take only the values Between 10 and 20
    Cell cell = worksheet.GetCells().Get(u"C1");

    // Access the validation applied on this cell
    Validation validation = cell.GetValidation();

    // Read various properties of the validation
    std::cout << "Reading Properties of Validation" << std::endl;
    std::cout << "--------------------------------" << std::endl;
    std::cout << "Type: " << static_cast<int>(validation.GetType()) << std::endl;
    std::cout << "Operator: " << static_cast<int>(validation.GetOperator()) << std::endl;
    std::cout << "Formula1: " << validation.GetFormula1().ToUtf8() << std::endl;
    std::cout << "Formula2: " << validation.GetFormula2().ToUtf8() << std::endl;
    std::cout << "Ignore blank: " << validation.GetIgnoreBlank() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## 関連記事

- [データの検証](/cells/ja/cpp/data-validation/)
