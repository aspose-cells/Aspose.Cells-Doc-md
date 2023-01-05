---
title: 设置 Excel 和 ODS 文件的条件格式。
linktitle: 条件格式
type: docs
weight: 60
url: /zh/net/conditional-formatting/
description: 如何在 CSharp 中将条件格式应用于 Excel 和 ODS 文件。
keywords: apply conditional formats 
---
## **介绍**

条件格式是一项高级 Microsoft Excel 功能，允许您将格式应用于单元格或单元格区域，并根据单元格的值或公式的值更改格式。例如，您可以让单元格仅在单元格的值大于 500 时显示为粗体。当单元格的值满足条件时，指定的格式将应用于单元格。如果单元格的值不满足格式条件，则使用单元格的默认格式。在 Microsoft Excel 中，选择**格式**， 然后**条件格式**打开条件格式对话框。

Aspose.Cells 支持在运行时对单元格应用条件格式。这篇文章解释了如何。它还解释了如何计算 Excel 用于色标条件格式的颜色。

## **应用条件格式**

Aspose.Cells 通过几种方式支持条件格式：

- 使用设计器电子表格
- 使用复制方法。
- 在运行时创建条件格式。

### **使用设计器电子表格**

开发人员可以在 Microsoft Excel 中创建包含条件格式的设计器电子表格，然后使用 Aspose.Cells 打开该电子表格。Aspose.Cells 加载并保存设计器电子表格，同时保留任何条件格式设置。

### **使用复制方法**

Aspose.Cells 允许开发人员通过调用[**范围.复制()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index)方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-UsingCopyMethod-1.cs" >}}

## **在运行时应用条件格式**

Aspose.Cells 允许您在运行时添加和删除条件格式。下面的代码示例显示了如何设置条件格式：

1. 实例化工作簿。
1. 添加一个空的条件格式。
1. 设置格式应适用的范围。
1. 定义格式化条件。
1. 保存文件。

在这个示例之后是许多其他较小的示例，这些示例展示了如何应用字体设置、边框设置和图案。

Microsoft Excel 2007 添加了 Aspose.Cells 也支持的更高级的条件格式。此处的示例说明如何使用简单格式，Microsoft Excel 2007 示例说明如何应用更高级的条件格式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConditionalFormattingatRuntime-1.cs" >}}

### **设置字体**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-1.cs" >}}

{{% alert color="primary" %}}

您只能更改字体样式、文本颜色、下划线样式和删除线样式。

{{% /alert %}}

### **设置边框**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetBorder-1.cs" >}}

{{% alert color="primary" %}}

您只能对轮廓边框使用细线样式。不允许使用对角线。

{{% /alert %}}

### **设置模式**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetPattern-1.cs" >}}

## **推进主题**
- [添加 2 色标和 3 色标条件格式](/cells/zh/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [应用高级条件格式](/cells/zh/net/apply-advanced-conditional-formatting/)
- [在工作表中应用条件格式](/cells/zh/net/apply-conditional-formatting-in-worksheets/)
- [使用条件格式将底纹应用于交替行和列](/cells/zh/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [生成条件格式 DataBars 图像](/cells/zh/net/generate-conditional-formatting-databars-images/)
- [获取条件格式中使用的图标集、数据条或色标对象](/cells/zh/net/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)

