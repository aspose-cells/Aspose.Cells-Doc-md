---
title: Specifying the Absolute Position of the Pivot Item
type: docs
weight: 50
url: /net/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

Sometimes, user needs to specify the absolute position of the pivot items, Aspose.Cells API has exposed few new properties and a method to achieve user requirement.

- Added [**PivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position) property that can be used to specify the position index in all the PivotItems regardless of the parent node. Added [**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode) property that can be used to specify the position index in the PivotItems under the same parent node.
- Added [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move) method in order to move the item up or down based on the count value, where count is the number of position to move the PivotItem up or down. If the count value is less than zero, the item will be moved up where as if the count value is larger than zero, the PivotItem will move down, Boolean type isSameParent parameter specify whether the moving operation has to be performed in the same parent node or not.
- Obsoleted the *PivotItem.Move(int count)* method therefore it is suggested to use the newly added method [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move) instead.

{{% /alert %}}

The following sample code creates a Pivot Table and then it specifies the Pivot Items positions in the same parent node. You can download the [source Excel](5112632.xlsx) and [output Excel](5112619.xlsx) files for your reference. If you open the output Excel file, you will see the Pivot Item "4H12" is at 0th position in parent "K11" and "DIF400" is at 3rd position. Similarly, CA32 is at position 1 and AAA3 is at position 2

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.cs" >}}

{{% alert color="primary" %}}

Please note, it is necessary to call the PivotTable.RefreshData and PivotTable.CalculateData methods before using [**PivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position), [**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode) properties and [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move) method.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}