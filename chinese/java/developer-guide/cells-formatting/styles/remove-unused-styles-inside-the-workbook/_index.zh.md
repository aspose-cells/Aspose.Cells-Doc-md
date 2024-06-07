---
title: 删除工作簿中未使用的样式
type: docs
weight: 470
url: /zh/java/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}} 

在Excel文件中未使用的样式不仅占用空间，还会导致在转换为PDF、HTML等不同格式时性能问题。Aspose.Cells提供了[Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles\(\))以删除工作簿中的所有未使用样式。

{{% /alert %}} 
## **删除工作簿中的未使用样式**
以下代码解释了如何使用[Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles\(\))。该代码加载了[模板excel文件](5473451.xlsx)，您可以从提供的链接下载。它包含一个名为**AsposeStyle**的未使用样式，在执行代码后，此样式以及所有其他未使用的样式将被移除。请查看以下截图以获取更多说明。

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RemoveUnusedStyles-RemoveUnusedStyles.java" >}}
