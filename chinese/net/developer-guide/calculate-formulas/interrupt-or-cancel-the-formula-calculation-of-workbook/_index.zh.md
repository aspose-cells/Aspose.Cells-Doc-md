---
title: 中断或取消工作簿的公式计算
description: 本文介绍如何使用Aspose.Cells库来中断或取消Microsoft Excel中工作簿的公式计算。通过加载现有的Excel文件或创建一个新的Excel文件，我们可以使用Aspose.Cells提供的方法来中断或取消公式计算并得到结果。最后，我们将修改后的 Excel 文件保存到磁盘。
keywords: Aspose.Cells, Excel, workbooks, formula calculations, breaks, cancellations
type: docs
weight: 50
url: /zh/net/interrupt-or-cancel-the-formula-calculation-of-workbook/
---
##  **可能的使用场景**

Aspose.Cells 提供了一种机制来中断或取消工作簿的公式计算，使用[**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)方法。当工作簿的公式计算花费太多时间并且您想要取消其处理时，这非常有用。

##  **中断或取消工作簿的公式计算**

下面的示例代码实现了[**BeforeCalculate()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/beforecalculate)的方法[**抽象计算监视器**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)班级。在此方法中，它使用行和列索引参数查找单元格名称。如果单元格名称为B8，则通过调用[**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)方法。曾经，具体类[**抽象计算监视器**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)类被实现，它的实例被分配给[**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/calculationmonitor)财产。最后，[**工作簿.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)通过传递来调用[**计算选项**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions)作为参数。请参阅[Excel 文件示例](51740731.xlsx)代码内部使用以及下面给出的代码的控制台输出以供参考。

##  **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.cs" >}}

##  **控制台输出**

{{< highlight "java" >}}

 0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
