---
title: 中断或取消工作簿的公式计算
type: docs
weight: 30
url: /zh/java/interrupt-or-cancel-the-formula-calculation-of-workbook/
---

## **可能的使用场景**

Aspose.Cells提供一种机制，使用 [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) 类的 interrupt() 方法来中断或取消工作簿的公式计算。 当工作簿的公式计算耗时过长且您希望取消其处理时，此方法就会派上用场。

## **中断或取消工作簿的公式计算**

以下示例代码实现了 [**beforeCalculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationmonitor#beforeCalculate(int,%20int,%20int)）方法的 [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) 类。 在此方法内部，使用行和列索引参数查找单元格名称。 如果单元格名称为 B8，则通过调用 AbstractCalculationMonitor.interrupt() 方法中断计算过程。 一旦 [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) 类的具体实现完成，其实例将分配给 [**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CalculationMonitor) 属性。 最后，通过传递 [**CalculationOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationOptions) 参数来调用 [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions))。 请参阅代码中使用的样本Excel文件及以下给出的代码的控制台输出作为参考。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.java" >}}

## **控制台输出**

{{< highlight java >}}

0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
