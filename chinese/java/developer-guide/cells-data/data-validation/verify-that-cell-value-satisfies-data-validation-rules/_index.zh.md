---
title: 验证单元格值是否满足数据验证规则
type: docs
weight: 90
url: /zh/java/verify-that-cell-value-satisfies-data-validation-rules/
---

{{% alert color="primary" %}}

Microsoft Excel允许用户向工作表单元格添加数据验证规则。例如，可以应用十进制验证以限制数字在10和20之间。如果输入此指定范围之外的任何其他数字，Microsoft Excel会显示错误消息并提示用户重新输入正确范围内的数字。如果用户复制粘贴一个数字，比如3，进入单元格，Excel不会运行验证检查或显示错误消息。

{{% /alert %}}

## 验证单元格值是否符合数据验证规则

有时，动态验证给定值是否满足应用于单元格的数据验证规则是必要的。为此，Aspose.Cells API提供了[**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--)方法。如果单元格中的值不满足应用于该单元格的数据验证规则，则返回**False**，否则返回**True**。

使用以下示例 Microsoft Excel 文件与下面的示例代码一起测试 [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) 方法。从快照中可以看到，单元格 **C1** 应用了 **十进制数据验证**，并且只接受 **10 到 20 之间**的值。每当单元格的值在 10 到 20 之间，[**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) 方法会返回 **True**，否则返回 **False**。

![todo:image_alt_text](verify-that-cell-value-satisfies-data-validation-rules_1.png)

以下示例代码说明了 [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) 方法的工作原理。首先，它将值 3 输入到 C1 中。因为这不符合数据验证规则，[**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) 方法返回 **False**。然后，它将值 15 输入到 C1 中。因为这个值符合数据验证规则，[**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) 方法返回 **True**。类似地，对值 30 返回 **False**。

## 用Java代码验证单元格值是否符合数据验证规则

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyCellValueSatisfiesDataValidationRules-VerifyCellValueSatisfiesDataValidationRules.java" >}}

## 示例代码生成的控制台输出

这是在上面显示的示例Excel文件执行示例代码生成的控制台输出。

{{< highlight java >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
