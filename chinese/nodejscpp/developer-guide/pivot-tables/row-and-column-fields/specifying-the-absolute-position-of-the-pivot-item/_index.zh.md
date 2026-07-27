---
title: 指定数据透视项的绝对位置
type: docs
weight: 50
url: /zh/nodejs-cpp/specifying-the-absolute-position-of-the-pivot-item/
---

{{% alert color="primary" %}}

有时用户需要指定数据透视项的绝对位置，Aspose.Cells for Node.js via C++ API提供了几个新属性和一个方法以满足此需求。

- 添加了[**PivotItem.setPosition**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPosition-number-)属性，可用于指定所有数据透视项的位置索引，而不论父节点如何。添加了[**PivotItem.setPositionInSameParentNode**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPositionInSameParentNode-number-)属性，可用于指定在同一父节点下的数据透视项的位置索引。
- 添加了[**PivotItem.move**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#move-number-boolean-)方法，以根据计数值将项上移或下移，其中计数是要将数据透视项上移或下移的位置数。如果计数值小于零，则数据透视项将上移，如果计数值大于零，则数据透视项将下移，Boolean类型的isSameParent参数指定移动操作是否必须在同一父节点中执行。
- 已废弃*PivotItem.move(int count)*方法，建议使用新增的方法 [**PivotItem.move(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#move-number-boolean-)。

{{% /alert %}}

以下示例代码创建了一个数据透视表，然后指定了数据透视项在同一父节点中的位置。您可以下载源Excel和输出Excel文件进行参考。如果打开输出Excel文件，您将看到数据透视项“4H12”位于父节点“K11”中的第0个位置，而“DIF400”位于第3个位置。同样，CA32位于第1个位置，AAA3位于第2个位置。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SpecifyAbsolutePositionOfPivotItem.js" >}}

{{% alert color="primary" %}}

请注意，在使用[**PivotItem.setPosition**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPosition-number-)、[**PivotItem.setPositionInSameParentNode**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#setPositionInSameParentNode-number-)属性和[**PivotItem.move**](https://reference.aspose.com/cells/nodejs-cpp/pivotitem/#move-number-boolean-)方法之前，必须先调用PivotTable.RefreshData和PivotTable.CalculateData方法。

{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}
