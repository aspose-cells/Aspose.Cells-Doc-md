---
title: 条件格式设置
type: docs
weight: 120
url: /zh/java/conditional-formatting/
---

{{% alert color="primary" %}} 

条件格式设置是Microsoft Excel的高级功能，允许您对单元格或一系列单元格应用格式，并根据单元格的值或公式的值进行更改。例如，只有当单元格的值大于500时，单元格才会显示为粗体。当单元格的值满足条件时，将应用指定格式到单元格。如果单元格的值不满足条件，则使用默认格式。在Microsoft Excel中，选择**格式**，然后**条件格式**来打开条件格式设置对话框。

**Microsoft Excel中的条件格式设置** 

![todo:image_alt_text](conditional-formatting_1.png)

Aspose.Cells支持在运行时向单元格应用条件格式。本文介绍了如何实现这一点。

{{% /alert %}} 
## **应用条件格式**
Aspose.Cells支持两种方式的条件格式：

- [使用设计者电子表格](/cells/zh/java/conditional-formatting/)
- [在运行时创建条件格式](/cells/zh/java/conditional-formatting/)
### **使用设计者电子表格**
开发人员可以在Microsoft Excel中创建包含条件格式设置的设计者电子表格，然后使用Aspose.Cells打开该电子表格。Aspose.Cells加载和保存设计者电子表格，保留任何条件格式设置。欲了解更多有关设计者电子表格的信息，请阅读[设计者电子表格是什么](/cells/zh/java/what-is-a-designer-spreadsheet/)
## **在运行时应用条件格式**
Aspose.Cells支持在运行时应用条件格式。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ConditionalFormattingatRuntime-ConditionalFormattingatRuntime.java" >}}
### **设置字体**
**在Microsoft Excel中设置字体** 

![todo:image_alt_text](conditional-formatting_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontStyle-SettingFontStyle.java" >}}
### **设置边框**
**在Microsoft Excel中设置边框** 

![todo:image_alt_text](conditional-formatting_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetBorder-SetBorder.java" >}}
### **设置填充**
**在Microsoft Excel中设置单元格填充** 

![todo:image_alt_text](conditional-formatting_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetPattern-SetPattern.java" >}}

## **高级主题**
- [使用单元格文本添加条件图标集](/cells/zh/java/add-conditional-icons-set-with-the-cell-text/)
- [添加2色阶和3色阶条件格式](/cells/zh/java/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [应用工作表中的条件格式](/cells/zh/java/apply-conditional-formatting-in-worksheets/)
- [使用条件格式为交替的行和列添加阴影](/cells/zh/java/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)

