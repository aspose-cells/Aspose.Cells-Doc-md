---
title: 在加载Excel文件时解析数据透视缓存记录
type: docs
weight: 70
url: /zh/python-net/parsing-pivot-cached-records-while-loading-excel-file/
description: 如何在使用Aspose.Cells for Python时加载Excel文件时解析Pivot缓存记录
keywords: 通过Aspose.Cells for Python Excel库，在加载Excel文件时解析Pivot缓存记录。
---

## **可能的使用场景**

当创建数据透视表时，Microsoft Excel会复制源数据并将其存储在数据透视缓存中。数据透视缓存保存在Microsoft Excel的内存中。您看不到它，但这是数据透视表在构建数据透视表、更改切片选择或移动行/列时引用的数据。这使得Microsoft Excel对数据透视表的更改非常敏感，但也可能使文件大小加倍。毕竟，数据透视缓存只是源数据的副本，因此你的文件大小有可能会加倍。

在加载Excel文件到Workbook对象中时，可以使用[**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/)属性决定是否也要加载数据透视缓存的记录。此属性的默认值为**false**。如果数据透视缓存非常大，则可以提高性能。但是，如果您想加载数据透视缓存的记录，就应将此属性设置为**true**。

## **在加载Excel文件时如何解析Pivot缓存记录**

以下示例代码解释了[**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/)属性的用法。它在解析数据透视缓存记录时加载了[示例Excel文件](61767773.xlsx)。然后刷新数据透视表并将其另存为[输出Excel文件](61767774.xlsx)。

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.py" >}}
