---
title: 获取应用在单元格上的验证
type: docs
weight: 200
url: /zh/net/get-validation-applied-on-a-cell/
description: 本文介绍如何在C#中对单元格应用验证
keywords: 在Excel中使用C#对单元格进行验证，在Excel中的单元格应用验证，使用C#在Excel中应用验证，Excel中的单元格验证，C#在Excel中应用单元格验证，C#在Excel中的单元格应用验证，C#在Excel中的单元格验证，C#单元格验证
---

{{% alert color="primary" %}}

您可以使用Aspose.Cells来获取应用到单元格的验证。Aspose.Cells提供了这个目的的 [**Cell.GetValidation()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidation) 方法。如果单元格上没有应用验证，它将返回null。

类似地，您可以使用 [**Worksheet.Validations.GetValidationInCell**](https://reference.aspose.com/cells/net/aspose.cells/validationcollection/methods/getvalidationincell) 方法通过提供其行和列索引来获取应用到单元格的验证。

{{% /alert %}}

## 用于获取单元格上应用的验证的C#代码

下面的代码示例展示了如何获取应用到单元格的验证。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetValidationAppliedOnCell-GetValidationAppliedOnCell.cs" >}}

## 相关文章

- [数据验证](/cells/zh/net/data-validation/)
