---
title: 在加载Excel文件时解析透视缓存记录
type: docs
weight: 100
url: /zh/java/parsing-pivot-cached-records-while-loading-excel-file/
---

## **可能的使用场景**

创建透视表时，Microsoft Excel会复制源数据并将其存储在透视缓存中。透视缓存保存在Microsoft Excel的内存中。您看不到它，但这是建立透视表、更改切片选择或移动行/列时透视表引用的数据。这使得Microsoft Excel能够对透视表的更改做出非常灵敏的响应，但它也可能使文件的大小翻倍。毕竟，透视缓存只是源数据的副本，因此您的文件大小可能会翻倍。

在加载Excel文件时，您可以使用[**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#ParsingPivotCachedRecords)属性来决定是否同时加载数据透视缓存记录。这个属性的默认值是**false**。如果数据透视缓存相当大，它可以提高性能。但如果您也想加载数据透视缓存记录，您应该将此属性设置为**true**。

## **在加载Excel文件时解析透视缓存记录**

以下示例代码解释了使用[**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#ParsingPivotCachedRecords)属性的用法。它在解析数据透视缓存记录时加载了[示例Excel文件](61767786.xlsx)。然后刷新数据透视表并将其保存为[输出Excel文件](61767785.xlsx)。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.java" >}}
{{< app/cells/assistant language="java" >}}
