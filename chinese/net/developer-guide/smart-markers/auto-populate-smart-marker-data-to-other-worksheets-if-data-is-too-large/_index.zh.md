---
title: 如果数据太大，自动将智能标记数据填充到其他工作表
type: docs
weight: 50
url: /zh/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/
---
## **可能的使用场景**
有时，如果智能标记数据太大，您希望将其自动填充到其他工作表。假设，您的数据源有 1500000 条记录。这些记录对于单个工作表来说太多了，那么您可以将其余记录移动到下一个工作表。
## **如果数据太大，自动将智能标记数据填充到其他工作表**
下面的示例代码有一个包含 21 条记录的数据源。我们希望在一个工作表中只显示 15 条记录，然后其余记录将自动移动到第二个工作表。请注意，第二个工作表也应具有相同的智能标记标签，您必须致电[WorkbookDesigner.Process(sheetIndex, isPreserved)](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/process/methods/2)两张纸的方法。请参阅[输出Excel文件](60489775.xlsx)生成的代码供参考。
## **示例代码**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-AutoPopulateSmartMarkerDataToOtherWorksheets.cs" >}}
