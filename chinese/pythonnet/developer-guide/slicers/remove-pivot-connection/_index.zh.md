---
title: 删除枢轴连接
type: docs
weight: 30
url: /zh/python-net/remove-pivot-connection/
description: 了解如何删除与 Aspose.Cells for Python via .NET 库的枢轴连接。
keywords: Remove pivot connection without office 2013, office 2016, office 2019 and office 365.
---
##  **可能的使用场景**

如果要在 Excel 中取消切片器和数据透视表的关联，则需要右键单击切片器并选择“报告连接...”项。在选项列表中，您可以对复选框进行操作。同样，如果您想以编程方式使用 Aspose.Cells for Python via .NET API 取消切片器和数据透视表的关联，请使用[**Slicer.remove_pivot_connection(pivot)**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicer/remove_pivot_connection/#aspose.cells.pivot.PivotTable)方法。它将取消切片器和数据透视表的关联。

##  **取消切片器和数据透视表的关联**

以下示例代码加载[Excel 文件示例](remove-pivot-connection.xlsx)包含现有切片器。它访问切片器，然后取消切片器和数据透视表的关联。最后，它将工作簿另存为[输出Excel文件](remove-pivot-connection-out.xlsx). 


##  **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Slicers-Removing-Pivot-Connection.py" >}}