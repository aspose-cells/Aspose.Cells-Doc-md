---
title: C++でセル値がデータ検証ルールを満たしているか確認する
linktitle: セルの値がデータ検証ルールを満たしているかを確認
type: docs
weight: 210
url: /ja/cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: Aspose.Cells for C++ APIを通じてセル値がデータ検証ルールを満たしているか確認する方法を学びます。
keywords: セル検証値を取得し、セル検証値を取得し、セルに適用されたデータ検証ルールを値が満たしているかを検証します
---

{{% alert color="primary" %}} 

Microsoft Excelは、セルにデータ検証ルールを追加できるようにしています。例えば、少数点の検証は10から20の間の数値のみを入力可能にします。異なる数字を入力した場合、Excelはエラーメッセージを表示し、正しい範囲の数字を入力するよう促します。数字をコピー＆ペーストした場合、検証は行われずエラーメッセージも表示されません。

時には、プログラムでセルに適用されたデータ検証ルールが値を満たしているかどうかを検証する必要があります。たとえば、上記の場合、エントリが失敗する必要があります。

{{% /alert %}} 

## **紹介**
Aspose.Cellsは、[Cell.GetValidationValue()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidationvalue/)メソッドを提供し、セルの値をプログラム的に検証します。セルの値がそのセルに適用されたデータ検証ルールを満たさない場合、**False**を返し、満たす場合は **True**を返します。

次のサンプルコードは、[Cell.GetValidationValue()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidationvalue/)メソッドの動作を示しています。最初にC1に値3を入力します。これがデータ検証ルールを満たさないため、[Cell.GetValidationValue()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidationvalue/)メソッドは **False**を返します。次に、C1に値15を入力します。この値は検証ルールを満たすため、メソッドは **True**を返します。同様に、値30の場合は **False**を返します。

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

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access Cell C1
    // Cell C1 has the Decimal Validation applied on it.
    // It can take only the values Between 10 and 20
    Cell cell = worksheet.GetCells().Get(u"C1");

    // Enter 3 inside this cell
    // Since it is not between 10 and 20, it should fail the validation
    cell.PutValue(3);

    // Check if number 3 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 3 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    // Enter 15 inside this cell
    // Since it is between 10 and 20, it should succeed the validation
    cell.PutValue(15);

    // Check if number 15 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 15 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    // Enter 30 inside this cell
    // Since it is not between 10 and 20, it should fail the validation again
    cell.PutValue(30);

    // Check if number 30 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 30 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **出力**
{{< highlight java >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
