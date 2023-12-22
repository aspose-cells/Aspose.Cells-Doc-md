---
title: 使用条件格式将底纹应用到交替行和列
description: 如何使用 C# 中的 Aspose.Cells 库为交替行和列应用条件格式阴影。通过调整这些标准，您可以更好地控制单元格的外观和显示方式。
keywords: Aspose.Cells, Conditional Formatting, C#, Alternate Rows, Alternate Columns, Shadows
type: docs
weight: 30
url: /zh/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---
{{% alert color="primary" %}}

 Aspose.Cells API 提供了添加和操作条件格式规则的方法[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)目的。可以通过多种方式定制这些规则，以根据条件或规则获得所需的格式。本文将演示如何使用 Aspose.Cells for .NET API 借助条件格式规则和 Excel 的内置函数将底纹应用于交替行和列。

{{% /alert %}}

本文利用 Excel 的内置函数，如 ROW、COLUMN 和 MOD。以下是这些函数的一些详细信息，以便更好地理解前面提供的代码片段。

- **ROW()**函数返回单元格引用的行号。如果省略引用参数，则假定引用是已输入 ROW 函数的单元格地址。
- **COLUMN()**函数返回单元格引用的列号。如果省略引用参数，则假定引用是已输入 COLUMN 函数的单元格地址。
- **MOD()**函数返回数字除以除数后的余数，其中函数的第一个参数是要查找余数的数值，第二个参数是用于除以数字参数的数字。如果除数为0，则返回#DIV/0！错误。

让我们在 Aspose.Cells for .NET API 的帮助下开始编写一些代码来实现这个目标。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-ApplyShadingToAlternateRowsColumns-1.cs" >}}

以下快照显示了 Excel 应用程序中加载的结果电子表格。

|![待办事项：图像_替代_文本](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

为了将阴影应用于替代列，您所要做的就是更改公式**=MOD(行(),2)=0**如*=MOD(COLUMN(),2)=0**，即；修改公式以检索列索引，而不是获取行索引。
在这种情况下，生成的电子表格将如下所示。

|![待办事项：图像_替代_文本](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
