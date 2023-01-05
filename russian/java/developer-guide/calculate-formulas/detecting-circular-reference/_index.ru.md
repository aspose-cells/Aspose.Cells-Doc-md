---
title: Обнаружение циклической ссылки
type: docs
weight: 70
url: /ru/java/detecting-circular-reference/
---
## **Вступление**

Рабочие книги могут иметь циклические ссылки, и иногда необходимо определить, есть ли циклические ссылки или нет.

## **Концепция обнаружения циклической ссылки**

Циклические ссылки могут быть обнаружены только при вычислении формулы, поскольку ссылки одной формулы обычно зависят от результата вычисления других частей или других формул. Поэтому мы предоставляем новые API для этого требования (для сбора ячеек с циклическими ссылками) в процессе вычисления формулы:

[**Расчетная ячейка**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell): Представляет вычисление релевантных данных об одной вычисляемой ячейке.

[**AbstractCalculationMonitor.OnCircular (IEnumerator circleCellsData)**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular(java.util.Iterator)): будет вызываться механизмом вычисления формулы при обнаружении циклических ссылок, элемент в перечислителе[**Расчетная ячейка**](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationCell) объекты, которые представляют все клетки в одном круге. Возвращаемое значение указывает, нужно ли обработчику формул вычислять эти ячейки по кругу после этого вызова.

 Пользователь может собирать эти циклические ссылки при реализации[**AbstractCalculationMonitor.OnCircular()**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor#onCircular(java.util.Iterator)) метод.

Исходный образец файла можно скачать по следующей ссылке:

[Круговые формулы.xls](77496332.xls)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-1.java" >}}

Значение*ЦиркулярМонитор* класс, производный от[**АннотацияРасчетМонитор**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationMonitor) класс выглядит следующим образом:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-DetectCircularReference-2.java" >}}
