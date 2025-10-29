---
title: 获取带格式和不带格式的单元格字符串值
type: docs
weight: 240
url: /zh/nodejs-cpp/get-cell-string-value-with-and-without-formatting/
description: 了解如何通过 Aspose.Cells for Node.js via C++ API 获取带格式和不带格式的单元格字符串值。
keywords: 用 C++ 通过 Node.js 获取带格式和不带格式的单元格字符串值，用 C++ 通过 Node.js 获取带格式和不带格式的单元格字符串值，利用 C++ 通过 Node.js 获取带格式和不带格式的单元格字符串值。
---

{{% alert color="primary" %}}

Aspose.Cells 提供一个 [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--) 方法，可以用来获取单元格的字符串值，无论是否带有格式。假设你有一个值为 0.012345 的单元格，你对其应用了格式，仅显示两位小数，那么在 Excel 中会显示为 0.01。你可以用 [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--) 方法同时获取为 0.01 和 0.012345两种值。该方法接受一个 [**CellValueFormatStrategy**](https://reference.aspose.com/cells/nodejs-cpp/cellvalueformatstrategy/) 枚举参数，具有以下值。

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

以下示例代码说明了[**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--)方法的使用。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-GetCellStringWithOrWithoutFormatting.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
