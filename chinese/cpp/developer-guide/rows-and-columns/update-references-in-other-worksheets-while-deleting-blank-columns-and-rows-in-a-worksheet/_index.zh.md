---
title: 用C++在删除工作表中的空白列和行时，更新其他工作表中的引用
linktitle: 更新其他工作表中的引用
type: docs
weight: 5000
url: /zh/cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
description: 学习如何在删除工作表中的空白列和行时，更新其他工作表中的引用（使用Aspose.Cells for C++ API）。
---

{{% alert color="primary" %}}

当你删除工作表中的空白列和行时，它在其他工作表中的引用会变得无效。若想避免此行 为，并确保其他工作表中的对当前工作表的引用也被更新，请使用 [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) 属性，将其设为 **true**。

{{% /alert %}}

## **删除工作表中的空白列和行时更新其他工作表中的引用**

请参阅以下示例代码及其控制台输出。第二个工作表中的单元格E3包含公式 `=Sheet1!C3`，引用第一个工作表中的C3单元格。如果将 [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) 属性设为 **true**，在删除第一个工作表中的空白列和行后，此公式将被更新为 `=Sheet1!A1`。但如果将 [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) 属性设为 **false**，则第二个工作表的E3单元格中的公式将保持为 `=Sheet1!C3`，并变得无效。

### **编程示例**

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

### **控制台输出**

当 [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) 属性设置为 **true** 时，上述示例代码的控制台输出。

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

当 [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) 属性设置为 **false** 时，上述示例代码的控制台输出。如图所示，第二个工作表中单元格E3中的公式未更新，其单元格值现为0而不是4，这是无效的。

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
