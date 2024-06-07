---
title: 如果数据量太大，无法一次性将SmartMarker数据自动填充到其他工作表中，您可以将剩余记录移动到下一个工作表。
type: docs
weight: 50
url: /zh/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/
---

## **可能的使用场景**
有时，如果数据太大，您可能希望将智能标记数据自动填充到其他工作表中。假设您的数据源有1500000条记录。对于单个工作表来说，这些记录太多了，那么您可以将剩余的记录移到下一个工作表。 
## **如果数据量太大，将SmartMarker数据自动填充到其他工作表**
以下示例代码具有包含21条记录的数据源。我们希望在一个工作表中仅显示15条记录，然后剩余的记录将自动移动到第二个工作表。请注意，第二个工作表应该也具有相同的Smart Marker标记，您必须为两个工作表都调用[WorkbookDesigner.Process(sheetIndex, isPreserved)](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/process/methods/2)方法。请查看代码生成的[输出Excel文件](60489775.xlsx)以获取参考。
## **示例代码**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-AutoPopulateSmartMarkerDataToOtherWorksheets.cs" >}}
