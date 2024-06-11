---
title: 删除工作簿中的未使用样式
type: docs
weight: 470
url: /zh/java/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}} 

Excel文件中未使用的样式不仅占用空间，而且在转换为PDF、HTML等不同格式时会导致性能问题。Aspose.Cells提供[Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles\(\))来移除工作簿内的所有未使用样式。

{{% /alert %}} 
## **在工作簿内移除未使用的样式**
以下代码解释了[Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles\(\))的用法。该代码加载了您可以从提供的链接下载的[模板Excel文件](5473451.xlsx)。它包含一个名为**AsposeStyle**的未使用样式，此样式和所有其他未使用样式将在执行代码后被移除。请参阅以下屏幕截图以获取更多说明。

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RemoveUnusedStyles-RemoveUnusedStyles.java" >}}
