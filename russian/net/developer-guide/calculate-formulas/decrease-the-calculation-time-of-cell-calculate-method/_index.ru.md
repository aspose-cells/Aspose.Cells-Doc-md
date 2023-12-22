---
title: Уменьшите время расчета Cell. Метод расчета.
description: В этой статье рассказывается, как использовать библиотеку Aspose.Cells для сокращения времени расчета методов расчета ячеек в Microsoft Excel. Загрузив существующий файл Excel или создав новый, мы можем использовать методы, предоставленные Aspose.Cells, для оптимизации метода расчета ячеек и повышения его производительности. Наконец, мы сохраняем измененный файл Excel на диск.
keywords: Aspose.Cells, Excel, Cell calculation methods, optimization, performance, reduction of calculation time
type: docs
weight: 100
url: /ru/net/decrease-the-calculation-time-of-cell-calculate-method/
---
##  **Возможные сценарии использования**

Обычно мы рекомендуем пользователям звонить[**Рабочая книга.ВычислитьФормула()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)метод один раз, а затем получите расчетные значения отдельных ячеек. Но иногда пользователи не хотят рассчитывать всю книгу. Они просто хотят вычислить одну ячейку. Aspose.Cells обеспечивает[**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive) свойство, которое вы можете установить для**ЛОЖЬ**и это значительно уменьшит время расчета отдельной ячейки. Потому что, когда для свойства recursive установлено значение *true**, все зависимые ячейки пересчитываются при каждом вызове. Но если рекурсивное свойство имеет значение *false**, зависимые ячейки вычисляются только один раз и не вычисляются повторно при последующих вызовах.

##  **Уменьшите время расчета метода Cell.Calculate().**

 Следующий пример кода иллюстрирует использование[**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive) свойство. Пожалуйста, выполните этот код с заданным[образец файла Excel](5113710.xlsx) и проверьте его консольный вывод. Вы обнаружите, что установка рекурсивного свойства на**ЛОЖЬ**значительно сократило время расчета. Пожалуйста, также прочитайте комментарии для лучшего понимания этого объекта недвижимости.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-1.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-TestCalcTimeRecursive.cs" >}}

##  **Консольный вывод**

 Это вывод консоли приведенного выше примера кода при выполнении с заданной[образец файла Excel](5113710.xlsx) на нашей машине. Обратите внимание: ваш вывод может отличаться, но время, прошедшее после установки рекурсивного свойства на**ЛОЖЬ**всегда будет меньше, чем значение *true**.

{{< highlight "java" >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
