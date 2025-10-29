---
title: 计算公式
type: docs
weight: 110
url: /zh/java/calculate-formulas/
---

## **添加公式及计算结果**

Aspose.Cells内置了一个公式计算引擎。它不仅可以重新计算从设计模板导入的公式，还支持计算在运行时添加的公式的结果。

Aspose.Cells支持大多数Microsoft Excel公式或函数（阅读[a list of the functions supported by the calculation engine](/cells/zh/java/supported-formula-functions/)）。这些函数可以通过API或设计工作表来使用。Aspose.Cells支持大量的数学、字符串、布尔、日期/时间、统计、数据库、查找和引用公式。

使用 [**Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) 属性或 [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) 类的 [**SetFormula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setFormula-java.lang.String-com.aspose.cells.FormulaParseOptions-java.lang.Object-) 方法来向单元格添加公式。在应用公式时，始终以等号（=）开头，就像在Microsoft Excel中创建公式时一样，并使用逗号（，）来分隔函数参数。

为了计算公式的结果，用户可以调用【**CalculateFormula**】(https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula-com.aspose.cells.CalculationOptions--) 方法，此方法属于 {0} 类的 {1} 方法，能够处理嵌入在 Excel 文件中的所有公式。或者用户可以调用 {2} 类中的 {3} 方法，也可以调用 {4} 类中的 {5} 方法，这些方法都用于处理单个单元格的公式：

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulas-CalculatingFormulas.java" >}}

### **重要知识**

{{% alert color="primary" %}}

[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)类的**Formula**属性和**SetFormula(...)**方法与[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)、[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)和[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)类的**Calculate**方法的工作方式不同。**Formula**属性和**SetFormula(...)**方法仅向单元格添加公式，但不会在运行时计算结果。要获取公式的结果，请调用**Calculate**方法。

{{% /alert %}}

## **直接计算公式**

Aspose.Cells内置了一个公式计算引擎。除了计算从设计文件导入的公式外，Aspose.Cells还可以直接计算公式的结果。

有时，您需要直接计算公式的结果，而无需将它们添加到工作表中。公式中使用的单元格的值已经存在于工作表中，您只需要根据一些Microsoft Excel公式找到这些值的结果，而不需要将公式添加到工作表中。

您可以使用Aspose.Cells的公式计算引擎API来 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 到 [**calculate**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#calculateFormula-java.lang.String-com.aspose.cells.CalculationOptions-) 不将这些公式添加到工作表中的结果。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DirectCalculationFormula-DirectCalculationFormula.java" >}}

以上代码生成以下输出：
{{< highlight java >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **重复计算公式**

当工作簿中有大量公式，用户需要重复计算它们，并且只需修改其中的一小部分时，启用公式计算链（[**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/java/com.aspose.cells/formulasettings#EnableCalculationChain)）可能有助于提高性能。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-CalculatingFormulasOnce-CalculatingFormulasOnce.java" >}}

### **重要知识**

{{% alert color="primary" %}}

默认情况下，计算链是禁用的。因为创建计算链也需要额外时间，第一次计算公式（[**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula-com.aspose.cells.CalculationOptions--)）可能比没有创建计算链直接计算公式消耗更多的 CPU 时间和内存。如果用户不需要反复计算公式，建议保持默认行为（直接计算公式而不创建计算链），这是更好的方式。

{{% /alert %}}

## **高级主题**
- [将单元格添加到Microsoft Excel公式监视窗口](/cells/zh/java/add-cells-to-microsoft-excel-formula-watch-window/)
- [Aspose.Cells公式计算引擎](/cells/zh/java/aspose-cells-formula-calculation-engine/)
- [使用Aspose.Cells计算IFNA函数](/cells/zh/java/calculating-ifna-function-using-aspose-cells/)
- [计算数据表的数组公式](/cells/zh/java/calculation-of-array-formula-of-data-tables/)
- [计算Excel 2016的MINIFS和MAXIFS函数](/cells/zh/java/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [减少Cell.Calculate方法的计算时间](/cells/zh/java/decrease-the-calculation-time-of-cell-calculate-method/)
- [检测循环引用](/cells/zh/java/detecting-circular-reference/)
- [在不将其写入工作表的情况下直接计算自定义函数](/cells/zh/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [实现自定义计算引擎以扩展Aspose.Cells的默认计算引擎](/cells/zh/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [中断或取消工作簿的公式计算](/cells/zh/java/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [使用AbstractCalculationEngine返回一系列值](/cells/zh/java/returning-a-range-of-values-using-abstractcalculationengine/)
- [使用ICustomFunction返回一系列值](/cells/zh/java/returning-a-range-of-values-using-icustomfunction/)
- [使用ICustomFunction功能](/cells/zh/java/using-icustomfunction-feature/)
{{< app/cells/assistant language="java" >}}
