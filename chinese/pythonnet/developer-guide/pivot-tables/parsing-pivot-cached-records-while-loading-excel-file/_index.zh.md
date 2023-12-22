---
title: 加载 Excel 文件时解析数据透视表缓存记录
type: docs
weight: 70
url: /zh/python-net/parsing-pivot-cached-records-while-loading-excel-file/
description: 如何在使用 Aspose.Cells for Python via .NET 加载 Excel 文件时解析数据透视缓存记录。
keywords: Parse Pivot Cached Records while loading Excel file.
---
##  **可能的使用场景**

创建数据透视表时，Microsoft Excel 会获取源数据的副本并将其存储在数据透视表缓存中。数据透视缓存保存在 Microsoft Excel 的内存中。您看不到它，但这是在构建数据透视表或更改切片器选择或移动行/列时数据透视表引用的数据。这使得 Microsoft Excel 能够非常灵敏地响应数据透视表中的更改，但它也会使文件大小加倍。毕竟，数据透视缓存只是源数据的副本，因此文件大小可能会增加一倍是有道理的。

当您在 Workbook 对象中加载 Excel 文件时，您可以使用以下命令决定是否还要加载 Pivot Cache 的记录：[**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/)财产。此属性的默认值为 *false**。如果Pivot Cache足够大，可以提高性能。但如果你还想加载Pivot Cache的记录，你应该将该属性设置为*true**。

##  **加载 Excel 文件时解析数据透视表缓存记录**

下面的示例代码解释了其用法[**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/)财产。它加载了[Excel 文件示例](61767773.xlsx)在解析数据透视缓存记录时。然后它刷新数据透视表并将其保存为[输出Excel文件](61767774.xlsx).

##  **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.py" >}}
