---
title: Уменьшить время вычисления метода Cell.Calculate
description: Эта статья рассказывает о том, как использовать библиотеку Aspose.Cells для снижения времени вычисления методов вычисления ячейки в Microsoft Excel. Загружая существующий файл Excel или создавая новый, мы можем использовать методы, предоставленные Aspose.Cells, для оптимизации метода вычисления ячейки и улучшения его производительности. Наконец, мы сохраняем измененный файл Excel на диск.
keywords: Aspose.Cells, Excel, методы вычисления ячейки, оптимизация, производительность, снижение времени вычисления
type: docs
weight: 100
url: /ru/net/decrease-the-calculation-time-of-cell-calculate-method/
---

## **Возможные сценарии использования**

Обычно мы рекомендуем пользователям вызвать метод [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula/index) один раз, а затем получить вычисленные значения отдельных ячеек. Но иногда пользователи не хотят вычислять весь книгу. Они хотят вычислить только одну ячейку. Aspose.Cells предоставляет свойство [**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive), которое можно установить в **false**, и это значительно снизит время вычисления отдельной ячейки. Потому что, когда свойство рекурсии установлено в **true**, то все зависимые ячейки пересчитываются при каждом вызове. Но когда свойство рекурсии **false**, то зависимые ячейки вычисляются только один раз и не вычисляются снова при последующих вызовах.

## **Уменьшение времени вычисления метода Cell.Calculate()**

В следующем образце кода показано использование свойства [**CalculationOptions.Recursive**](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/recursive). Пожалуйста, выполните этот код с данным [образцом файла Excel](5113710.xlsx) и проверьте его вывод в консоли. Вы увидите, что установка свойства рекурсии в **false** значительно уменьшила время вычисления. Пожалуйста, также прочитайте комментарии для лучшего понимания этого свойства.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-1.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-DecreaseCalculationTime-TestCalcTimeRecursive.cs" >}}

## **Вывод в консоль**

Это вывод консоли вышеприведенного образца кода при выполнении с данным [образцом файла Excel](5113710.xlsx) на нашей машине. Обратите внимание, что ваш вывод может отличаться, но затраченное время после установки свойства рекурсии в **false** всегда будет меньше, чем при установке его в **true**.

{{< highlight java >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
