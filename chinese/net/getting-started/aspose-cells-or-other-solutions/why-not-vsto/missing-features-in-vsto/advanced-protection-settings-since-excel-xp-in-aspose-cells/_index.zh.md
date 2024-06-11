---
title: 自Aspose.Cells中的Excel XP以来的高级保护设置
type: docs
weight: 20
url: /zh/net/advanced-protection-settings-since-excel-xp-in-aspose-cells/
---

{{% alert color="primary" %}}

- 删除行或列。
- 编辑内容、对象或方案。
- 格式化单元格、行或列。
- 插入行、列或超链接。
- 选择锁定或解锁的单元格。
- 使用数据透视表等功能。

Aspose.Cells支持Excel XP或更高版本提供的所有高级保护设置。

{{% /alert %}}

## **使用Excel XP和更高版本的高级保护设置**

要查看Excel XP中提供的保护设置：

1. 从**工具**菜单中选择**保护**，然后选择**保护工作表**。
   将显示对话框。

   **在Excel XP中显示保护选项的对话框**

![todo:image_alt_text](advanced-protection-settings-since-excel-xp-in-aspose-cells_1.png)

1. 允许或限制工作表功能或应用密码。

### **使用Aspose.Cells的高级保护设置**

Aspose.Cells支持所有高级保护设置。

Aspose.Cells 提供了一个类，[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，它代表一个 Microsoft Excel 文件。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类包含一个 [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) 集合，允许访问 Excel 文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类表示。

[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类提供了 [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) 属性，用于应用这些高级保护设置。[**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) 属性实际上是 [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/protection) 类的对象，封装了几个布尔属性，用于禁用或启用限制。

下面是一个小例子应用程序。它打开一个 Excel 文件，并使用 Excel XP 及更新版本支持的大部分高级保护设置。

**C#**

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook excel = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = excel.Worksheets[0];

//Restricting users to delete columns of the worksheet

worksheet.Protection.AllowDeletingColumn = false;

//Restricting users to delete row of the worksheet

worksheet.Protection.AllowDeletingRow = false;

//Restricting users to edit contents of the worksheet

worksheet.Protection.AllowEditingContent = false;

//Restricting users to edit objects of the worksheet

worksheet.Protection.AllowEditingObject = false;

//Restricting users to edit scenarios of the worksheet

worksheet.Protection.AllowEditingScenario = false;

//Restricting users to filter

worksheet.Protection.AllowFiltering = false;

//Allowing users to format cells of the worksheet

worksheet.Protection.AllowFormattingCell = true;

//Allowing users to format rows of the worksheet

worksheet.Protection.AllowFormattingRow = true;

//Allowing users to insert columns in the worksheet

worksheet.Protection.AllowFormattingColumn = true;

//Allowing users to insert hyperlinks in the worksheet

worksheet.Protection.AllowInsertingHyperlink = true;

//Allowing users to insert rows in the worksheet

worksheet.Protection.AllowInsertingRow = true;

//Allowing users to select locked cells of the worksheet

worksheet.Protection.AllowSelectingLockedCell = true;

//Allowing users to select unlocked cells of the worksheet

worksheet.Protection.AllowSelectingUnlockedCell = true;

//Allowing users to sort

worksheet.Protection.AllowSorting = true;

//Allowing users to use pivot tables in the worksheet

worksheet.Protection.AllowUsingPivotTable = true;

//Saving the modified Excel file

excel.Save("output.xls", SaveFormat.Excel97To2003);

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Advanced%20Protection%20Settings)

## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
