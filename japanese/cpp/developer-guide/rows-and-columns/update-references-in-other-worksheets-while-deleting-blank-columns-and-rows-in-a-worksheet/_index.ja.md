---
title: C++でワークシートの空白列と行を削除しながら他のワークシートの参照を更新する方法
linktitle: 他のワークシートの参照を更新する
type: docs
weight: 5000
url: /ja/cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
description: Aspose.Cells for C++を使用して、ワークシートの空白列と行を削除する際に他のワークシートの参照を更新する方法を学びます。
---

{{% alert color="primary" %}}

空白列と行を削除すると、そのワークシート内の参照は無効になります。これを避けて、他のワークシート内の現在のワークシートへの参照も更新したい場合は、[**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/)プロパティを**true**に設定します。

{{% /alert %}}

## **ワークシート内の空白の列と行を削除する際に、他のワークシートの参照を更新する**

サンプルコードとそのコンソール出力は以下のとおりです。第2のワークシートのセルE3には`=Sheet1!C3`という数式があり、これは最初のワークシートのセルC3を参照しています。[**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/)プロパティを**true**に設定すると、最初のワークシートで空白列と行を削除した後、この数式は`=Sheet1!A1`に更新されます。ただし、[**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/)プロパティを**false**に設定すると、セルE3の数式は`=Sheet1!C3`のままで無効になります。

### **プログラミングサンプル**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook wb;

    // Add second sheet with name Sheet2
    wb.GetWorksheets().Add(u"Sheet2");

    // Access first sheet and add some integer value in cell C1
    // Also add some value in any cell to increase the number of blank rows and columns
    Worksheet sht1 = wb.GetWorksheets().Get(0);
    sht1.GetCells().Get(u"C1").PutValue(4);
    sht1.GetCells().Get(u"K30").PutValue(4);

    // Access second sheet and add formula in cell E3 which refers to cell C1 in first sheet
    Worksheet sht2 = wb.GetWorksheets().Get(1);
    sht2.GetCells().Get(u"E3").SetFormula(u"'Sheet1'!C1");

    // Calculate formulas of workbook
    wb.CalculateFormula();

    // Print the formula and value of cell E3 in second sheet before deleting blank columns and rows in Sheet1.
    std::cout << "Cell E3 before deleting blank columns and rows in Sheet1." << std::endl;
    std::cout << "--------------------------------------------------------" << std::endl;
    std::cout << "Cell Formula: " << sht2.GetCells().Get(u"E3").GetFormula().ToUtf8() << std::endl;
    std::cout << "Cell Value: " << sht2.GetCells().Get(u"E3").GetStringValue().ToUtf8() << std::endl;

    // If you comment DeleteOptions.UpdateReference property below, then the formula in cell E3 in second sheet will not be updated
    DeleteOptions opts;
    opts.SetUpdateReference(true);

    // Delete all blank rows and columns with delete options
    sht1.GetCells().DeleteBlankColumns(opts);
    sht1.GetCells().DeleteBlankRows(opts);

    // Calculate formulas of workbook
    wb.CalculateFormula();

    // Print the formula and value of cell E3 in second sheet after deleting blank columns and rows in Sheet1.
    std::cout << std::endl;
    std::cout << std::endl;
    std::cout << "Cell E3 after deleting blank columns and rows in Sheet1." << std::endl;
    std::cout << "--------------------------------------------------------" << std::endl;
    std::cout << "Cell Formula: " << sht2.GetCells().Get(u"E3").GetFormula().ToUtf8() << std::endl;
    std::cout << "Cell Value: " << sht2.GetCells().Get(u"E3").GetStringValue().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **コンソール出力**

上記のサンプルコードのコンソール出力は、[**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/)プロパティを**true**に設定した場合です。

{{< highlight java >}}

Cell E3 before deleting blank columns and rows in Sheet1.
--------------------------------------------------------
Cell Formula: =Sheet1!C1
Cell Value: 4

Cell E3 after deleting blank columns and rows in Sheet1.
--------------------------------------------------------
Cell Formula: =Sheet1!A1
Cell Value: 4

{{< /highlight >}}

上記のサンプルコードのコンソール出力は、[**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/)プロパティを**false**に設定した場合です。ご覧のとおり、セルE3の数式は更新されず、そのセルの値は4ではなく0になり、無効です。

{{< highlight java >}}

Cell E3 before deleting blank columns and rows in Sheet1.
--------------------------------------------------------
Cell Formula: =Sheet1!C1
Cell Value: 4

Cell E3 after deleting blank columns and rows in Sheet1.
--------------------------------------------------------
Cell Formula: =Sheet1!C1
Cell Value: 0

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
