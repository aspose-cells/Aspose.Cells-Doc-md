---
title: 指定数据透视项的绝对位置
type: docs
weight: 50
url: /zh/net/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

有时，用户需要指定数据透视项的绝对位置，Aspose.Cells API公开了一些新属性和方法来满足用户需求。

- 添加[**PivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position)属性，可用于指定在所有PivotItems中的位置索引，而不考虑父节点。添加[**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode)属性，可用于指定在相同父节点下PivotItems中的位置索引。
- 添加[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move)方法，以根据计数值将项目向上或向下移动，其中计数是要将PivotItem向上或向下移动的位置数。如果计数值小于零，则项目将向上移动，如果计数值大于零，则PivotItem将向下移动，布尔类型isSameParent参数指定是否在相同的父节点中执行移动操作。
- 弃用*PivotItem.Move(int count)*方法，因此建议使用新添加的[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move)方法。

{{% /alert %}}

以下示例代码创建一个数据透视表，然后指定相同父节点中数据透视项的位置。您可以下载[源Excel](5112632.xlsx)和[输出Excel](5112619.xlsx)文件供参考。如果打开输出Excel文件，您将看到数据透视项"4H12"在"K11"父节点中的第0个位置，"DIF400"在第3个位置。同样，CA32位于第1个位置，AAA3位于第2个位置

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.cs" >}}

{{% alert color="primary" %}}

请注意，在使用[**PivotItem.Position**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position)、[**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode)属性和[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move)方法之前，需要调用PivotTable.RefreshData和PivotTable.CalculateData方法。

{{% /alert %}}
