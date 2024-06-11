---
title: 指定数据透视项的绝对位置
type: docs
weight: 50
url: /zh/net/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

有时，用户需要指定数据透视项的绝对位置，Aspose.Cells API公开了一些新属性和方法来实现用户需求。

- 添加了[**PivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position)属性，可用于指定所有数据透视项的位置索引，而不论父节点如何。添加了[**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode)属性，可用于指定在同一父节点下的数据透视项的位置索引。
- 添加了[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move)方法，以根据计数值将项上移或下移，其中计数是要将数据透视项上移或下移的位置数。如果计数值小于零，则数据透视项将上移，如果计数值大于零，则数据透视项将下移，Boolean类型的isSameParent参数指定移动操作是否必须在同一父节点中执行。
 - 废弃了*PivotItem.Move(int count)*方法，因此建议使用新添加的方法[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move)。

{{% /alert %}}

以下示例代码创建了一个数据透视表，然后指定了数据透视项在同一父节点中的位置。您可以下载源Excel和输出Excel文件进行参考。如果打开输出Excel文件，您将看到数据透视项“4H12”位于父节点“K11”中的第0个位置，而“DIF400”位于第3个位置。同样，CA32位于第1个位置，AAA3位于第2个位置。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.cs" >}}

{{% alert color="primary" %}}

请注意，在使用[**PivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position)、[**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode)属性和[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move)方法之前，必须先调用PivotTable.RefreshData和PivotTable.CalculateData方法。

{{% /alert %}}
