---
title: 在 Cell 上应用验证
type: docs
weight: 200
url: /zh/net/get-validation-applied-on-a-cell/
description: 本文介绍如何在 Cell 和 C# 上应用验证
keywords: apply cell validation in excel with c#, apply validation on a cell in excel with c#, apply validation in excel with c#, cell validation in excel with c#, c# apply cell validation in excel, c# apply validation on a cell in excel, c# cell validation in excel, c# cell validation
---
{{% alert color="primary" %}}

您可以使用 Aspose.Cells 将验证应用于单元格。 Aspose.Cells 提供了[**Cell.GetValidation()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidation)为此目的的方法。如果没有对单元格应用验证，则返回 null。

同样，您可以使用[**工作表.Validations.GetValidationInCell**](https://reference.aspose.com/cells/net/aspose.cells/validationcollection/methods/getvalidationincell)方法通过提供其行和列索引来获取应用于单元格的验证。

{{% /alert %}}

## C# 用于获取应用于 Cell 的验证的代码

下面的代码示例向您展示了如何在单元格上应用验证。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetValidationAppliedOnCell-GetValidationAppliedOnCell.cs" >}}

## 相关文章

- [数据验证](/cells/zh/net/data-validation/)
