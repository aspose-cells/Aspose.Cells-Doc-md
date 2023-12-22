---
title: 验证 Cell 值是否满足数据验证规则
type: docs
weight: 210
url: /zh/net/verify-that-cell-value-satisfies-data-validation-rules/
description: 了解如何通过 Aspose.Cells for .NET API.. 验证 Cell 值是否满足数据验证规则。
keywords: Get Cell Validation Value, Obtain Cell Validation Value, Verify whether a value satisfies the data validation rules applied to the cell
---
{{% alert color="primary" %}} 

Microsoft Excel 允许用户向单元格添加数据验证规则。例如，小数验证指定只能输入 10 到 20 之间的数字。如果用户输入不同的号码。 Microsoft Excel 显示错误消息并提示他们输入正确范围内的数字。如果将数字（例如 3）复制并粘贴到单元格中，Excel 不会运行验证检查或显示错误消息。

有时，需要验证某个值是否满足以编程方式应用于单元格的数据验证规则。例如，在上述情况下，输入应该会失败。

{{% /alert %}} 
##  **介绍**
 Aspose.Cells 提供[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue)以编程方式验证单元格值的方法。如果单元格中的值不满足应用于该单元格的数据验证规则，则返回*False**，否则返回*True**。

以下示例代码说明了如何[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue)方法有效。首先，它将值 3 输入到 C1 中。因为这不满足数据有效性规则，[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue)方法返回**错误的**。然后，将值 15 输入到 C1 中。由于该值满足数据验证规则，因此 [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) 方法返回 **True**。同样，它返回**False**值为 30。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}
###  **输出**
{{< highlight "java" >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
