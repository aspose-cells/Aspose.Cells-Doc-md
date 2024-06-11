---
title: 使用原始值搜索数据
type: docs
weight: 380
url: /zh/python-net/search-data-using-original-values/
description: 通过Aspose.Cells for Python通过.NET API学习如何使用原始值搜索数据。
keywords: Python Excel库，使用原始值搜索数据，Python使用原始值搜索数据，Python使用原始值查找数据，Python使用原始值搜索数据，Python使用原始值查找数据
---

{{% alert color="primary" %}}

有时数据的值是隐藏的，因为以某种方式进行格式化。 例如，假设单元格D4具有公式=Sum(A1:A2)并且其值为20，但格式化为---，那么值20将被隐藏，无法使用Microsoft Excel的查找选项找到。 但是，您可以使用Aspose.Cells for Python通过.NET使用[**LookInType.ORIGINAL_VALUES**](https://reference.aspose.com/cells/python-net/aspose.cells/lookintype)来找到。

{{% /alert %}}

以下示例代码说明了上述观点。它找到了单元格 D4，使用 Microsoft Excel 查找选项找不到，但使用 Aspose.Cells 可以使用 [**LookInType.ORIGINAL_VALUES**](https://reference.aspose.com/cells/python-net/aspose.cells/lookintype) 找到它。请阅读代码内部的注释以了解更多信息。

## 用于使用原始值搜索数据的Python代码

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SearchDataUsingOriginalValues.py" >}}

## 示例代码生成的控制台输出

这是上述示例代码的控制台输出。

{{< highlight java >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
