---
title: Specifying the Absolute Position of the Pivot Item with Golang via C++
linktitle: Specifying the Absolute Position of the Pivot Item
type: docs
weight: 50
url: /go-cpp/specifying-the-absolute-position-of-the-pivot-item/
description: Learn how to specify the absolute position of pivot items in C++ using Aspose.Cells.
---

{{% alert color="primary" %}}

Sometimes, users need to specify the absolute position of the pivot items. Aspose.Cells API has exposed a few new properties and a method to achieve this requirement.

- Added [**PivotItem.GetPosition()**](https://reference.aspose.com/cells/go-cpp/pivotitem/getposition/) property that can be used to specify the position index among all the PivotItems regardless of the parent node. Added [**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/) property that can be used to specify the position index among the PivotItems under the same parent node.  
- Added [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/go-cpp/pivotitem/move/) method in order to move the item up or down based on the count value, where **count** is the number of positions to move the PivotItem. If the count value is less than zero, the item will be moved up; if the count value is greater than zero, the PivotItem will move down. The Boolean‑type `isSameParent` parameter specifies whether the move operation should be performed within the same parent node.  
- Obsoleted the `PivotItem.Move(int count)` method; therefore, it is suggested to use the newly added method [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/go-cpp/pivotitem/move/) instead.

{{% /alert %}}

The following sample code creates a Pivot Table and then specifies the positions of the Pivot Items in the same parent node. You can download the [source Excel](5112632.xlsx) and [output Excel](5112619.xlsx) files for your reference. If you open the output Excel file, you will see that the Pivot Item **"4H12"** is at the 0th position in parent **"K11"**, and **"DIF400"** is at the 3rd position. Similarly, **CA32** is at position 1 and **AAA3** is at position 2.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyingTheAbsolutePositionOfThePivotItem.go" >}}
{{% alert color="primary" %}}

Please note that it is necessary to call the `PivotTable.RefreshData` and `PivotTable.CalculateData` methods before using [**PivotItem.GetPosition()**](https://reference.aspose.com/cells/go-cpp/pivotitem/getposition/), [**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/) properties, and the [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/) method.

{{% /alert %}}