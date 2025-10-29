---
title: 获取应用在单元格上的验证（用Golang via C++）
linktitle: 获取应用于单元格的验证
type: docs
weight: 200
url: /zh/go-cpp/get-validation-applied-on-a-cell/
description: 本文介绍如何用Golang via C++对单元格应用验证。
keywords: 用C++在Excel中应用单元格验证；在Excel中对单元格应用验证；在Excel中进行验证；Excel中的单元格验证；使用C++在Excel中应用单元格验证；用C++对Excel中的单元格进行验证；C++在Excel中的单元格验证；C++在Excel中应用验证。
---

{{% alert color="primary" %}}

您可以使用Aspose.Cells获取应用于单元格的验证。Aspose.Cells为此提供了[**Cell::GetValidation()**](https://reference.aspose.com/cells/go-cpp/cell/getvalidation/)方法。如果单元格上没有应用验证，则返回null。

同样，您可以使用 [**Worksheet::Validations::GetValidationInCell**](https://reference.aspose.com/cells/go-cpp/validationcollection/getvalidationincell/) 方法通过提供它的行和列索引来获取应用于单元格的验证。

{{% /alert %}}

## 用C++获取已应用到单元格的验证

下面的代码示例演示了如何获取应用到单元格的验证。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetValidationAppliedOnACell.go" >}}
## 相关文章

- [数据有效性](/cells/zh/cpp/data-validation/)
