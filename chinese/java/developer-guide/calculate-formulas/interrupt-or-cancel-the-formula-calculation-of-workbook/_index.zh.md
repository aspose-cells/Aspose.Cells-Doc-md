---
title: 中断或取消工作簿的公式计算
type: docs
weight: 30
url: /zh/java/interrupt-or-cancel-the-formula-calculation-of-workbook/
---

## **可能的使用场景**

Aspose.Cells提供了使用AbstractCalculationMonitor类的interrupt()方法来中断或取消工作簿的公式计算的机制。当工作簿的公式计算时间过长并且需要取消其处理时，这将非常有用。

## **中断或取消工作簿的公式计算**

以下示例代码实现了AbstractCalculationMonitor.interrupt()方法的[**beforeCalculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationmonitor#beforeCalculate(int,%20int,%20int)类。在该方法内部，使用行和列索引参数找到单元格名称。如果单元格名称为B8，它将通过调用AbstractCalculationMonitor.interrupt()方法来中断计算过程。一旦[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor)类的具体类被实现，它的实例就被分配给[**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor)属性。最后，通过传递[**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CalculationMonitor)作为参数来调用[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)。还请参考给定以下代码的[sample Excel file](51740744.xlsx)和控制台输出。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.java" >}}

## **控制台输出**

{{< highlight java >}}

0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
