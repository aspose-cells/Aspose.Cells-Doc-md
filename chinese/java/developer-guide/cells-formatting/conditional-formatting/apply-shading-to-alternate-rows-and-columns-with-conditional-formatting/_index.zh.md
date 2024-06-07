---
title: 使用条件格式对交替行和列应用阴影
type: docs
weight: 10
url: /zh/java/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells API提供了为[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)对象添加和操作条件格式规则的手段。这些规则可以根据条件或规则以多种方式进行调整，以获得所需的格式设置。本文将演示如何使用Aspose.Cells for Java API来应用条件格式规则和Excel内置函数，以对交替行和列应用底纹。

{{% /alert %}} 
## **使用条件格式为交替行和列应用底纹**
本文使用了Excel的内置函数，例如ROW、COLUMN和MOD。以下是这些函数的一些详细信息，以更好地理解后面提供的代码片段。

- **ROW()** 函数返回单元格引用的行号。如果省略引用，则假定引用是输入ROW函数的单元格地址。
- **COLUMN()** 函数返回单元格引用的列号。如果省略引用，则假定引用是输入COLUMN函数的单元格地址。
- **MOD()** 函数返回数字除以除数后的余数，其中函数的第一个参数是要查找其余数的数字值，第二个参数是用于除以数字参数的数字。如果除数是 0，则返回 #DIV/0! 错误。

让我们开始编写一些代码，以借助Aspose.Cells for Java API实现目标。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ApplyShadingToAlternateRowsAndColumns-ApplyShadingToAlternateRowsAndColumns.java" >}}



以下快照显示了在 Excel 应用程序中加载的结果电子表格。

![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)

为了将交替列着色应用到电子表格，您只需将公式 **=MOD(ROW(),2)=0** 更改为 **=MOD(COLUMN(),2)=0**，也就是; 修改公式以检索列索引，而不是行索引。 
在这种情况下，生成的电子表格将如下图所示。

![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)
