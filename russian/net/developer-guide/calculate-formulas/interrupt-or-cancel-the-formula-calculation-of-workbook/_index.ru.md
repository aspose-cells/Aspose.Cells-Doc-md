---
title: Прервать или Отменить Расчет Формулы Рабочей Книги
description: В этой статье объясняется, как использовать библиотеку Aspose.Cells для прерывания или отмены расчета формул рабочих книг в Microsoft Excel. Путем загрузки существующего файла Excel или создания нового мы можем использовать методы, предоставленные Aspose.Cells, для прерывания или отмены расчета формул и получить результат. Наконец, мы сохраняем измененный файл Excel на диск.
keywords: Aspose.Cells, Excel, рабочие книги, расчеты формул, прерывания, отмены
type: docs
weight: 50
url: /ru/net/interrupt-or-cancel-the-formula-calculation-of-workbook/
---

## **Возможные сценарии использования**

Aspose.Cells предоставляет механизм для прерывания или отмены расчета формул рабочей книги с использованием метода [**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt). Это полезно, когда расчет формул рабочей книги занимает слишком много времени, и вы хотите отменить его обработку.

## **Прерывание или отмена расчета формул книги**

Следующий образец кода реализует метод [**BeforeCalculate()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/beforecalculate) класса [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor). Внутри этого метода он находит имя ячейки с использованием параметров индекса строки и столбца. Если имя ячейки - B8, он прерывает процесс расчета, вызывая метод [**AbstractCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt). После того как конкретный класс [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) реализован, его экземпляр присваивается свойству [**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/calculationmonitor). Наконец, вызывается [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index), передавая [**CalculationOptions**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions) в качестве параметра. Пожалуйста, смотрите [образец файла Excel](51740731.xlsx), использованный в коде, а также вывод консоли ниже для справки.

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.cs" >}}

## **Вывод в консоль**

{{< highlight java >}}

 0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
