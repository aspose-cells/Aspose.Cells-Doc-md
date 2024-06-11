---
title: 如果数据过大，自动将 Smart Marker 数据填充到其他工作表
type: docs
weight: 50
url: /zh/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/
---

## **可能的使用场景**
有时，如果数据源包含 1500000 条记录，对于单个工作表来说太多了，那么您可以将其余的记录移动到下一个工作表。 
## **如果数据过大，自动填充 Smart Marker 数据到其他工作表**
以下示例代码具有一个数据源，其中包含 21 条记录。我们只想在一个工作表中显示 15 条记录，其余记录将自动移至第二个工作表。请注意，第二个工作表也应具有相同的 Smart Marker 标记，并且您必须为这两个工作表都调用 [WorkbookDesigner.Process(sheetIndex, isPreserved)](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/process/methods/2) 方法。请参阅代码生成的[输出 Excel 文件](60489775.xlsx)以进行参考。
## **示例代码**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-AutoPopulateSmartMarkerDataToOtherWorksheets.cs" >}}
