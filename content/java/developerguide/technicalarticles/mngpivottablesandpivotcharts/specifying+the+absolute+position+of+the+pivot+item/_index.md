---
title : "Specifying the absolute position of the Pivot Item" 
description : "" 
weight : 16411 
toc : false
type: docs
url: /java/developerguide/technicalarticles/mngpivottablesandpivotcharts/specifying+the+absolute+position+of+the+pivot+item/
---

# Aspose.Cells for Java : Specifying the absolute position of the Pivot Item


Sometimes, the user needs to specify the absolute position of the pivot items, Aspose.Cells API has exposed a few new properties and a method to achieve this user requirement.

*   Added [PivotItem.setPosition()](https://apireference.aspose.com/java/cells/com.aspose.cells/pivotitem#Position) property that can be used to specify the position index in all the PivotItems regardless of the parent node. Added [PivotItem.setPositionInSameParentNode()](https://apireference.aspose.com/java/cells/com.aspose.cells/pivotitem#PositionInSameParentNode) property that can be used to specify the position index in the PivotItems under the same parent node.

*   Added [PivotItem.move(int count, boolean isSameParent)](https://apireference.aspose.com/java/cells/com.aspose.cells/pivotitem#move(int,%20boolean)) method in order to move the item up or down based on the count value, where the count is the number of positions to move the PivotItem up or down. If the count value is less than zero, the item will be moved up whereas if the count value is larger than zero, the PivotItem will move down, Boolean type isSameParent parameter specifying whether the moving operation has to be performed in the same parent node or not.

*   Obsoleted the *PivotItem.move(int count)* method, therefore, it is suggested to use the newly added method [PivotItem.move(int count, boolean isSameParent)](https://apireference.aspose.com/java/cells/com.aspose.cells/pivotitem#move(int,%20boolean))instead.

Please note, it is necessary to call the [PivotTable.refreshData](https://apireference.aspose.com/java/cells/com.aspose.cells/pivottable#refreshData()) and [PivotTable.calculateData](https://apireference.aspose.com/java/cells/com.aspose.cells/pivottable#calculateData()) methods before using [PivotItem.setPosition()](https://apireference.aspose.com/java/cells/com.aspose.cells/pivotitem#Position), [PivotItem.setPositionInSameParentNode()](https://apireference.aspose.com/java/cells/com.aspose.cells/pivotitem#PositionInSameParentNode)properties and [PivotItem.move(int count, boolean isSameParent)](https://apireference.aspose.com/java/cells/com.aspose.cells/pivotitem#move(int,%20boolean)) method.

#### Example

The following sample code creates a Pivot Table and then it specifies the Pivot Items positions in the same parent node.


