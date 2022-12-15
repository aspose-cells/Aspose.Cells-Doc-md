---
title: 验证 Cell 值是否满足数据验证规则
type: docs
weight: 90
url: /zh/java/verify-that-cell-value-satisfies-data-validation-rules/
---
{{% alert color="primary" %}}

Microsoft Excel 允许用户向工作表单元格添加数据验证规则。例如，可以应用小数验证来限制 10 到 20 之间的数字。如果输入此指定范围之外的任何其他数字，Microsoft Excel 会显示错误消息并提示用户重新输入正确范围内的数字。如果用户将数字（例如 3）复制粘贴到单元格中，Excel 不会运行验证检查或显示错误消息。

{{% /alert %}}

## 验证 Cell 值是否满足数据验证规则

有时，需要动态验证给定值是否满足应用于单元格的数据验证规则。为此，Aspose.Cells API 提供了[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ） 方法。如果单元格中的值不满足应用于该单元格的数据有效性规则，则返回**错误的**， 别的**真的**.

以下示例 Microsoft Excel 文件与下面的示例代码一起用于测试[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue()） 方法。正如您在快照中看到的那样，细胞**C1**有**十进制数据验证**应用并且只接受值**10 到 20 之间**.每当单元格的值介于 10 和 20 之间时，[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) 方法将返回**真的** 否则返回**错误的**.

![待办事项：图像_替代_文本](verify-that-cell-value-satisfies-data-validation-rules_1.png)

下面的示例代码说明了如何[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() 方法有效。首先，它将值 3 输入 C1。因为这不满足数据验证规则，所以[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() 方法返回**错误的**.然后，它将值 15 输入 C1。因为这个值满足数据验证规则，所以[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() 方法返回**真的**.同样，它返回**错误的**价值 30。

## Java 验证 Cell 值是否满足数据验证规则的代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyCellValueSatisfiesDataValidationRules-VerifyCellValueSatisfiesDataValidationRules.java" >}}

## 示例代码生成的控制台输出

这是使用上面显示的示例 Excel 文件执行示例代码时生成的控制台输出。

{{< highlight "java" >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
