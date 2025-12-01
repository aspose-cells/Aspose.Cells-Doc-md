---
title: Specifying the absolute position of the Pivot Item
type: docs
weight: 40
url: /java/specifying-the-absolute-position-of-the-pivot-item/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes, the user needs to specify the absolute position of the pivot items, Aspose.Cells API has exposed a few new properties and a method to achieve this user requirement.

- Added [**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position) property that can be used to specify the position index in all the PivotItems regardless of the parent node. Added [**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) property that can be used to specify the position index in the PivotItems under the same parent node.
- Added [**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move-int-boolean-) method in order to move the item up or down based on the count value, where the count is the number of positions to move the PivotItem up or down. If the count value is less than zero, the item will be moved up whereas if the count value is larger than zero, the PivotItem will move down, Boolean type isSameParent parameter specifying whether the moving operation has to be performed in the same parent node or not.
- Obsoleted the *PivotItem.move(int count)* method, therefore, it is suggested to use the newly added method [**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move-int-boolean-) instead.

Please note, it is necessary to call the [**PivotTable.refreshData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData--) and [**PivotTable.calculateData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData--) methods before using [**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position), [**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) properties and [**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move-int-boolean-) method.

{{% /alert %}}

## Sample Code

The following sample code creates a Pivot Table and then it specifies the Pivot Items positions in the same parent node.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.java" >}}
{{< app/cells/assistant language="java" >}}
