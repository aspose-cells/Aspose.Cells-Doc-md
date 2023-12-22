---
title: 计算公式的方法
type: docs
weight: 30
url: /zh/cpp/ways-to-calculate-formulas/
---
##  **介绍**
Aspose.Cells具有嵌入式公式计算引擎。它不仅可以重新计算从设计器模板导入的公式，还支持计算运行时添加的公式的结果。
##  **添加公式并计算结果**
Aspose.Cells 支持 Microsoft Excel 中的大多数公式或函数。它们可以通过 API 或使用设计器电子表格来使用。 Aspose.Cells 支持大量数学、字符串、布尔、日期/时间、统计、查找和参考公式。

使用 Cell.SetFormula 方法将公式添加到单元格。将公式应用于单元格时，请始终以等号 (=) 开头字符串，就像在 Microsoft Excel 中创建公式时一样。使用逗号 (,) 分隔函数参数。

要计算公式的结果，请调用 Workbook.CalculateFormula() 方法，该方法处理 Excel 文件中嵌入的所有公式。请参阅以下添加公式并计算其结果的示例代码。请检查[输出Excel文件](38109185.xlsx)用此代码生成。

**示例代码**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-AddingFormulasAndCalculatingResults-new.cpp" >}}
<!---## **Direct Calculation of Formula**
Sometimes, you need to calculate formula results directly without adding them into a worksheet. The values of the cells used in the formula already exist in a worksheet and all you need is to find the result of those values based on some Microsoft Excel formula without adding the formula in a worksheet.

You can use Worksheet.CalculateFormula(String formula) method to calculate the results of such formulas without adding them to worksheet.

The code below produces the following output.

{{< highlight java >}}

 Value of A1: 20

Value of A2: 30

Result of Sum(A1:A2): 50

{{< /highlight >}}

**Sample Code**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-DirectCalculationOfFormula.cpp" >}}   --->
##  **仅计算一次公式**
当调用 Workbook.CalculateFormula() 来计算工作簿模板中的公式值时，Aspose.Cells 创建一个计算链。当第二次或第三次计算公式时，它会提高性能。

但是，如果模板包含大量公式，则第一次计算公式会消耗大量 CPU 处理时间和内存。

Aspose.Cells 允许您关闭创建计算链，当您只想计算公式一次时，这非常有用。

请使用 false 参数调用 Workbook.GetISettings().SetCreateCalcChain()。您可以使用[提供excel文件](38109186.xlsx)来测试这段代码。

**示例代码**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-WaysToCalculateFormulas-CalculatingFormulasOnceOnly-new.cpp" >}}
