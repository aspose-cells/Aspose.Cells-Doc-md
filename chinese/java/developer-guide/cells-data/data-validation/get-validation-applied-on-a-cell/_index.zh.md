---
title: 获取应用于单元格的验证
type: docs
weight: 80
url: /zh/java/get-validation-applied-on-a-cell/
description: 本文介绍如何在Java中对单元格应用验证。
keywords: 在Java中在Excel中应用单元格验证，使用Java在Excel中对单元格应用验证，在Java中在Excel中应用验证，Java中在Excel中的单元格验证，Java在Excel中应用单元格验证，Java在Excel中对单元格应用验证，Java中的Excel中的单元格验证，Java中的单元格验证。
---

{{% alert color="primary" %}}

您可以使用Aspose.Cells API获取应用于任何单元格的验证。Aspose.Cells为此目的提供了[**Cell.getValidation()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidation--)方法。如果单元格上没有验证，它将返回null。同样，您可以通过提供其行和列索引使用[**Worksheet.getValidations().getValidationInCell(int row, int column)**](https://reference.aspose.com/cells/java/com.aspose.cells/validationcollection#getValidationInCell-int-int-)方法获取应用于单元格的验证。

{{% /alert %}}

以下快照显示了示例代码中使用的示例Microsoft Excel文件。单元格**C1**应用了**十进制验证**，并且只能接受**10到20之间**的值。

**具有验证的单元格**

![todo:image_alt_text](get-validation-applied-on-a-cell_1.png)

以下示例代码获取应用于 C1 的验证并读取其各种属性。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetValidationAppliedonCell-GetValidationAppliedonCell.java" >}}

以下是在上述快照中显示的示例文件中执行示例代码产生的控制台输出。

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

- [数据有效性](/cells/zh/java/data-validation/)
{{< app/cells/assistant language="java" >}}
