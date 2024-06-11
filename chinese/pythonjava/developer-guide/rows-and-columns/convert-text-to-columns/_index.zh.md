---
title: 将文本转换为列
type: docs
weight: 10
url: /zh/python-java/convert-text-to-columns/
---

## **将文本转换为列**
您可以使用Microsoft Excel将文本转换为列。此功能在“数据”选项卡的“数据工具”下可用。为了将一列的内容拆分为多列，数据应包含特定的分隔符，如逗号（或任何其他字符），基于该分隔符，Microsoft Excel将单元格的内容拆分为多个单元格。Aspose.Cells也通过[TextToColumns](https://reference.aspose.com/cells/python/asposecells.api/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\))方法提供此功能。以下代码段演示了如何使用[TextToColumns](https://reference.aspose.com/cells/python/asposecells.api/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\))方法通过使用空格作为分隔符将文本转换为列。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "RowsAndColumns-ConvetTextToColumns.py" >}}
