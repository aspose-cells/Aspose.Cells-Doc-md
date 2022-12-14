---
title: 计算公式的方法
type: docs
weight: 30
url: /zh/cpp/ways-to-calculate-formulas/
---
## **介绍**
Aspose.Cells 内嵌公式计算引擎。它不仅可以重新计算从设计器模板导入的公式，还支持计算运行时添加的公式的结果。
## **添加公式和计算结果**
Aspose.Cells 支持 Microsoft Excel 中的大部分公式或函数。它们可以通过 API 或使用设计器电子表格使用。 Aspose.Cells 支持大量数学、字符串、布尔值、日期/时间、统计、查找和参考公式。

使用 Cell.Formula 方法将公式添加到单元格。将公式应用于单元格时，始终以等号 (=) 开头字符串，就像在 Microsoft Excel 中创建公式时所做的那样。使用逗号 (,) 分隔函数参数。

要计算公式的结果，请调用 Workbook.CalculateFormula() 方法，该方法处理嵌入在 Excel 文件中的所有公式。请参阅以下添加公式并计算其结果的示例代码。请检查[输出excel文件](38109185.xlsx)使用此代码生成。

**示例代码**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-AddingFormulasAndCalculatingResults.cpp" >}}
## **公式直接计算**
有时，您需要直接计算公式结果而不将它们添加到工作表中。公式中使用的单元格值已存在于工作表中，您只需根据某些 Microsoft Excel 公式查找这些值的结果，而无需在工作表中添加公式。

您可以使用 Worksheet.CalculateFormula(String formula) 方法来计算此类公式的结果，而无需将它们添加到工作表中。

下面的代码产生以下输出。

{{< highlight "java" >}}

 Value of A1: 20

Value of A2: 30

Result of Sum(A1:A2): 50

{{< /highlight >}}

**示例代码**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-DirectCalculationOfFormula.cpp" >}}
## **只计算一次公式**
当调用 Workbook.CalculateFormula() 计算工作簿模板中公式的值时，Aspose.Cells 创建一个计算链。当第二次或第三次计算公式时，它会提高性能。

但是，如果模板包含大量公式，第一次计算公式会消耗大量 CPU 处理时间和内存。

Aspose.Cells 允许您关闭创建计算链，这在您只想计算一次公式时很有用。

请使用 false 参数调用 Workbook.GetISettings().SetCreateCalcChain()。您可以使用[提供的excel文件](38109186.xlsx)测试这段代码。

**示例代码**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-CalculatingFormulasOnceOnly.cpp" >}}
