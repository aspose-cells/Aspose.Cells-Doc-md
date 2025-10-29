---
title: 使用C++的高级保护设置（自Excel XP起）
linktitle: 自Excel XP以来的高级保护设置
type: docs
weight: 30
url: /zh/cpp/advanced-protection-settings-since-excel-xp/
description: 学习如何使用Aspose.Cells结合C++应用Excel文件中的高级保护设置。
---

{{% alert color="primary" %}}

自Excel 2002或XP发布以来，微软已添加了许多高级保护设置。

{{% /alert %}}

## **介绍**

这些保护设置限制或允许用户:

- 删除行或列。
- 编辑内容、对象或场景。
- 格式化单元格、行或列。
- 插入行、列或超链接。
- 选择锁定或解锁的单元格。
- 使用数据透视表等功能。

Aspose.Cells支持Excel XP或更高版本提供的所有高级保护设置。

### **使用Excel XP和更高版本的高级保护设置**

要查看Excel XP中提供的保护设置：

1. 从**工具**菜单中选择**保护**，然后选择**保护工作表**。将显示一个对话框。

 在Excel 2016中查看可用的保护设置：

1. 从**文件**菜单中选择**保护工作簿**，然后选择**保护当前工作表**。
1. 在**审阅**菜单中选择**保护工作表**。

 按照上述步骤操作，将弹出一个对话框，您可以在其中允许或限制工作表功能，或为工作表设置密码。

### **使用Aspose.Cells的高级保护设置**

Aspose.Cells支持所有高级保护设置。

Aspose.Cells 提供了一个类，[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)，它代表一个 Microsoft Excel 文件。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) 类包含一个 [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) 集合，允许访问 Excel 文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类表示。

[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类提供了 [**GetProtection()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getprotection/) 属性，用于应用这些高级保护设置。[**GetProtection()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getprotection/) 属性实际上是 [**Protection**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/) 类的对象，封装了几个布尔属性，用于禁用或启用限制。

下面是一个小例子应用程序。它打开一个 Excel 文件，并使用 Excel XP 及更新版本支持的大部分高级保护设置。

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook
    Workbook excel(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = excel.GetWorksheets().Get(0);

    // Restricting users to delete columns of the worksheet
    worksheet.GetProtection().SetAllowDeletingColumn(false);

    // Restricting users to delete row of the worksheet
    worksheet.GetProtection().SetAllowDeletingRow(false);

    // Restricting users to edit contents of the worksheet
    worksheet.GetProtection().SetAllowEditingContent(false);

    // Restricting users to edit objects of the worksheet
    worksheet.GetProtection().SetAllowEditingObject(false);

    // Restricting users to edit scenarios of the worksheet
    worksheet.GetProtection().SetAllowEditingScenario(false);

    // Restricting users to filter
    worksheet.GetProtection().SetAllowFiltering(false);

    // Allowing users to format cells of the worksheet
    worksheet.GetProtection().SetAllowFormattingCell(true);

    // Allowing users to format rows of the worksheet
    worksheet.GetProtection().SetAllowFormattingRow(true);

    // Allowing users to format columns of the worksheet
    worksheet.GetProtection().SetAllowFormattingColumn(true);

    // Allowing users to insert hyperlinks in the worksheet
    worksheet.GetProtection().SetAllowInsertingHyperlink(true);

    // Allowing users to insert rows in the worksheet
    worksheet.GetProtection().SetAllowInsertingRow(true);

    // Allowing users to select locked cells of the worksheet
    worksheet.GetProtection().SetAllowSelectingLockedCell(true);

    // Allowing users to select unlocked cells of the worksheet
    worksheet.GetProtection().SetAllowSelectingUnlockedCell(true);

    // Allowing users to sort
    worksheet.GetProtection().SetAllowSorting(true);

    // Allowing users to use pivot tables in the worksheet
    worksheet.GetProtection().SetAllowUsingPivotTable(true);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    excel.Save(outputFilePath, SaveFormat::Excel97To2003);

    Aspose::Cells::Cleanup();

    return 0;
}
```

{{% alert color="primary" %}}

 在使用 [**GetProtection()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getprotection/) 属性时，请勿调用 [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类的 [**Protect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/) 方法。此外，应将文件保存为Excel97至2003或Xlsx格式，因为高级保护设置只支持Excel XP及更高版本。

{{% /alert %}}

### **单元格锁定问题**

 如果要限制用户编辑单元格，必须在应用任何保护设置之前将单元格锁定。否则，即使工作表受保护，单元格仍可编辑。在Microsoft Excel XP中，可以通过以下对话框锁定单元格：

|**在Excel XP中锁定单元格的对话框**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

也可以使用 Aspose.Cells API 来锁定单元格。每个单元格可以获得 [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) 格式，其中包含一个布尔属性 [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/)。将 [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) 属性设置为 **true** 或 **false**，即可锁定或解锁单元格。

```cpp
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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Lock the style of cell A1
    worksheet.GetCells().Get(u"A1").GetStyle().SetIsLocked(true);

    // Protect the sheet
    worksheet.Protect(ProtectionType::All);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Worksheet protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
