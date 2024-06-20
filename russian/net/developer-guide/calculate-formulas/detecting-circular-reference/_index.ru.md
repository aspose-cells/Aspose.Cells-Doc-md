---
title: Обнаружение циклической ссылки
description: Эта статья рассказывает о том, как использовать библиотеку Aspose.Cells для обнаружения циклических ссылок в Microsoft Excel. Загружая существующий файл Excel или создавая новый, мы можем использовать метод, предоставленный Aspose.Cells, для обнаружения циклических ссылок и получения результатов. Наконец, мы сохраняем измененный файл Excel на диск.
keywords: Aspose.Cells, Excel, циклические ссылки, обнаружение
type: docs
weight: 70
url: /ru/net/detecting-circular-reference/
---

## **Введение**

У книг Excel могут быть циклические ссылки, и иногда необходимо определить, есть ли циклические ссылки или нет.

## **Концепция обнаружения циклических ссылок**

Кольцевые ссылки могут быть обнаружены только при расчете формулы, поскольку ссылки одной формулы обычно зависят от расчитанного результата других частей или других формул. Поэтому мы предоставляем новые API для этого требования (чтобы собирать ячейки с кольцевыми ссылками) в процессе расчета формулы:

[**CalculationCell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell): Представляет расчет соответствующих данных по одной вычисляемой ячейке

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular): будет вызван движком расчета формул при обнаружении кольцевых ссылок, элемент в перечислителе - [**CalculationCell**](https://reference.aspose.com/cells/net/aspose.cells/calculationcell) объектов, которые представляют все ячейки в одном круге. Возвращенное значение указывает, нужно ли движку формулы рассчитать эти ячейки в кольцевом порядке после этого вызова.

Пользователь может собирать эти кольцевые ссылки в реализации метода [**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor/methods/oncircular).

Образец исходного файла можно загрузить по следующей ссылке:

[Circular Formulas.xls](77496332.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-1.cs" >}}

Определение класса *CircularMonitor*, который происходит от класса [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationmonitor), приведено ниже:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-DetectCircularReference-2.cs" >}}
