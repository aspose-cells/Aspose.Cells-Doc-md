---
title: Прервать или Отменить Расчет Формулы Рабочей Книги
type: docs
weight: 30
url: /ru/java/interrupt-or-cancel-the-formula-calculation-of-workbook/
---

## **Возможные сценарии использования**

Aspose.Cells предоставляет механизм для прерывания или отмены расчета формул в книге рабочих с помощью метода interrupt() класса [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor). Это полезно, когда расчет формул в книге занимает слишком много времени и вы хотите отменить его обработку.

## **Прерывание или отмена расчета формул книги**

Приведенный ниже образец кода реализует метод [**beforeCalculate()**](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationmonitor#beforeCalculate-int-int-int-) класса [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor). Внутри этого метода он находит имя ячейки, используя параметры индекса строки и столбца. Если имя ячейки B8, он прерывает процесс вычисления, вызывая метод interrupt() класса AbstractCalculationMonitor. Как только конкретный класс [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) реализован, его экземпляр назначается свойству [**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CalculationMonitor). Наконец, вызывается [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula-com.aspose.cells.CalculationOptions-), передавая [**CalculationOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationOptions) в качестве параметра. Пожалуйста, ознакомьтесь с [примером файла Excel](51740744.xlsx), используемым в коде, а также с выводом консоли приведенного ниже кода для справки.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.java" >}}

## **Вывод в консоль**

{{< highlight java >}}

0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
