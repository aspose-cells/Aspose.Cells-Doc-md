---
title: 验证单元格值是否满足数据验证规则
type: docs
weight: 210
url: /zh/nodejs-cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: 学习如何通过 Aspose.Cells for Node.js via C++ API 验证单元格值是否满足数据验证规则。
keywords: 通过 C++ 使用 Node.js 获取单元格验证值，使用 C++ 获取 Node.js 中的单元格验证值，验证值是否满足单元格应用的数据验证规则  Node.js 通过 C++
---

{{% alert color="primary" %}} 

Microsoft Excel允许用户为单元格添加数据验证规则。例如，小数验证指定只能输入10到20之间的数字。如果用户输入不同的数字，Excel会显示错误信息并提示他们输入正确范围内的数字。如果复制粘贴一个数字，比如3，Excel不会进行验证检查或显示错误信息。

有时，有必要以编程方式验证一个值是否满足应用于该单元格的数据验证规则。例如，上面的情况下，输入应该是失败的。

{{% /alert %}} 
## **介绍**
Aspose.Cells for Node.js via C++ 提供了 [Cell.getValidationValue()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--) 方法来以编程方式验证单元格值。如果单元格中的值不满足该单元格应用的数据验证规则，则返回 **false**，否则返回 **true**。

以下示例代码演示了 [Cell.getValidationValue()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--) 方法的工作原理。首先，在 C1 输入值 3。因为这不满足数据验证规则，所以 [Cell.getValidationValue()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--) 方法返回 **false**。然后，在 C1 输入值 15。因为此值满足数据验证规则，所以该方法返回 **true**。类似地，对于值 30，也会返回 **false**。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-VerifyValidationCellValues.js" >}}


### **输出**
{{< highlight javascript >}}

 Is 3 a Valid Value for this Cell: false

Is 15 a Valid Value for this Cell: true

Is 30 a Valid Value for this Cell: false

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
