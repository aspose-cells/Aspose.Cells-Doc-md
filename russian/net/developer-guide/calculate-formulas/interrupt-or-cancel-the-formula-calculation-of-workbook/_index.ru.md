---
title: Прервите или отмените расчет формулы в рабочей книге
description: В этой статье рассказывается, как использовать библиотеку Aspose.Cells для прерывания или отмены вычислений по формулам в книгах в Microsoft Excel. Загрузив существующий файл Excel или создав новый, мы можем использовать методы, предоставленные Aspose.Cells, чтобы прервать или отменить расчет формулы и получить результат. Наконец, мы сохраняем измененный файл Excel на диск.
keywords: Aspose.Cells, Excel, workbooks, formula calculations, breaks, cancellations
type: docs
weight: 50
url: /ru/net/interrupt-or-cancel-the-formula-calculation-of-workbook/
---
##  **Возможные сценарии использования**

Aspose.Cells предоставляет механизм прерывания или отмены расчета формулы книги с помощью[**АннотацияCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)метод. Это полезно, когда расчет формулы книги занимает слишком много времени и вы хотите отменить ее обработку.

##  **Прервите или отмените расчет формулы в рабочей книге**

Следующий пример кода реализует[**BeforeCalculate()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/beforecalculate)метод[**АннотацияРасчетМонитор**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor) сорт. Внутри этого метода он находит имя ячейки, используя параметры индекса строки и столбца. Если имя ячейки — B8, процесс расчета прерывается путем вызова метода[**АннотацияCalculationMonitor.Interrupt()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/interrupt)метод. Однажды конкретный класс[**АннотацияРасчетМонитор**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor)класс реализован, его экземпляр присвоен[**CalculationOptions.CalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/calculationmonitor)свойство. Окончательно,[**Рабочая книга.ВычислитьФормула()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)вызывается путем прохождения[**Параметры расчета**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions) в качестве параметра. Пожалуйста, ознакомьтесь с[образец файла Excel](51740731.xlsx) используется внутри кода, а также в консольном выводе кода, приведенного ниже для справки.

##  **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-InterruptOrCancelFormulaCalculationOfWorkbook.cs" >}}

##  **Консольный вывод**

{{< highlight "java" >}}

 0----1----3----D2

0----4----6----G5

0----7----1----B8

{{< /highlight >}}
