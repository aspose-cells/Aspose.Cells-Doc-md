---
title: 删除数据透视连接
type: docs
weight: 30
url: /zh/java/remove-pivot-connection/
description: 了解使用 Aspose.Cells Java 库删除数据透视表连接
keywords: 在没有office 2013、office 2016、office 2019和office 365的情况下删除数据透视连接。
---

## **可能的使用场景**

如果要在Excel中取消切片器与数据透视表的关联，您需要右键单击切片器并选择"Report Connections..."选项。在选项列表中，您可以操作复选框。同样，如果要使用Aspose.Cells API编程方式取消切片器与数据透视表的关联，请使用[**Slicer.removePivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#removePivotConnection(com.aspose.cells.PivotTable))方法。这将取消切片器与数据透视表的关联。

## **移除切片器**

以下示例代码加载了包含现有切片器的[sample Excel file](remove-pivot-connection.xlsx)。它访问切片器，然后取消切片器与数据透视表的关联，最后将工作簿保存为[output Excel file](remove-pivot-connection-out.xlsx)。 


## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-Removing-Pivot-Connection.java" >}}
