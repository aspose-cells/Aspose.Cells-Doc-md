---
title: 将 Excel 表转换为数据范围
type: docs
weight: 10
url: /zh/python-java/convert-an-excel-table-to-a-range-of-data/
---
## **将 Excel 表转换为数据范围**
 Aspose.Cells for Python via Java 提供将 Excel 表格转换为一系列数据的选项。为此，API 提供了[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\) ） 方法。下面的代码片段演示了使用[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(\)方法将 Excel 表格转换为一系列数据。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRange.py" >}}
## **使用选项将 Excel 表转换为范围**
在将表转换为范围时，您可以提供其他选项[TableToRange选项](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions)班级。你可以传递一个实例[TableToRange选项](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions)类到[ListObject.convertToRange](https://reference.aspose.com/cells/python/asposecells.api/listobject#convertToRange\(com.aspose.cells.TableToRangeOptions\)方法来指定附加选项。下面的代码片段演示了使用[TableToRange选项](https://reference.aspose.com/cells/python/asposecells.api/TableToRangeOptions)类来设置表的最后一行索引。表格格式将保留到指定的行索引，其余格式将被删除。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-ConvertTableToRangeWithOptions.py" >}}
