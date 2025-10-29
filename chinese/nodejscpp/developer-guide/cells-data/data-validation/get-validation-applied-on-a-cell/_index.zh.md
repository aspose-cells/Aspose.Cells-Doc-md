---
title: 获取应用于单元格的验证
type: docs
weight: 200
url: /zh/nodejs-cpp/get-validation-applied-on-a-cell/
description: 本文展示了如何通过 Node.js 使用 C++ 对单元格应用验证。
keywords: 在 Excel 中通过 Node.js 使用 C++ 应用单元格验证，在 Excel 中通过 C++ 使用 Node.js 进行验证，在 C++ 中使用 Node.js 在 Excel 中进行单元格验证，在 C++ 中用 Node.js 在 Excel 中应用单元格验证，Node.js 通过 C++ 在 Excel 中应用单元格验证，Node.js 通过 C++ 在 Excel 中对单元格进行验证
---

{{% alert color="primary" %}}

您可以使用 Aspose.Cells for Node.js 获取应用于单元格的验证。Aspose.Cells 提供了 [**Cell.getValidation()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidation--) 方法来实现此功能。如果单元格没有应用验证，则返回 null。

同样，您可以使用 [**Worksheet.validations.getValidationInCell(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/validationcollection/#getValidationInCell-number-number-) 方法通过提供它的行和列索引来获取应用于单元格的验证。

{{% /alert %}}

## 使用 Node.js 获取应用于单元格验证的代码示例

下面的代码示例演示了如何获取应用到单元格的验证。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-ReadingValidationPropertiesOfCell.js" >}}


## 相关文章

- [数据有效性](/cells/zh/nodejs-cpp/data-validation/)
{{< app/cells/assistant language="nodejs-cpp" >}}
