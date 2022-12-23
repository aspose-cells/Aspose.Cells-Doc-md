---
title: 如果数据太大，自动将智能标记数据填充到其他工作表
type: docs
weight: 10
url: /zh/java/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/
---
## **可能的使用场景**

有时，如果智能标记数据太大，您希望将其自动填充到其他工作表。假设，您的数据源有 1500000 条记录。这些记录对于单个工作表来说太多了，那么您可以将其余记录移动到下一个工作表。

## **如果数据太大，自动将智能标记数据填充到其他工作表**

以下示例代码有一个包含 21 条记录的数据源。我们希望在一个工作表中只显示 15 条记录，然后其余记录将自动移动到第二个工作表。请注意，第二个工作表也应具有相同的智能标记标签，您必须调用[**WorkbookDesigner.process(sheetIndex, isPreserved)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process(int,%20boolean) ) 两张纸的方法。请检查[Microsoft 访问数据库文件](60489777.accdb)在此代码中使用以及[输出Excel文件](60489786.xlsx)生成的代码供参考。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-AutoPopulateSmartMarkerDataToOtherWorksheets.java" >}}
