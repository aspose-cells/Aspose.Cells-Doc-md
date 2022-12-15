---
title: Прервать или отменить расчет формулы рабочей книги
type: docs
weight: 50
url: /ru/net/interrupt-or-cancel-the-formula-calculation-of-workbook/
---
## **Возможные сценарии использования**

Aspose.Cells предоставляет механизм для прерывания или отмены вычисления формулы рабочей книги с помощью[**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)метод. Это полезно, когда расчет формулы рабочей книги занимает слишком много времени, и вы хотите отменить ее обработку.

## **Прервать или отменить расчет формулы рабочей книги**

Следующий пример кода реализует[**ПередРасчетом()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/beforecalculate)метод[**АннотацияРасчетМонитор**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) учебный класс. Внутри этого метода он находит имя ячейки, используя параметры индекса строки и столбца. Если имя ячейки — B8, процесс расчета прерывается вызовом функции[**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)метод. Однажды конкретный класс[**АннотацияРасчетМонитор**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)класс реализован, его экземпляр присваивается[**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/calculationmonitor)имущество. Окончательно,[**Рабочая книга.ВычислитьФормулу()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)вызывается путем передачи[**Варианты расчета**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions) как параметр. Пожалуйста, смотрите[образец файла Excel](51740731.xlsx)используется внутри кода, а также консольный вывод кода, приведенного ниже для справки.

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.cs" >}}

## **Консольный вывод**

{{< highlight "java" >}}

 0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
