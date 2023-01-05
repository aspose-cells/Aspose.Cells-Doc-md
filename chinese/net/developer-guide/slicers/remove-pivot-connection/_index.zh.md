---
title: 删除枢轴连接
type: docs
weight: 30
url: /zh/net/remove-pivot-connection/
description: 了解如何使用 Aspose.Cells 库删除枢轴连接。
keywords: Remove pivot connection without office 2013, office 2016, office 2019 and office 365.
---
## **可能的使用场景**

如果要在 Excel 中取消关联切片器和数据透视表，您需要右键单击切片器并选择“报告连接...”项。在选项列表中，您可以对复选框进行操作。同样，如果您想以编程方式使用 Aspose.Cells API 取消切片器和数据透视表的关联，请使用[**Slicer.RemovePivotConnection（数据透视表数据透视表）**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/removepivotconnection/)方法。它将解除切片器和数据透视表的关联。

## **分离切片器和数据透视表**

下面的示例代码加载[示例 Excel 文件](remove-pivot-connection.xlsx)包含一个现有的切片器。它访问切片器，然后解除切片器和数据透视表的关联。最后，它将工作簿另存为[输出Excel文件](remove-pivot-connection-out.xlsx). 


## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-Removing-Pivot-Connection.cs" >}}