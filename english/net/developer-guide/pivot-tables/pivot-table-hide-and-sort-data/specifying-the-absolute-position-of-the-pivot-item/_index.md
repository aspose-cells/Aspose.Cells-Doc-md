---
title: Specifying the Absolute Position of the Pivot Item
type: docs
weight: 50
url: /net/specifying-the-absolute-position-of-the-pivot-item/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes, the user needs to specify the absolute position of the pivot items. The Aspose.Cells API has exposed a few new properties and a method to achieve this requirement.

- Added the [**PivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position) property that can be used to specify the position index in all the PivotItems regardless of the parent node. Added the [**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode) property that can be used to specify the position index in the PivotItems under the same parent node.
- Added the [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move) method in order to move the item up or down based on the count value, where count is the number of positions to move the PivotItem. If the count value is less than zero, the item will be moved up, whereas if the count value is greater than zero, the PivotItem will move down. The Boolean **isSameParent** parameter specifies whether the moving operation has to be performed in the same parent node.
- Obsoleted the *PivotItem.Move(int count)* method; therefore, it is suggested to use the newly added **PivotItem.Move(int count, bool isSameParent)** method instead.

{{% /alert %}}

The following sample code creates a Pivot Table and then specifies the Pivot Item positions in the same parent node. You can download the [source Excel](5112632.xlsx) and [output Excel](5112619.xlsx) files for your reference. If you open the output Excel file, you will see that the Pivot Item "4H12" is at the 0th position in parent "K11" and "DIF400" is at the 3rd position. Similarly, CA32 is at position 1 and AAA3 is at position 2.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.cs" >}}

{{% alert color="primary" %}}

Please note that it is necessary to call the PivotTable.RefreshData and PivotTable.CalculateData methods before using the **PivotItem.Position**, **PivotItem.PositionInSameParentNode** properties, and the **PivotItem.Move(int count, bool isSameParent)** method.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
