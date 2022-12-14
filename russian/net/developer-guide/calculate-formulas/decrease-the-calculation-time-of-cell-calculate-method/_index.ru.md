---
title: Уменьшите время расчета Cell. Метод расчета
type: docs
weight: 100
url: /ru/net/decrease-the-calculation-time-of-cell-calculate-method/
---
## **Возможные сценарии использования**

Обычно мы рекомендуем пользователям звонить[**Рабочая книга.ВычислитьФормулу()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index)метод один раз, а затем получить рассчитанные значения отдельных ячеек. Но иногда пользователи не хотят вычислять всю книгу. Они просто хотят вычислить одну ячейку. Aspose.Cells предоставляет[**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive) свойство, которое вы можете установить для**ЛОЖЬ** и это значительно уменьшит время расчета отдельной ячейки. Поскольку, когда рекурсивное свойство установлено в**истинный** , то все зависимые ячейки пересчитываются при каждом вызове. Но когда рекурсивное свойство**ЛОЖЬ**, то зависимые ячейки вычисляются только один раз и не вычисляются повторно при последующих вызовах.

## **Уменьшить время расчета метода Cell.Calculate().**

 Следующий пример кода иллюстрирует использование[**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive) имущество. Пожалуйста, выполните этот код с указанным[образец эксель файла](5113710.xlsx) и проверьте его консольный вывод. Вы обнаружите, что установка рекурсивного свойства на**ЛОЖЬ**значительно сократил время расчета. Также прочитайте комментарии, чтобы лучше понять это свойство.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-1.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-TestCalcTimeRecursive.cs" >}}

## **Консольный вывод**

 Это консольный вывод приведенного выше примера кода при выполнении с заданным[образец эксель файла](5113710.xlsx)на нашей машине. Обратите внимание, что ваш вывод может отличаться, но время, прошедшее после установки рекурсивного свойства на**ЛОЖЬ** всегда будет меньше, чем при установке**истинный**.

{{< highlight "java" >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
