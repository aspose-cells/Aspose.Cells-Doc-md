---
title: 在范围内搜索和替换数据
type: docs
weight: 60
url: /zh/java/search-and-replace-data-in-a-range/
description: 本文展示如何使用Java代码在Excel中搜索和替换数据范围。
keywords: java在excel中搜索和替换数据，java在excel中搜索数据，java搜索和替换数据在一个范围内，在范围内搜索数据，java在范围内搜索数据，在范围内搜索数据，java在excel中搜索数据，java在范围内搜索数据，用java在excel中搜索和替换数据，在一个范围内用java搜索和替换数据，在范围内用java搜索和替换数据
---

{{% alert color="primary" %}}

有时，您需要搜索并替换特定范围内的数据，忽略所需范围之外的任何单元格值。Aspose.Cells允许您将搜索限制为特定范围。本文对此进行了解释。

{{% /alert %}}

Aspose.Cells提供了[**FindOptions.setRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#setRange(com.aspose.cells.CellArea))方法，用于在搜索数据时指定范围。

假设您想要在范围E3:H6中搜索字符串"search"并替换为"replace"。如下方的屏幕截图所示，在几个单元格中可以看到字符串"search"，但我们只想在给定范围内替换它，这里用黄色突出显示。

**输入文件**

![todo:image_alt_text](search-and-replace-data-in-a-range_1.png)

执行代码后，输出文件如下所示。范围内的所有"search"字符串都已替换为"replace"。

**输出文件**

![todo:image_alt_text](search-and-replace-data-in-a-range_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchReplaceDataInRange-SearchReplaceDataInRange.java" >}}

## 相关文章

- [查找或搜索数据](/cells/zh/java/find-or-search-data/)
