---
title: 设置Excel和ODS文件的条件格式。
linktitle: 条件格式
type: docs
weight: 60
url: /zh/python-net/conditional-formatting/
description: 在Python中如何应用条件格式到Excel和ODS文件中。
keywords: 应用条件格式 
---

## **介绍**

条件格式是Microsoft Excel的高级功能，允许您对单元格或一系列单元格应用格式，并根据单元格的数值或公式的值更改格式。例如，只有当单元格的值大于500时，该单元格才会显示为粗体。当单元格的值满足条件时，会将指定的格式应用到单元格。如果单元格的值不符合格式条件，则使用单元格的默认格式。在Microsoft Excel中，选择**格式**，然后选择**条件格式**以打开条件格式对话框。

Aspose.Cells for Python via .NET支持在运行时向单元格应用条件格式。本文将介绍如何操作，也会说明Excel的颜色尺度条件格式使用的颜色是如何计算的。

## **应用条件格式**

Aspose.Cells for Python via .NET支持多种条件格式：

- 使用设计师电子表格
- 使用复制方法。
- 在运行时创建条件格式。

### **使用设计者电子表格**

开发者可以创建一个包含条件格式的设计者电子表格，然后用Aspose.Cells for Python via .NET打开该电子表格。Aspose.Cells for Python via .NET会加载和保存设计者电子表格，并保留任何条件格式设置。

### **使用复制方法**

Aspose.Cells for Python via .NET 允许开发者通过调用 [**Range.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy) 方法将条件格式设置从一个单元格复制到工作表中的另一个单元格。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UsingCopyMethod-1.py" >}}

## **在运行时应用条件格式**

Aspose.Cells for Python via .NET 让您在运行时添加和删除条件格式。下面的示例展示了如何设置条件格式：

1. 实例化一个工作簿。
1. 添加一个空的条件格式。
1. 设置应用格式的范围。
1. 定义格式条件。
1. 保存文件。

在此示例之后还有许多其他小示例，演示如何应用字体设置、边框设置和图案。

Microsoft Excel 2007 添加了更高级的条件格式，Aspose.Cells for Python via .NET 也支持。这里列出的示例说明了如何使用简单格式，Microsoft Excel 2007 示例显示了如何应用更复杂的条件格式。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConditionalFormattingatRuntime-1.py" >}}

### **设置字体**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SettingFontStyle-1.py" >}}

{{% alert color="primary" %}}

您只能更改字体样式、文字颜色、下划线样式和删除线样式。

{{% /alert %}}

### **设置边框**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetBorder-1.py" >}}

{{% alert color="primary" %}}

您只能使用细线样式来设置轮廓边框，不允许使用对角线。

{{% /alert %}}

### **设置填充**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetPattern-1.py" >}}

## **高级主题**
- [添加2色阶和3色阶条件格式](/cells/zh/python-net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [应用工作表中的条件格式](/cells/zh/python-net/apply-conditional-formatting-in-worksheets/)
- [使用条件格式为交替的行和列添加阴影](/cells/zh/python-net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [生成条件格式设置数据条图像](/cells/zh/python-net/generate-conditional-formatting-databars-images/)
- [获取在条件格式设置中使用的图标集、数据条或颜色刻度对象](/cells/zh/python-net/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)

{{< app/cells/assistant language="csharp" >}}
{{< app/cells/assistant language="python-net" >}}
