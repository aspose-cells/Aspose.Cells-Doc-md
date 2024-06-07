---
title: 指定数据透视项的绝对位置
type: docs
weight: 40
url: /zh/java/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

有时，用户需要指定数据透视项的绝对位置，Aspose.Cells API公开了一些新的属性和方法来实现这一用户需求。

- 添加[**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position)属性，可用于指定在所有PivotItems中的位置索引，而不考虑父节点。添加[**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode)属性，可用于指定在相同父节点下PivotItems中的位置索引。
- 添加[**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean))方法，以根据计数值上移或下移项目的位置，其中计数是要将PivotItem上移或下移的位置数。如果计数值小于零，则项目将上移，而如果计数值大于零，则PivotItem将下移，布尔类型isSameParent参数指定是否在相同的父节点中执行移动操作。
- 将*PivotItem.move(int count)*方法作废，因此建议使用新添加的方法[**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)) 。

请注意，必须在使用[**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position)、[**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode)属性和[**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean))方法之前调用[**PivotTable.refreshData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData())和[**PivotTable.calculateData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData())方法。

{{% /alert %}}

## 示例代码

以下示例代码创建一个数据透视表，然后在相同的父节点中指定数据透视项的位置。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.java" >}}
