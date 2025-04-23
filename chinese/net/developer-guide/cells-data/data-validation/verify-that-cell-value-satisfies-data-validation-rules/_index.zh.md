---
title: 验证单元格值是否满足数据验证规则
type: docs
weight: 210
url: /zh/net/verify-that-cell-value-satisfies-data-validation-rules/
description: 学习如何通过Aspose.Cells for .NET API验证单元格值是否满足数据验证规则。
keywords: 获取单元格验证值，获取单元格验证值，验证值是否满足应用于单元格的数据验证规则
---

{{% alert color="primary" %}} 

Microsoft Excel 允许用户向单元格添加数据验证规则。例如，十进制验证指定只能输入介于 10 和 20 之间的数字。如果用户输入不同的数字，则 Microsoft Excel 显示一个错误消息，并提示其输入正确范围的数字。如果您复制并粘贴一个数字，比如 3，到该单元格，Excel 不会运行验证检查或显示错误消息。

有时，有必要以编程方式验证一个值是否满足应用于该单元格的数据验证规则。例如，上面的情况下，输入应该是失败的。

{{% /alert %}} 
## **介绍**
Aspose.Cells提供了[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue)方法，以便以编程方式验证单元格值。如果单元格中的值不满足应用于该单元格的数据验证规则，则返回**False**，否则返回**True**。

以下示例代码说明了[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue)方法的工作方式。首先，它将值3输入到C1。因为这不满足数据验证规则，[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue)方法返回**False**。然后，它将值15输入到C1。因为这个值满足数据验证规则，[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue)方法返回**True**。类似地，对于值30，它返回**False**。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}
### **输出**
{{< highlight java >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
