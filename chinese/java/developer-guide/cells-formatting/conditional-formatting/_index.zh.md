---
title: 条件格式设置
type: docs
weight: 120
url: /zh/java/conditional-formatting/
---

{{% alert color="primary" %}} 

条件格式设置是Microsoft Excel的一项高级功能，允许您对单元格或单元格范围应用格式，并根据单元格的值或公式的值更改该格式。例如，只有当单元格的值大于500时，该单元格才会以粗体显示。当单元格的值符合条件时，将应用指定的格式。如果单元格的值不符合条件，则使用默认格式。在Microsoft Excel中，选择**格式**，然后选择**条件格式设置**以打开条件格式设置对话框。

**Microsoft Excel中的条件格式设置** 

![todo:image_alt_text](conditional-formatting_1.png)

Aspose.Cells支持在运行时对单元格应用条件格式设置。本文介绍了如何实现这一点。

{{% /alert %}} 
## **应用条件格式**
Aspose.Cells支持两种方式应用条件格式设置：

- [使用设计师电子表格](/cells/zh/java/条件格式设置/)。
- [在运行时创建条件格式设置](/cells/zh/java/条件格式设置/)。
### **使用设计器表格**
开发人员可以创建一个包含Microsoft Excel中条件格式设置的设计师电子表格，然后使用Aspose.Cells打开该电子表格。Aspose.Cells加载和保存设计师电子表格，保留任何条件格式设置。要了解有关设计师电子表格的更多信息，请阅读[什么是设计师电子表格](/cells/zh/java/什么是设计师电子表格/)。
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
### **设置图案**
**在Microsoft Excel中设置单元格模式** 

![todo:image_alt_text](conditional-formatting_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetPattern-SetPattern.java" >}}

## **高级主题**
- [使用单元格文本添加条件图标集](/cells/zh/java/add-conditional-icons-set-with-the-cell-text/)
- [添加2色比例和3色比例条件格式](/cells/zh/java/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [在工作表中应用条件格式](/cells/zh/java/apply-conditional-formatting-in-worksheets/)
- [使用条件格式为交替行和列着色](/cells/zh/java/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)

