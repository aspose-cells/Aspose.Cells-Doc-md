---
title: 自Excel XP以来的高级保护设置
type: docs
weight: 30
url: /zh/net/advanced-protection-settings-since-excel-xp/
---

{{% alert color="primary" %}}

自Excel 2002或XP发布以来，微软已添加了许多高级保护设置。

{{% /alert %}}

## **介绍**

这些保护设置限制或允许用户:

- 删除行或列。
- 编辑内容、对象或方案。
- 格式化单元格、行或列。
- 插入行、列或超链接。
- 选择锁定或解锁的单元格。
- 使用数据透视表等功能。

Aspose.Cells支持Excel XP或更高版本提供的所有高级保护设置。

### **使用Excel XP和更高版本的高级保护设置**

要查看Excel XP中提供的保护设置：

1. 从**工具**菜单中选择**保护**，然后选择**保护工作表**。将显示一个对话框。

要查看Excel 2016中提供的保护设置

1. 从**文件**菜单中选择**保护工作簿**，然后选择**保护当前工作表**。
1. 在**审阅**菜单中选择**保护工作表**。

按上述步骤将显示一个对话框，您可以在其中允许或限制工作表功能或向工作表添加密码。

### **使用Aspose.Cells的高级保护设置**

Aspose.Cells支持所有高级保护设置。

Aspose.Cells提供了一个代表Microsoft Excel文件的类[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)集合，允许访问Excel文件中的每个工作表。一个工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。

[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了[**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection)属性，用于应用这些高级保护设置。[**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection)属性实际上是[**Protection**](https://reference.aspose.com/cells/net/aspose.cells/protection)类的对象，封装了用于禁用或启用限制的几个布尔属性。

下面是一个小例子应用程序。它打开一个 Excel 文件，并使用 Excel XP 及更新版本支持的大部分高级保护设置。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-AdvancedProtectionSettings-1.cs" >}}

{{% alert color="primary" %}}

在使用[**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection)属性时，请不要调用[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类的[**Protect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index)方法。此外，将文件保存为Excel97To2003或Xlsx格式，因为高级保护设置仅受Excel XP及以后版本支持。

{{% /alert %}}

### **单元格锁定问题**

如果您希望限制用户编辑单元格，则需要在应用任何保护设置之前锁定单元格。否则，即使工作表受到保护，用户也可以编辑单元格。在Microsoft Excel XP中，可以通过以下对话框锁定单元格：

|**在Excel XP中锁定单元格的对话框**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

也可以使用Aspose.Cells API锁定单元格。每个单元格可以获得包含布尔属性[**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)的[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)格式。将[**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)属性设置为**true**或**false**以锁定或解锁单元格。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-LockCell-1.cs" >}}
