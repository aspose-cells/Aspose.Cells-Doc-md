---
title: 获取应用于单元格的验证
type: docs
weight: 200
url: /zh/net/get-validation-applied-on-a-cell/
description: 本文展示了如何使用C#在单元格上应用验证
keywords: 使用C#在Excel中应用单元格验证，在Excel中对单元格应用验证，使用C#在Excel中应用验证，在Excel中对单元格应用验证，用C#在Excel中应用单元格验证，用C#在Excel中对单元格应用验证
---

{{% alert color="primary" %}}

您可以使用Aspose.Cells获取应用于单元格的验证。Aspose.Cells为此提供了[**Cell.GetValidation()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidation)方法。如果单元格上没有应用验证，则返回null。

同样，您可以使用 [**Worksheet.Validations.GetValidationInCell**](https://reference.aspose.com/cells/net/aspose.cells/validationcollection/methods/getvalidationincell) 方法通过提供它的行和列索引来获取应用于单元格的验证。

{{% /alert %}}

## 用于获取单元格上应用的验证的C#代码

下面的代码示例演示了如何获取应用于单元格的验证。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetValidationAppliedOnCell-GetValidationAppliedOnCell.cs" >}}

## 相关文章

- [数据有效性](/cells/zh/net/data-validation/)
{{< app/cells/assistant language="csharp" >}}
