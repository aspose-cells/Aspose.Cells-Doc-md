---
title: 移除数据透视表连接
type: docs
weight: 30
url: /zh/java/remove-pivot-connection/
description: 学习如何使用Aspose.Cells Java库移除数据透视连接。
keywords: 在不使用office 2013、office 2016、office 2019和office 365的情况下移除数据透视表连接。
---

## **可能的使用场景**

如果您想要在Excel中取消切片器和数据透视表的关联，您需要右键单击切片器，然后选择“报表连接...”选项。在选项列表中，您可以操作复选框。同样，如果您想要使用Aspose.Cells API以编程方式取消切片器和数据透视表的关联，请使用 [**Slicer.removePivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#removePivotConnection(com.aspose.cells.PivotTable) 方法。它会取消切片器和数据透视表的关联。

## **移除分割器**

以下示例代码加载包含现有缩略图的[sample Excel file](remove-pivot-connection.xlsx)，然后访问缩略图并取消关联缩略图和数据透视表。最后，将工作簿另存为[output Excel file](remove-pivot-connection-out.xlsx)。 


## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-Removing-Pivot-Connection.java" >}}
