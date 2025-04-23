---
title: 删除工作簿中的未使用样式
type: docs
weight: 470
url: /zh/java/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}} 

Excel文件中未使用的样式不仅占用空间，还可能导致转换为PDF、HTML等格式时的性能问题。Aspose.Cells提供了[Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles--)方法来删除工作簿中的所有未使用样式。

{{% /alert %}} 
## **在工作簿内移除未使用的样式**
以下代码演示了 [Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles--) 的用法。代码加载了一个[模板Excel文件](5473451.xlsx)，你可以通过提供的链接下载。文件中包含一个未使用的样式，名为 **AsposeStyle**，执行后该样式以及所有其他未使用的样式将被删除。以下截图提供了更直观的示意：

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RemoveUnusedStyles-RemoveUnusedStyles.java" >}}
{{< app/cells/assistant language="java" >}}
