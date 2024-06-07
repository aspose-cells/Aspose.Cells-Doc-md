---
title: 在加载Excel文件时解析数据透视缓存记录
type: docs
weight: 100
url: /zh/java/parsing-pivot-cached-records-while-loading-excel-file/
---

## **可能的使用场景**

当创建数据透视表时，Microsoft Excel会复制源数据并将其存储在数据透视缓存中。数据透视缓存保存在Microsoft Excel的内存中。您看不到它，但这是数据透视表在构建数据透视表、更改切片选择或移动行/列时引用的数据。这使得Microsoft Excel对数据透视表的更改非常敏感，但也可能使文件大小加倍。毕竟，数据透视缓存只是源数据的副本，因此你的文件大小有可能会加倍。

当您在Workbook对象中加载Excel文件时，可以决定是否还要加载数据透视缓存的记录，使用[**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#ParsingPivotCachedRecords)属性。此属性的默认值为**false**。如果数据透视缓存非常大，可以提高性能。但如果您也想加载数据透视缓存的记录，应将此属性设置为**true**。

## **在加载Excel文件时解析数据透视缓存记录**

以下示例代码说明了[**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#ParsingPivotCachedRecords)属性的使用。它在解析数据透视缓存记录时加载了[sample Excel文件](61767786.xlsx)，然后刷新数据透视表并将其另存为[output Excel文件](61767785.xlsx)。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.java" >}}
