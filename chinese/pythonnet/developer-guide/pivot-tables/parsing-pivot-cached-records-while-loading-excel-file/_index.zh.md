---
title: 在加载Excel文件时解析透视缓存记录
type: docs
weight: 70
url: /zh/python-net/parsing-pivot-cached-records-while-loading-excel-file/
description: 如何使用Aspose.Cells for Python via .NET在加载Excel文件时解析数据透视缓存记录。
keywords: 使用Aspose.Cells for Python Excel库，在加载Excel文件时解析数据透视缓存记录。
---

## **可能的使用场景**

创建透视表时，Microsoft Excel会复制源数据并将其存储在透视缓存中。透视缓存保存在Microsoft Excel的内存中。您看不到它，但这是建立透视表、更改切片选择或移动行/列时透视表引用的数据。这使得Microsoft Excel能够对透视表的更改做出非常灵敏的响应，但它也可能使文件的大小翻倍。毕竟，透视缓存只是源数据的副本，因此您的文件大小可能会翻倍。

在将Excel文件加载到Workbook对象中时，您可以决定是否也要加载透视缓存记录，使用[**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/)属性。此属性的默认值为**false**。如果透视缓存相当大，它会提高性能。但如果您也想加载透视缓存记录，应将此属性设置为**true**。

## **加载Excel文件时如何解析数据透视缓存记录**

以下示例代码解释了[**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/)属性的用法。它在解析透视缓存记录时加载[示例Excel文件](61767773.xlsx)。然后刷新透视表并将其保存为[输出Excel文件](61767774.xlsx)。

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.py" >}}
