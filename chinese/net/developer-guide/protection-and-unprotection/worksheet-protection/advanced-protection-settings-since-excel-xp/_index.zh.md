---
title: 自 Excel XP 以来的高级保护设置
type: docs
weight: 30
url: /zh/net/advanced-protection-settings-since-excel-xp/
---
{{% alert color="primary" %}}

自 Excel 2002 或 XP 发布以来，Microsoft 添加了许多高级保护设置。

{{% /alert %}}

## **介绍**

这些保护设置限制或允许用户：

- 删除行或列。
- 编辑内容、对象或场景。
- 格式化单元格、行或列。
- 插入行、列或超链接。
- 选择锁定或解锁的单元格。
- 使用数据透视表等等。

Aspose.Cells 支持 Excel XP 或更高版本提供的所有高级保护设置。

### **使用 Excel XP 及更高版本的高级保护设置**

查看 Excel XP 中可用的保护设置：

1. 来自**工具**菜单，选择**保护**其次是**保护表**.将显示一个对话框。

查看 Excel 2016 中可用的保护设置

1. 来自**文件**菜单，选择**保护工作簿**其次是**保护当前工作表**.
1. 选择**保护表**在里面**审查**菜单。

按照上面提到的步骤将显示一个对话框，您可以在其中允许或限制工作表功能或将密码应用于工作表。

### **使用 Aspose.Cells 的高级保护设置**

Aspose.Cells 支持所有高级保护设置。

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，代表一个 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)允许访问 Excel 文件中每个工作表的集合。工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。

这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了[**保护**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection)用于应用这些高级保护设置的属性。这[**保护**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection)财产实际上是[**保护**](https://reference.aspose.com/cells/net/aspose.cells/protection)封装了几个用于禁用或启用限制的布尔属性的类。

下面是一个小的示例应用程序。它打开一个 Excel 文件并使用 Excel XP 和更高版本支持的大部分高级保护设置。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-AdvancedProtectionSettings-1.cs" >}}

{{% alert color="primary" %}}

请不要致电[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级'[**保护**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index)使用时的方法[**保护**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection)财产。另外，将文件保存为 Excel97To2003 或 Xlsx 格式，因为高级保护设置仅 Excel XP 及更高版本支持。

{{% /alert %}}

### **Cell 锁定问题**

如果要限制用户编辑单元格，则必须在应用任何保护设置之前锁定单元格。否则，即使工作表受到保护，也可以编辑单元格。在 Microsoft Excel XP 中，可以通过以下对话框锁定单元格：

|**在 Excel XP 中锁定单元格的对话框**|
|:- |
|![待办事项：图像_替代_文本](advanced-protection-settings-since-excel-xp_1.png)|

也可以使用 Aspose.Cells API 锁定单元格。每个细胞都能得到[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)包含布尔属性的格式，[**被锁住了**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked).设置[**被锁住了**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)财产给**真的**或者**错误的**锁定或解锁单元格。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-LockCell-1.cs" >}}
