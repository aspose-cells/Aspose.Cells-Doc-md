---
title: 指定 Pivot Item 的绝对位置
type: docs
weight: 40
url: /zh/java/specifying-the-absolute-position-of-the-pivot-item/
---
{{% alert color="primary" %}}

有时，用户需要指定枢轴项目的绝对位置，Aspose.Cells API 公开了一些新属性和实现此用户需求的方法。

- 添加[**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position)可用于指定所有 PivotItems 中的位置索引的属性，而不考虑父节点。添加[**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode)可用于指定同一父节点下的 PivotItems 中的位置索引的属性。
- 添加[**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)方法以便根据计数值向上或向下移动项目，其中计数是将 PivotItem 向上或向下移动的位置数。如果计数值小于零，项目将向上移动，如果计数值大于零，则 PivotItem 将向下移动，布尔类型 isSameParent 参数指定移动操作是否必须在同一父节点或不是。
- 废弃的*PivotItem.move（整数计数）*方法，因此建议使用新添加的方法[**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)） 反而。

请注意，有必要致电[**数据透视表.refreshData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#refreshData() ） 和[**数据透视表.calculateData**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#calculateData() ) 使用前的方法[**PivotItem.setPosition()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#Position), [**PivotItem.setPositionInSameParentNode()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#PositionInSameParentNode)属性和[**PivotItem.move(int count, boolean isSameParent)**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotitem#move(int,%20boolean)） 方法。

{{% /alert %}}

## 示例代码

以下示例代码创建一个数据透视表，然后它指定同一父节点中的数据透视项位置。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.java" >}}
