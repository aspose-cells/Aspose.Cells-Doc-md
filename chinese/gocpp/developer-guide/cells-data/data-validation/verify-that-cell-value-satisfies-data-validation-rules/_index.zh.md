---
title: 验证单元格值是否满足数据验证规则（用Golang via C++）
linktitle: 验证单元格值是否满足数据验证规则
type: docs
weight: 210
url: /zh/go-cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: 学习如何通过Aspose.Cells for C++ API验证单元格值是否符合数据验证规则。
keywords: 获取单元格验证值，获取单元格验证值，验证值是否满足应用于单元格的数据验证规则
---

{{% alert color="primary" %}} 

Microsoft Excel允许用户为单元格添加数据验证规则。例如，小数验证指定只能输入10到20之间的数字。如果用户输入不同的数字，Excel会显示错误信息并提示他们输入正确范围内的数字。如果复制粘贴一个数字，比如3，Excel不会进行验证检查或显示错误信息。

有时，有必要以编程方式验证一个值是否满足应用于该单元格的数据验证规则。例如，上面的情况下，输入应该是失败的。

{{% /alert %}} 

## **介绍**
Aspose.Cells提供[Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/)方法以编程方式验证单元格值。如果单元格中的值不满足应用的验证规则，则返回**False**，否则返回**True**。

以下示例代码演示了[Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/)方法的工作原理。首先，在C1输入值3，因为这不满足验证规则，返回值为**False**。然后，在C1输入值15，因为该值满足验证规则，返回值为**True**。类似地，输入30时返回**False**。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-VerifyThatCellValueSatisfiesDataValidationRules.go" >}}
### **输出**
{{< highlight java >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
