---
title: 使用原始值搜索数据
type: docs
weight: 380
url: /zh/net/search-data-using-original-values/
description: 通过 Aspose.Cells for .NET API 学习如何使用原始值搜索数据。
keywords: 使用原始值搜索数据，通过原始值查找数据，使用原始值搜索数据，通过原始值查找数据
---

{{% alert color="primary" %}}

有时，数据的值因为某种格式而被隐藏。例如，假设单元格 D4 公式为 =Sum(A1:A2)，其值为 20，但格式为 ---，则值 20 被隐藏，无法使用 Microsoft Excel 查找选项找到。不过，您可以使用 Aspose.Cells 使用 [**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype) 来找到它。

{{% /alert %}}

以下示例代码说明了上述观点。它找到了单元格 D4，使用 Microsoft Excel 查找选项找不到，但使用 Aspose.Cells 可以使用 [**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype) 找到它。请阅读代码内部的注释以了解更多信息。

## 用于使用原始值搜索数据的 C# 代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.cs" >}}

## 示例代码生成的控制台输出

这是上述示例代码的控制台输出。

{{< highlight java >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
