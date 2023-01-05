---
title: 搜索和替换范围内的数据
type: docs
weight: 60
url: /zh/java/search-and-replace-data-in-a-range/
description: 本文介绍如何使用 Java 代码在 Excel 中搜索和替换范围内的数据。
keywords: java search and replace data in excel, java search data in excel, java search and replace data in a range, java search data in a range, java searching data in a range, java searching data in range, java searching data in excel, java search data in range, search and replace data in excel with java, search and replace data in a range with java, search and replace data in range with java
---
{{% alert color="primary" %}}

有时，您需要搜索和替换范围内的特定数据，忽略所需范围之外的任何单元格值。 Aspose.Cells 允许您将搜索限制在特定范围内。这篇文章解释了如何。

{{% /alert %}}

Aspose.Cells 提供了[**FindOptions.setRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#setRange(com.aspose.cells.CellArea)) 搜索数据时指定范围的方法。

假设你想搜索字符串**“搜索”**并将其替换为**“代替”**范围中**E3:H6**.在下面的屏幕截图中，可以在多个单元格中看到字符串“search”，但我们只想在给定范围内替换它，此处以黄色突出显示。

**输入文件**

![待办事项：图片_替代_文本](search-and-replace-data-in-a-range_1.png)

代码执行后，输出文件如下所示。范围内的所有“搜索”字符串都已替换为“替换”。

**输出文件**

![待办事项：图片_替代_文本](search-and-replace-data-in-a-range_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchReplaceDataInRange-SearchReplaceDataInRange.java" >}}

## 相关文章

- [查找或搜索数据](/cells/zh/java/find-or-search-data/)
