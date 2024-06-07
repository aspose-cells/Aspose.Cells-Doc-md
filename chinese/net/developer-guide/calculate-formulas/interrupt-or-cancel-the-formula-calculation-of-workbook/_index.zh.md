---
title: 中断或取消工作簿的公式计算
description: 该文章介绍了如何使用Aspose.Cells库来中断或取消Microsoft Excel工作簿中的公式计算。通过加载现有的Excel文件或创建新文件，我们可以使用Aspose.Cells提供的方法来中断或取消公式计算并获取结果。最后，我们将修改后的Excel文件保存到磁盘。
keywords: Aspose.Cells，Excel，工作簿，公式计算，中断，取消
type: docs
weight: 50
url: /zh/net/interrupt-or-cancel-the-formula-calculation-of-workbook/
---

## **可能的使用场景**

Aspose.Cells提供了一种使用[**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)方法中断或取消工作簿的公式计算的机制。当工作簿的公式计算耗时过长并且您想取消其处理时，这很有用。

## **中断或取消工作簿的公式计算**

以下示例代码实现了[**BeforeCalculate()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/beforecalculate)类的[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)方法。在此方法中，它使用行和列索引参数查找单元格名称。如果单元格名称为B8，则通过调用[**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)方法中断计算过程。一旦[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)类的具体类实现，其实例将分配给[**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/calculationmonitor)属性。最后，通过将[**CalculationOptions**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions)作为参数传递来调用[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)。请参阅下面给出的代码的控制台输出和代码中使用的[示例Excel文件](51740731.xlsx)以供参考。

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.cs" >}}

## **控制台输出**

{{< highlight java >}}

 0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
