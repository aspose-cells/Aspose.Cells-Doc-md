---
title: 加载 Excel 文件时解析数据透视缓存记录
type: docs
weight: 70
url: /zh/net/parsing-pivot-cached-records-while-loading-excel-file/
---
## **可能的使用场景**

创建数据透视表时，Microsoft Excel 会获取源数据的副本并将其存储在数据透视缓存中。数据透视缓存保存在 Microsoft Excel 的内存中。您看不到它，但这是在您构建数据透视表或更改切片器选择或四处移动行/列时数据透视表引用的数据。这使 Microsoft Excel 能够非常灵敏地响应数据透视表中的更改，但它也会使文件的大小加倍。毕竟，Pivot Cache 只是源数据的副本，因此文件大小可能翻倍是有道理的。

当您将 Excel 文件加载到 Workbook 对象中时，您可以决定是否还要加载 Pivot Cache 的记录，使用[**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/parsingpivotcachedrecords)财产。该属性的默认值为**错误的**.如果 Pivot Cache 很大，它可以提高性能。但是如果你还想加载Pivot Cache的记录，你应该将这个属性设置为**真的**.

## **加载 Excel 文件时解析数据透视缓存记录**

下面的示例代码解释了[**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/parsingpivotcachedrecords)财产。它加载了[示例 Excel 文件](61767773.xlsx)在解析枢轴缓存记录时。然后它刷新数据透视表并将其保存为[输出Excel文件](61767774.xlsx).

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.cs" >}}
