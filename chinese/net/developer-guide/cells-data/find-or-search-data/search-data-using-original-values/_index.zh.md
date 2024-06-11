---
title: 使用原始值搜索数据
type: docs
weight: 380
url: /zh/net/search-data-using-original-values/
description: 使用Aspose.Cells for .NET API学习如何使用原始值搜索数据。
keywords: 使用原始值搜索数据，使用原始值查找数据，按原始值搜索数据，按原始值查找数据
---

{{% alert color="primary" %}}

有时，数据的值因为以某种方式格式化而被隐藏。例如，假设单元格 D4 公式为 =Sum(A1:A2) 并且其值为 20 但格式为---，那么值 20 将被隐藏，并且无法使用 Microsoft Excel 查找选项找到。但是，您可以使用 Aspose.Cells 使用 [**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype) 找到它

{{% /alert %}}

以下示例代码说明了上述观点。它会找到无法使用Microsoft Excel的查找选项找到的单元格D4，但Aspose.Cells可以使用[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype)找到它。请阅读代码内的注释以获取更多信息。

## 使用原始值搜索数据的 C# 代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.cs" >}}

## 示例代码生成的控制台输出

这是上面示例代码的控制台输出。

{{< highlight java >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
