---
title: 中断或取消工作簿的公式计算
type: docs
weight: 50
url: /zh/net/interrupt-or-cancel-the-formula-calculation-of-workbook/
---
## **可能的使用场景**

Aspose.Cells 提供中断或取消工作簿公式计算的机制[**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)方法。当工作簿的公式计算花费太多时间并且您想取消其处理时，这很有用。

## **中断或取消工作簿的公式计算**

下面的示例代码实现了[**计算前()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/beforecalculate)的方法[**抽象计算监视器**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)班级。在此方法内部，它使用行和列索引参数查找单元格名称。如果单元格名称是 B8，它会通过调用[**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)方法。曾经，具体类[**抽象计算监视器**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)类被实现，它的实例被分配给[**计算选项.计算监视器**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/calculationmonitor)财产。最后，[**工作簿.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)通过传递调用[**计算选项**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions)作为参数。请参阅[示例 Excel 文件](51740731.xlsx)代码内部使用以及下面给出的代码的控制台输出供参考。

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.cs" >}}

## **控制台输出**

{{< highlight "java" >}}

 0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
