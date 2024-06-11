---
title: 如果数据过大，自动将 Smart Marker 数据填充到其他工作表
type: docs
weight: 10
url: /zh/java/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/
---

## **可能的使用场景**

有时，如果数据太大，您希望自动将智能标记数据填充到其他工作表。假设您的数据源有 1500000 条记录。这对于单个工作表来说是太多的记录，那么您可以将其余记录移至下一个工作表。

## **如果数据太大，可以将智能标记数据自动填充到其他工作表**

以下示例代码具有一个数据源，其中有 21 条记录。我们希望在一个工作表中只显示 15 条记录，那么其余记录将自动移至第二个工作表。请注意，第二个工作表也应具有相同的智能标记标签，您必须为两个工作表调用 [**WorkbookDesigner.process(sheetIndex, isPreserved)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process(int,%20boolean)) 方法。请查看本代码中使用的 [Microsoft Access 数据库文件](60489777.accdb) 以及代码生成的 [输出 Excel 文件](60489786.xlsx) 作为参考。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-AutoPopulateSmartMarkerDataToOtherWorksheets.java" >}}
