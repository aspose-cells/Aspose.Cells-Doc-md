---
title: 获取应用在单元格上的验证
type: docs
weight: 80
url: /zh/java/get-validation-applied-on-a-cell/
description: 本文展示了如何使用Java对单元格应用验证
keywords: 在Java中用于在Excel中应用单元格验证，使用Java在Excel中对单元格应用验证，使用Java在Excel中应用验证，Excel中的Java单元格验证，Excel中的Java中应用单元格验证，Excel中的Java中应用验证，Excel中的Java单元格验证，Java中Excel单元格验证，Java中Excel中的单元格验证
---

{{% alert color="primary" %}}

您可以使用Aspose.Cells API获取应用于任何单元格的验证。Aspose.Cells为此目的提供了[**Cell.getValidation**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidation()) 方法。如果单元格上没有验证，则返回null。同样，您可以利用[**Worksheet.getValidations().getValidationInCell(int row, int column)**](https://reference.aspose.com/cells/java/com.aspose.cells/validationcollection#getValidationInCell(int,%20int)) 方法来获取应用于单元格的验证，提供其行和列索引。

{{% /alert %}}

以下快照显示了样本代码下使用的示例Microsoft Excel文件。单元格**C1**应用了**十进制验证**，只能接受**介于 10 和 20 之间**的值。

**带有验证的单元格**

![todo:image_alt_text](get-validation-applied-on-a-cell_1.png)

以下示例代码获取了C1应用的验证并读取了它的各种属性。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetValidationAppliedonCell-GetValidationAppliedonCell.java" >}}

这是使用在快照中显示的样本文件执行示例代码生成的控制台输出。

{{< highlight java >}}

Reading Properties of Validation

\--------------------------------

Type: 2

Operator: 0

Formula1: =10

Formula2: =20

Ignore blank: true

{{< /highlight >}}

## 相关文章

- [数据验证](/cells/zh/java/data-validation/)
