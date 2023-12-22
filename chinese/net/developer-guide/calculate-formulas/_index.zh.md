---
title: 计算公式
description: 本文介绍如何使用Aspose.Cells库在Microsoft Excel中计算公式。通过加载现有的Excel文件或者新建一个Excel文件，我们可以使用Aspose.Cells提供的方法来计算公式并得到结果。最后，我们将修改后的 Excel 文件保存到磁盘。
keywords: Aspose.Cells, Excel, formulas, calculations, Direct Calculation of Formula, Calculate Formulas repeatedly, add formulas.
type: docs
weight: 125
url: /zh/net/calculate-formulas/
---
##  **添加公式并计算结果**

Aspose.Cells具有嵌入式公式计算引擎。不仅可以重新计算从设计器模板导入的公式，还支持计算运行时添加的公式的结果。

 Aspose.Cells 支持 Microsoft Excel 中的大多数公式或函数（阅读[计算引擎支持的函数列表](/cells/zh/net/supported-formula-functions/)）。这些功能可以通过 API 或设计器电子表格使用。 Aspose.Cells 支持大量数学、字符串、布尔值、日期/时间、统计、数据库、查找和参考公式。

使用[**公式**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula)财产或[**设置公式(...)**](https://reference.aspose.com/cells/net/aspose.cells.cell/setformula/methods/2)的方法[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类将公式添加到单元格。应用公式时，请始终以等号 (=) 开头，就像在 Microsoft Excel 中创建公式时一样，并使用逗号 (,) 分隔函数参数。

要计算公式的结果，用户可以调用[**计算公式**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1)的方法[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook)处理 Excel 文件中嵌入的所有公式的类。或者，用户可以调用[**计算公式**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/calculateformula)的方法[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)处理工作表中嵌入的所有公式的类。或者，用户也可以调用[**计算**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/calculate)的方法[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)处理 Cell 的公式的类：

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulas-1.cs" >}}

###  **公式重要知识**

{{% alert color="primary" %}}

这**公式**财产和**设置公式(...)**的方法[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)课堂作业与课堂作业不同**计算**的方法[**练习册**](https://reference.aspose.com/cells/net/aspose.cells/workbook), [**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)和[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类。这**公式**财产和**设置公式(...)**方法只是将公式添加到单元格中，但不会在运行时计算结果。如需获取公式结果，请致电**计算**方法。

{{% /alert %}}

##  **直接计算公式**

Aspose.Cells具有嵌入式公式计算引擎。除了从设计器文件导入的计算公式外，Aspose.Cells还可以直接计算公式结果。

有时，您需要直接计算公式结果，而不将其添加到工作表中。公式中使用的单元格的值已存在于工作表中，您所需要做的就是根据某些 Microsoft Excel 公式查找这些值的结果，而无需在工作表中添加公式。

您可以使用Aspose.Cells'公式计算引擎API[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)到[**计算**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3)此类公式的结果，无需将其添加到工作表中：

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DirectCalculationFormula-1.cs" >}}

上面的代码产生以下输出：
{{< highlight "net" >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

##  **如何重复计算公式**

当工作簿中有大量公式，并且用户需要仅修改其中一小部分而重复计算时，启用公式计算链可能对性能有帮助：[**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/enablecalculationchain).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulasOnce-1.cs" >}}

###  **重要了解**

{{% alert color="primary" %}}

默认情况下，计算链被禁用。由于创建链也需要额外的时间，所以第一次计算公式（[**工作簿.CalculateFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1)）与没有链式的计算公式相比，可能会消耗更多的CPU处理时间和内存。如果用户不需要重复计算公式，那么默认行为（直接计算公式而不创建计算链）应该是更好的方法。

{{% /alert %}}


##  **高级主题**
- [将 Cells 添加到 Microsoft Excel 公式监视窗口](/cells/zh/net/add-cells-to-microsoft-excel-formula-watch-window/)
- [使用 Aspose.Cells 计算 IFNA 函数](/cells/zh/net/calculating-ifna-function-using-aspose-cells/)
- [数据表数组公式计算](/cells/zh/net/calculation-of-array-formula-of-data-tables/)
- [Excel 2016 MINIFS 和 MAXIFS 函数的计算](/cells/zh/net/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [减少Cell的计算时间。计算方法](/cells/zh/net/decrease-the-calculation-time-of-cell-calculate-method/)
- [检测循环参考](/cells/zh/net/detecting-circular-reference/)
- [自定义函数直接计算，无需将其写入工作表](/cells/zh/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [实现自定义计算引擎以扩展Aspose.Cells的默认计算引擎](/cells/zh/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [中断或取消工作簿的公式计算](/cells/zh/net/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [使用 AbstractCalculationEngine 返回一系列值](/cells/zh/net/returning-a-range-of-values-using-abstractcalculationengine/)
- [使用 ICustomFunction 返回值范围](/cells/zh/net/returning-a-range-of-values-using-icustomfunction/)
- [设置工作簿公式计算模式](/cells/zh/net/setting-formula-calculation-mode-of-workbook/)
- [使用Aspose.Cells中的FormulaText函数](/cells/zh/net/using-formulatext-function-in-aspose-cells/)
- [使用 ICustomFunction 功能](/cells/zh/net/using-icustomfunction-feature/)
