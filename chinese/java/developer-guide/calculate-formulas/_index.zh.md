---
title: 计算公式
type: docs
weight: 110
url: /zh/java/calculate-formulas/
---

## **添加公式并计算结果**

Aspose.Cells具有内置的公式计算引擎。它不仅可以重新计算从设计模板导入的公式，还支持计算运行时添加的公式的结果。

Aspose.Cells 支持 Microsoft Excel 的大多数公式或功能（阅读 [计算引擎支持的函数列表](/cells/zh/java/supported-formula-functions/)）。这些函数可以通过 API 或设计器电子表格使用。Aspose.Cells 支持大量的数学、字符串、布尔、日期/时间、统计、数据库、查找、引用公式。

使用 [**Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) 属性或 [**SetFormula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setFormula(java.lang.String,%20com.aspose.cells.FormulaParseOptions,%20java.lang.Object)) 方法的 [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) 类，将公式添加到单元格中。在应用公式时，始终以等号（=）开头，就像在 Microsoft Excel 中创建公式一样，并使用逗号（）来分隔函数参数。

要计算公式的结果，用户可以调用 [**CalculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)) 方法，该方法处理 Excel 文件中嵌入的所有公式。或者，用户可以调用 [**CalculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula(com.aspose.cells.CalculationOptions,%20boolean)) 方法，它处理工作表中嵌入的所有公式。或者，用户还可以调用 [**Calculate**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#calculate(com.aspose.cells.CalculationOptions)) 方法，该方法处理一个单元格的公式:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulas-CalculatingFormulas.java" >}}

### **重要知识**

{{% alert color="primary" %}}

[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)类的**Formula**属性和**SetFormula(...)**方法与[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)、[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)和[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)类的**计算**方法有所不同。**Formula**属性和**SetFormula(...)**方法仅向单元格添加公式，而不会在运行时计算结果。要获得公式的结果，请调用**Calculate**方法。

{{% /alert %}}

## **公式的直接计算**

Aspose.Cells具有内置的公式计算引擎。除了计算从设计文件导入的公式外，Aspose.Cells还可以直接计算公式结果。

有时，您需要直接计算公式结果，而不将其添加到工作表中。公式中使用的单元格的值已经存在于工作表中，您只需根据一些Microsoft Excel公式找到这些值的结果即可，而无需将公式添加到工作表中。

用户可以使用 Aspose.Cells 的公式计算引擎 API 来在不将其添加到工作表的情况下计算此类公式的结果 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 到 [**calculate**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula(java.lang.String,%20com.aspose.cells.CalculationOptions))。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DirectCalculationFormula-DirectCalculationFormula.java" >}}

上述代码产生以下输出:
{{< highlight java >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **重复计算公式**

当工作簿中有大量公式，用户需要反复计算这些公式并仅修改其中的一小部分时，启用公式计算链可能有助于性能: [**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#EnableCalculationChain)。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulasOnce-CalculatingFormulasOnce.java" >}}

### **重要知识**

{{% alert color="primary" %}}

默认情况下，计算链是禁用的。因为创建链也需要额外的时间，所以第一次计算公式时（[**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)），与创建计算链时相比，可能会消耗更多的 CPU 处理时间和内存。如果用户不需要重复计算公式，则默认行为（直接计算公式而不创建计算链）应该是更好的方式。

{{% /alert %}}

## **高级主题**
- [将单元格添加到Microsoft Excel公式监视窗口](/cells/zh/java/add-cells-to-microsoft-excel-formula-watch-window/)
- [Aspose.Cells 公式计算引擎](/cells/zh/java/aspose-cells-formula-calculation-engine/)
- [使用Aspose.Cells计算IFNA函数](/cells/zh/java/calculating-ifna-function-using-aspose-cells/)
- [数据表数组公式的计算](/cells/zh/java/calculation-of-array-formula-of-data-tables/)
- [Excel 2016 MINIFS和MAXIFS函数的计算](/cells/zh/java/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [减少Cell.Calculate方法的计算时间](/cells/zh/java/decrease-the-calculation-time-of-cell-calculate-method/)
- [检测循环引用](/cells/zh/java/detecting-circular-reference/)
- [在工作表中直接计算自定义函数而不将其写入](/cells/zh/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [实现自定义计算引擎以扩展Aspose.Cells的默认计算引擎](/cells/zh/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [中断或取消工作簿的公式计算](/cells/zh/java/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [使用AbstractCalculationEngine返回一系列值](/cells/zh/java/returning-a-range-of-values-using-abstractcalculationengine/)
- [使用ICustomFunction返回一系列值](/cells/zh/java/returning-a-range-of-values-using-icustomfunction/)
- [使用ICustomFunction功能](/cells/zh/java/using-icustomfunction-feature/)
