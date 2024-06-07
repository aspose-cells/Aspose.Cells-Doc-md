---
title: 格式化列表对象
type: docs
weight: 30
url: /zh/python-java/formatting-list-object/
---

## **格式化列表对象**
表是一系列包含相关数据的行和列，独立管理于其他行和列中的数据。默认情况下，表中的每列都启用了标头行中的筛选，因此您可以快速筛选或排序列表对象数据。您可以为列表对象添加一个总行（列表中提供用于处理数值数据的聚合函数的下拉列表框），从而使总行单元可用的下拉列表框用于每个总行单元格。

Aspose.Cells支持对列表对象进行格式化。为此，API提供了[ListObject](https://reference.aspose.com/cells/python/asposecells.api/ListObject)和[TableStyleType](https://reference.aspose.com/cells/python/asposecells.api/TableStyleType)类。TableStyleType类中包含表示内置表样式的常量。以下代码片段创建一个新的列表对象并将其表格样式类型设置为[TABLE_STYLE_MEDIUM_10](https://reference.aspose.com/cells/python/asposecells.api/tablestyletype#TABLE_STYLE_MEDIUM_10)



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-FormatListObject.py" >}}
