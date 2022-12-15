---
title: 条件格式
type: docs
weight: 120
url: /zh/java/conditional-formatting/
---
{{% alert color="primary" %}} 

条件格式是一项高级 Microsoft Excel 功能，允许您将格式应用于单元格或单元格区域，并根据单元格的值或公式的值更改格式。例如，您可以让单元格仅在单元格的值大于 500 时显示为粗体。当单元格的值满足条件时，指定的格式将应用于单元格。如果单元格的值不满足条件，则使用默认格式。在 Microsoft Excel 中，选择**格式**， 然后**条件格式**打开条件格式对话框。

**Microsoft Excel 中的条件格式** 

![待办事项：图像_替代_文本](conditional-formatting_1.png)

Aspose.Cells 支持在运行时对单元格应用条件格式。这篇文章解释了如何。

{{% /alert %}} 
## **应用条件格式**
Aspose.Cells 通过两种方式支持条件格式：

- [使用设计器电子表格](/cells/zh/java/conditional-formatting/).
- [在运行时创建条件格式](/cells/zh/java/conditional-formatting/).
### **使用设计器电子表格**
开发人员可以在 Microsoft Excel 中创建包含条件格式的设计器电子表格，然后使用 Aspose.Cells 打开该电子表格。Aspose.Cells 加载并保存设计器电子表格，同时保留任何条件格式设置。要了解有关设计器电子表格的更多信息，请阅读[什么是设计器电子表格](/cells/zh/java/what-is-a-designer-spreadsheet/).
## **在运行时应用条件格式**
Aspose.Cells 支持在运行时应用条件格式。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ConditionalFormattingatRuntime-ConditionalFormattingatRuntime.java" >}}
### **设置字体**
**在 Microsoft Excel 中设置字体** 

![待办事项：图像_替代_文本](conditional-formatting_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontStyle-SettingFontStyle.java" >}}
### **设置边框**
**在 Microsoft Excel 中设置边框** 

![待办事项：图像_替代_文本](conditional-formatting_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetBorder-SetBorder.java" >}}
### **设置模式**
**在 Microsoft Excel 中设置单元格模式** 

![待办事项：图像_替代_文本](conditional-formatting_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetPattern-SetPattern.java" >}}

## **推进主题**
- [添加使用 Cell 文本设置的条件图标](/cells/zh/java/add-conditional-icons-set-with-the-cell-text/)
- [添加 2 色标和 3 色标条件格式](/cells/zh/java/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [在工作表中应用条件格式](/cells/zh/java/apply-conditional-formatting-in-worksheets/)
- [使用条件格式将底纹应用于交替行和列](/cells/zh/java/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)

