---
title: 中断或取消工作簿的公式计算
type: docs
weight: 30
url: /zh/java/interrupt-or-cancel-the-formula-calculation-of-workbook/
---
## **可能的使用场景**

Aspose.Cells 提供了一种机制，可以使用 interrupt() 方法中断或取消工作簿的公式计算[**抽象计算监视器**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor)班级。当工作簿的公式计算花费太多时间并且您想取消其处理时，这很有用。

## **中断或取消工作簿的公式计算**

下面的示例代码实现了[**之前计算（）**](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationmonitor#beforeCalculate(int,%20int,%20int)) 的方法[**抽象计算监视器**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor)班级。在此方法内部，它使用行和列索引参数查找单元格名称。如果单元格名称为 B8，则通过调用 AbstractCalculationMonitor.interrupt() 方法中断计算过程。曾经，具体类[**抽象计算监视器**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor)类被实现，它的实例被分配给[**计算选项.计算监视器**](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CalculationMonitor)财产。最后，[**工作簿.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)) 通过传递调用[**计算选项**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationOptions)作为参数。请参阅[示例 Excel 文件](51740744.xlsx)代码内部使用以及下面给出的代码的控制台输出供参考。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.java" >}}

## **控制台输出**

{{< highlight "java" >}}

0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
