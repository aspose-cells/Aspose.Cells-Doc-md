---
title: 使用条件格式对交替行和列应用阴影
description: 如何在C#中使用Aspose.Cells库应用交替行和列的条件格式阴影。通过调整这些条件，您可以更好地控制单元格的外观。
keywords: Aspose.Cells, 条件格式, C#, 交替行, 交替列, 阴影
type: docs
weight: 30
url: /zh/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Aspose.Cells API提供添加和操作条件格式规则的手段为[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 对象。这些规则可以在多种方式下进行调整，以根据条件或规则获得所需的格式。本文将演示如何使用Aspose.Cells for .NET API通过条件格式规则和Excel内置函数将阴影应用于交替行和列。

{{% /alert %}}

本文使用了Excel的内置函数，例如ROW、COLUMN和MOD。以下是这些函数的一些细节，以便更好理解前面提供的代码片段。

- **ROW()** 函数返回单元格引用的行号。如果省略了引用参数，则假定引用是输入了 ROW 函数的单元格地址。
- **COLUMN()** 函数返回单元格引用的列号。如果省略了引用参数，则假定引用是输入了 COLUMN 函数的单元格地址。
- **MOD()** 函数返回数字除以除数后的余数，其中函数的第一个参数是要查找其余数的数字值，第二个参数是用于除以数字参数的数字。如果除数是 0，则返回 #DIV/0! 错误。

让我们开始编写一些代码，以完成此目标，并借助 Aspose.Cells for .NET API。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-ApplyShadingToAlternateRowsColumns-1.cs" >}}

以下快照显示了在 Excel 应用程序中加载的结果电子表格。

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

为了将交替列着色应用到电子表格，您只需将公式 **=MOD(ROW(),2)=0** 更改为 **=MOD(COLUMN(),2)=0**，也就是; 修改公式以检索列索引，而不是行索引。 
在这种情况下，生成的电子表格将如下所示。

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
