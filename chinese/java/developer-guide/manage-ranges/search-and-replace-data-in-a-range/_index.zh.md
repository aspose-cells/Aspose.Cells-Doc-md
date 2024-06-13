---
title: 在 Excel 中使用 C# 代码搜索和替换范围内的数据
type: docs
weight: 60
url: /zh/java/search-and-replace-data-in-a-range/
description: 本文介绍了如何使用Java代码在Excel中搜索和替换范围内的数据。
keywords: Java在Excel中搜索和替换数据，Java在Excel中搜索数据，Java在Excel中搜索和替换数据，Java在范围内搜索和替换数据，Java在范围内搜索数据，Java在范围内搜索和替换数据，Java在范围中搜索和替换数据，Java在范围中搜索数据，Java在范围中搜索和替换数据，使用Java在Excel中搜索和替换数据，使用Java在范围中搜索和替换数据，使用Java在范围中搜索和替换数据
---

{{% alert color="primary" %}}

有时，您需要在范围内搜索并替换特定数据，忽略范围之外的任何单元格值。Aspose.Cells允许您把搜索限制在特定范围内。本文将对此进行详细解释。

{{% /alert %}}

Aspose.Cells 提供了用于在搜索数据时指定范围的 [**FindOptions.setRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#setRange(com.aspose.cells.CellArea)) 方法。

假设您想要在范围E3:H6中搜索字符串**"search"**并将其替换为**"replace"**。在下面的屏幕截图中，可以看到字符串"search"出现在多个单元格中，但我们只想在给定范围内进行替换，此处用黄色突出显示。

输入文件

![todo:image_alt_text](search-and-replace-data-in-a-range_1.png)

执行代码后，输出文件的外观如下。范围内的所有"search"字符串都已被替换为"replace"。

**输出文件**

![todo:image_alt_text](search-and-replace-data-in-a-range_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchReplaceDataInRange-SearchReplaceDataInRange.java" >}}

## 相关文章

- [查找或搜索数据](/cells/zh/java/find-or-search-data/)
