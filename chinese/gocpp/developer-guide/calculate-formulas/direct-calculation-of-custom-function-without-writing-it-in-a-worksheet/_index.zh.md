---
title: 通过C++和Golang直接计算自定义函数，无需在工作表中书写
linktitle: 直接计算自定义函数
description: 本文介绍如何使用Aspose.Cells库在Microsoft Excel中直接计算自定义函数，而无需在工作表中编写函数。 通过加载现有的Excel文件或创建一个新的Excel文件，我们可以使用Aspose.Cells提供的方法来计算自定义函数并获得结果。 最后，我们将修改后的Excel文件保存到磁盘。
keywords: Aspose.Cells, Excel, 自定义函数, 直接计算, 无需书写, 工作表
type: docs
weight: 90
url: /zh/go-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **无需在工作表中编写，直接计算自定义函数**

本主题介绍如何在不先写入工作表的情况下直接计算自定义函数。请使用[**Worksheet::CalculateFormula(System::String formula, CalculationOptions opts)**](https://reference.aspose.com/cells/go-cpp/worksheet/calculateformula_string/)方法实现此目的。

请参见以下示例代码，说明了此方法的使用。我们使用了一个名为MyCompany::CustomFunction()的自定义函数，自己计算其值为“Aspose.Cells。”，然后此值将由计算引擎自动与单元格A1的值“欢迎来到”拼接，最终返回“欢迎来到Aspose.Cells。”。如代码所示，我们没有在工作表中写入任何自定义函数，而是通过我们自己的自定义逻辑直接计算。

### **编程示例**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DirectCalculationOfCustomFunctionWithoutWritingItInAWorksheet.go" >}}
### **控制台输出**

以下是上面示例代码的控制台输出。

{{< highlight java >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **相关文章**

{{% alert color="primary" %}}

[实现自定义计算引擎以扩展Aspose.Cells的默认引擎](/cells/zh/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
