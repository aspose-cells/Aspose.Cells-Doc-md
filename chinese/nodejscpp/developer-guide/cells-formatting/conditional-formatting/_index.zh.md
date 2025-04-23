---  
title: 设置 Excel 和 ODS 文件的条件格式
linktitle: 条件格式  
type: docs  
weight: 60  
url: /zh/nodejs-cpp/conditional-formatting/  
description: 如何在 Node.js 和 C++ 中对 Excel 和 ODS 文件应用条件格式。  
keywords: 通过 C++ 在 Node.js 中应用条件格式  
---  

## **介绍**

条件格式是一项高级功能，允许您对单元格或单元格范围应用格式，并根据单元格的值或公式的值改变该格式。例如，只有当单元格的值大于 500 时，单元格才显示为加粗。当单元格满足条件时，指定的格式会应用到单元格；如果不满足条件，则使用单元格的默认格式。在 Microsoft Excel 中，选择 **格式**，然后选择 **条件格式** 来打开条件格式对话框。

Aspose.Cells支持在运行时将条件格式应用于单元格。本文解释了如何实现这一点。它还解释了如何计算Excel用于颜色标度条件格式的颜色。

## **应用条件格式**

Aspose.Cells支持多种方式的条件格式：

- 使用设计师电子表格
- 使用复制方法。
- 在运行时创建条件格式。

### **使用设计者电子表格**

开发人员可以在Microsoft Excel中创建一个包含条件格式的设计师电子表格，然后用Aspose.Cells打开该电子表格。Aspose.Cells加载并保存设计师电子表格，并保留任何条件格式设置。

### **使用复制方法**

Aspose.Cells允许开发人员通过调用[**Range.copy()**](https://reference.aspose.com/cells/nodejs-cpp/range/#copy-range-)方法将一个单元格的条件格式设置复制到工作表中的另一个单元格。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-CopyConditionalFormattsByCopyRange.js" >}}


## **在运行时应用条件格式**

Aspose.Cells允许您在运行时添加和删除条件格式。下面的代码示例显示了如何设置条件格式：

1. 实例化一个工作簿。
1. 添加一个空的条件格式。
1. 设置应用格式的范围。
1. 定义格式条件。
1. 保存文件。

在此示例之后还有许多其他小示例，演示如何应用字体设置、边框设置和图案。

Microsoft Excel 2007 增加了更高级的条件格式，Aspose.Cells 也支持。这里的示例展示如何使用简单的格式，而 Microsoft Excel 2007 的示例则显示如何应用更复杂的条件格式。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-ApplyingConditionalFormattingAtRuntime.js" >}}


### **设置字体**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-SetFont.js" >}}



{{% alert color="primary" %}}

您只能更改字体样式、文字颜色、下划线样式和删除线样式。

{{% /alert %}}

### **设置边框**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-SetBorder.js" >}}


{{% alert color="primary" %}}

您只能使用细线样式作为轮廓边框。禁止使用对角线。

{{% /alert %}}

### **设置填充**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-SetPattern.js" >}}



## **高级主题**  
- [添加2色阶和3色阶条件格式](/cells/zh/nodejs-cpp/adding-2-color-scale-and-3-color-scale-conditional-formattings/)  
- [应用工作表中的条件格式](/cells/zh/nodejs-cpp/apply-conditional-formatting-in-worksheets/)  
- [使用条件格式为交替的行和列添加阴影](/cells/zh/nodejs-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)  
- [生成条件格式设置数据条图像](/cells/zh/nodejs-cpp/generate-conditional-formatting-databars-images/)  
- [获取在条件格式设置中使用的图标集、数据条或颜色刻度对象](/cells/zh/nodejs-cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)  


