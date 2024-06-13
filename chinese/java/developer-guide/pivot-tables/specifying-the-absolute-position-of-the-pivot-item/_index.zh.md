---
title: 指定数据透视表项的绝对位置
type: docs
weight: 40
url: /zh/java/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

有时，用户需要指定数据透视表项的绝对位置，Aspose.Cells API公开了一些新属性和方法来满足此用户需求。

- 添加了[**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position)属性，可用于指定所有数据透视项的位置索引，而不论父节点如何。添加了[**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode)属性，可用于指定在同一父节点下的数据透视项的位置索引。
- 添加了 [**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)) 方法以根据计数值向上或向下移动项，其中计数是要向上或向下移动PivotItem的位置数。如果计数值小于零，项将向上移动，而如果计数值大于零，PivotItem将向下移动，布尔类型的 isSameParent 参数指定是否在同一父节点中执行移动操作或不执行移动操作。
- 废弃了 *PivotItem.move(int count)* 方法，因此建议使用新添加的 [**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)) 方法。

请注意，在使用 [**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position)、[**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode) 属性和 [**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)) 方法之前，需要调用 [**PivotTable.refreshData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData--) 和 [**PivotTable.calculateData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData--) 方法。

{{% /alert %}}

## 示例代码

以下示例代码创建一个数据透视表，然后指定相同父节点中数据透视表项的位置。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.java" >}}
