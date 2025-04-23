---
title: 使用Aspose.Cells库在C#中应用条件格式阴影以交替显示行和列。通过调整这些条件，您可以更好地控制单元格的外观。
linktitle: 使用Aspose.Cells库在C#中应用条件格式阴影以交替显示行和列。通过调整这些条件，您可以更好地控制单元格的外观。
description: 如何通过 C++ 在 Node.js 中使用 Aspose.Cells 库为交替行列添加条件格式阴影。通过调整这些条件，你可以更好地控制单元格的外观。
keywords: Aspose.Cells，条件格式，Node.js via C++，交替行，交替列，阴影
type: docs
weight: 30
url: /zh/nodejs-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Aspose.Cells API 提供了为 [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 对象添加和操作条件格式规则的手段。这些规则可以多种方式定制，以根据条件或规则实现理想的格式。本文章将演示如何使用 Aspose.Cells for Node.js via C++ API 结合条件格式规则和 Excel 内置函数，对奇偶行和列进行阴影填充。

{{% /alert %}}

本文使用Excel内置函数，如ROW、COLUMN和MOD。以下是这些函数的一些详细信息，以便更好地理解提供的代码片段。

- **ROW()** 函数返回单元格引用的行号。如果省略引用参数，则假定引用为输入 ROW 函数的单元格地址。
- **COLUMN()** 函数返回单元格引用的列号。如果省略引用参数，则假定引用为输入 COLUMN 函数的单元格地址。
- **MOD()**函数返回一个数字被除数除后的余数，函数的第一个参数是要查找余数的数值，第二个参数是用来除以数值参数的数。如果除数为0，则会返回#DIV/0!错误。

让我们开始编写一些代码，利用 Aspose.Cells for Node.js via C++ API 实现此目标。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-ApplyShadingToAlternateRowsAndColumns.js" >}}


以下快照显示了加载到Excel应用程序中的结果电子表格。

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

为了将底纹应用于交替列，您只需将公式**=MOD(ROW(),2)=0**更改为**=MOD(COLUMN(),2)=0**，即不再获取行索引，而是修改公式以检索列索引。  
在这种情况下，生成的电子表格将如下所示。

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
