---
title: 刷新和计算包含计算项的数据透视表
type: docs
weight: 40
url: /zh/python-net/refresh-and-calculate-pivot-table-having-calculated-items/
description: 这篇文章展示了如何通过Aspose.Cells for Python刷新和计算具有计算项的数据透视表。
keywords: 通过Aspose.Cells for Python Excel库，刷新和计算具有计算项的数据透视表。
---

{{% alert color="primary" %}}

Aspose.Cells for Python通过.NET现在支持刷新和计算具有计算项的数据透视表。

{{% /alert %}}

## **刷新和计算包含计算项的数据透视表**

以下示例代码加载包含三个计算项目“add”、“div”、“div2”的数据透视表的[源Excel文件](5115238.xlsx)。我们首先将单元格 D2 的值更改为 20，然后通过 Aspose.Cells for Python 通过 .NET API 刷新和计算数据透视表，并将工作簿保存为 PDF 格式。 [输出PDF](5115229.pdf) 中的结果显示 Aspose.Cells for Python 通过 .NET 成功刷新和计算具有计算项目的数据透视表。您可以使用 Microsoft Excel 进行验证，方法是手动在单元格 D2 中放置值 20，然后通过 Alt+F5 快捷键刷新数据透视表或单击数据透视表刷新按钮。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-RefreshAndCalculateItems-1.py" >}}
