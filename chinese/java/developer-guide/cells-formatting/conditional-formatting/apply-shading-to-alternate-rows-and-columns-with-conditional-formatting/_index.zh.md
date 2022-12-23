---
title: 使用条件格式将底纹应用于交替行和列
type: docs
weight: 10
url: /zh/java/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---
{{% alert color="primary" %}} 

Aspose.Cells API 提供了添加和操作条件格式规则的方法[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)目的。这些规则可以通过多种方式进行定制，以根据条件或规则获得所需的格式。本文将演示如何使用 Aspose.Cells for Java API 借助条件格式规则和 Excel 的内置函数将底纹应用于交替的行和列。

{{% /alert %}} 
## **使用条件格式将底纹应用于交替行和列**
本文使用 Excel 的内置函数，如 ROW、COLUMN 和 MOD。下面是这些函数的一些细节，以便更好地理解前面提供的代码片段。

- **排（）**函数返回单元格引用的行号。如果省略引用，则假定引用是输入 ROW 函数的单元格地址。
- **柱子（）**函数返回单元格引用的列号。如果省略引用，则假定引用是输入 COLUMN 函数的单元格地址。
- **模组()**函数返回数字除以除数后的余数，其中函数的第一个参数是要求余数的数值，第二个参数是用于除以数字参数的数字。如果除数为 0，则返回 #DIV/0！错误。

让我们在 Aspose.Cells for Java API 的帮助下开始编写一些代码来实现目标。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ApplyShadingToAlternateRowsAndColumns-ApplyShadingToAlternateRowsAndColumns.java" >}}



以下快照显示了在 Excel 应用程序中加载的结果电子表格。

![待办事项：图片_替代_文本](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)

为了将阴影应用于替代列，您所要做的就是更改公式**=MOD(行(),2)=0**作为**=MOD(列(),2)=0** ， 那是;不是获取行索引，而是修改公式以检索列索引。
在这种情况下，生成的电子表格将如下图所示。

![待办事项：图片_替代_文本](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)
