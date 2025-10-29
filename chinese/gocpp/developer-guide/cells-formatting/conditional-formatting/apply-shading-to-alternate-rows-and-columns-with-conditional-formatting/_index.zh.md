---
title: 使用 Golang 通过 C++ 对交替行和列应用阴影的条件格式化
linktitle: 为交替行列应用阴影
description: 如何在C++中使用Aspose.Cells库为交替行列的条件格式添加阴影。通过调整这些条件，您可以更好地控制单元格的外观和显示。
keywords: Aspose.Cells，条件格式，C++，交替行，交替列，阴影
type: docs
weight: 30
url: /zh/go-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Aspose.Cells API提供了添加和操作 [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) 对象的条件格式规则的方法。这些规则可以以多种方式定制，以根据条件或规则获得所需的格式。本文将演示如何使用Aspose.Cells for C++ API，通过条件格式规则和Excel内置函数，为交替行列添加阴影。

{{% /alert %}}

本文使用Excel内置函数，如ROW、COLUMN和MOD。以下是这些函数的一些详细信息，以便更好地理解提供的代码片段。

- **ROW()**函数返回单元格引用的行号。如果省略引用参数，则假定引用是输入ROW函数的单元格地址。
- **COLUMN()**函数返回单元格引用的列号。如果省略引用参数，则假定引用是输入COLUMN函数的单元格地址。
- **MOD()**函数返回一个数字被除数除后的余数，函数的第一个参数是要查找余数的数值，第二个参数是用来除以数值参数的数。如果除数为0，则会返回#DIV/0!错误。

让我们开始编写一些代码，借助Aspose.Cells for C++ API实现此目标。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ApplyShadingToAlternateRowsAndColumnsWithConditionalFormatting.go" >}}
以下快照显示了加载到Excel应用程序中的结果电子表格。

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

为了将底纹应用于交替列，您只需将公式**=MOD(ROW(),2)=0**更改为**=MOD(COLUMN(),2)=0**，即不再获取行索引，而是修改公式以检索列索引。 
在这种情况下，生成的电子表格将如下所示。

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
