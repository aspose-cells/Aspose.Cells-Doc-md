---
title: 如果数据量太大，无法一次性将SmartMarker数据自动填充到其他工作表中，您可以将剩余记录移动到下一个工作表。
type: docs
weight: 10
url: /zh/java/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/
---

## **可能的使用场景**

有时，如果数据量太大，您希望将智能标记数据自动填充到其他工作表。假设您的数据源有1500000条记录，这对于单个工作表来说太多了，那么您可以将剩余的记录移动到下一个工作表。

## **如果数据太大，则自动填充智能标记数据到其他工作表。**

以下示例代码有一个数据源包含21条记录。我们要在一个工作表中仅显示15条记录，剩余的记录将自动移动到第二个工作表。请注意，第二个工作表还应具有相同的智能标记标签，您必须为两个工作表都调用 [**WorkbookDesigner.process(sheetIndex, isPreserved)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process(int,%20boolean)) 方法。还请查看此代码中使用的 [Microsoft Access数据库文件](60489777.accdb) 以及代码生成的 [输出Excel文件](60489786.xlsx) 进行参考。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-AutoPopulateSmartMarkerDataToOtherWorksheets.java" >}}
