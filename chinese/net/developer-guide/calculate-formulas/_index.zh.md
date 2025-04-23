---
title: 计算公式
description: 本文介绍如何使用Aspose.Cells库来计算Microsoft Excel中的公式。通过加载现有的Excel文件或创建新的Excel文件，我们可以使用Aspose.Cells提供的方法来计算公式并获取结果。最后，我们将修改后的Excel文件保存到磁盘。
keywords: Aspose.Cells、Excel、公式、计算、公式的直接计算、重复计算公式、添加公式。
type: docs
weight: 125
url: /zh/net/calculate-formulas/
---

## **添加公式及计算结果**

Aspose.Cells内置了一个公式计算引擎。它不仅可以重新计算从设计模板导入的公式，还支持计算在运行时添加的公式的结果。

Aspose.Cells支持大部分Microsoft Excel公式或函数（阅读 [计算引擎支持的函数列表](/cells/zh/net/supported-formula-functions/)）。这些函数可以通过API或设计师电子表格来使用。Aspose.Cells支持大量的数学、字符串、布尔值、日期/时间、统计、数据库、查找和引用公式。

使用 [**Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) 属性或 [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) 类的 [**SetFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.cell/setformula/methods/2) 方法来向单元格添加公式。在应用公式时，始终以等号（=）开头，就像在Microsoft Excel中创建公式时一样，并使用逗号（，）来分隔函数参数。

要计算公式的结果，用户可以调用 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类的 [**CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1) 方法，该方法处理Excel文件中嵌入的所有公式。或者，用户可以调用 [**Worsheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类的 [**CalculateFormula**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/calculateformula) 方法，该方法处理工作表中嵌入的所有公式。用户还可以调用 [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) 类的 [**Calculate**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/calculate) 方法，该方法处理一个单元格的公式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulas-1.cs" >}}

### **公式重复计算的重要信息**

{{% alert color="primary" %}}

[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类的**Formula**属性和**SetFormula(...)**方法与[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)、[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)和[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)类的**Calculate**方法的工作方式不同。**Formula**属性和**SetFormula(...)**方法仅向单元格添加公式，但不会在运行时计算结果。要获取公式的结果，请调用**Calculate**方法。

{{% /alert %}}

## **直接计算公式**

Aspose.Cells内置了一个公式计算引擎。除了计算从设计文件导入的公式外，Aspose.Cells还可以直接计算公式的结果。

有时，您需要直接计算公式的结果，而无需将它们添加到工作表中。公式中使用的单元格的值已经存在于工作表中，您只需要根据一些Microsoft Excel公式找到这些值的结果，而不需要将公式添加到工作表中。

您可以使用Aspose.Cells的公式计算引擎API来 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 到 [**calculate**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/calculateformula/methods/3) 不将这些公式添加到工作表中的结果。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DirectCalculationFormula-1.cs" >}}

以上代码生成以下输出：
{{< highlight net >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **如何重复计算公式**

当工作簿中有大量公式，用户需要重复计算它们，并且只需修改其中的一小部分时，启用公式计算链（[**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/net/aspose.cells/formulasettings/properties/enablecalculationchain)）可能有助于提高性能。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-CalculatingFormulasOnce-1.cs" >}}

### **重要知识**

{{% alert color="primary" %}}

默认情况下，计算链是禁用的。因为创建链也需要额外的时间，第一次计算公式([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/net/aspose.cells.workbook/calculateformula/methods/1))可能比不创建链直接计算公式时消耗更多的CPU处理时间和内存。如果用户不需要重复计算公式，那么默认行为（直接计算公式而不创建计算链）应该是更好的方式。

{{% /alert %}}


## **高级主题**
- [将单元格添加到Microsoft Excel公式监视窗口](/cells/zh/net/add-cells-to-microsoft-excel-formula-watch-window/)
- [使用Aspose.Cells计算IFNA函数](/cells/zh/net/calculating-ifna-function-using-aspose-cells/)
- [计算数据表的数组公式](/cells/zh/net/calculation-of-array-formula-of-data-tables/)
- [计算Excel 2016的MINIFS和MAXIFS函数](/cells/zh/net/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [减少Cell.Calculate方法的计算时间](/cells/zh/net/decrease-the-calculation-time-of-cell-calculate-method/)
- [检测循环引用](/cells/zh/net/detecting-circular-reference/)
- [在不将其写入工作表的情况下直接计算自定义函数](/cells/zh/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [实现自定义计算引擎以扩展Aspose.Cells的默认计算引擎](/cells/zh/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [中断或取消工作簿的公式计算](/cells/zh/net/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [使用AbstractCalculationEngine返回一系列值](/cells/zh/net/returning-a-range-of-values-using-abstractcalculationengine/)
- [使用ICustomFunction返回一系列值](/cells/zh/net/returning-a-range-of-values-using-icustomfunction/)
- [设置工作簿的公式计算模式](/cells/zh/net/setting-formula-calculation-mode-of-workbook/)
- [在 Aspose.Cells 中使用 FormulaText 函数](/cells/zh/net/using-formulatext-function-in-aspose-cells/)
- [使用ICustomFunction功能](/cells/zh/net/using-icustomfunction-feature/)
{{< app/cells/assistant language="csharp" >}}
