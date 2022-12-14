---
title: 计算公式
type: docs
weight: 125
url: /zh/net/calculate-formulas/
---
## **添加公式和计算结果**

Aspose.Cells 内嵌公式计算引擎。它不仅可以重新计算从设计器模板导入的公式，还支持计算运行时添加的公式的结果。

 Aspose.Cells 支持 Microsoft Excel 中的大部分公式或函数（阅读[计算引擎支持的函数列表](/cells/zh/net/supported-formula-functions/)).这些功能可以通过 API 或设计器电子表格使用。 Aspose.Cells 支持大量数学、字符串、布尔值、日期/时间、统计、数据库、查找和参考公式。

使用[**公式**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula)财产或[**设置公式（...）**](https://reference.aspose.com/cells/net/aspose.cells.cell/setformula/methods/2)的方法[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类将公式添加到单元格。应用公式时，始终以等号 (=) 开头字符串，就像在 Microsoft Excel 中创建公式时所做的那样，并使用逗号 (,) 分隔函数参数。

要计算公式的结果，用户可以调用[**计算公式**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1)的方法[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)处理嵌入在 Excel 文件中的所有公式的类。或者，用户可以调用[**计算公式**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/calculateformula)的方法[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)处理工作表中嵌入的所有公式的类。或者，用户也可以调用[**计算**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/calculate)的方法[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)处理一个 Cell 的公式的类：

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulas-1.cs" >}}

### **重要须知**

{{% alert color="primary" %}}

这**公式**财产和**设置公式（...）**的方法[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)班级工作不同于**计算**的方法[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook), [**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)和[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类。这**公式**财产和**设置公式（...）**方法只是将公式添加到单元格，但不在运行时计算结果。要获得公式的结果，请致电**计算**方法。

{{% /alert %}}

## **公式直接计算**

Aspose.Cells 内嵌公式计算引擎。除了从设计器文件导入计算公式，Aspose.Cells 还可以直接计算公式结果。

有时，您需要直接计算公式结果而不将它们添加到工作表中。公式中使用的单元格值已存在于工作表中，您只需根据某些 Microsoft Excel 公式查找这些值的结果，而无需在工作表中添加公式。

您可以使用 Aspose.Cells' 公式计算引擎 APIs[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)至[**计算**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3)这些公式的结果而不将它们添加到工作表中：

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DirectCalculationFormula-1.cs" >}}

上面的代码产生以下输出：
{{< highlight "net" >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **反复计算公式**

当工作簿中的公式很多，用户需要重复计算而只修改其中的一小部分时，启用公式计算链可能对性能有帮助：[**公式设置.启用计算链**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/enablecalculationchain).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulasOnce-1.cs" >}}

### **重要须知**

{{% alert color="primary" %}}

默认情况下，计算链是禁用的。因为创建链也需要额外的时间，第一次计算公式（[**工作簿.CalculateFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1)) 与不使用链式计算公式相比，可能会消耗更多的 CPU 处理时间和内存。如果用户不需要重复计算公式，默认行为（直接计算公式而不创建计算链）应该是更好的方法。

{{% /alert %}}


## **推进主题**
- [添加 Cells 到 Microsoft Excel 公式监视窗口](/cells/zh/net/add-cells-to-microsoft-excel-formula-watch-window/)
- [使用 Aspose.Cells 计算 IFNA 函数](/cells/zh/net/calculating-ifna-function-using-aspose-cells/)
- [数据表数组公式计算](/cells/zh/net/calculation-of-array-formula-of-data-tables/)
- [Excel 2016 MINIFS和MAXIFS函数的计算](/cells/zh/net/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [减少Cell.Calculate方法的计算时间](/cells/zh/net/decrease-the-calculation-time-of-cell-calculate-method/)
- [检测循环引用](/cells/zh/net/detecting-circular-reference/)
- [自定义函数直接计算，无需写在工作表中](/cells/zh/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [实施自定义计算引擎以扩展 Aspose.Cells 的默认计算引擎](/cells/zh/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [中断或取消工作簿的公式计算](/cells/zh/net/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [使用 AbstractCalculationEngine 返回值范围](/cells/zh/net/returning-a-range-of-values-using-abstractcalculationengine/)
- [使用 ICustomFunction 返回值范围](/cells/zh/net/returning-a-range-of-values-using-icustomfunction/)
- [设置工作簿的公式计算方式](/cells/zh/net/setting-formula-calculation-mode-of-workbook/)
- [在 Aspose.Cells 中使用 FormulaText 函数](/cells/zh/net/using-formulatext-function-in-aspose-cells/)
- [使用 ICustomFunction 功能](/cells/zh/net/using-icustomfunction-feature/)
