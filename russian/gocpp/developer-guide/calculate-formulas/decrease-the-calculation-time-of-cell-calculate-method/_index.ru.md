---
title: Ускорение времени вычисления метода Cell.Calculate с Golang через C++
linktitle: Ускорение времени вычисления Cell.Calculate
description: Эта статья рассказывает о том, как использовать библиотеку Aspose.Cells для снижения времени вычисления методов вычисления ячейки в Microsoft Excel. Загружая существующий файл Excel или создавая новый, мы можем использовать методы, предоставленные Aspose.Cells, для оптимизации метода вычисления ячейки и улучшения его производительности. Наконец, мы сохраняем измененный файл Excel на диск.
keywords: Aspose.Cells, Excel, методы вычисления ячейки, оптимизация, производительность, снижение времени вычисления
type: docs
weight: 100
url: /ru/go-cpp/decrease-the-calculation-time-of-cell-calculate-method/
---

## **Возможные сценарии использования**

Обычно мы рекомендуем пользователям вызывать метод [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) один раз и затем получать рассчитанные значения отдельных ячеек. Но иногда пользователи не хотят вычислять всю книгу. Они просто хотят вычислить одну ячейку. Aspose.Cells предоставляет свойство [**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getrecursive/), которое можно установить в **false**, что значительно уменьшит время вычисления отдельных ячеек. Потому что при установленном свойстве recursive в **true**, все зависимые ячейки пересчитываются при каждом вызове. Но при значении **false** зависимые ячейки вычисляются только один раз и не пересчитываются при последующих вызовах.

## **Уменьшение времени вычисления метода Cell.Calculate()**

Следующий пример иллюстрирует использование свойства [**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/go-cpp/calculationoptions/getrecursive/). Пожалуйста, выполните этот код с указанным [образцом файла Excel](5113710.xlsx) и проверьте вывод в консоли. Вы заметите, что установка свойства recursive в **false** значительно ускоряет вычисление. Также читайте комментарии для лучшего понимания этого свойства.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DecreaseTheCalculationTimeOfCellCalculateMethod.go" >}}
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DecreaseTheCalculationTimeOfCellCalculateMethod-1.go" >}}
## **Вывод в консоль**

Это вывод консоли вышеуказанного кода при выполнении его с указанным [образцом файла Excel](5113710.xlsx) на нашей машине. Обратите внимание, что ваш вывод может отличаться, но затраченное время после установки свойства recursive в **false** всегда будет меньше, чем при его установке в **true**.

{{< highlight java >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
