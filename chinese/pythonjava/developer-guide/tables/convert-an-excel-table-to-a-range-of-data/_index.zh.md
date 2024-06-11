---
title: 将Excel表转换为数据范围
type: docs
weight: 10
url: /zh/python-java/convert-an-excel-table-to-a-range-of-data/
---

## **将Excel表转换为数据范围**
Aspose.Cells for Python via Java提供将Excel表转换为数据范围的选项。为此，API提供了[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\))方法。以下代码段演示了使用[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\))方法将Excel表转换为数据范围。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRange.py" >}}
## **使用选项将Excel表转换为范围**
您可以在使用 [TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) 类将表转换为范围时提供额外的选项。您可以将 [TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) 类的实例传递给 [ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(com.aspose.cells.TableToRangeOptions\)) 方法，以指定额外的选项。以下代码片段演示了使用 [TableToRangeOptions](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions) 类设置表的最后一行索引。表的格式将保留至指定行索引，其余格式将被移除。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRangeWithOptions.py" >}}
