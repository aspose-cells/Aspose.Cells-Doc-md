---
title: 验证单元格值是否满足数据验证规则
type: docs
weight: 210
url: /zh/python-net/verify-that-cell-value-satisfies-data-validation-rules/
description: 了解如何通过 Aspose.Cells for Python via .NET API 验证单元格值是否满足数据验证规则。
keywords: Python Excel 库，Python 获取单元格验证值，Python 获取单元格验证值，Python 验证单元格中的值是否满足数据验证规则
---

{{% alert color="primary" %}} 

Microsoft Excel 允许用户向单元格添加数据验证规则。例如，十进制验证指定只能输入介于 10 和 20 之间的数字。如果用户输入不同的数字，则 Microsoft Excel 显示一个错误消息，并提示其输入正确范围的数字。如果您复制并粘贴一个数字，比如 3，到该单元格，Excel 不会运行验证检查或显示错误消息。

有时，有必要以编程方式验证一个值是否满足应用于该单元格的数据验证规则。例如，上面的情况下，输入应该是失败的。

{{% /alert %}} 
## **介绍**
Aspose.Cells for Python via .NET 提供了 [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) 方法，用于以编程方式验证单元格值。如果单元格中的值不满足应用于该单元格的数据验证规则，则返回**False**，否则返回**True**。

下面的示例代码说明了 [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) 方法的工作原理。首先，它将值 3 输入到 C1。因为这不满足数据验证规则，[Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) 方法返回**False**。然后，它将值 15 输入到 C1。因为这个值满足数据验证规则，[Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) 方法返回**True**。同样，对值 30 返回**False**。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-DataValidationRules-1.py" >}}

### **输出**
{{< highlight java >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
