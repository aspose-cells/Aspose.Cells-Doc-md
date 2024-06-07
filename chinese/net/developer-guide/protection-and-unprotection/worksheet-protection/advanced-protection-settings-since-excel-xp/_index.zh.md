---
title: 自Excel XP以来的高级保护设置
type: docs
weight: 30
url: /zh/net/advanced-protection-settings-since-excel-xp/
---

{{% alert color="primary" %}}

自Excel 2002或XP发布以来，Microsoft添加了许多高级保护设置。

{{% /alert %}}

## **介绍**

这些保护设置会限制或允许用户:

- 删除行或列。
- 编辑内容、对象或场景。
- 格式化单元格、行或列。
- 插入行、列或超链接。
- 选择锁定或解锁的单元格。
- 使用数据透视表等等。

Aspose.Cells支持Excel XP或更高版本提供的所有高级保护设置。

### **使用Excel XP和更高版本的高级保护设置**

查看Excel XP中可用的保护设置:

1. 从**工具**菜单中，选择**保护**，然后选择**保护工作表**。将显示一个对话框。

查看Excel 2016中可用的保护设置

1. 从**文件**菜单中选择**保护工作簿**，然后选择**保护当前工作表**。
1. 在**审阅**菜单中选择**保护工作表**。

按照上述步骤将显示一个对话框，您可以在其中允许或限制工作表功能，或为工作表应用密码。

### **使用Aspose.Cells进行高级保护设置**

Aspose.Cells支持所有高级保护设置。

Aspose.Cells提供一个代表Microsoft Excel文件的[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含了一个[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)集合，允许访问Excel文件中的每个工作表。一个工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。

[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了[**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection)属性，用于应用这些高级保护设置。[**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection)属性实际上是[**Protection**](https://reference.aspose.com/cells/net/aspose.cells/protection)类对象，封装了用于禁用或启用限制的几个布尔属性。

以下是一个简单的示例应用程序。它打开一个Excel文件，并使用Excel XP及更高版本支持的大多数高级保护设置。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-AdvancedProtectionSettings-1.cs" >}}

{{% alert color="primary" %}}

使用[**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection)属性时请勿调用[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类的[**Protect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index)方法。此外，将文件保存为Excel97至2003或Xlsx格式，因为高级保护设置仅受Excel XP及更高版本支持。

{{% /alert %}}

### **单元格锁定问题**

如果要限制用户编辑单元格，则必须在应用任何保护设置之前锁定单元格。否则，即使工作表受保护，也可以编辑单元格。在Microsoft Excel XP中，可以通过以下对话框锁定单元格：

|**Excel XP中锁定单元格的对话框**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

也可以使用Aspose.Cells API锁定单元格。每个单元格可以获取一个包含布尔属性[**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)的[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)格式。将[**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)属性设置为**true**或**false**以锁定或解锁单元格。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-LockCell-1.cs" >}}
