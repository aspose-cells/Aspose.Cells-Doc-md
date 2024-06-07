---
title: 添加数据透视表连接
type: docs
weight: 30
url: /zh/java/add-pivot-connection/
description: 学习如何使用Aspose.Cells Java库添加数据透视连接。
keywords: 在不使用office 2013、office 2016、office 2019和office 365的情况下添加数据透视表连接。
---

## **可能的使用场景**

如果要在Excel中关联切片器和数据透视表，您需要右键单击切片器，然后选择"Report Connections..."项。在选项列表中，您可以操作复选框。同样，如果要使用Aspose.Cells Java API以编程方式关联切片器和数据透视表，请使用[**Slicer.addPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#addPivotConnection(com.aspose.cells.PivotTable)/) 方法。它将关联切片器和数据透视表。

## **关联缩略图和数据透视表**

以下示例代码加载包含现有缩略图的[sample Excel file](add-pivot-connection.xlsx)，访问缩略图，然后关联缩略图和数据透视表。最后，它将工作簿另存为[output Excel file](add-pivot-connection-out.xlsx)。 


## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-Adding-Pivot-Connection.java" >}}
