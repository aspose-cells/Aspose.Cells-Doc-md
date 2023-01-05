---
title: Прервать или отменить расчет формулы рабочей книги
type: docs
weight: 30
url: /ru/java/interrupt-or-cancel-the-formula-calculation-of-workbook/
---
## **Возможные сценарии использования**

Aspose.Cells предоставляет механизм для прерывания или отмены вычисления формулы рабочей книги с помощью метода interrupt() класса[**АннотацияРасчетМонитор**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) учебный класс. Это полезно, когда расчет формулы рабочей книги занимает слишком много времени, и вы хотите отменить ее обработку.

## **Прервать или отменить расчет формулы рабочей книги**

Следующий пример кода реализует[**передРассчитать()**](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationmonitor#beforeCalculate(int,%20int,%20int)) метод[**АннотацияРасчетМонитор**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor)учебный класс. Внутри этого метода он находит имя ячейки, используя параметры индекса строки и столбца. Если имя ячейки — B8, процесс расчета прерывается вызовом метода AbstractCalculationMonitor.interrupt(). Однажды конкретный класс[**АннотацияРасчетМонитор**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor)класс реализован, его экземпляр присваивается[**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CalculationMonitor)имущество. В заключение,[**Рабочая книга.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula(com.aspose.cells.CalculationOptions)) вызывается путем передачи[**Варианты расчета**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationOptions)как параметр. Пожалуйста, смотрите[образец файла Excel](51740744.xlsx)используется внутри кода, а также консольный вывод кода, приведенного ниже для справки.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.java" >}}

## **Консольный вывод**

{{< highlight "java" >}}

0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
