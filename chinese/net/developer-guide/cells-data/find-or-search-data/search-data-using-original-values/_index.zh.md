---
title: 使用原始值搜索数据
type: docs
weight: 380
url: /zh/net/search-data-using-original-values/
---
{{% alert color="primary" %}}

有时数据的价值是隐藏的，因为它是以某种方式格式化的。例如，假设单元格 D4 具有公式 =Sum(A1:A2) 并且其值为 20 但其格式为 ---，则值 20 被隐藏并且无法使用 Microsoft Excel 查找选项找到。但是，您可以使用 Aspose.Cells 找到它[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype)

{{% /alert %}}

以下示例代码说明了上述观点。它找到使用 Microsoft Excel 查找选项无法找到的单元格 D4，但 Aspose.Cells 可以使用[**LookInType.OriginalValues**](https://reference.aspose.com/cells/net/aspose.cells/lookintype).请阅读代码中的注释以获取更多信息。

## C# 使用原始值搜索数据的代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.cs" >}}

## 示例代码生成的控制台输出

这是上述示例代码的控制台输出。

{{< highlight "java" >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]{{< /highlight >}}
