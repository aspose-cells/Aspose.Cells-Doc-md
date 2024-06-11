---
title: 使用原始值搜索数据
type: docs
weight: 380
url: /zh/python-net/search-data-using-original-values/
description: 学习如何通过Aspose.Cells for Python via .NET API使用原始值搜索数据。
keywords: Python Excel库，Python使用原始值搜索数据，Python查找使用原始值的数据，Python使用原始值搜索数据，Python查找使用原始值的数据
---

{{% alert color="primary" %}}

有时，数据的值由于某种方式的格式而被隐藏。例如，假设单元格D4具有公式=Sum(A1:A2)，其值为20，但其格式为---，则值20被隐藏，无法使用Microsoft Excel的查找选项找到。但是，您可以使用Aspose.Cells for Python via .NET使用[**LookInType.ORIGINAL_VALUES**](https://reference.aspose.com/cells/python-net/aspose.cells/lookintype)找到它。

{{% /alert %}}

以下示例代码说明了上述观点。它会找到无法使用Microsoft Excel的查找选项找到的单元格D4，但Aspose.Cells可以使用[**LookInType.ORIGINAL_VALUES**](https://reference.aspose.com/cells/python-net/aspose.cells/lookintype)找到它。请阅读代码内的注释以获取更多信息。

## 用于搜索原始值的Python代码

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SearchDataUsingOriginalValues.py" >}}

## 示例代码生成的控制台输出

这是上面示例代码的控制台输出。

{{< highlight java >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
