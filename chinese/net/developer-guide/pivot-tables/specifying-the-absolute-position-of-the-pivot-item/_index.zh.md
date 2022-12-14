---
title: 指定枢轴项的绝对位置
type: docs
weight: 50
url: /zh/net/specifying-the-absolute-position-of-the-pivot-item/
---
{{% alert color="primary" %}}

有时，用户需要指定枢轴项的绝对位置，Aspose.Cells API 公开了一些新属性和实现用户需求的方法。

- 添加[**枢轴项.位置**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position)可用于指定所有 PivotItems 中的位置索引的属性，而不考虑父节点。添加[**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode)可用于指定同一父节点下的 PivotItems 中的位置索引的属性。
- 添加[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move)方法，以便根据计数值向上或向下移动项目，其中计数是将 PivotItem 向上或向下移动的位置数。如果计数值小于零，item将向上移动，如果计数值大于零，则PivotItem将向下移动，布尔类型isSameParent参数指定是否必须在同一父节点进行移动操作或不。
- 废弃的*PivotItem.Move（整数计数）*方法因此建议使用新添加的方法[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move)反而。

{{% /alert %}}

以下示例代码创建一个数据透视表，然后它指定同一父节点中的数据透视项位置。您可以下载[源Excel](5112632.xlsx)和[输出Excel](5112619.xlsx)文件供您参考。如果您打开输出的 Excel 文件，您将看到枢轴项“4H12”在父项“K11”中的第 0 个位置，“DIF400”在第 3 个位置。同样，CA32 在位置 1，AAA3 在位置 2

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-SpecifyAbsolutePositionOfPivotItem-SpecifyAbsolutePositionOfPivotItem.cs" >}}

{{% alert color="primary" %}}

请注意，使用前需要调用 PivotTable.RefreshData 和 PivotTable.CalculateData 方法[**枢轴项.位置**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/position), [**PivotItem.PositionInSameParentNode**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/properties/positioninsameparentnode)属性和[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotitem/methods/move)方法。

{{% /alert %}}
