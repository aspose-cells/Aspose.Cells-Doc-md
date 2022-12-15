---
title: 在 Cell 上应用验证
type: docs
weight: 80
url: /zh/java/get-validation-applied-on-a-cell/
description: 本文介绍如何在 Cell 和 Java 上应用验证
keywords: apply cell validation in excel with java, apply validation on a cell in excel with java, apply validation in excel with java, cell validation in excel with java, java apply cell validation in excel, java apply validation on a cell in excel, java cell validation in excel, java cell validation
---
{{% alert color="primary" %}}

您可以使用 Aspose.Cells API 将验证应用于任何单元格。 Aspose.Cells 提供了[**Cell.getValidation**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidation() 方法用于此目的。如果单元格没有验证，则返回 null。同样，您可以使用[**Worksheet.getValidations().getValidationInCell(int row, int column)**](https://reference.aspose.com/cells/java/com.aspose.cells/validationcollection#getValidationInCell(int,%20int)) 方法通过提供其行和列索引来获取应用于单元格的验证。

{{% /alert %}}

以下快照显示了以下示例代码中使用的示例 Microsoft Excel 文件。 Cell**C1**有**十进制验证**已应用且只能取值**10 到 20 之间**.

**具有验证功能的单元格**

![待办事项：图像_替代_文本](get-validation-applied-on-a-cell_1.png)

下面的示例代码获取应用于 C1 的验证并读取其各种属性。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetValidationAppliedonCell-GetValidationAppliedonCell.java" >}}

这是使用上面快照中显示的示例文件执行的示例代码的控制台输出。

{{< highlight "java" >}}

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
