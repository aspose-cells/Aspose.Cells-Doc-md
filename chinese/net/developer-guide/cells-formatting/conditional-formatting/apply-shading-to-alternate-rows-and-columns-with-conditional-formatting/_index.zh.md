---
title: 使用Aspose.Cells库在C#中应用条件格式阴影以交替显示行和列。通过调整这些条件，您可以更好地控制单元格的外观。
description: Aspose.Cells，条件格式，C#，交替行，交替列，阴影
keywords: Aspose.Cells API提供了添加和操作条件格式规则的方法。这些规则可以根据条件或规则以多种方式定制，从而根据要求获取所需的格式。本文将演示如何使用Aspose.Cells for .NET API通过条件格式规则和Excel内置函数为交替行和列应用底纹。
type: docs
weight: 30
url: /zh/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Aspose.Cells API 提供了添加和操作条件格式规则的方法，用于 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 对象。这些规则可以根据条件或规则以多种方式定制，以便根据需求进行格式设置。本文将演示使用 Aspose.Cells for .NET API 来通过条件格式规则和 Excel 内置函数将交替行和列着色的方法。

{{% /alert %}}

本文使用Excel内置函数，如ROW、COLUMN和MOD。以下是这些函数的一些详细信息，以便更好地理解提供的代码片段。

- **ROW()**函数返回单元格引用的行号。如果省略引用参数，则假定引用是输入ROW函数的单元格地址。
- **COLUMN()**函数返回单元格引用的列号。如果省略引用参数，则假定引用是输入COLUMN函数的单元格地址。
- **MOD()**函数返回一个数字被除数除后的余数，函数的第一个参数是要查找余数的数值，第二个参数是用来除以数值参数的数。如果除数为0，则会返回#DIV/0!错误。

让我们开始编写一些代码，利用 Aspose.Cells for .NET API 实现这一目标。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-ApplyShadingToAlternateRowsColumns-1.cs" >}}

以下快照显示了加载到Excel应用程序中的结果电子表格。

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

为了将底纹应用于交替列，您只需将公式**=MOD(ROW(),2)=0**更改为**=MOD(COLUMN(),2)=0**，即不再获取行索引，而是修改公式以检索列索引。 
在这种情况下，生成的电子表格将如下所示。

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
{{< app/cells/assistant language="csharp" >}}
