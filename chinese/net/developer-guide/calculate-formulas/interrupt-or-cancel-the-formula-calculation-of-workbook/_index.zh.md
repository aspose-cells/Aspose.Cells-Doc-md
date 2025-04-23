---
title: 中断或取消工作簿的公式计算
description: 本文介绍了如何使用 Aspose.Cells 库来中断或取消 Microsoft Excel 工作簿的公式计算。通过加载现有的 Excel 文件或创建新文件，我们可以使用 Aspose.Cells 提供的方法中断或取消公式计算，并获得结果。最后，将修改后的 Excel 文件保存到磁盘。
keywords: Aspose.Cells, Excel, 工作簿, 公式计算, 中断, 取消
type: docs
weight: 50
url: /zh/net/interrupt-or-cancel-the-formula-calculation-of-workbook/
---

## **可能的使用场景**

Aspose.Cells 提供了一种通过 [**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt) 方法来中断或取消工作簿的公式计算的机制。当工作簿的公式计算耗时较长，您希望取消其处理时，这将会很有用。

## **中断或取消工作簿的公式计算**

以下示例代码实现了 [**BeforeCalculate()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/beforecalculate) 类的 [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) 方法。在此方法内部，它使用行和列索引参数查找单元格名称。如果单元格名称为 B8，则通过调用 [**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt) 方法中断计算过程。一旦 [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) 类的具体类实现完成，它的实例将被分配给 [**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/calculationmonitor) 属性。最后，通过传递 [**CalculationOptions**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions) 作为参数调用 [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)。请参阅以下示例代码中使用的 [示例 Excel 文件](51740731.xlsx) 以及代码的控制台输出作为参考。

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.cs" >}}

## **控制台输出**

{{< highlight java >}}

 0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
