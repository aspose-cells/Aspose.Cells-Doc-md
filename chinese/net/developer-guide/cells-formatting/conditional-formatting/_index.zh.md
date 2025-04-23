---
title: 设置Excel和ODS文件的条件格式。
linktitle: 条件格式
type: docs
weight: 60
url: /zh/net/conditional-formatting/
description: 如何在C#中应用Excel和ODS文件的条件格式。
keywords: 应用条件格式 
---

## **介绍**

条件格式是Microsoft Excel的高级功能，允许您对单元格或一系列单元格应用格式，并根据单元格的数值或公式的值更改格式。例如，只有当单元格的值大于500时，该单元格才会显示为粗体。当单元格的值满足条件时，会将指定的格式应用到单元格。如果单元格的值不符合格式条件，则使用单元格的默认格式。在Microsoft Excel中，选择**格式**，然后选择**条件格式**以打开条件格式对话框。

Aspose.Cells支持在运行时将条件格式应用于单元格。本文解释了如何实现这一点。它还解释了如何计算Excel用于颜色标度条件格式的颜色。

## **应用条件格式**

Aspose.Cells支持多种方式的条件格式：

- 使用设计师电子表格
- 使用复制方法。
- 在运行时创建条件格式。

### **使用设计者电子表格**

开发人员可以在Microsoft Excel中创建一个包含条件格式的设计师电子表格，然后用Aspose.Cells打开该电子表格。Aspose.Cells加载并保存设计师电子表格，并保留任何条件格式设置。

### **使用复制方法**

Aspose.Cells允许开发人员通过调用[**Range.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index)方法将一个单元格的条件格式设置复制到工作表中的另一个单元格。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-UsingCopyMethod-1.cs" >}}

## **在运行时应用条件格式**

Aspose.Cells允许您在运行时添加和删除条件格式。下面的代码示例显示了如何设置条件格式：

1. 实例化一个工作簿。
1. 添加一个空的条件格式。
1. 设置应用格式的范围。
1. 定义格式条件。
1. 保存文件。

在此示例之后还有许多其他小示例，演示如何应用字体设置、边框设置和图案。

Microsoft Excel 2007添加了更高级的条件格式设置，Aspose.Cells也支持。这里的示例说明了如何使用简单的格式设置，而Microsoft Excel 2007的示例则展示了如何应用更高级的条件格式设置。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConditionalFormattingatRuntime-1.cs" >}}

### **设置字体**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-1.cs" >}}

{{% alert color="primary" %}}

您只能更改字体样式、文字颜色、下划线样式和删除线样式。

{{% /alert %}}

### **设置边框**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetBorder-1.cs" >}}

{{% alert color="primary" %}}

您只能使用细线样式来设置轮廓边框，不允许使用对角线。

{{% /alert %}}

### **设置填充**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetPattern-1.cs" >}}

## **高级主题**
- [添加2色阶和3色阶条件格式](/cells/zh/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [应用高级条件格式](/cells/zh/net/apply-advanced-conditional-formatting/)
- [应用工作表中的条件格式](/cells/zh/net/apply-conditional-formatting-in-worksheets/)
- [使用条件格式为交替的行和列添加阴影](/cells/zh/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [生成条件格式设置数据条图像](/cells/zh/net/generate-conditional-formatting-databars-images/)
- [获取在条件格式设置中使用的图标集、数据条或颜色刻度对象](/cells/zh/net/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)

{{< app/cells/assistant language="csharp" >}}
