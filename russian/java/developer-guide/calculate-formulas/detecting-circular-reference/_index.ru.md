---
title: Обнаружение циклической ссылки
type: docs
weight: 70
url: /ru/java/detecting-circular-reference/
---

## **Введение**

У книг Excel могут быть циклические ссылки, и иногда необходимо определить, есть ли циклические ссылки или нет.

## **Концепция обнаружения циклических ссылок**

Кольцевые ссылки могут быть обнаружены только при расчете формулы, поскольку ссылки одной формулы обычно зависят от расчитанного результата других частей или других формул. Поэтому мы предоставляем новые API для этого требования (чтобы собирать ячейки с кольцевыми ссылками) в процессе расчета формулы:

[**CalculationCell**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell): Представляет расчет соответствующих данных по одной вычисляемой ячейке

[**AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular-java.util.Iterator-): будет вызван движком расчета формул при обнаружении кольцевых ссылок, элемент в перечислителе - [**CalculationCell**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell) объектов, которые представляют все ячейки в одном круге. Возвращенное значение указывает, нужно ли движку формулы рассчитать эти ячейки в кольцевом порядке после этого вызова.

Пользователь может собирать эти кольцевые ссылки в реализации метода [**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular-java.util.Iterator-).

Образец исходного файла можно загрузить по следующей ссылке:

[Circular Formulas.xls](77496332.xls)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-1.java" >}}

Определение класса *CircularMonitor*, который происходит от класса [**AbstractCalculationMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor), приведено ниже:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-2.java" >}}
{{< app/cells/assistant language="java" >}}
