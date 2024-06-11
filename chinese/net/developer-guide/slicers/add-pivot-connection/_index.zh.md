---
title: 添加数据透视连接
type: docs
weight: 30
url: /zh/net/add-pivot-connection/
description: 学习如何使用Aspose.Cells库添加数据透视连接。
keywords: 在无Office 2013、Office 2016、Office 2019和Office 365的情况下添加数据透视连接
---

## **可能的使用场景**

如果你想在Excel中关联切片器和数据透视表，你需要右键单击切片器，然后选择"报表连接..."项目。在选项列表中，你可以操作复选框。 类似地，如果你想使用Aspose.Cells API以编程方式关联切片器和数据透视表，请使用[**Slicer.AddPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/addpivotconnection/) 方法。 它将关联切片器和数据透视表。

## **关联切片器和数据透视表**

以下示例代码加载包含现有切片器的[sample Excel file](add-pivot-connection.xlsx)。它访问切片器然后将切片器与数据透视表关联。最后，将工作簿另存为[output Excel file](add-pivot-connection-out.xlsx)。 


## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-Adding-Pivot-Connection.cs" >}}
