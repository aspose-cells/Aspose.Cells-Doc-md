---
title: 验证单元格值是否符合数据验证规则
type: docs
weight: 210
url: /zh/python-net/verify-that-cell-value-satisfies-data-validation-rules/
description: 通过Aspose.Cells for Python通过.NET API学习如何验证单元格值是否符合数据验证规则。
keywords: Python Excel库，Python获取单元格验证值，Python获取单元格验证值，Python验证值是否符合应用于单元格的数据验证规则。
---

{{% alert color="primary" %}} 

Microsoft Excel允许用户向单元格添加数据验证规则。例如，十进制验证指定只能输入10到20之间的数字。如果用户输入不同的数字，则Microsoft Excel会显示错误消息并提示他们输入正确范围内的数字。如果将一个数字，比如3，复制粘贴到单元格中，Excel不会运行验证检查或显示错误消息。

有时，有必要通过编程方式验证一个值是否符合应用到单元格的数据验证规则。例如，在上面的情况下，输入应该会失败。

{{% /alert %}} 
## **介绍**
Aspose.Cells for Python通过.NET提供了[Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#)方法，以便以编程方式验证单元格值。 如果单元格中的值不满足应用的数据验证规则，则返回**False**，否则返回**True**。

以下示例代码说明了[Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#)方法的工作原理。 首先，将值3输入到C1。 因为这不符合数据验证规则，因此[Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#)方法返回**False**。 然后，将值15输入到C1。 因为这个值符合数据验证规则，所以[Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#)方法返回**True**。 类似地，对于值30返回**False**。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-DataValidationRules-1.py" >}}

### **输出**
{{< highlight java >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
